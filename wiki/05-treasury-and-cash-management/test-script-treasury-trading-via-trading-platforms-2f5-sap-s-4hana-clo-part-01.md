---
id: 05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-01
title: "Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 1 of 2"
description: "Test script for SAP S/4HANA Cloud scope item 2F5 (2608): FX, money market and MMF trading via trading platforms, external and intercompany scenarios."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-trading-platforms-and-swift]
aliases: []
keywords: [Treasury Trading Platforms and SWIFT Correspondence, trading platform integration, external fx trade requests, fx inbound trades, intercompany fx trading, back-to-back trading, trade aggregation, money market trades, intercompany money market, cash trade requests]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx#lines-1-3618"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-821
topic: 05-treasury-and-cash-management/treasury-trading-platforms-and-swift
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx`, part 1 of 2 (lines 1–3618 of the extracted text), extracted with `mammoth`. Grouped under **Treasury Trading Platforms and SWIFT Correspondence** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Treasury Trading via Trading Platforms (2F5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 6](#_Toc232846350)

[2 Prerequisites 10](#_Toc232846351)

[2.1 System Access 10](#_Toc232846352)

[2.2 Roles 10](#_Toc232846353)

[2.3 Master Data, Organizational Data, and Other Data 11](#_Toc232846354)

[2.4 Additional Manual Configuration 12](#_Toc232846355)

[2.5 Business Conditions 12](#_Toc232846356)

[2.6 Preliminary Steps 13](#_Toc232846357)

[2.6.1 Set Up the Connection 13](#_Toc232846358)

[2.6.2 Create Business Partner in S/4HANA Cloud 13](#_Toc232846359)

[2.6.3 Business Configuarion in SAP Trading Platform Integration 14](#_Toc232846360)

[2.6.3.1 Configura SAP Back-end Systems 14](#_Toc232846361)

[2.6.3.2 Configure Trading Platforms 14](#_Toc232846362)

[2.6.3.3 Manage Subscriptions (Optional) 15](#_Toc232846363)

[2.6.3.4 Configure Field Mapping 15](#_Toc232846364)

[2.6.3.5 Configure Business Rules 16](#_Toc232846365)

[2.6.3.6 Manage Counterparties in SAP Trading Platform Integration 16](#_Toc232846366)

[3 Overview Table 19](#_Toc232846367)

[4 Test Procedures 26](#_Toc232846368)

[4.1 Treasury Management Integration for Trading Platform - External Scenario for FX 26](#_Toc232846369)

[4.1.1 Treasury Trading via Trading Platforms - FX Outbound 26](#_Toc232846370)

[4.1.1.1 Create External FX Trade Requests in SAP S/4HANA Cloud Public Edition 26](#_Toc232846371)

[4.1.1.2 Review External FX Trade Requests in SAP Trading Platform Integration 28](#_Toc232846372)

[4.1.1.3 Decline External FX Trade Requests in SAP Trading Platform Integration 29](#_Toc232846373)

[4.1.1.4 Process External FX Trade Requests in SAP Trading Platform Integration 30](#_Toc232846374)

[4.1.1.4.1 Group External FX Trade Requests into a Block in SAP Trading Platform Integration (Optional) 31](#_Toc232846375)

[4.1.1.4.2 Split External FX Trade Requests in SAP Trading Platform Integration (Optional) 33](#_Toc232846376)

[4.1.1.5 Send External FX Trade Requests to External Trading Platform in SAP Trading Platform Integration 34](#_Toc232846377)

[4.1.1.6 Review External FX Trade Request Status in External Trading Platform 36](#_Toc232846378)

[4.1.1.7 Reset External FX Trade Requests in SAP Trading Platform Integration (Optional) 36](#_Toc232846379)

[4.1.1.8 Call Counterparty for Phone Trade 37](#_Toc232846380)

[4.1.2 Treasury Trading via Trading Platforms - FX Inbound 37](#_Toc232846381)

[4.1.2.1 Analyze Exposure and Check Limit in SAP S/4HANA Cloud Public Edition 37](#_Toc232846382)

[4.1.2.2 Review External FX Trade Requests in External Trading Platform 38](#_Toc232846383)

[4.1.2.3 Create FX Trade in External Trading Platform 38](#_Toc232846384)

[4.1.2.4 Generate FX Trades in SAP Trading Platform Integration 38](#_Toc232846385)

[4.1.2.5 Enter Phone Trade Details in SAP Trading Platform Integration 39](#_Toc232846386)

[4.1.2.6 Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 40](#_Toc232846387)

[4.2 Treasury Management Integration for Trading Platform – Intercompany Scenarios for FX 42](#_Toc232846388)

[4.2.1 Foreign Exchange Intercompany scenario 1: Back-to-Back Trading (Subsidiary) 43](#_Toc232846389)

[4.2.1.1 Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition 43](#_Toc232846390)

[4.2.1.2 Review Intercompany FX Trade Request in SAP Trading Platform Integration 45](#_Toc232846391)

[4.2.1.3 Create External FX Trade Requests in SAP Trading Platform Integration 46](#_Toc232846392)

[4.2.1.4 Process External FX Trade Requests in SAP Trading Platform Integration 47](#_Toc232846393)

[4.2.1.4.1 Split External FX Trade Requests in SAP Trading Platform Integration (Optional) 47](#_Toc232846394)

[4.2.1.4.2 Send External FX Trade Requests from SAP Trading Platform Integration to External Trading Platform 48](#_Toc232846395)

[4.2.1.4.3 Review External FX Trade Request Status in External Trading Platform 50](#_Toc232846396)

[4.2.1.4.4 Create FX Trade in External Trading Platform 50](#_Toc232846397)

[4.2.1.4.5 Generate FX Trades in SAP Trading Platform Integration 51](#_Toc232846398)

[4.2.1.4.6 Call Counterparty for Phone Trade 52](#_Toc232846399)

[4.2.1.4.7 Enter the Phone Trade Details in SAP Trading Platform Integration 52](#_Toc232846400)

[4.2.1.4.8 External FX Trades Aggregation in SAP Trading Platform Integration 54](#_Toc232846401)

[4.2.1.4.9 Generate Intercompany FX Trades in SAP Trading Platform Integration 56](#_Toc232846402)

[4.2.1.4.10 Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 58](#_Toc232846403)

[4.2.1.4.11 Decline FX Trade Requests in SAP Trading Platform Integration (Optional) 59](#_Toc232846404)

[4.2.2 Foreign Exchange Intercompany scenario 2: Manual Trading 63](#_Toc232846405)

[4.2.2.1 Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition 63](#_Toc232846406)

[4.2.2.2 Review Intercompany FX Trade Request in SAP Trading Platform Integration 65](#_Toc232846407)

[4.2.2.3 Create Intercompany FX Manual Trade in SAP Trading Platform Integration 66](#_Toc232846408)

[4.2.2.4 Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 67](#_Toc232846409)

[4.2.3 Foreign Exchange Intercompany scenario 3: Automated Trading 68](#_Toc232846410)

[4.2.3.1 Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition 68](#_Toc232846411)

[4.2.3.2 Review Intercompany FX Trade Request in SAP Trading Platform Integration 70](#_Toc232846412)

[4.2.3.3 Generate Intercompany FX Trades in SAP Trading Platform Integration 71](#_Toc232846413)

[4.2.3.4 Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 72](#_Toc232846414)

[4.2.4 Foreign Exchange Intercompany scenario 4: Trading via Trading Platform 72](#_Toc232846415)

[4.2.4.1 Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition 72](#_Toc232846416)

[4.2.4.2 Review Intercompany FX Trade Request in SAP Trading Platform Integration 74](#_Toc232846417)

[4.2.4.3 Send Intercompany FX Trade Requests from SAP Trading Platform Integration to External Trading Platform 75](#_Toc232846418)

[4.2.4.4 Review Intercompany FX Trade Request Status in External Trading Platform 76](#_Toc232846419)

[4.2.4.5 Create Intercompany FX Trades in External Trading Platform 77](#_Toc232846420)

[4.2.4.6 Generate Intercompany FX Trades in SAP Trading Platform Integration 77](#_Toc232846421)

[4.2.4.7 Create Intercompany Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 78](#_Toc232846422)

[4.2.5 Foreign Exchange Intercompany scenario 5: Back-to-Back Trading (Treasury Center) 78](#_Toc232846423)

[4.2.5.1 Create External FX Trade Requests in SAP S/4HANA Cloud Public Edition 78](#_Toc232846424)

[4.2.5.2 Review External FX Trade Request in SAP Trading Platform Integration 80](#_Toc232846425)

[4.2.5.3 Send External FX Trade Requests from SAP Trading Platform Integration to External Trading Platform 82](#_Toc232846426)

[4.2.5.4 Review External FX Trade Request Status in External Trading Platform 83](#_Toc232846427)

[4.2.5.5 Create FX Trade in External Trading Platform 83](#_Toc232846428)

[4.2.5.6 Generate FX Trades in SAP Trading Platform Integration 83](#_Toc232846429)

[4.2.5.7 Call Counterparty for Phone Trade 84](#_Toc232846430)

[4.2.5.8 Enter the Phone Trade Details in SAP Trading Platform Integration 84](#_Toc232846431)

[4.2.5.9 Generate Intercompany FX Trades in SAP Trading Platform Integration 86](#_Toc232846432)

[4.2.5.10 Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition 87](#_Toc232846433)

[4.3 Treasury Management Integration for Trading Platform - External Scenario for MM 87](#_Toc232846434)

[4.3.1 Treasury Trading via Trading Platforms – MM Outbound 88](#_Toc232846435)

[4.3.1.1 Create External MM Trade Requests in SAP S/4HANA Cloud Public Edition 88](#_Toc232846436)

[4.3.1.2 Review External MM Trade Request in SAP Trading Platform Integration 91](#_Toc232846437)

[4.3.1.3 Decline External MM Trade Requests in SAP Trading Platform Integration (Optional) 92](#_Toc232846438)

[4.3.1.4 Update the Instrument Category of External MM Trade Requests in SAP Trading Platform Integration 93](#_Toc232846439)

[4.3.1.5 Send External MM Trade Requests to External Trading Platform in SAP Trading Platform Integration 94](#_Toc232846440)

[4.3.1.6 Review External MM Trade Request Status in External Trading Platform 95](#_Toc232846441)

[4.3.1.7 Reset External MM Trade Requests in SAP Trading Platform Integration (Optional) 96](#_Toc232846442)

[4.3.1.8 Call Counterparty for Phone Trade 97](#_Toc232846443)

[4.3.2 Treasury Trading via Trading Platforms – MM Inbound 97](#_Toc232846444)

[4.3.2.1 Check Liquidity Forecast in SAP S/4HANA Cloud Public Edition 97](#_Toc232846445)

[4.3.2.2 Review Trade Requests in External Trading Platform 98](#_Toc232846446)

[4.3.2.3 Create Money Market Trade in External Trading Platform 98](#_Toc232846447)

[4.3.2.4 Generate MM Trades in SAP Trading Platform Integration 98](#_Toc232846448)

[4.3.2.5 Enter the Phone Trade Details in SAP Trading Platform Integration 99](#_Toc232846449)

[4.3.2.6 Create Money Market Transaction in SAP S/4HANA Cloud Public Edition 101](#_Toc232846450)

[4.4 Treasury Management Integration for Trading Platforms – Intercompany Scenarios for MM 102](#_Toc232846451)

[4.4.1 Money Market Intercompany scenario 1: Back-to-Back Trading 102](#_Toc232846452)

[4.4.1.1 Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition 102](#_Toc232846453)

[4.4.1.2 Review Intercompany MM Trade Request in SAP Trading Platform Integration 105](#_Toc232846454)

[4.4.1.3 Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration 106](#_Toc232846455)

[4.4.1.4 Create External MM Trade Requests in SAP Trading Platform Integration 107](#_Toc232846456)

[4.4.1.5 Process External MM Trade Requests 108](#_Toc232846457)

[4.4.1.5.1 Send External MM Trade Requests to Trading Platform in SAP Trading Platform Integration 108](#_Toc232846458)

[4.4.1.5.2 Review External MM Trade Request Status in External Trading Platform 110](#_Toc232846459)

[4.4.1.5.3 Create MM Trade in External Trading Platform 110](#_Toc232846460)

[4.4.1.5.4 Generate MM Trades in SAP Trading Platform Integration 110](#_Toc232846461)

[4.4.1.5.5 Call Counterparty for Phone Trade 111](#_Toc232846462)

[4.4.1.5.6 Enter the Phone Trade Details in SAP Trading Platform Integration 112](#_Toc232846463)

[4.4.1.5.7 Generate Intercompany MM Trades in SAP Trading Platform Integration 113](#_Toc232846464)

[4.4.1.5.8 Create Money Market Transactions in SAP S/4HANA Cloud Public Edition 115](#_Toc232846465)

[4.4.1.5.9 Decline MM Trade Requests in SAP Trading Platform Integration (Optional) 115](#_Toc232846466)

[4.4.2 Money Market Intercompany scenario 2: Manual Trading 120](#_Toc232846467)

[4.4.2.1 Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition 120](#_Toc232846468)

[4.4.2.2 Review Intercompany MM Trade Request in SAP Trading Platform Integration 122](#_Toc232846469)

[4.4.2.3 Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration 123](#_Toc232846470)

[4.4.2.4 Create Intercompany Manual Trade in SAP Trading Platform Integration 125](#_Toc232846471)

[4.4.2.5 Create Money Market Transactions in SAP S/4HANA Cloud Public Edition 126](#_Toc232846472)

[4.4.3 Money Market Intercompany scenario 4: Trading via Trading Platform 126](#_Toc232846473)

[4.4.3.1 Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition 127](#_Toc232846474)

[4.4.3.2 Review Intercompany MM Trade Request in SAP Trading Platform Integration 129](#_Toc232846475)

[4.4.3.3 Update the Instrument Category of the Intercompany MM 130](#_Toc232846476)

[4.4.3.4 Send Intercompany MM Trade Requests from SAP Trading Platform Integration to External Trading Platform 132](#_Toc232846477)

[4.4.3.5 Review Intercompany MM Trade Request Status in External Trading Platform 133](#_Toc232846478)

[4.4.3.6 Create Intercompany MM Trades in External Trading Platform 133](#_Toc232846479)

[4.4.3.7 Generate Intercompany MM Trades in SAP Trading Platform Integration 133](#_Toc232846480)

[4.4.3.8 Create Intercompany Money Market Transactions in SAP S/4HANA Cloud Public Edition 134](#_Toc232846481)

[4.5 Treasury Management Integration for Trading Platform - MMF 135](#_Toc232846482)

[4.5.1 Analyze Liquidity Forecast in S/4HANA Cloud 135](#_Toc232846483)

[4.5.2 Create Money Market Fund Trade in External Trading Platform 135](#_Toc232846484)

[4.5.3 Treasury Management Integration for Trading Platform – MMF w/o Clearing House Scenario 136](#_Toc232846485)

[4.5.3.1 Generate Money Market Fund Trade in SAP Trading Platform Integration 136](#_Toc232846486)

[4.5.3.2 Create Money Market Fund Transactions in SAP S/4HANA Cloud Public Edition 137](#_Toc232846487)

[4.5.4 Treasury Management Integration for Trading Platform – MMF Clearing House Scenario 138](#_Toc232846488)

[4.5.4.1 Generate Money Market Fund Trade w/o Known Quantity and Price in SAP Trading Platform Integration 138](#_Toc232846489)

[4.5.4.2 Create Money Market Fund Transactions w/o Known Quantity and Price in SAP S/4HANA Cloud Public Edition 140](#_Toc232846490)

[4.5.4.3 Update Money Market Fund Trade with Quantity and Price Information in External Trading Platform 141](#_Toc232846491)

[4.5.4.4 Update Money Market Fund Trade with Quantity and Price Information in SAP Trading Platform Integration 141](#_Toc232846492)

[4.5.4.5 Update Money Market Fund Transactions with Quantity and Price Information in SAP S/4HANA Cloud Public Edition 142](#_Toc232846493)

[5 Appendix 144](#_Toc232846494)

[5.1 Set Trade Requests to Completed (Optional) 144](#_Toc232846495)

[5.2 Edit Trades (Optional） 145](#_Toc232846496)

[5.3 Assign and Unassign Processor of Trade Requests (Optional) 146](#_Toc232846497)

[5.4 Partial Decline for a Trade Request (Optional) 147](#_Toc232846498)

[5.5 Check Counterparty Limit in SAP Trading Platform Integration 148](#_Toc232846499)

[5.6 Field Mapping Settings Example 149](#_Toc232846500)

[5.6.1 Configure Mappings - Trading Platform Format 149](#_Toc232846501)

[5.6.2 Configure Mappings - Back-End Format 152](#_Toc232846502)

[5.6.3 Configure Mappings - Back-End Format (Intercompany) 156](#_Toc232846503)

[5.7 Business Rules Settings Example 159](#_Toc232846504)

[5.7.1 Configure Business Rules 159](#_Toc232846505)

[5.7.1.1 Counterparty 159](#_Toc232846506)

[5.7.1.2 Counterparty Limit 160](#_Toc232846507)

[5.7.1.3 External Trading 161](#_Toc232846508)

[5.7.1.4 Intercompany Trading 162](#_Toc232846509)

[5.7.1.5 Market Data Adapter 163](#_Toc232846510)

[5.7.1.6 Counterparty Mapping 164](#_Toc232846511)

[5.8 Useful Resources 165](#_Toc232846512)

## Purpose

Overview

This scope item enables you to integrate deal requests and transactions between trading platforms and SAP S/4HANA Cloud Public Edition automatically. We now support financial instruments like Foreign Exchange, Money Market Fixed Term, and Money Market Fund.

Currently, the scope item covers communication with trading platforms for 360T (subsidiary of Deutsche Boerse), FXall (via partner Brisken), and ICD portal.

For the outbound scenario, trade requests generated in SAP S/4HANA Cloud Public Edition can be sent to trading platforms through SAP Business Technology Platform. For the inbound scenario, customers can upload transactions automatically from trading platforms to SAP S/4HANA Cloud Public Edition.

The following figure provides an overview of the integration of SAP trading platform integration with the SAP Treasury and Risk Management component in the back-end system and with the external trading platform:

<!-- image omitted: unnamed -->

The following options are available for connecting SAP trading platform integration with external trading platforms:

- Direct connection based on 360T format
- Connection to other trading platforms using the Generic Format interface

360T

If you're using 360T as your external trading platform, the following processes and instruments are supported:

|  |  |  |
| --- | --- | --- |
|  | Trading Process (Inbound) | Trade Request Process (Outbound) |
| Supported Instruments | FX ForwardFX SpotFX SwapNon-Deliverable Forward (NDF)FX OptionFX Non-Deliverable Swap (NDS)Money Market Fixed Term | FX ForwardFX SpotFX SwapNon-Deliverable Forward (NDF)FX OptionMoney Market Fixed Term |

Generic Format Interface

If you're using the Generic Format interface to connect the application to external trading platforms other than 360T, for example, FXall via partner Brisken, the following processes and FX instruments are supported:

|  |  |  |
| --- | --- | --- |
|  | Trading Process (Inbound) | Trade Request Process (Outbound) |
| Supported Instruments | FX ForwardFX SpotFX SwapNon-Deliverable Forward (NDF)FX OptionFX CollarMoney Market Fund | FX ForwardFX SpotFX SwapNon-Deliverable Forward (NDF)FX OptionFX Collar |

In this release, the scope item supports external trade scenarios (non-intercompany scenarios) as well as intercompany scenarios. Depending on your business scenarios, you have the option to leverage these scenarios together or individually.

- External Scenario (Non-intercompany scenarios):

This scenario handles Foreign Exchange (FX), Money Market (MM) and Money Market Fund (MMF) instruments process with the external counterparties.

This scenario covers Inbound and outbound processes with external counterparties:

In the outbound process, FX or MM trade requests are firstly generated in the SAP S/4HANA Cloud Public Edition system. Then the trade requests are imported into SAP trading platform integration. Finally, the trade requests can be sent to external trading platforms from Trading Platform Integration for further process.

In the inbound process, in the external trading platforms, you may create new FX or MM or MMF trades with external counterparties (without outbound process), or continue to process the external trade requests you’ve sent via outbound process and create FX or MM trades accordingly. Once created in the external trading platforms, the FX or MM or MMF trades information will be automatically imported into SAP trading platform integration. SAP trading platform integration will then pass the trade information to the SAP S/4HANA Cloud Public Edition system in which FX or MM or MMF transactions are created.

|  |
| --- |
| Note In current release, SAP trading platform integration only supports the inbound process of Money Market Fund instruments. |

- Intercompany Scenarios:
    - Back-to-Back Trading (Subsidiary)

A corporate might have more than one legal entity (company code) in its SAP S/4HANA Cloud Public Edition system. This scenario handles trades between two company codes (legal entities), for example, a subsidiary company code and a treasury center company code as treasury center. One company code (the subsidiary) makes an FX or MM trade with the treasury-center company code (headquarter), then the treasury-center company code (headquarter) will make another reversing trade with the external counterparty. These two trades are treated as back-to-back trades. For example, the subsidiary buys 110,000 USD with 100,000 EUR from the headquarter to support its daily business. In the meantime, the headquarter make another FX contract with an external bank to buy the same amount USD with EUR. In this way, the subsidiary's foreign exchange exposure will be hedged by the FX contract with the external bank. The whole process is described as below.

Firstly, one company code (subsidiary) releases a trade request from the SAP S/4HANA Cloud Public Edition system to the SAP trading platform integration, where the request is identified as an intercompany trade request scenario is identified as 1: Back-to-back trading (Subsidiary). Meanwhile, another external trade request is created automatically under the treasury-center company code (headquarter).

Once the external trade request is fulfilled by an external trade (either via phone trade or closed on the external trading platform), the following three trades will be generated automatically in the SAP trading platform integration and imported to the SAP S/4HANA Cloud Public Edition system:

-
    -
        - An external trade with the external counterparty (i.e., an external Bank) in the treasury-center company code (headquarter).
        - An internal trade with the intercompany subsidiary counterparty (i.e., subsidiary company code) in the treasury-center company code(headquarter).
        - An internal trade with the intercompany treasury-center counterparty (i.e., headquarter company code) in the company code (subsidiary).

|  |
| --- |
| Note You may also split the external trade request into several ones and send those split sub-trade requests to external trading platforms to make trades separately. In this case, once all the split sub-trade requests are fulfilled with external trades, the SAP trading platform integration will aggregate those sub-trades and generate intercompany trades in both company codes, and the following trades will be generated:all external sub-trades with the counterparty in the treasury-center company code (headquarter).One or more aggregated internal trade with the intercompany subsidiary counterparty (i.e. subsidiary company code) in the treasury-center company code (headquarter).One or more aggregated internal trade with the intercompany headquarter counterparty (i.e., headquarter company code) in the subsidiary company code. |

|  |
| --- |
| Note You may also manually trigger the generation of the aggregated intercompany trades when part of the split trade requests is fulfilled, given that the fields of the split trades are matched as required. |

- Back-to-Back Trading (Treasury Center)

This scenario is similar to scenario Back-to-Back Trading (Subsidiary). The only difference is that the company code (Treasury Center) releases a trade request from the SAP S/4HANA Cloud Public Edition system to the SAP trading platform integration on behalf of the subsidiary company code. The subsidiary company code is stored in the On Behalf of Company Code field of the trade request.

- Manual Trading

This scenario handles trades between two company codes, for example, the subsidiary company code and the headquarter company code as the treasury center, where external counterparties are not involved. For example, the subsidiary buys 110,000 USD with 100,000 EUR from the headquarter to support its daily business. This way the foreign exchange exposure will be transferred from subsidiary to the headquarter. The whole process is described as below:

Firstly, one company code releases a trade request from the SAP S/4HANA Cloud Public Edition system to SAP trading platform integration, where the request is identified as an intercompany trade request and the scenario should be identified as 2: Manual trading. Then you create manual trade for this intercompany trade request in SAP trading platform integration, the following two intercompany trades are generated automatically in SAP trading platform integration and imported to the SAP S/4HANA Cloud Public Edition system:

-
    - An intercompany trade with the intercompany subsidiary counterparty (i.e., subsidiary company code) in the headquarter company code.
    - An intercompany trade with the intercompany headquarter counterparty (i.e., headquarter company code) in the subsidiary company code.

Currently this scenario only supports all MM instruments and FX instruments excluding FX NDS.

- Automated Trading

This scenario is similar to the Manual trading scenario except that you don’t need to manually enter the transaction details when creating the intercompany trades. Instead, it will read the business rules configurations (Markup or Markdown Decision) determine the pre-agreed rate based on market rate (maintained in SAP S/4HANA Cloud Public Edition). The whole process is described as below:

Firstly, one company code releases a trade request from the SAP S/4HANA Cloud Public Edition system to SAP trading platform integration, where the request is identified as an intercompany trade request and the scenario should be identified as 3: Automated Trading. Then you sync this intercompany trade request into SAP trading platform integration, the following two intercompany trades are generated automatically in SAP trading platform integration and imported to the SAP S/4HANA Cloud Public Edition system:

-
    - An intercompany trade with the intercompany subsidiary counterparty (i.e., subsidiary company code) in the headquarter company code.
    - An intercompany trade with the intercompany headquarter counterparty (i.e., headquarter company code) in the subsidiary company code.

Currently this scenario only supports the following product types:

-
    - FX Spot
    - FX Forward
    - FX NDF
- Trading via Trading Platform

With this scenario, you can make use of an external platform for the creation and processing of your intercompany trades. For example, the intra group trading platform iTEX of 360T. The whole process is described as below:

Firstly, one company code releases a trade request from the SAP S/4HANA Cloud Public Edition system to SAP trading platform integration, where the request is identified as an intercompany trade request and the scenario should be identified as 4: Trading via Trading Platform. Then you sync this intercompany trade request into SAP trading platform integration and send it to external trading platforms for further process. Once you approve the intercompany trade request and intercompany trades are created in external trading platforms. The intercompany trades will be automatically generated in SAP trading platform integration and imported to the SAP S/4HANA Cloud Public Edition system.

Currently this scenario only supports all MM instruments and FX instruments excluding FX Option, FX Collar and FX NDS.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Trading Platform Integration (on SAP BTP) | Accessible via Fiori Launchpad redirecting. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed SAP Best Practices Baseline, you can use the following baseline package sample data.

|  |
| --- |
| Caution Sample values for master data values are country/region-specific and the values provided in the following table are for DE. Substitute the country/region-specific values provided by the Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| COMPANY CODE | 1010 |  | Treasury-center company code (Headquarter): it can do both external trades with external counterparties and intercompany trades with intercompany business partner 17401710 (representing 1710 subsidiary). |
| COMPANY CODE | 1710 |  | Other company code (Subsidiary): it can only do intercompany trade with treasury-center company code (1010). |
| CURRENCY | EUR |  | local currency (risk-free currency) |
| FOREIGN CURRENCY 1 | USD |  | foreign currency (risk currency) |
| BUSINESS PARTNER | 10537001 |  | An external counterparty |
| BUSINESS PARTNER FOR INTERCOMPANY TRADE | 10401010 |  | BP master representing company code 1010 in 1710. |
| BUSINESS PARTNER FOR INTERCOMPANY TRADE | 17401710 |  | BP master representing company code 1710 in 1010. |
| SECURITY ACCOUNT | DE_MMF |  | Security account used for Money Market Fund trades with external counterparties. |
| SECURITY ID | MMF_DE1 |  | Security ID used for Money Market Fund trades with external counterparties. |
| SECURITY ID | MMF_DE2 |  | Security ID used for Money Market Fund trades with external counterparties. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2619730f5acca416666a876dd4c7ec27)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1X1 - Foreign Currency Risk Management | Perform the following steps of the Create Trade Request section in the Foreign Currency Risk Management(1X1) test script:Create Trade Request via Balance Sheet Exposure Hedge RequestCreate Trade Request via Cash Flow Exposure Hedge RequestCreate Trade Request Manually |
| J78 - Advanced Cash Operations | Perform the following steps in the Cash Trade Request section in the Advanced Cash Operations(J78) test script.Create and Submit Cash Trade Request for FXCreate and Submit Cash Trade Request for Money MarketRelease Cash Trade Request |
| 1WV - Debt and Investment Management | The scope item 1WV must be activated in SAP S/4HANA Cloud Public Edition so that the external and intercompany scenarios for MM could be tested. |
| 2UN - Money Market Mutual Fund Management | The scope item 2UN must be activated in SAP S/4HANA Cloud Public Edition so that the external and intercompany scenarios for MMF could be tested.Perform the following steps in the Money Market Mutual Fund Management(2UN) test script:Create Security AccountCreate Security Class |
| 1YI - Intercompany Process for Debt and Investment Mgmt | Perform the following step in the Intercompany Process for Debt and Investment Mgmt(1YI) test script:Maintain Data for Intercompany Business Partner |

### Preliminary Steps

#### Set Up the Connection

Purpose

You need to set up the connection between the Trading Platform Integration application on SAP BTP and the SAP S/4HANA Cloud Public Edition system, and between the Trading Platform Integration application and the external trading platform.

Procedure

Please follow the steps in the Setup Instructions of communication scenario 0226 to set up the connection.

Result

You have set up the connection between the external trading platform(s), Trading Platform Integration application and the SAP S/4HANA Cloud Public Edition system.

#### Create Business Partner in S/4HANA Cloud

Purpose

In this step, you will create business partners master data which are necessary to perform the test of this test script in S/4HANA Cloud.

Procedure

Please follow the following sections in the Create Business Partner for Treasury and Risk Management - MDS (22G) master data script and Intercompany Process for Debt and Investment Mgmt (1YI) test script to create the necessary business partners.

- Maintain Data for Normal Business Partner
- Maintain Data for Intercompany Business Partner

|  |
| --- |
| Note Please make sure to select the Auth. Checkbox for the following folders under the SI: Authorizations tab for intercompany business partners (For example, 10401710 and 17401710):Foreign ExchangeOTC optionsMoney Market |

Result

You have created the intercompany business partners (for example, 10401010, 17401710) as well as normal business partner for the external trading platform (for example, 10537001).

#### Business Configuarion in SAP Trading Platform Integration

Configure the relevant settings in the Trading Platform Integration application to complete the integration with your SAP back-end system and the external trading platform.

To complete the integration of the application with your SAP back-end system and the external trading platform, the following tasks have to be performed:

- [Configura SAP Back-end Systems](#unique_11) [page ] 14
- [Configure Trading Platforms](#unique_12) [page ] 14
- [Manage Subscriptions (Optional)](#unique_13) [page ] 15
- [Configure Field Mapping](#unique_14) [page ] 15
- [Configure Business Rules](#unique_15) [page ] 16
- [Manage Counterparties in SAP Trading Platform Integration](#unique_16) [page ] 16

##### Configura SAP Back-end Systems

Purpose

Add and configure the relevant SAP back-end systems that you want to connect to the application.

You need to specify the back-end profile, format code, direction, business system ID, and destination for the connection to your SAP back-end system.

Procedure

Please refer to the following steps in the [Administration Guide of Trading Platform Integration](https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION) in the help portal:

- Configure Back-End Systems

##### Configure Trading Platforms

Purpose

Add and configure the trading platforms that you use for your trading activities.

Procedure

Please refer to the following steps in the [Administration Guide of Trading Platform Integration](https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION) in the help portal:

- Configure Trading Platforms

##### Manage Subscriptions (Optional)

Purpose

Enter your email address to receive email notifications for specific events.

Procedure

Please refer to the following steps in the [Administration Guide of Trading Platform Integration](https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION) in the help portal.

- Manage Subscriptions

##### Configure Field Mapping

Purpose

In this step, you need to set up the field mapping between the external trading platforms and SAP trading platform integration, as well as between the SAP trading platform integration and the SAP S/4HANA Cloud Public Edition system

For example, you need to map the company code 1010 in the SAP S/4HANA Cloud Public Edition system to the equivalent in the external trading platform (for example, REQUESTCOMPANY in 360T) to successfully transfer trade requests and trades information.

Procedure

Please refer to the following steps in the [Administration Guide of Trading Platform Integration](https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION) in the help portal.

- Configure Mappings to Trading Platform Format
- Configure Mappings to Back-End Format
- Configure Mappings to Back-End Format (Intercompany)

|  |
| --- |
| Note You can refer to the Field Mapping Settings Example step in the Appendix for examples. |

##### Configure Business Rules

Purpose

In this step, you define SAP Cloud Platform Business Rules to automate decisions for intercompany FX trading.

Procedure

Please refer to the following section in the [Administration Guide of Trading Platform Integration](https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION) in the help portal.

- Configure Business Rules
    - Trade Request Routing Category Decision
    - Intercompany Trading Scenario Decision
    - Trade Request Values Adaption
    - Markup Markdown Decision
    - Derive which trading partners to use
    - Decision for Creating Intercompany Trades

|  |
| --- |
| Note You can refer to the Business Rules Settings Example step in the Appendix for examples |

##### Manage Counterparties in SAP Trading Platform Integration

Purpose

You can manage your counterparties centrally in the trading platform integration application. Once you start editing the IDs of your counterparty entries, this app acts as your single source of truth for your counterparties.

You have two options for maintaining your counterparties. You can either replicate the counterparty business partners from your back-end system, or create new entries manually in the Manage Counterparties app.

Procedure

Option 1: Replicate counterparties from SAP S/4HANA Cloud Public Edition

To synchronize your counterparties between your back-end system and the trading platform integration application, you need to set up the data replication of business partners which relies on SOAP service communications from the connected back-end system to this application. This entails maintaining the data replication framework and the SOAMANAGER configuration.

For more information on how to set this up, see [SAP Note 2959101](https://me.sap.com/notes/%20SAP%0a%09%09%09%09%09Note%202959101).

Option 2: Create counterparties manually

Create external counterparty

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open Manage Counterparties in SAP trading platform integration. |  |  |
| 2 | Retrieve All Available Counterparties | Choose Go to retrieve all counterparties for your configuration. | All available counterparties are displayed. |  |
| 3 | Create a New Counterparty Manually | Enter the following parameters and choose Save.ID: for example, 10537003.Name: for example, Alternative BP. | The counterparty is created successfully. |  |

Create intercompany counterparty for treasury center company code

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open Manage Counterparties in SAP trading platform integration. |  |  |
| 2 | Retrieve All Available Counterparties | Choose Go to retrieve all counterparties for your configuration. | All available counterparties are displayed. |  |
| 3 | Create a New Counterparty Manually | Enter the following parameters and choose Save.ID: for example, 10401010.Name: for example, BP 1010 in company code 1710.Allocated Company ID: 1010 | The counterparty is created successfully. |  |
| 4 | Enter Details of Trading Platform Profiles | Under group Trading Platform Profiles, choose Create and enter following data:Trading Platform Configuration: <select from dropdown list>Counterparty ID (Trading Platform): for example, 10401010 |  |  |
| 5 | Enter Details of Back-End Profiles | Under group Trading Platform Profiles, choose Create and enter following data and choose Save.Back-End Configuration: <select from dropdown list>Business Partner: for example, 10401010 | The business partner is saved successfully. |  |

Create intercompany counterparty for subsidiary company code

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open Manage Counterparties in SAP trading platform integration. |  |  |
| 2 | Retrieve All Available Counterparties | Choose Go to retrieve all counterparties for your configuration. | All available counterparties are displayed. |  |
| 3 | Create a New Counterparty Manually | Enter the following parameters and choose Save.ID: for example, 17401710.Name: for example, BP 1710 in company code 1010.Allocated Company ID: 1710 | The counterparty is created successfully. |  |
| 4 | Enter Details of Trading Platform Profiles | Under group Trading Platform Profiles, choose Create and enter following data:Trading Platform Configuration: <select from dropdown list>Counterparty ID (Trading Platform): for example, 17401710 |  |  |
| 5 | Enter Details of Back-End Profiles | Under group Trading Platform Profiles, choose Create and enter following data and choose Save.Back-End Configuration: <select from dropdown list>Business Partner: for example, 17401710 | The business partner is saved successfully. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| Treasury Trading via Trading Platforms - External Scenario for FX |  |  |  |
| [Create External FX Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_18) [page ] 26 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | Trade request is created and released. |
| [Review External FX Trade Requests in SAP Trading Platform Integration](#unique_19) [page ] 28 | N/A | Manage Trade Requests | Trade requests are imported into the SAP trading platform integration. |
| [Decline External FX Trade Requests in SAP Trading Platform Integration](#unique_20) [page ] 29 | N/A | Manage Trade Requests | Trade Request is declined. |
| [Group External FX Trade Requests into a Block in SAP Trading Platform Integration (Optional)](#unique_21) [page ] 31 | N/A | Manage Trade Requests | Trade requests are grouped into a block. |
| [Split External FX Trade Requests in SAP Trading Platform Integration (Optional)](#unique_22) [page ] 33 | N/A | Manage Trade Requests | The trade request is split to several sub-trade requests. |
| [Send External FX Trade Requests to External Trading Platform in SAP Trading Platform Integration](#unique_23) [page ] 34 | N/A | Manage Trade Requests | Trade requests are sent to the external trading platform. |
| [Review External FX Trade Request Status in External Trading Platform](#unique_24) [page ] 36 | N/A | N/A | You've reviewed the trade request detail in the external trading platform. |
| [Reset External FX Trade Requests in SAP Trading Platform Integration (Optional)](#unique_25) [page ] 36 | N/A | Manage Trade Requests | You reset the status of a trade request in SAP trading platform integration. |
| [Call Counterparty for Phone Trade](#unique_26) [page ] 37 | N/A | N/A | You get quotation by calling banks. |
| [Analyze Exposure and Check Limit in SAP S/4HANA Cloud Public Edition](#unique_27) [page ] 37 |  |  |  |
| [Review External FX Trade Requests in External Trading Platform](#unique_28) [page ] 38 | N/A | N/A | You've reviewed the trade request detail in the external trading platform. |
| [Create FX Trade in External Trading Platform](#unique_29) [page ] 38 | N/A | N/A | You create a foreign exchange deal request in the external trading platforms. |
| [Generate FX Trades in SAP Trading Platform Integration](#unique_30) [page ] 38 | N/A | Manage Trades | SAP trading platform integration automatically receives and submits the FX transaction to SAP S/4HANA Cloud Public Edition. |
| [Enter Phone Trade Details in SAP Trading Platform Integration](#unique_31) [page ] 39 | N/A | Manage Trades | FX transaction is created in SAP S/4HANA Cloud Public Edition system. |
| [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_32) [page ] 40 | Treasury Specialist - Front Office | Process Spots/Forwards - Collective Processing (TX06)Process OTC Options - Collective Processing (TI91) | FX transaction is created in SAP S/4HANA Cloud Public Edition. |
| Treasury Management Integration for Trading Platforms – Intercompany Scenarios for FX |  |  |  |
| [Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_33) [page ] 43 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | Intercompany FX trade requests are created in the SAP S/4HANA Cloud Public Edition system for the Back-to-Back Trading scenario. |
| [Review Intercompany FX Trade Request in SAP Trading Platform Integration](#unique_34) [page ] 45 | N/A | Manage Intercompany Trade Requests | The Intercompany FX trade requests are imported from SAP S/4HANA Cloud Public Edition into SAP trading platform integration. |
| [Create External FX Trade Requests in SAP Trading Platform Integration](#unique_35) [page ] 46 | N/A | Manage Trade Requests | An external trade request is created automatically in the treasury center company code. |
| [Split External FX Trade Requests in SAP Trading Platform Integration (Optional)](#unique_36) [page ] 47 | N/A | Manage Trade Requests | You split one external trade request into several trade requests. |
| [Send External FX Trade Requests from SAP Trading Platform Integration to External Trading Platform](#unique_37) [page ] 48 | N/A | Manage Trade Requests | You send the external trade requests to External Trading Platform for further process. |
| [Review External FX Trade Request Status in External Trading Platform](#unique_38) [page ] 50 | N/A | N/A | You review the trade requests in the external trading platform. |
| [Create FX Trade in External Trading Platform](#unique_39) [page ] 50 | N/A | N/A | You get quotations in the external trading platform and choose a suitable offer. |
| [Generate FX Trades in SAP Trading Platform Integration](#unique_40) [page ] 51 | N/A | Manage Trades | The FX transactions created in the external trading platform is automatically imported into SAP trading platform integration. |
| [Call Counterparty for Phone Trade](#unique_41) [page ] 52 | N/A | N/A | You get quotations by calling banks. |
| [Enter the Phone Trade Details in SAP Trading Platform Integration](#unique_42) [page ] 52 | N/A | Manage Trades | You manually enter the phone trade details. |
| [External FX Trades Aggregation in SAP Trading Platform Integration](#unique_43) [page ] 54 | N/A | Manage Intercompany Trades | The sub-trade requests are aggregated in SAP trading platform integration. |
| [Generate Intercompany FX Trades in SAP Trading Platform Integration](#unique_44) [page ] 56 | N/A | Manage Intercompany Trade Requests | Once the transactions aggregation is done, the corresponding intercompany transactions are generated automatically. |
| [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_45) [page ] 58 | N/A | Manage Intercompany Trade Requests | FX transactions are automatically created in SAP S/4HANA Cloud Public Edition. |
| [Decline External FX Trade Requests in SAP Trading Platform Integration](#unique_46) [page ] 59 | N/A | Manage Trade Requests | The external trade request is declined. |
| [Decline Intercompany FX Trade Requests in SAP Trading Platform Integration](#unique_47) [page ] 60 | N/A | Manage Intercompany Trade Requests | The intercompany trade requests are declined. |
| [Update the Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_48) [page ] 61 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | The status of the declined trade request becomes Canceled |
| [Reprocess Intercompany FX Trade Requests in SAP Trading Platform Integration](#unique_49) [page ] 62 | N/A | Manage Intercompany Trade RequestsManage Trade Requests | The status of the intercompany trade request is changed to Processed, and the status of the external trade request is Initiated. |
| [Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_50) [page ] 63 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | You create FX intercompany trade requests in SAP S/4HANA Cloud Public Edition system for Manual Trading scenario. |
| [Review Intercompany FX Trade Request in SAP Trading Platform Integration](#unique_51) [page ] 65 | N/A | Manage Intercompany Trade Requests | Intercompany FX trade requests for Manual Trading scenario are imported from SAP S/4HANA Cloud Public Edition into SAP trading platform integration. |
| [Create Intercompany FX Manual Trade in SAP Trading Platform Integration](#unique_52) [page ] 66 | N/A | Manage Intercompany Trade Requests | You manually create intercompany transactions for the intercompany trade requests of intercompany scenario 2: Manual Trading in SAP trading platform integration |
| [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_53) [page ] 67 | Treasury Specialist - Front Office | Process Spots/Forwards - Collective Processing (TX06)Process OTC Options - Collective Processing (TI91) | FX transaction is created in SAP S/4HANA Cloud Public Edition. |
| [Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_54) [page ] 68 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | Trade request is created and released in SAP S/4HANA Cloud Public Edition. |
| [Review Intercompany FX Trade Request in SAP Trading Platform Integration](#unique_55) [page ] 70 | N/A | Manage Intercompany Trade Requests | Trade request is imported into SAP trading platform integration. |
| [Generate Intercompany FX Trades in SAP Trading Platform Integration](#unique_56) [page ] 71 | N/A | Manage Intercompany Trade Requests | Intercompany trades are created automatically with rate set in SAP S/4HANA Cloud Public Edition. |
| [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_57) [page ] 72 | Treasury Specialist - Front Office | Process Spots/Forwards - Collective Processing (TX06)Process OTC Options - Collective Processing (TI91) | Intercompany trades are created in the SAP S/4HANA Cloud Public Edition system. |
| Treasury Trading via Trading Platforms - External Scenario for MM |  |  |  |
| [Create External MM Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_58) [page ] 88 | Cash Management Specialist | Manage Memo Records (F2986) | You create money market trade request in SAP S/4HANA Cloud Public Edition. |
| [Review External MM Trade Request in SAP Trading Platform Integration](#unique_59) [page ] 91 | N/A | Manage Trade Requests | The external MM trade requests are imported into SAP trading platform integration. |
| [Update the Instrument Category of External MM Trade Requests in SAP Trading Platform Integration](#unique_60) [page ] 93 | N/A | Manage Trade Requests | The instrument category of the imported trade request is changed. |
| [Send External MM Trade Requests to External Trading Platform in SAP Trading Platform Integration](#unique_61) [page ] 94 | N/A | Manage Trade Requests | You send the MM trade requests to the external trading platform. |
| [Review External MM Trade Request Status in External Trading Platform](#unique_62) [page ] 95 | N/A | N/A | You review the trade request in the external trading platform. |
| [Reset External MM Trade Requests in SAP Trading Platform Integration (Optional)](#unique_63) [page ] 96 | N/A | Manage Trade Requests | The status of the trade request is reset in SAP trading platform integration. |
| [Call Counterparty for Phone Trade](#unique_64) [page ] 97 | N/A | N/A | You get quotations from banks. |
| [Check Liquidity Forecast in SAP S/4HANA Cloud Public Edition](#unique_65) [page ] 97 |  |  |  |
| [Review Trade Requests in External Trading Platform](#unique_66) [page ] 98 | N/A | N/A | You review the trade request in the external trading platform. |
| [Create Money Market Trade in External Trading Platform](#unique_67) [page ] 98 | N/A | N/A | You create a money market deal request in external trading platforms. |
| [Generate MM Trades in SAP Trading Platform Integration](#unique_68) [page ] 98 | N/A | Manage Trades | The transaction is transferred to SAP trading platform integration and submitted to the SAP S/4HANA Cloud Public Edition system automatically. |
| [Enter the Phone Trade Details in SAP Trading Platform Integration](#unique_69) [page ] 99 | N/A | Manage Trades | You enter the details of the trade into SAP trading platform integration. |
| [Create Money Market Transaction in SAP S/4HANA Cloud Public Edition](#unique_70) [page ] 101 | Treasury Specialist - Back Office | Process MM Transactions - Collective Processing (TM00) | The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. |
| Treasury Management Integration for Trading Platforms – Intercompany Scenarios for MM |  |  |  |
| [Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_71) [page ] 102 | Cash Management Specialist | Manage Memo Records (F2986) | You create intercompany MM trade requests in the SAP S/4HANA Cloud Public Edition system for the Back-to-Back Trading scenario. |
| [Review Intercompany MM Trade Request in SAP Trading Platform Integration](#unique_72) [page ] 105 | N/A | Manage Intercompany Trade Requests | The intercompany MM trade requests are imported from SAP S/4HANA Cloud Public Edition into SAP trading platform integration. |
| [Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration](#unique_73) [page ] 106 | N/A | Manage Trade Requests | The instrument category of the imported trade request is changed. |
| [Create External MM Trade Requests in SAP Trading Platform Integration](#unique_74) [page ] 107 | N/A | Manage Trade Requests | An external MM trade request is created automatically in the treasury center company code. |
| [Send External MM Trade Requests to Trading Platform in SAP Trading Platform Integration](#unique_75) [page ] 108 | N/A | Manage Trade Requests | The external trade requests are sent to the external trading platform. |
| [Review External MM Trade Request Status in External Trading Platform](#unique_76) [page ] 110 | N/A | N/A | You review the trade request status in the external trading platform. |
| [Create MM Trade in External Trading Platform](#unique_77) [page ] 110 | N/A | N/A | You choose a suitable offer. |
| [Generate MM Trades in SAP Trading Platform Integration](#unique_78) [page ] 110 | N/A | Manage Trades | The trades created in the trading platform is automatically imported into SAP trading platform integration. |
| [Call Counterparty for Phone Trade](#unique_79) [page ] 111 | N/A | N/A | You get quotation from banks. |
| [Enter the Phone Trade Details in SAP Trading Platform Integration](#unique_80) [page ] 112 | N/A | Manage Trades | You enter phone trade details in SAP trading platform integration. |
| [Generate Intercompany MM Trades in SAP Trading Platform Integration](#unique_81) [page ] 113 | N/A | Manage Intercompany Trades | An intercompany Money Market transaction will be created in each company code automatically. |
| [Create Money Market Transactions in SAP S/4HANA Cloud Public Edition](#unique_82) [page ] 115 | Treasury Specialist - Back Office | Process MM Transactions - Collective Processing (TM00) | The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. |
| [Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition](#unique_83) [page ] 120 | Cash Management Specialist | Manage Memo Records (F2986) | You create intercompany MM trade requests in the SAP S/4HANA Cloud Public Edition system for the Manual Trading scenario. |
| [Review Intercompany MM Trade Request in SAP Trading Platform Integration](#unique_84) [page ] 122 | N/A | Manage Intercompany Trade Requests | The intercompany MM trade requests are imported from SAP S/4HANA Cloud Public Edition into SAP trading platform integration. |
| [Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration](#unique_85) [page ] 123 | N/A | Manage Intercompany Trade Requests | The instrument category of Money Market is changed. |
| [Create Intercompany Manual Trade in SAP Trading Platform Integration](#unique_86) [page ] 125 | N/A | Manage Intercompany Trade RequestsManage Intercompany Trades | You manually create intercompany MM transactions for the intercompany trade requests of intercompany scenario 2: Manual Trading in SAP trading platform integration. |
| [Create Money Market Transactions in SAP S/4HANA Cloud Public Edition](#unique_87) [page ] 126 | Treasury Specialist - Back Office | Process MM Transactions - Collective Processing (TM00) | The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. |
| Treasury Management Integration for Trading Platform - External Scenario for Money Market Fund |  |  |  |
| [Analyze Liquidity Forecast in S/4HANA Cloud](#unique_88) [page ] 135 | N/A | N/A | You check the liquidity forecast. |
| [Create Money Market Fund Trade in External Trading Platform](#unique_89) [page ] 135 | N/A | N/A | You create a money market fund trade in external trading platforms. |
| [Generate Money Market Fund Trade in SAP Trading Platform Integration](#unique_90) [page ] 136 | N/A | Manage Trades | The money market fund transaction is imported into SAP trading platform integration. |
| [Create Money Market Fund Transactions in SAP S/4HANA Cloud Public Edition](#unique_91) [page ] 137 | Treasury Specialist - Front Office | Process Securities Transactions - Collective Processing (TS00) | The money market fund transaction is created in SAP S/4HANA Cloud Public Edition automatically. |
| [Generate Money Market Fund Trade w/o Known Quantity and Price in SAP Trading Platform Integration](#unique_92) [page ] 138 | N/A | N/A | You create a money market fund trade in external trading platforms. |
| [Create Money Market Fund Transactions w/o Known Quantity and Price in SAP S/4HANA Cloud Public Edition](#unique_93) [page ] 140 | Treasury Specialist - Front Office | Process Securities Transactions - Collective Processing (TS00) | The money market fund transaction is created in SAP S/4HANA Cloud Public Edition automatically. |
| [Update Money Market Fund Trade with Quantity and Price Information in External Trading Platform](#unique_94) [page ] 141 | N/A | N/A | You update a money market fund trade in external trading platforms. |
| [Update Money Market Fund Trade with Quantity and Price Information in SAP Trading Platform Integration](#unique_95) [page ] 141 | N/A | Manage Trades | The updated money market fund transaction is imported to SAP trading platform integration. |
| [Update Money Market Fund Transactions with Quantity and Price Information in SAP S/4HANA Cloud Public Edition](#unique_96) [page ] 142 | Treasury Specialist - Front Office | Process Securities Transactions - Collective Processing (TS00) | The money market fund transaction is updated in SAP S/4HANA Cloud Public Edition automatically. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Treasury Management Integration for Trading Platform - External Scenario for FX

The external scenario handles trades with external counterparties. From SAP S/4HANA Cloud Public Edition point of view, this include two sub-processes: outbound process and inbound process.

- Outbound process: Trade requests created in the SAP S/4HANA Cloud Public Edition system are sent to SAP trading platform integration and then to the external trading platforms. Main steps in outbound process:
    - Create and release trade requests from SAP S/4HANA Cloud Public Edition
    - Import trade requests into SAP trading platform integration
    - Send trade requests from SAP trading platform integration to external trading platforms
- Inbound process: create trades with external counterparties in external trading platform and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition. Main steps in inbound process：
    - Create FX Deal Requests in External Trading Platforms
    - Generate FX Transactions in SAP trading platform integration
    - Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

#### Treasury Trading via Trading Platforms - FX Outbound

In the outbound scenario, external FX trade requests generated in the SAP S/4HANA Cloud Public Edition system can be sent to the external trading platform via SAP trading platform integration on SAP BTP.

##### Create External FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release FX trade requests in the SAP S/4HANA Cloud Public Edition system. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Note Make sure that you’ve made relevant business rule settings so that the trade request is identified as an external trade request. |

Procedure

You have several options to create an external trade request.

Option 1: Trade requests generated in Treasury and Risk Management:

You can create and release trade requests through Balance Sheet Exposure Hedge Request, Cash Flow Exposure Hedge Request or manually.

To create trade requests via hedge requests, follow the following sections in the Foreign Currency Risk Management(1X1) test script:

- Create Trade Request via Balance Sheet Exposure Hedge Request
- Create Trade Request via Cash Flow Exposure Hedge Request

Or to create trade requests manually, execute the following section:

- Create Trade Request Manually

Option 2: Trade requests generated in Cash Management

Perform the following section in the Advanced Cash Operations(J78) test script.

- Cash Trade Request
    - Create and Submit Cash Trade Request for FX
    - Release Cash Trade Request

As an example, create a manual external trade request by executing the following steps.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Request screen is displayed. |  |
| 3 | Enter FX Forward trade request details | Choose Create. On the Trade Request - Create screen, enter the following data and choose Submit.Trade Request ID (Text): for example, External FX Forward trade requestCompany Code: for example,1010Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 1000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month> | The request is processed. |  |
| 4 | Release the trade request | Choose Change. On the Trade Request - Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and name it as Trade Request ID (backend) - External FX Forward 1 |  |
| 5 | Create and release more trade requests | Repeat the above steps to create more trade requests.Note You may also create other instrument category trade requests, for example, FX Spot, FX Non-Deliverable Forward, FX Collar, FX Swap, FX Option, etc. | Note down the Trade Request IDs and name them as Trade Request ID (backend) - External FX Forward 2Trade Request ID (backend) - External FX Forward 3Trade Request ID (backend) - External FX Forward 4Trade Request ID (backend) - External FX Forward 5Trade Request ID (backend) - External FX Forward 6 |  |

##### Review External FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the external FX trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

|  |
| --- |
| Note Make sure that you’ve made relevant business rule settings so that the trade requests are identified as external trade requests. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter the Filters and Reload Page | On the Manage Trade Requests screen, enter the following data and choose Go to reload the page.Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 1/2/3/4/5/6 you’ve noted down in the previous step>Reload the page, and confirm with the new trade request.Note If your trade requests are not showed up automatically, choose Go to refresh the list.Note If the filters section is not displayed, please choose Show Filter to display it.You may click on the Limit Check button to check the limit utilization status in app Manage Trade Requests. | The status of the new trade request is now Initiated |  |

##### Decline External FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You may reject a trade request if it doesn’t follow your company’s trading rules or policies

In this step, you decline an external trade request. Once declined, the trade request can no longer be processed. And the status of the trade request in the SAP S/4HANA Cloud Public Edition system will also be updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go.Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 6 you’ve noted down in previous step> | The following trade request is displayed.Trade Request ID (backend) - External FX Forward 6 |  |
| 3 | Decline a Trade Request | Choose Details ( >) to review the details.On the Mange Trade Requests screen, choose More (…), and choose Decline. | The Reason for Declining screen is displayed. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen, the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined. |  |
| 5 | Reload the page | Choose Go to refresh the page. | The following Trade Request is in the Declined status:Trade Request ID (backend) - External FX Forward 6 |  |

##### Process External FX Trade Requests in SAP Trading Platform Integration

You can process trade requests before you send them to the external trading platforms. You can group several trade requests into a block, or to split one trade request into several trade requests.

###### Group External FX Trade Requests into a Block in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an optional step. In this step, you group several external trade requests into a block to process them at once.

|  |
| --- |
| Note You can’t process the trade request in a block individually. You need to remove it from the block before you can process it individually. |

Procedure

Create a Block

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 1/2/3 you’ve noted down in previous step> | The following three trade requests are displayed.Trade Request ID (backend) – External FX Forward 1Trade Request ID (backend) – External FX Forward 2Trade Request ID (backend) - External FX Forward 3 |  |
| 3 | Create a Block | On the Manage Trade Requests screen, select the checkboxes before the above mentioned trade requests with the Initiated status, and choose Create Block.Choose Create Block in the dialog box to confirm the creation of the block.Note In case of FX swap or FX collar option, you should select both legs. | The following message is displayed:Block XXXXXXXXXXXXXXX createdNote You may find the block ID XXXXXXXXXXXXXXX in the Block ID column.A block is created for the following 3 trade requests:Trade Request ID (backend) – External FX Forward 1Trade Request ID (backend) – External FX Forward 2Trade Request ID (backend) - External FX Forward 3 |  |

Remove a Trade Request From a Block

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Re-quest ID (backend) - External FX Forward 1/2/3 you’ve noted down in previous step> | The following three trade requests in the same block are displayed.Trade Request ID (backend) – External FX Forward 1Trade Request ID (backend) – External FX Forward 2Trade Request ID (backend) - External FX Forward 3 |  |
| 3 | Remove a Trade Request From a Block | On the Manage Trade Requests screen, select the checkbox before trade request ID (backend) - External FX Forward 1, choose Undo Block.Choose Undo Block in the dialog box to confirm the removal of the trade request from the block. | The following message is displayed:Trade requests removed from blockThe following trade request is removed from the block.Trade Request ID (backend) – External FX Forward 1 |  |

Assign a Trade Request to an Existing Block

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Re-quest ID (backend) - External FX Forward 1/2/3 you’ve noted down in previous step> | The following three trade requests are displayed:Trade Request ID (backend) – External FX Forward 1Trade Request ID (backend) – External FX Forward 2Trade Request ID (backend) - External FX Forward 3 |  |
| 3 | Add a Trade Request to a Block | On the Manage Trade Requests screen, select the checkbox before Trade Request ID (backend) - External FX Forward 1, choose Assign to Block.In the Select Block dialog box, select the block ID you just created in the previous step, and choose Assign to Block. | The following message is displayed:Trade requests assigned to blockThe following trade request is added back to the block:Trade Request ID (backend) – External FX Forward 1 |  |

###### Split External FX Trade Requests in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you split one trade request into several trade requests to process separately.

Procedure

Table 2: Split a Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 4 you’ve noted down in previous step> | The following trade request is displayed:Trade Request ID (backend) – External FX Forward 4 |  |
| 3 | Split a Trade Request | On the Manage Trade Requests screen, select the checkbox before Trade Request ID (backend) - External FX Forward 4, choose Split.On the Select Split Criteria screen, Choose Create, and enter following data, and choose Split:1: enter an amount that’s less than the Remaining amount, for example, 302: enter another amount that’s less than the Remaining amount, for example, 40 | The following message is displayed:Splitting of trade request was successful. |  |

Table 3: Undo Split of a Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Undo Split of a Trade Request | On the Manage Trade Requests screen, select the checkboxes before the newly created trade requests via splitting, choose Undo Split.Choose Undo Split on the Confirmation screen. | The following message is displayed on the Undo Split of Trade Requests - Result screen:Split of trade request was reversed.The split of following trade request is reversed:Trade Request ID (backend) - External FX Forward 4 |  |

##### Send External FX Trade Requests to External Trading Platform in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you send trade requests to the external trading platform.

Prerequisite

An external trade request has been transferred to the SAP trading platform integration from SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 4/5 you’ve noted down in previous step> | The following trade requests are displayed:Trade Request ID (backend) – External FX Forward 4Trade Request ID (backend) – External FX Forward 5 |  |
| 3 | Goto De-tailed Page | Choose Details (arrow > ) to go to the detailed page. | Note down the Trade Request ID and name them as following:Trade Request ID (SAP trading platform integration) – External FX Forward 4Trade Request ID (SAP trading platform integration) – External FX Forward 5 |  |
| 4 | Send Trade Request | Choose Close to close the detailed screen. Find your trade request and choose the checkboxes at the beginning of the two lines, then choose Send.In the dialog box of Confirmation screen, choose Send to confirm. | Trade requests are sent to the external trading platform. |  |
| 5 | Reload Page | Reload the page, and confirm the status of the trade request is Sent to Trading Platform. | The status of the trade request is now Sent to Trading Platform. |  |

##### Review External FX Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the external trading platform.

Prerequisite

You’ve sent trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

##### Reset External FX Trade Requests in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an optional step. In some cases, you may need to reset the status of a trade request in SAP trading platform integration.

For example, if a trade request has been sent to the external trading platform and the status is In Process or Received by Trading Platform, but it is not available in the external trading platform. In this case, you may reset the status of this trade request and resend it to the trading platform.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 4 you’ve noted down in previous step> | The following trade requests is displayed.Trade Request ID (backend) – External FX Forward 4 |  |
| 3 | Reset a Trade Request | On the Manage Trade Requests screen, select the checkbox before Trade Request ID (backend) - External FX Forward 4, choose Details(arrow  ).On the Trade Request screen, choose More(...) > Reset .Choose Reset in the subsequent Warning dialog box. | The following message is displayed:Trade request was reset. |  |

##### Call Counterparty for Phone Trade

Purpose

If you decide to make the deal via phone instead of sending the trade request to the external trading platform, you need to call banks and get quotations.

Procedure

This is a step outside of the SAP S/4HANA Cloud Public Edition system, SAP trading platform integration and the external trading platforms.

#### Treasury Trading via Trading Platforms - FX Inbound

##### Analyze Exposure and Check Limit in SAP S/4HANA Cloud Public Edition

Purpose

In this step, you check and analyze the exposure and limit utilization that are described in the Foreign Currency Risk Management (1X1) test script.

Procedure

Perform the following steps in the Foreign Currency Risk Management (1X1) test script.

- Analyze Exposure and Agree on Hedging Actions
- Check Limit Utilization Report

##### Review External FX Trade Requests in External Trading Platform

Purpose

In this step, you review the trade request that you have sent to the external trading platform.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or Trading Platform Integration apps on SAP BTP. You need to do this step in the External Trading Platforms.

|  |
| --- |
| Note You may use the following trade request IDs you’ve noted down to search for your trade requests in the external trading platforms:Trade Request ID – External FX Forward 5 |

##### Create FX Trade in External Trading Platform

Purpose

In this step, you create a foreign exchange trade in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or SAP trading platform integration on SAP BTP. You need to do this step in External Trading Platforms.

|  |
| --- |
| Note You may note down the Trade ID and name it as Trade ID – external trading platform. |

##### Generate FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once an FX trade is closed in the external trading platforms, SAP trading platform integration will automatically receive and submit the FX trade to SAP S/4HANA Cloud Public Edition. If you want to check the FX trade data in SAP trading platform integration, you can follow the following procedures to check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. | A list of all FX trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go.Trade Request ID : <Trade Request ID – External FX Forward 5 > | The FX trade you created in external trading platforms in the previous step is displayed in SAP trading platform integration.The status of the FX trade should be Successful. |  |
| 3 | Goto Detailed Page | Choose Details (arrow > ) to go to detailed page. | The detailed trade information is displayed.Note down the Financial transaction:XXXX/XXXXXXXXXXXXXNote The first 4 chars XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

##### Enter Phone Trade Details in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you manually maintain the FX trade agreed with your counter-party bank via phone in the Manage Trades app.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

A trade request has been retrieved from the SAP S/4HANA Cloud Public Edition system into the Manage Trade Requests app.

Procedure

Table 4: Create Phone Trade:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - External FX Forward 4 you’ve noted down in previous step> |  |  |
| 3 | Enter Trade Details | Select the checkbox in front of the trade request choose Create Phone Trade, the Manage Trades screen is displayed.Enter the trade details and choose Save.Note Please make sure you enter all the mandatory fields such as Valuation Date, Spot Rate, etc.Note Please use the right counterparty for the company code, for example, 0010537001 for company code 1010, and 0017537001 for company code 1710Note If mentioned counterparty is not available, then follow the prerequisites step Manage Counterparties in SAP trading platform integration, Option 2 to create the counterparty. | The trade is in the Successful status. |  |

##### Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The FX transactions are automatically created in the SAP S/4HANA Cloud Public Edition system by Treasury Trading via Trading Platforms. In this step, you can check the FX transaction data in the SAP S/4HANA Cloud Public Edition system.

Depending on the FX transaction you created in the previous step, you may need to use different apps to review the FX contract.

You can use the following apps to check the FX transaction data in the SAP S/4HANA Cloud Public Edition system:

- Process Spots/Forwards - Collective Processing (TX06)
- Process OTC Options - Collective Processing (TI91)

Procedure

Option 1: For FX spot, FX forward, FX swap or FX NDF.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06). | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute：Company code: <The first 4 chars of the Financial Transaction Reference ID from previous step you noted down in previous step>Transaction: <The last 13 chars of the Financial Transaction you noted down in previous step> | In the Forex: Collective Processing screen, the FX transaction is displayed under title FX: Collective Processing – Results. |  |
| 4 | Display the FX transaction details | Select the checkbox at the beginning of the FX transaction and choose Display.Note You can now compare the FX transaction data on the external trading platform with that in the SAP S/4HANA Cloud Public Edition system. | The FX transaction is displayed. The FX transaction data should be consistent with that in external trading platforms. |  |

Option 2: For FX option.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process OTC Options - Collective Processing (TI91). | The OTC Options: Collective Processing view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:External Reference: for example, <enter the trade ID in the external trading platform> | The OTC Options: Collective Processing screen is displayed |  |
| 4 | Display the FX transaction details | Select the checkbox at the beginning of the FX transaction and choose Display.Note You can now compare the FX transaction data in external trading platforms with that in the SAP S/4HANA Cloud Public Edition system. | The FX transaction is displayed. The FX transaction data should be consistent with that in external trading platforms. |  |

### Treasury Management Integration for Trading Platform – Intercompany Scenarios for FX

This scenario handles trades between two company codes, for example, a subsidiary company code and a headquarters company code as treasury center. This test script assumes that the following data exists in your in S/4HANA Cloud system:

Company code:

- 1710 Initiate the intercompany trade requests process and fulfill them with Intercompany Trades with company code 1010.
- 1010 Receive the intercompany trade requests from 1710 and fulfill them with Intercompany Trades and make reversing trade with external counterparties for Back-to-Back scenario.

External Business Partner:

- 10537001 (in company code 1010) Representing an external counterparty.

Intercompany Business Partner

- 17401710 (in company code 1010) Representing intercompany counterparty for 1710 in company code 1010
- 10401010 (in company code 1710) Representing intercompany counterparty for 1010 in company code 1710

#### Foreign Exchange Intercompany scenario 1: Back-to-Back Trading (Subsidiary)

##### Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany FX trade requests in the SAP S/4HANA Cloud Public Edition system for the Back-to-Back Trading scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request in the company code is identified as an intercompany trade request and the intercompany scenario is 1: Back-to-Back Trading (Subsidiary). You can refer to the relevant section in the Appendix for examples.

Procedure

You have several options to create an intercompany FX trade request:

1. Trade requests generated in Treasury and Risk Management

You can create FX trade requests through balance sheet exposure hedge request, cash flow exposure hedge request or manually.

For details, refer to the following sections in the Foreign Currency Risk Management(1X1) test script:

-
    - Create Trade Request via Balance Sheet Exposure Hedge Request
    - Create Trade Request via Cash Flow Exposure Hedge Request

1. Trade requests generated in Cash Management

For details, refer to the Cash Trade Request section of the Advanced Cash Operations(J78) test script.

As an example, create manual intercompany FX trade requests by executing the following steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Enter FX Forward Trade Request Details | Choose Create Trade Requests. On the Trade Request – Create screen, enter the following data and choose Submit.On the General tab:Trade Request ID (Text): for example, <Intercompany FX Forward trade request – B2B >Company Code: for example, 1710Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 1000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month>On the Additional Attributes tab:Assignment: B2B_TRADING_SB | The request is submitted. |  |
| 4 | Release the Trade Request | Choose Change. On the Trade Request – Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and name it as Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1 |  |
| 5 | Create and Release More Trade Requests | Repeat the above steps to create more trade requests.Note You may also create other instrument category trade requests, for example, FX Spot, FX Non-Deliverable Forward, FX Collar, FX Swap, FX Option, etc. | Note down the Trade Request IDs and named them as:Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 2Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 3Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 4Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 5Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 6 |  |

##### Review Intercompany FX Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany FX trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1/2/3/4/5/6>Confirm the following:The Status of the Back-to-Back Trade Requests is Processed.Fulfillment Status is InitialScenario is Back-to-Back Trading (Subsidiary)Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests is displayed.Trade Request ID (backend) – Back-to-Back Trading FX Forward 1/2/3/4/5/6This means these Trade requests got imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow > ) to go to detailed page. | Note down the Trade Request ID and name it as following:Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 1 |  |
| 5 | Repeat for All of the Trade Re-quests |  | Note down the Trade Request ID and name them as following:Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 2Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 3Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 4Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 5Trade Request ID (SAP trading platform integration) – Back-to-Back Trading FX Forward 6 |  |

##### Create External FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a Back-to-Back Trading intercompany trade request in the subsidiary company code is imported into SAP trading platform integration, an external trade request will be created automatically in the treasury center company code.

You can review the automatically created external trade requests as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the Automatically Generated External Trade Requests | On the Manage Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1/2/3/4/5/6 you’ve noted down in the previous step> | The status of the external trade requests is Initiated. |  |

##### Process External FX Trade Requests in SAP Trading Platform Integration

In this section, you further process the trade requests created automatically when importing the intercompany trade requests into SAP trading platform integration.

###### Split External FX Trade Requests in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you split one external trade request into several trade requests, which you can process separately. For example, if the amount of the original trade request is too big, you may use this function to split it into small amounts. Later in the external trading platform, you can make separate trades with different counterparties.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the External Trade Request | On the Manage Trade Requests screen, enter the following data:Trade Request ID (Back End): <Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1>Choose Go. | The external trade request is displayed. |  |
| 3 | Split the External Trade Request | On the Manage Trade Requests screen, select the checkbox before the external trade request, choose Split.On the Select Split Criteria screen, enter the following data, and choose Split:Enter an amount that’s less than the Remaining amount, for example, 30Note The external trade request to be split should have the Initiated or Edited status. | The following message is displayed:Splitting of trade request was successful.The external trade request of Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1 has been split into two sub-trade requests. |  |
| 4 | Split Other External Trade Requests | Repeat the above steps for the external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 2 and split it into three sub-trade requests.Repeat the above steps for the external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 3 and split it into two sub-trade requests.Repeat the above steps for the external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4and split it into three sub-trade requests. | The external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 2 has been split into three sub-trade requests.The external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 3 has been split into two sub-trade requests.The external trade request of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4 has been split into three sub-trade requests. |  |

###### Send External FX Trade Requests from SAP Trading Platform Integration to External Trading Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the external trade requests are valid, you may send the external trade requests to External Trading Platform for further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests | A list of trade requests is displayed. |  |
| 2 | Display the External Trade Request(s) | On the Manage Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 1>Note If you have split the external trade request in previous step, then more than one trade request is displayed. | The two sub-trade requests of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 1 are displayed.Go to the detailed page of the trade requests and note down the trade request IDs:XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX |  |
| 3 | Send External Trade Request(s) | Select the checkbox(es) of all the external trade request(s) under the same Back End Trade Request ID, and choose Send.Select the trading platform in the Select Trading Platform Profile dialog box and choose OK to confirm. | The two sub-trade requests of the following backend trade request have been sent to external Trading platform:Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 1 |  |
| 4 | Reload Page | Reload the page, and confirm the status of the trade request(s) is Sent to trading platform. | The status of the trade request(s) is now Sent to Trading Platform. |  |
| 5 | Send other Trade requests to External Trading Platforms | Repeat the above steps and send two sub-trade requests of following trade request to external trading platforms and leave one sub-trade request open so that you can do manual aggregation in later steps.Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 2Note If you get following message, this means the sub-trade request you are sending is the parent trade request. Once split, one sub-trade request is considered as the parent trade request and all others are considered as child trade requests. You can't send the parent trade request before sending all child trade request.Trade request with UUID XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX cannot be sent because it has been split. All trade requests belonging to the original request have to be sent out or declined first. | The two sub-trade requests of the following backend trade request have been sent to the external Trading platforms:Trade Request ID (backend) - Back-to-Back Trading SB FX Forward 2 |  |

###### Review External FX Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the external trading platform.

Prerequisite

You’ve sent trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

|  |
| --- |
| Note You may use the trade request IDs you’ve noted down in previous step to search for your trade requests in the external trading platforms. |

###### Create FX Trade in External Trading Platform

Purpose

In this step, you create foreign exchange trades for the trade requests you’ve reviewed in previous step in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system. You need to do this step in External Trading Platforms.

Note down the IDs of the FX Trade you created in the external trading platform. This ID will be filled in the External reference field in the Manage Trades app in Trading Platform Integration.

|  |
| --- |
|  |

Make sure you have created external trades for both sub-trade requests of the following Trade request (Backend):

- Trade Request ID (backend) – Back-to-Back SB Trading FX Forward 1
- Trade Request ID (backend) – Back-to-Back Trading FX Forward 2

###### Generate FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The FX trades created in the external trading platform will be automatically imported into SAP trading platform integration. Follow the steps below to review the FX trades in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. | A list of all FX trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:External reference: <Reference IDs noted from the previous step>Note You may also filter by Trade request IDs you’ve noted down in previous step.(XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX) | The FX trades you created in external trading platforms in the previous step are displayed in SAP trading platform integration.The status of the FX trades should be Successful. |  |

###### Call Counterparty for Phone Trade

Purpose

If you decide to make the deal via phone for the external trade request, you need to call banks and get quotations.

Procedure

This is a step outside of the SAP S/4HANA Cloud Public Edition system, SAP trading platform integration and the external trading platforms.

###### Enter the Phone Trade Details in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Like the external scenario, you may also fulfill the external trade requests of intercompany trade requests via phone trade. In this step, you will manually enter the phone trade details for following trade requests:

- Trade Request ID (backend) - Back-to-Back Trading FX Forward 3
- Trade Request ID (backend) - Back-to-Back Trading FX Forward 4

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Prerequisite

An intercompany trade request has been retrieved from SAP S/4HANA Cloud Public Edition into the Manage Intercompany Trade Requests app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 3> | The two sub-trade requests of the following intercompany trade request are displayed.Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 3 |  |
| 3 | Create Phone Trade | Select the checkbox of child sub-trade request whose Parent ID is blank, choose Create Phone Trade, the Manage Trades screen is displayed. Enter the trade details and choose Save.Repeat this step to create phone trade for the other sub-trade request.Note Please first select the sub-trade request with Parent ID to create phone trade. Otherwise an error message will occur. | Both sub-trade requests of following intercompany trade request are fulfilled:Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 3 |  |
| 4 | Create Phone Trade for Sub-trade Requests of Another Intercompany Trade Request | Repeat the above steps to create two phone trades for two out of three sub-trade requests of Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4Note Please use the right counterparty for the company code, for example, 0010537001 for company code 1010, and 0017537001 for company code 1710 | Two out of three sub-trade requests of following intercompany trade requests have been fulfilled by phone trades:Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4 |  |

###### External FX Trades Aggregation in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For each intercompany trade request, you can split the corresponding external trade request into several sub-trade requests and close them one-by-one in the external trading platform. If the fulfilled sub-trade requests meet the field matching requirement, they can be aggregated in SAP trading platform integration.

Automatic Aggregation:

If all the sub-trade requests of a back-to-back intercompany trade request are fulfilled, SAP trading platform integration will aggregate all the sub-trades created automatically and generate intercompany FX trades accordingly.

Manual Aggregation:

If only part of the sub-trade requests is fulfilled, for those fulfilled parts, you have the option to manually aggregate them.

Procedure

Automatic Aggregation:

First get the intercompany trade request ID.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:Trade Request ID (Back End): < Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 1> or <Trade Request ID (backend) - Back-to-Back Trading FX Forward 3> | The Intercompany Trade Request is displayed. |  |
| 3 | Go to Detailed Screen | Choose Details (>) | The detailed screen of the intercompany trade request is displayed.Note down the intercompany trade request ID (SAP trading platform integration) XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX. |  |

Display aggregated trades

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | The Manage Intercompany Trades screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:Trade Request ID: <The intercompany trade request ID(SAP trading platform integration)noted down in previous step> | Since the corresponding external trade request of intercompany trade request is split into two trade requests, the following trades are displayed. You can see the following four new entries in the table:Two intercompany trades in both company codes with the Successful statusTwo Aggregation Candidate trades with the Aggregated status. |  |

Manual Aggregation:

Prerequisite: You've split a back-to-back trade request and split it into several sub-trade requests and fulfill some of them.

First get the intercompany trade request ID.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Enter Filter | Enter the following data and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4> | The intercompany trade request is displayed. |  |
| 3 | Go to Detailed Screen | Choose Details (>) | The detailed screen of the intercompany trade request is displayed.Note down the intercompany trade request ID (SAP trading platform integration) XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX and name it as Intercompany trade request for manual aggregation - SB FX Forward 4 (SAP trading platform integration). |  |

Manual aggregation for Manual aggregation for Trade Request ID (backend) - Back-to-Back Trading FX Forward 4

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | The Manage Intercompany Trades screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:Trade Request ID: <Intercompany trade request for manual aggregation - SB FX Forward 4 (SAP trading platform integration)> | Since the corresponding external trade request of the intercompany trade request Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 4 is split into three sub-trade requests, and only two of them are fulfilled, the following trades are displayed:two trades with the Pending status are displayed. |  |
| 3 | Manual Aggregate the Pending trades | Select the checkboxes of the two entries, and choose Aggregate.Choose OK to confirm the aggregation. | The status of the pending trades are changed to Aggregated. |  |
| 4 | Display the Aggregated trades | Choose Go to refresh the page. | Since the corresponding external trade request of the intercompany trade request is split into three sub-trade requests, and only two of them are manually aggregated, the following trades are displayed:two intercompany trades are generated in each company code with status SuccessfulAggregation candidate trades with status Aggregated |  |
| 5 | Manual Aggregation for Other Intercompany Trade Requests | Repeat the above steps to do manual aggregation for the following trade request:Trade Request ID (backend) - Back-to-Back SB Trading FX Forward 2 |  |  |

###### Generate Intercompany FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. In the Back-to-Back Trading scenario, once the transactions aggregation is done, SAP trading platform integration will generate the corresponding intercompany transactions automatically.

You may follow the steps described below to display the intercompany FX transactions.

|  |
| --- |
| Note The contract rate of intercompany FX transactions is determined by FX rate of the external FX transaction and Markup Markdown Decision rule. |

Prerequisite

If the external transaction request is not split, then once it’s fulfilled, an intercompany transaction will be automatically generated in each company code.

If the external transaction request is split and manual or automatic aggregated, one or more intercompany transactions will be automatically generated in each company code.

Procedure

First get the intercompany transaction request ID.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:transaction Request ID (Back End): <transaction Request ID (backend) - Back-to-Back SB Trading FX Forward 3> | The intercompany transaction Request is displayed.The status of the intercompany transaction request is CompletedThe Fulfillment Status is Fulfilled. |  |
| 3 | Go to Detailed Screen | Choose Details (>) | The detailed screen of the intercompany transaction request is displayed.Note down the intercompany transaction request ID (SAP trading platform integration) XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX and name it as Intercompany transaction request for manual aggregation - SB FX Forward 3 (SAP trading platform integration). |  |

Check Intercompany Transactions

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | The Manage Intercompany Trades screen is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:Transaction Request ID: <Intercompany transaction request for manual aggregation - SB FX Forward 3(SAP trading platform integration)> | Since the corresponding external transaction request of the intercompany transaction requests is split into two sub-transaction requests, and both of them are fulfilled, the following transactions are displayed:two intercompany transactions in each company codes.two aggregated transactionsNote The Financial Transactions field in the detailed screen is the transaction ID in SAP S/4HANA Cloud Public Edition. You can use this number to search for the transaction in the SAP S/4HANA Cloud Public Edition system. |  |
| 4 | Repeat to Check Other Intercompany Transactions | Repeat the above steps to check the intercompany transactions for other intercompany transaction requests:transaction Request ID (backend) - Back-to-Back SB Trading FX Forward 4 | Since the corresponding external transaction request of the intercompany transaction request is split into three sub-transaction requests, and only two of them are manually aggregated, the following transactions are displayed:two intercompany transactions are generated in each company codes.2 aggregated transactionsNote The Financial Transactions field in the detailed screen is the transaction ID in SAP S/4HANA Cloud Public Edition. You may use this number to search for the transaction in the SAP S/4HANA Cloud Public Edition system. |  |

###### Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. In the intercompany scenario, the Trading Platform Integration application will automatically send the FX transactions (one external transaction with the external counterparty, and two intercompany transactions) to the SAP S/4HANA Cloud Public Edition system once they are created successfully in the Trading Platform Integration application on SAP BTP.

You may follow the following section under Treasury Trading via Trading Platforms - FX Inbound of this test script to check the FX transactions data in the SAP S/4HANA Cloud Public Edition.

- [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_32) [page ] 40

|  |
| --- |
| Note You may use the financial transactions you noted down to filter the FX transactions. |

###### Decline FX Trade Requests in SAP Trading Platform Integration (Optional)

Purpose

You may reject the intercompany trade requests if it doesn’t follow your company’s trading rules or policies.

Prerequisite

An intercompany trade request has been imported into the Trading Platform Integration application from the SAP S/4HANA Cloud Public Edition systems.

###### Decline External FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you decline the external trade request which is created when importing the intercompany trade request. Once declined, the external trade request can no longer be further processed.

After you decline the external trade request, you have two options to further process the intercompany trade request in the Trading Platform Integration application on SAP BTP:

- Decline the intercompany trade request

If you choose to decline the intercompany trade request, then the intercompany trade request status will change to Declined and the trade request in the SAP S/4HANA Cloud Public Edition system will be canceled. No further process could be done for the intercompany trade request.

- Reprocess the intercompany trade request

If you choose to reprocess the intercompany trade request, then the intercompany trade request status will change to Processed and another external trade request will be created in the Trading Platform Integration application and you may further process the external trade request, for example, fulfill it.

Prerequisite

Please recreate and release intercompany FX Back-to-Back trade requests and note down the trade request IDs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the Automatically Generated External Trade Requests | On the Manage Trade Requests screen, enter following data, and choose Go:Trade Request ID (Back End):<Trade request IDs (back end) you noted down in the previous step> | The trade requests that you’ve noted down in the previous step are displayed on the screen. |  |
| 3 | Decline The External Trade Request | On the Manage Trade Requests screen, select the checkbox in the front of the trade request you want to decline, and choose Additional Options > Decline. | The Reason for Declining dialog box is displayed. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined.Now the trade request’s status is Declined. |  |

###### Decline Intercompany FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the external trade request of an intercompany Back-to-Back FX trade request has been declined, you can decline the intercompany trade request.

In this step, you decline the intercompany trade requests. Once the intercompany trade request is declined in the Trading Platform Integration application, the status of the corresponding trade request in SAP S/4HANA Cloud Public Edition will be automatically changed to Canceled and the whole process is done.

Prerequisite

The external trade request of the intercompany Back-to-Back FX trade request has been declined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Display the Intercompany Trade Requests | Choose Go. | A list of intercompany trade requests is displayed.Check the status of the intercompany trade requests. |  |
| 3 | Decline the Intercompany Trade Request | Select the checkbox in the front of the trade request that you want to decline.Choose Additional Options > Decline . | The Reason for Declining dialog box displays. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined. |  |
| 5 | Refresh to check the Status of the Intercompany Trade Request | Choose Go to refresh the list | Now the intercompany trade request’s status is Declined. |  |

###### Update the Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Purpose

Once the intercompany trade request is declined in the Trading Platform Integration application, the status of the corresponding trade request in the SAP S/4HANA Cloud Public Edition system is automatically updated to Canceled and the whole process is done.

This is an automatic step. Please follow the following section of this test script to check the status of the intercompany trade requests.

- Review External FX Trade Request Status in SAP S/4HANA Cloud Public Edition

|  |
| --- |
| Note The status of the intercompany trade request should be Canceled. |

Prerequisite

You have declined the intercompany trade request in the Trading Platform Integration application.

###### Reprocess Intercompany FX Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reprocess the intercompany Back-to-Back trade requests. Once the intercompany trade request is reprocessed, the status will be changed to Processed and the corresponding external trade request will be automatically created again and ready for further processing.

Prerequisite

You have declined the related external trade request.

Procedure

Table 5: Reprocess the intercompany trade request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Display the Intercompany trade requests | Choose Go.Note You may use Trade Request ID (Back End) as the filter. | A list of intercompany trade requests is displayed.The status of the intercompany trade request should be Technical error. |  |
| 3 | Decline the intercompany trade request | Select the checkbox in front of the trade request that you want to reprocess.Choose Reprocess.A warning message shows up. Choose OK to confirm. |  |  |
| 4 | Refresh to Check the Status of the intercompany Trade Request | Choose Go to refresh the list | Now the intercompany trade request’s status is ProcessedNote down the trade request ID (backend). |  |

Table 6: Check the Status of External Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the Automatically Generated External Trade Requests | On the Manage Trade Requests screen, enter following data:Trade Request ID (Backend):<Trade request IDs (back End) that you’ve noted down in previous step>Choose Go. | A new line of the external trade request is displayed and the status is Initiated. |  |

#### Foreign Exchange Intercompany scenario 2: Manual Trading

##### Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany FX trade requests in the SAP S/4HANA Cloud Public Edition system for the Manual Trading scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Note Make sure that you’ve made relevant business rule settings so that the trade request is identified as an intercompany trade request and the intercompany scenario is 2: Manual Trading. You may refer to the relevant section in the Appendix for examples of business rule settings. |

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Procedure

You have several options to create an intercompany FX trade request. Please refer to the following section of this test script:

- Foreign Exchange Intercompany scenario 1: Back-to-Back Trading (Subsidiary)
    - Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Please follow the steps below to create intercompany trade requests manually for the Manual Trading scenario:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests screen is displayed. |  |
| 3 | Enter FX Forward Trade Request Details | Choose Create Trade Requests. On the Trade Request - Create screen, enter the following data and choose Submit.On the General tab,Trade Request ID (Text): for example, <Intercompany FX Forward trade request - Manual>Company Code: for example, 1710Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 2000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month>On the Additional Attributes tab,Assignment: MANUAL_TRADING | The request is submitted. |  |
| 4 | Release the Trade Request | Choose Change. On the Trade Request - Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and named it as Trade Request ID (backend) - Manual Trading FX Forward 1 |  |
| 5 | Create and Release More Trade Requests | Repeat the above steps to create more trade requests.Note You may also create other instrument category trade requests, for example, FX Spot, FX Non-Deliverable Forward, FX Collar, FX Swap, FX Option, etc. | Note down the Trade Request IDs and named them as Trade Request ID (backend) - Manual Trading FX Forward 2 and Trade Request ID (backend) - Manual Trading FX Forward 3 |  |

##### Review Intercompany FX Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review intercompany FX trade requests for Manual Trading scenario sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter following data and choose Go.Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - Manual Trading FX Forward 1/2/3>Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests are displayed.Trade Request ID (backend) - Manual Trading FX Forward 1/2/3This means these Trade requests are imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details(arrow > ) to go to detailed page.Confirm the following information:Status of the Manual Trade Requests is Process Manually.Fulfillment Status is InitialScenario is Manual Trading | Note down the Trade Request ID and name it as following:Trade Request ID (SAP trading platform integration) - Manual Trading FX Forward 1 |  |

##### Create Intercompany FX Manual Trade in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you manually create intercompany trades for the intercompany trade requests of intercompany scenario 2: Manual Trading in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration, and choose Go. | A list of intercompany trade requests is displayed. |  |
| 2 | Enter Filter | On the Manage Intercompany Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) - Manual Trading FX Forward 1> | The intercompany trade request is displayed and the status is Initiated. |  |
| 3 | Create Manual Trade | Select the checkbox in front of the trade request, choose Create Manual Trade. | The Manage Intercompany Trades screen is displayed.New Manual Intercompany Trade is displayed right under the header. |  |
| 4 | Enter the Manual Trade Details | On the Manage Intercompany Trades screen, fill out all mandatory fields and choose Create.Note Depending on the instrument type, different trade information need to be entered. | The Manage Intercompany Trades screen is displayed. And the following message is displayed:Trade Created |  |
| 5 | Display the Intercompany transactions | On the Manage Intercompany Trades screen, enter following data and choose Go:Trade Request ID: <Trade Request ID (SAP trading platform integration) - Manual Trading FX Forward 1>Note If the filters section is not displayed, please choose Show Filter to display it. | Two intercompany transactions are displayed.Note down the Financial Transaction XXXX/XXXXXXXXXXXXX. |  |

##### Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. In the intercompany scenario, the FX transactions (for example, without external trade request splitting, one external transaction with the external counterparty, and two intercompany transactions) are automatically sent from SAP trading platform integration to SAP S/4HANA Cloud Public Edition once they are created successfully in SAP trading platform integration.

You may follow the following section under Treasury Trading via Trading Platforms - FX Inbound of this test script to check the FX transactions data in the SAP S/4HANA Cloud Public Edition:

- [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_32) [page ] 40

|  |
| --- |
| Note You may use the financial transactions you noted down to filter the FX transactions. |

#### Foreign Exchange Intercompany scenario 3: Automated Trading

##### Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany FX trade requests in the SAP S/4HANA Cloud Public Edition system for the Automated Trading scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Note Currently this scenario only supports the following foreign exchange transactions:FX SpotFX ForwardFX NDF |

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request in the company code is identified as an intercompany trade request and the intercompany scenario is 3: Automated Trading. You can refer to the relevant section in the Appendix for examples.

Procedure

You have several options to create an intercompany FX trade request:

1. Trade requests generated in Treasury and Risk Management

You can create FX trade requests through balance sheet exposure hedge request, cash flow exposure hedge request or manually.

For details, refer to the following sections in the Foreign Currency Risk Management(1X1) test script:

-
    - Create Trade Request via Balance Sheet Exposure Hedge Request
    - Create Trade Request via Cash Flow Exposure Hedge Request

1. Trade requests generated in Cash Management

For details, refer to the Cash Trade Request section of the Advanced Cash Operations(J78) test script.

As an example, create manual intercompany FX trade requests by executing the following steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Enter FX Forward Trade Request Details | Choose Create Trade Requests. On the Trade Request – Create screen, enter the following data and choose Submit.On the General tab:Trade Request ID (Text): for example, <Intercompany FX Forward – AUTO_TRADING>Company Code: for example, 1710Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 1000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month>On the Additional Attributes tab:Assignment: AUTO_TRADING | The request is submitted. |  |
| 4 | Release the Trade Request | Choose Change. On the Trade Request – Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and name it as Trade Request ID (backend) – Automated Trading FX Forward 1 |  |

##### Review Intercompany FX Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany FX trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) – Auto Trading FX Forward 1>Confirm the following:The Status of the Automated Trading trade requests is Completed.Fulfillment Status is FulfilledScenario is Automated TradingNote If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests is displayed.Trade Request ID (backend) – Auto Trading FX Forward 1This means this Trade request got imported into SAP trading platform integration. And the intercompany trades are also created automatically. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow > ) to go to detailed page. | Note down the Trade Request ID and name it as following:Trade Request ID (SAP trading platform integration) – Auto Trading FX Forward 1 |  |

##### Generate Intercompany FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once an Automated Trading intercompany trade request in the subsidiary company code is imported into SAP trading platform integration, the SAP trading platform integration will create intercompany FX trades automatically in both company codes based on the configurations (Markup or Markdown Decision) and market data in SAP S/4HANA Cloud Public Edition.

You can review the automatically created intercompany FX trades as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | A list of intercompany is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:Trade Request ID: <Trade Request ID (SAP trading platform integration) - Auto Trading FX Forward 1> | Two intercompany FX trades are displayed.The status of the FX trades should be Successful. |  |
| 3 | Go to Detailed Page | Select the checkbox of one intercompany FX trade, choose Details (arrow > ) to go to the detailed page. | Note down the Financial Transaction:XXXX/XXXXXXXXXXXXX |  |

##### Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. In the intercompany scenario, the Trading Platform Integration application will automatically generate the intercompany FX transactions ( two intercompany transactions) to the SAP S/4HANA Cloud Public Edition system.

You may follow the following section under Treasury Trading via Trading Platforms - FX Inbound of this test script to check the FX transactions data in the SAP S/4HANA Cloud Public Edition.

- [Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition](#unique_32) [page ] 40

You may use the financial transactions you noted down to filter the FX transactions.

#### Foreign Exchange Intercompany scenario 4: Trading via Trading Platform

With this intercompany trading scenario, you can make use of an external platform for the creation and processing of your intercompany trades.

##### Create Intercompany FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany FX trade requests in the SAP S/4HANA Cloud Public Edition system for the Trading via Trading Platform scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request in the company code is identified as an intercompany trade request and the intercompany scenario is 4: Trading via Trading Platform. You can refer to the relevant section in the Appendix for examples.

Procedure

You have several options to create an intercompany FX trade request:

1. Trade requests generated in Treasury and Risk Management

You can create FX trade requests through balance sheet exposure hedge request, cash flow exposure hedge request or manually.

For details, refer to the following sections in the Foreign Currency Risk Management(1X1) test script:

-
    - Create Trade Request via Balance Sheet Exposure Hedge Request
    - Create Trade Request via Cash Flow Exposure Hedge Request

1. Trade requests generated in Cash Management

For details, refer to the Cash Trade Request section of the Advanced Cash Operations(J78) test script.

As an example, create manual intercompany FX trade requests by executing the following steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Enter FX Forward Trade Request Details | Choose Create Trade Requests. On the Trade Request – Create screen, enter the following data and choose Submit.On the General tab:Trade Request ID (Text): for example, <Intercompany FX Forward – Trading via TP>Company Code: for example, 1710Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 1000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month>On the Additional Attributes tab:Assignment: TRADING_VIA_TP | The request is submitted. |  |
| 4 | Release the Trade Request | Choose Change. On the Trade Request – Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and name it as Trade Request ID (backend) – Trading via Trading Platform FX Forward 1 |  |

##### Review Intercompany FX Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany FX trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) – Trading via Trading Platform FX Forward 1>Confirm the following:The Status of the trade requests is Process Manually.Fulfillment Status is InitialScenario is Trading via Trading PlatformNote If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests are displayed.Trade Request ID (backend) – Trading via Trading Platform FX Forward 1This means these Trade requests got imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow > ) to go to detailed page. | Note down the Trade Request ID and name it as following:Trade Request ID (SAP trading platform integration) – Trading via Trading Platform FX Forward 1 |  |

##### Send Intercompany FX Trade Requests from SAP Trading Platform Integration to External Trading Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the intercompany trade requests are valid, you may send the intercompany trade requests to External Trading Platform (for example, iTEX of 360T) for further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | A list of intercompany trade requests is displayed. |  |
| 2 | Display the External Trade Request(s) | On the Manage Intercompany Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) – Trading via Trading Platform FX Forward 1> | The following trade request is displayed:Trade Request ID (backend) – Trading via Trading Platform FX Forward 1Go to the detailed page of the trade requests and note down the trade request IDs:XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX |  |
| 3 | Send External Trade Request(s) | Select the checkbox(es) of all the external trade request(s) under the same Back End Trade Request ID, and choose Send.Select the trading platform in the Select Trading Platform Profile dialog box and choose OK to confirm. | The intercompany trade request has been sent to external trading platform:Trade Request ID (backend) – Trading via Trading Platform FX Forward 1 |  |
| 4 | Reload Page | Reload the page, and confirm the status of the trade request is Sent to Trading Platform. | The status of the trade request is now Sent to Trading Platform. |  |

##### Review Intercompany FX Trade Request Status in External Trading Platform

Purpose

In this step, you may review the intercompany trade requests in the external trading platform.

Prerequisite

You’ve sent the intercompany trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

You may use the trade request IDs you’ve noted down in the previous step to search for your trade requests in the external trading platforms.

##### Create Intercompany FX Trades in External Trading Platform

Purpose

In this step, you create intercompany foreign exchange trades for the intercompany trade requests you’ve reviewed in previous step in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system. You need to do this step in External Trading Platforms.

Note down the IDs of the intercompany FX trades you created in the external trading platform. This ID will be filled in the External reference field in the Manage Intercompany Trades app in SAP trading platform integration.

Make sure you have created intercompany trades for following intercompany trade request:

- Trade Request ID (backend) – Trading via Trading Platform FX Forward 1

##### Generate Intercompany FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The intercompany FX trades created in the external trading platform will be automatically imported into SAP trading platform integration. Follow the steps below to review the intercompany FX trades in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | A list of all intercompany FX trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:Trade Request ID: <Trade Request ID (SAP trading platform integration) – Trading via Trading Platform FX Forward 1>Note You may also filter by Trade request IDs you’ve noted down in previous step.(XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX) | The intercompany FX trades you created in external trading platforms in the previous step are displayed in SAP trading platform integration.The status of the FX trades should be Successful.Note Note down the Financial transaction in the detailed page: XXXX/XXXXXXXXXXXXX Note The first 4 chars XXXX is the company code in SAP S/4HANA Cloud Public Edition. The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

##### Create Intercompany Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. In the intercompany scenario, the SAP trading platform integration will automatically send the intercompany FX trades to the SAP S/4HANA Cloud Public Edition system once they are created successfully in SAP trading platform integration on SAP BTP.

You may follow the following section under Treasury Trading via Trading Platforms - FX Inbound of this test script to check the FX transactions data in the SAP S/4HANA Cloud Public Edition.

- Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

You may use the financial transactions you noted down to filter the FX transactions.

#### Foreign Exchange Intercompany scenario 5: Back-to-Back Trading (Treasury Center)

##### Create External FX Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release external FX trade requests in the SAP S/4HANA Cloud Public Edition system for the Back-to-Back Trading (Treasury Center) scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request in the company code is identified as an external trade request and the external scenario is 5: Back-to-Back Trading (Treasury Center). You can refer to the relevant section in the Appendix for examples.

Procedure

You have several options to create an external FX trade request:

1. Trade requests generated in Treasury and Risk Management

You can create FX trade requests through balance sheet exposure hedge request, cash flow exposure hedge request or manually.

For details, refer to the following sections in the Foreign Currency Risk Management(1X1) test script:

-
    - Create Trade Request via Balance Sheet Exposure Hedge Request
    - Create Trade Request via Cash Flow Exposure Hedge Request

1. Trade requests generated in Cash Management

For details, refer to the Cash Trade Request section of the Advanced Cash Operations(J78) test script.

As an example, create manual external FX trade requests by executing the following steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Enter FX Forward Trade Request Details | Choose Create Trade Requests. On the Trade Request – Create screen, enter the following data and choose Submit.On the General tab:Trade Request ID (Text): for example, <Intercompany FX Forward trade request – B2B HQ>Company Code: for example, <enter the treasury center company code, for example, 1010>Instrument Cat.: for example, FXFW FX ForwardBuy/Sell: for example, B BuyRequested Amount: for example, 1000000 USDOpposite Currency: for example, EURValue Date: for example, <Current day + 1 Month>On the Additional Attributes tab:On Behalf of CoCode: <enter the subsidiary company code, for example, 1710> | The request is submitted. |  |
| 4 | Release the Trade Request | Choose Change. On the Trade Request – Modify screen, choose Release. | The status of the new trade request is now In Transfer in SAP S/4HANA Cloud Public Edition.Note down the Trade Request ID and name it as Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1 |  |
| 5 | Create and Release More Trade Requests | Repeat the above steps to create more trade requests.Note You may also create other instrument category trade requests, for example, FX Spot, FX Non-Deliverable Forward, FX Collar, FX Swap, FX Option, etc. | Note down the Trade Request IDs and named them as:Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2 |  |

##### Review External FX Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the external FX trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1/2>Confirm the following:The Status of the trade requests is Initiated.Fulfillment Status is InitialScenario is Back-to-Back Trading (Treasury Center)Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests is displayed.Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1/2This means this trade request got imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow > ) to go to detailed page. | Note down the Trade Request ID and name it as following:Trade Request ID (SAP trading platform integration) – Back-to-Back HQ Trading FX Forward 1Trade Request ID (SAP trading platform integration) – Back-to-Back HQ Trading FX Forward 2 |  |

##### Send External FX Trade Requests from SAP Trading Platform Integration to External Trading Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the external trade requests are valid, you may send the external trade requests to External Trading Platform for further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the External Trade Request(s) | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1> | The external trade request of Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1 is displayed.Go to the detailed page of the trade requests and note down the trade request IDs:XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX |  |
| 3 | Send External Trade Request(s) | Select the checkbox(es) of all the external trade request(s) under the same Back End Trade Request ID, and choose Send.Select the trading platform in the Select Trading Platform Profile dialog box and choose Send to confirm. | The external trade request of the following backend trade request has been sent to external Trading platform:Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1 |  |
| 4 | Reload Page | Reload the page, and confirm the status of the trade request is Sent to Trading Platform. | The status of the trade request(s) is now Sent to Trading Platform. |  |

##### Review External FX Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the external trading platform.

Prerequisite

You’ve sent trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

You may use the trade request IDs you’ve noted down in the previous step to search for your trade requests in the external trading platforms.

##### Create FX Trade in External Trading Platform

Purpose

In this step, you create foreign exchange trades for the trade requests you’ve reviewed in previous step in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system. You need to do this step in External Trading Platforms.

Note down the IDs of the FX trades you created in the external trading platform. This ID will be filled in the External reference field in the Manage Intercompany Trades app in SAP trading platform integration.

Make sure you have created intercompany trades for following intercompany trade request:

- Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 1

##### Generate FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The FX trades created in the external trading platform will be automatically imported into SAP trading platform integration. Follow the steps below to review the FX trades in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. | A list of all FX trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:Trade Request ID: <Reference IDs noted from the previous step>Note You may also filter by Trade request IDs you’ve noted down in previous step.(XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX) | The FX trades you created in external trading platforms in the previous step are displayed in SAP trading platform integration.The status of the FX trades should be Successful. |  |

##### Call Counterparty for Phone Trade

Purpose

If you decide to make the deal via phone for the external trade request, you need to call banks and get quotations.

Procedure

This is a step outside of the SAP S/4HANA Cloud Public Edition system, SAP trading platform integration and the external trading platform.

##### Enter the Phone Trade Details in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Like the external scenario, you may also fulfill the external trade requests via phone trade. In this step, you will manually enter the phone trade details for following trade requests:

- Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Prerequisite

An intercompany trade request has been retrieved from SAP S/4HANA Cloud Public Edition into the Manage Intercompany Trade Requests app.

Procedure

Table 7: Create Phone Trade:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2> | The external trade request of the following intercompany trade request is displayed.Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2 |  |
| 3 | Create Phone Trade | Select the checkbox of the external request, choose Create Phone Trade, the Manage Trades screen is displayed. Enter the trade details and choose Save. | The phone trade is created for the external trade request:Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2 |  |

##### Generate Intercompany FX Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. In the Back-to-Back Trading (Treasury Center) scenario, once the external trade is imported from external trading platform, SAP trading platform integration will generate the corresponding intercompany trades automatically.

You may follow the steps described below to display the intercompany FX trades.

|  |
| --- |
| Note The contract rate of intercompany FX trades is determined by FX rate of the external FX trade and Markup Markdown Decision rule. |

Prerequisite

If the external trade request is not split, then once it’s fulfilled, an intercompany FX trade will be automatically generated in each company code.

If the external trade request is split and manual or automatic aggregated, one or more intercompany trades will be automatically generated in each company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | The Manage Trade Requests screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:Transaction Request ID (Back End): < Trade Request ID (backend) – Back-to-Back HQ Trading FX Forward 2> | The intercompany trade request is displayed.The status of the intercompany trade request is CompletedThe Fulfillment Status is Fulfilled. |  |
| 3 | Go to Detailed Screen | Choose Details (>) | The detailed screen of the intercompany trade request is displayed. |  |
| 4 | Display External Trade | On the Detailed screen, choose More > Display Related Trades . Choose the external trade in the dialogbox. | The external trade is displayed. |  |
| 5 | Display Intercompany Trades | On the Detailed screen, choose More > Display Related Intercompany Trades . Choose the external trade in the dialogbox. | The intercompany trade is displayed. |  |

##### Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. In the intercompany scenario, the SAP trading platform integration will automatically send the FX trades (one external transaction with the external counterparty, and two intercompany transactions) to the SAP S/4HANA Cloud Public Edition system once they are created successfully in the SAP trading platform integration application on SAP BTP.

You may follow the following section under Treasury Trading via Trading Platforms - FX Inbound of this test script to check the FX transactions data in the SAP S/4HANA Cloud Public Edition.

- Create Foreign Exchange Transactions in SAP S/4HANA Cloud Public Edition

You may use the financial transactions you noted down to filter the FX transactions.

### Treasury Management Integration for Trading Platform - External Scenario for MM

The Money Market external scenario handles trades with external counterparties. From SAP S/4HANA Cloud Public Edition point of view, this include 2 sub-processes: Outbound process and Inbound process.

Outbound process: Money Market trade requests created in the SAP S/4HANA Cloud Public Edition system are sent to the SAP trading platform integration and then to the external trading platforms.

- Main steps in outbound process:
    - Create and release trade requests from SAP S/4HANA Cloud Public Edition
    - Import trade requests into SAP trading platform integration
    - Send trade requests from SAP trading platform integration to external trading platforms

Inbound process: Create MM transactions with external counterparties in external trading platform and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition.

- Main steps in inbound process
    - Create MM Deal Requests in External Trading Platforms
    - Generate MM Transactions in SAP trading platform integration
    - Create Money Market Transactions in SAP S/4HANA Cloud Public Edition

#### Treasury Trading via Trading Platforms – MM Outbound

Treasury Trading via Trading Platforms supports the inbound and outbound scenarios with external counterparties for Money Market Instruments.

In the outbound scenario, external trade requests generated in the SAP S/4HANA Cloud Public Edition system can be sent to the external trading platform via the Trading Platform Integration application on SAP BTP.

##### Create External MM Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release external Money Market trade requests in the SAP S/4HANA Cloud Public Edition system. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Note Make sure that you’ve made relevant business rule settings so that the trade request is identified as an external trade request. |

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Please follow the Enable Cash Request Integration section in Advanced Cash Operations(J78) to enable the cash request integration.

Procedure

Perform the following section in the test script:

- Cash Trade Request
    - Create and Submit Cash Trade Request for Money Market
    - Release Cash Trade Request

Please follow below steps to create external trade requests for Money Market Instruments as an example.:

- Create and submit Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Create Money Market Request (MM) | Choose Create Memo Record and choose Create Cash Trade Request (MM) from the dropdown list. | The Memo Record screen is displayed. |  |
| 4 | Enter Cash Trade Request Data | On the Cash Trade Request Data section, make following mandatory fields and choose Enter:Instrument Category: MM (Money Market Undefined)Invest / Borrow: <Invest or Borrow>Term Start Date: <Current date>Term End Date: <Current date+1 year>Company Code: 1010Requested Amount: for example, 1000,000EURText: for example, cash request for SAP trading platform integration - MM external scenarioNote If the following error message occurs, follow the Enable Cash Request Integration section in Advanced Cash Operations(J78) to enable the cash request integration.Cash trade request integration is disabled. |  |  |
| 5 | Save Cash Trade Request | Choose Create.Note Before submitting, you can edit or delete the cash trade request by choosing Edit or Delete. | The following message occurs:Memo record XXXXXXXXXX is created.The Cash Trade Request is created with status Created.Note down the memo record ID. |  |
| 6 | Submit Cash Trade Request | Choose Submit.After Submitted, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated as Submitted. |  |
| 7 | Create More Cash Requests | Repeat the above steps to create more cash requests. |  |  |

Release Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Search Cash Trade Request | Make the following data and choose Go:Company Code: 1010Certainty Level: Cash Trade RequestCash Trade Request Status: S (Submitted) | The cash trade requests are displayed. |  |
| 4 | Release Cash Trade Request | Select a cash trade request and choose Release. | The cash trade request is released. And a trade request is created automatically in the Treasury and Risk Management (TRM). |  |
| 5 | Go to detailed page | Choose the entry to go to the detailed page of the cash trade request. | Note down the MM Trade Request ID under General Information and name it as MM Trade Request ID (Backend) - External 1. |  |
| 6 | Release More Cash Trade Requests | Repeat the above steps and release all of the cash trade requests that are created in the previous step. | Note down the MM Trade Request IDs and name them asMM Trade Request ID (Backend) - External 2MM Trade Request ID (Backend) - External 3 | 3 |

Review Trade request status

Perform the following section in the Debt and Investment Management(1WV) test script:

- Review Money Market Trade Request Status

|  |
| --- |
| Note The trade request status should be In Process. |

##### Review External MM Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the external MM trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

|  |
| --- |
| Note Make sure that you’ve made relevant business rule settings so that the trade requests are identified as external trade request. |

Prerequisite

Before performing this step, you need to make sure you’ve created and released MM trade requests trade requests in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app on SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of external trade requests is displayed. |  |
| 3 | Enter the Filters and Reload Page | On the Manage Trade Requests screen, enter the following data and choose Go to reload the page.Trade Request ID (Back End): for example, <Enter the MM Trade Request (Backend) - External 1/2 you’ve note down in previous step>Note If your trade requests are not showed up automatically, choose Go to refresh the list.Note If the filters section is not displayed, please choose Show Filter to display it. | The status of the MM trade request is Initiated.The fulfillment status of the trade request is Initial. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow >) to go to detailed page.Confirm the following fields:Status: Initiated.Fulfillment Status: InitialInstrument Category: Money Market UndefinedIntercompany FX Trading Scenario: <Blank> | Note down the Trade Request ID and name it as following:MM Trade Request ID (SAP trading platform integration) - External 1MM Trade Request ID (SAP trading platform integration) - External 2MM Trade Request ID (SAP trading platform integration) - External 3 |  |

##### Decline External MM Trade Requests in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You may reject a trade request if it doesn’t follow your company’s trading rules or policies

In this step, you decline an external trade request. Once declined, the trade request can no longer be processed. And the status of the trade request in the SAP S/4HANA Cloud Public Edition system will also be updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go.Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) you’ve noted down in the previous step> | The trade request is displayed. |  |
| 3 | Decline a Trade Request | Choose Details ( >) to review the details.On the Mange Trade Requests screen, choose More (…), and choose Decline. | The Reason for Declining screen is displayed. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen, the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined. |  |
| 5 | Reload the page | Choose Go to refresh the page. | The Trade Request is in the Declined status: |  |

##### Update the Instrument Category of External MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the MM trade requests are imported into SAP trading platform integration, the instrument category is Money Market Undefined. You need to update this field to the right instrument category before sending it to the external trading platform. In this step, you update this field for all of the MM trade requests created in the previous step.

Prerequisite

An MM external trade request has been transferred to the SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app on SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go：Trade Request ID (Back End): for example, <Enter the MM trade request ID (Backend) - External 1 you’ve noted down in previous step> | The following trade request is displayed:MM Trade Request (Backend) - External 1 |  |
| 3 | Go to Detailed Page | Choose Details (arrow >) to go to detailed page.Confirm the following field:Instrument Category: Money Market Undefined |  |  |
| 4 | Change Instrument Category | Choose Change Instrument Category. The Select Instrument Category dialog box is displayed.Choose MM Fixed Term Deposit/Loan. | The following message is displayed:Instrument category is being changed |  |
| 5 | Change Instrument Category for more MM Trade requests | Repeat the above steps to change the instrument category for the rest of the MM trade requests. | The Instrument category of MM trade requests has been updated.The Status of MM trade requests is Edited. |  |

##### Send External MM Trade Requests to External Trading Platform in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you send MM trade requests to the external trading platform.

Prerequisite

An external MM trade request has been transferred to SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the MM trade request ID (Backend) - External 1 you’ve noted down in previous step> | The following trade requests is displayed:MM Trade Request ID (Backend) - External 1 |  |
| 3 | Send Trade Request | Choose the checkbox before the trade request, then choose Send.Choose the right external trading platform if the dialog box Select Trading Platform Profile is displayed,Choose Send to confirm if following message is displayed:Do you want to send 1 trade request? | The following message is displayed in the Sending Trade Requests - Result dialog box:Trade request was sent to the selected trading platform. |  |
| 4 | Reload Page | Reload the page, and confirm the status of the trade request is Sent to trading platform. | The status of the following trade request is now Sent to trading platform:MM Trade Request ID (Backend) - External 1 |  |
| 5 | Send More Trade Requests | Repeat the above steps to send another trade request:MM Trade request ID (Backend) - External 2 | The status of the following trade request is now Sent to trading platform:MM trade request ID (Backend) - External 2 |  |

##### Review External MM Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the external trading platform.

Prerequisite

You’ve sent MM trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

##### Reset External MM Trade Requests in SAP Trading Platform Integration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, you may need to reset the status of a trade request in SAP trading platform integration.

For example, if a trade request has been sent to the trading platform and the status is Sent to trading platform, but it is not available in the trading platform. In this case, you may reset the status of this trade request and resend it to the trading platform.

Prerequisite

The trade request should have following status before you can reset it：

- Sent to trading platform
- Received
- Outbound trade request processed
- Receiver determined
- Mapping successful (trading platform format)
- Trading platform call executed

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <MM Trade request ID (Backend) - External 1 you’ve noted down in previous step> | The following trade request is displayed.MM trade request ID (Backend) - External 1 |  |
| 3 | Reset a Trade Request | On the Manage Trade Requests screen, select the checkbox before the trade request MM Trade request ID (Backend) - External 1Choose Details (arrow >).On the Trade Request screen, choose Reset.Choose OK in the subsequent Warning dialog box. | The following message is displayed:Trade request XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX was reset. |  |

##### Call Counterparty for Phone Trade

Purpose

If you decide to make the deal via phone instead of sending the trade request to trading platform, you need to call banks and get quotations.

Procedure

This is a step outside of the SAP S/4HANA Cloud Public Edition system, SAP trading platform integration and the external trading platform.

#### Treasury Trading via Trading Platforms – MM Inbound

##### Check Liquidity Forecast in SAP S/4HANA Cloud Public Edition

Purpose

The cash manager reviews the liquidity forecast regularly and makes decisions regarding medium-term or long-term financial instruments, such as investment, loan, or foreign exchange.

Procedure

Perform the following steps in the Debt and Investment Management(1WV) test script.

- Analyze Liquidity Forecast

##### Review Trade Requests in External Trading Platform

Purpose

In this step, you review the trade request that you have sent to the external trading platform.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or SAP trading platform integration. You need to do this step in the external trading platforms.

|  |
| --- |
| Note You may use the following trade request IDs you’ve noted down to search for your trade requests in the external trading platforms:MM Trade Request ID (SAP trading platform integration) - External 2 |

##### Create Money Market Trade in External Trading Platform

Purpose

In this step, you create a money market trade in external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or SAP trading platform integration. You need to do this step in the external trading platforms.

|  |
| --- |
| Note You may note down the Trade ID and name it as Trade ID - external trading platform. |

##### Generate MM Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once an MM trade is closed in the external trading platform, the trade is transferred to SAP trading platform integration and submitted to the SAP S/4HANA Cloud Public Edition system automatically. If you want to check the MM trade data in SAP trading platform integration, you can follow the steps below to check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. | A list of all trades imported from the external trading platform is displayed. |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go:Trade Request ID:<MM Trade Request ID (SAP trading platform integration) - External 2> | The MM trade you created in the external trading platform in the previous step is displayed in SAP trading platform integration.The status of the MM trade should be Successful. |  |
| 3 | Go to Detailed Page | Choose Details (arrow >) to go to detailed page. | The detailed trade information is displayed.Note down the Financial transaction:XXXX/XXXXXXXXXXXXXNote The first 4 chars XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

##### Enter the Phone Trade Details in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once you made deal with counterparty via phone trade, you need to enter the details of the trade into SAP trading platform integration.

In this step, you maintain the information of the MM Transactions made via phone in the app in SAP trading platform integration.

Prerequisite

A trade request has been retrieved from SAP S/4HANA Cloud Public Edition into the Manage Trade Requests app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Enter FiltersEnter Selection Criteria and Execute | On the Manage Trade Requests screen, enter the following data and choose Go：Trade Request ID (Back End): for example, MM Trade Re-quest ID (SAP trading platform integration) – External 3 | The following trade requests is displayed.MM Trade Request(Backend) - External 3 |  |
| 4 | Create Phone Trade | Choose Create Phone Trade, the Manage Trades screen is displayed. Enter the trade details and choose Save.Counterparty: for example, 10537001Interest Rate: for example, 2.0Interest Calculation Method Code: for example, ACT/360Trade ID: for example, MM trade - external 3 | The phone trade has been saved successfully.The Manage Trades screen is displayed.Note The Trade Request status is changed to Completed. |  |
| 5 | Go to detailed page of the MM Transaction | On the Manage Trades screen, enter following data and choose Go:Trade Request ID: <MM Trade Request ID (SAP trading platform integration) - External 3>Choose Details. | The detailed trade information is displayed.Note down the Financial Transaction:XXXX / XXXXXXXXXXXXXNote The first 4 chars XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

##### Create Money Market Transaction in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the MM transaction information in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data:Company Code: for example, 1010Transaction: <Transaction Numbers you’ve note down in previous step>Accept default values for other parameters and choose Execute. | The MM transactions are displayed. |  |
| 4 | Go to Detailed Page | Select the checkbox before a MM transaction, choose Display | The MM transaction details are displayed.Note The status of the MM transactions is Contract. |  |

### Treasury Management Integration for Trading Platforms – Intercompany Scenarios for MM

This scenario handles trades between two company codes, for example, a subsidiary company code and a headquarter company code as treasury center. This test script assumes that the following data exists in your in S/4HANA Cloud system:

Company code:

- 1710 Initiate the intercompany trade requests process and fulfill them with Intercompany Trades with company code 1010.
- 1010 Receive the intercompany trade requests from 1710 and fulfill them with Intercompany Trades and make reversing trade with external counterparties for Back-to-Back scenario.

External Business partner:

- 10537001(in company code 1010) Representing an external counterparty.

Intercompany Business Partner:

- 17401710 (in company code 1010) Representing intercompany counterparty for 1710 in company code 1010
- 10401010 (in company code 1710) Representing intercompany counterparty for 1010 in company code 1710

#### Money Market Intercompany scenario 1: Back-to-Back Trading

##### Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany MM trade requests in the SAP S/4HANA Cloud Public Edition system for the Back-to-Back Trading scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request is identified as an intercompany trade request scenario 1: Back-to-Back Trading. You can refer to the following section in the Appendix for examples:

[Business Rules Settings Example](#unique_126) [page ] 159

Procedure

Perform the following section in the Advanced Cash Operations(J78) test script to create an MM Trade Request.

- Cash Trade Request
- Create and Submit Cash Trade Request for Money Market
- Release Cash Trade Request

Please follow below steps to create intercompany trade requests for Money Market Instruments as an example.

Create and Submit Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Create Money Market Request (MM) | Choose Create Memo Record and choose Create Cash Trade Request (MM) from the dropdown list. | The Memo Record screen is displayed. |  |
| 4 | Enter Cash Trade Request Data | On the Cash Trade Request Data section, maintain the following mandatory fields and choose Enter:Instrument Category: MM (Money Market Undefined)Invest / Borrow: <Invest or Borrow>Term Start Date: <Current date>Term End Date: <Current date+1 year>Company Code: 1710Requested Amount: for example, 1000,000 EURText: for example, cash request for SAP trading platform integration – MM B2B subsidiary scenario |  |  |
| 5 | Save Cash Trade Request | Choose Save.Note Before submitting, you can edit or delete the cash trade request by choosing Edit or Delete. | The following message occurs:Memo record XXXXXXXXXX is created.The Cash Trade Request is created with status Created.Note down the memo record ID. |  |
| 6 | Submit Cash Trade Request | Choose Submit.Note After Submitting, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated to Submitted. |  |
| 7 | Create More Cash Requests | Repeat the above steps to create more cash requests. |  |  |

Release Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 1710Certainty Level: Cash Trade RequestCash Trade Request Status: S(Submitted) | The cash trade requests are displayed. |  |
| 4 | Release Cash Trade Request | Select a cash trade request and choose Release. | The cash trade request is released. And a trade request is created automatically in the Treasury and Risk Management (TRM). |  |
| 5 | Go to Detailed Page | Choose the entry to go to the detailed page of the cash trade request. | Note down the MM Trade Request ID XXXX under General Information and name it as Trade Request ID (backend) – Back-to-Back SB Trading MM 1 |  |
| 6 | Release More Cash Trade Requests | Repeat the above steps and release all of the cash trade requests that are created in previous step. | Note down the MM Trade Request IDs XXXX and name them asTrade Request ID (backend) – Back-to-Back SB Trading MM 2 |  |

##### Review Intercompany MM Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany MM trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - Back-to-Back SB Trading MM 1/2>Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests are displayed:Trade Request ID (backend) Back-to-Back SB Trading MM 1/2This means these Trade requests are imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow >) to go to detailed page.Confirm the following:Status: Initiated.Fulfillment Status: InitialInstrument Category: Money Market UndefinedScenario: Blank | The status of the MM trade request is Initiated.The fulfillment status of the trade request is Initial. |  |
| 5 | Repeat for All of the Trade Requests | Repeat the above steps for the rest of the trade requests. |  |  |

##### Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the MM trade requests are imported into the SAP trading platform integration, the instrument category is Money Market Undefined. You need to update this field to the right Instrument category first. In this step, you update this field for all the intercompany MM trade requests created in the previous step.

Prerequisite

An intercompany MM trade request has been transferred to SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app on SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - Back-to-Back SB Trading MM 1/2 you’ve noted down in previous step> | The following trade requests are displayed.Trade Request ID (backend) - Back-to-Back SB Trading MM 1/2 |  |
| 3 | Go to Detailed Page | Select the checkbox of one trade request and choose Details (arrow >) to go to the detailed page.Confirm the following field:Instrument Category: Money Market UndefinedScenario： <Blank> |  |  |
| 4 | Change Instrument Category | Choose Change Instrument Category. The Select Instrument Category dialog box is displayed.Choose MM Fixed Term Deposit/Loan. | The following message is displayed:Instrument category is being changed |  |
| 5 | Change Instrument Category for more MM Trade requests | Repeat the above steps to change the instrument category for the rest of the intercompany MM trade requests. | The instrument category of MM trade requests is updated.The Status of MM trade requests is Edited. |  |
| 6 | Reprocess the Trade Request | On the Manage Intercompany Trade Requests screen, choose More (symbol…), choose Reprocess and choose OK to confirm the warning:Do you want to reprocess trade request XXX - XXXXXXXXXXXXXXXXXXXXXXXXXX? | The following message is displayed:Trade Request is being reprocessed. |  |
| 7 | Reload the Page | Reload the page, and confirm the following:Status: ProcessedScenario: Back-to-Back Trading |  |  |
| 8 | Edit and Reprocess More Trade Requests | Repeat the above steps to update the instrument category of the rest intercompany MM trade requests. | The following trade requests have been processed:Trade Request ID (backend) - Back-to-Back SB Trading MM 1Trade Request ID (backend) - Back-to-Back SB Trading MM 2 |  |

##### Create External MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the Back-to-Back Trading intercompany MM trade request is reprocessed successfully after updating the instrument category, an external MM trade request will be created automatically in the treasury center company code.

You can review the automatically created external trade request as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the automatically generated external trade requests | On the Manage Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End):<Trade Request ID (backend) - Back-to-Back Trading MM 1/2> | The status of the external trade requests is Initiated. |  |

##### Process External MM Trade Requests

###### Send External MM Trade Requests to Trading Platform in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you send the valid external trade requests to the external trading platforms for further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the external Trade Request(s) | On the Manage Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End):<Trade Request ID (backend) - Back-to-Back Trading MM 1> |  |  |
| 3 | Go to Detailed Page | Select the checkbox before the trade request, choose Details (arrow >) to go to detailed page.Confirm the following field:Request Category: Cash ManagementCompany ID: 1010Instrument Category: Money Market Fixed TermTechnical Status: Mapping successful (domain format)Documents Available: NoIntercompany FX Trading Scenario: Back-to-Back Trading (Subsidiary) | Go to the detailed page of the trade requests and note down the trade request ID and name it as External - Trade Request ID (SAP trading platform integration) - Back-to-Back Trading MM 1 |  |
| 4 | Send External Trade Request(s) | Select the checkbox of the external trade request, and choose Send.In the popup dialog box of the Send screen, choose Send to confirm. | The request of the following backend trade request has been sent to external Trading platform:Trade Request ID (backend) - Back-to-Back SB Trading MM 1 |  |
| 5 | Reload Page | Reload the page, and confirm the status of the trade request(s) is Sent to trading platform. | The status of the trade request(s) is now Sent to trading platform. |  |

###### Review External MM Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the trading platform.

Prerequisite

You’ve sent trade requests to the trading platform.

Procedure

This step is performed on the external trading platform.

|  |
| --- |
| Note You may use the following trade request ID (SAP trading platform integration) you’ve noted down in the previous step to search for your trade requests on the external trading platforms:External - Trade Request ID (SAP trading platform integration) - Back-to-Back SB Trading MM 1 |

###### Create MM Trade in External Trading Platform

Purpose

In this step, you create foreign exchange trades for the trade requests you’ve reviewed in previous step in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system. You need to do this step on the external trading platforms.

Note down the IDs of the MM trades you created in the External Trading Platform. This ID will be filled in the External reference field in the Manage Trades app in SAP trading platform integration.

|  |
| --- |
| Note Make sure you have created external trade for the following trade request (Backend):.Trade Request ID (backend) - Back-to-Back SB Trading MM 1 |

###### Generate MM Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The trades created in the trading platform can be automatically imported into SAP trading platform integration. Follow the steps below to review the trade information in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. | A list of all external trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:External reference: <Reference IDs noted from the previous step>Note You may also filter by the following trade request ID (SAP trading platform integration) you’ve noted down in previous step.External - Trade Request ID (SAP trading platform integration) - Back-to-Back SB Trading MM 1 | The MM trades you closed in the external trading platform in the previous step are displayed in SAP trading platform integration.The status of the MM trades should be Successful. |  |

###### Call Counterparty for Phone Trade

Purpose

If you decide to make the deal via phone for the external trade request, you need to call banks and get quotations.

Procedure

This step is outside of the SAP S/4HANA Cloud Public Edition system, SAP trading platform integration and the external trading platform.

###### Enter the Phone Trade Details in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Like the external scenario, you may also fulfill the external trade requests of intercompany trade requests via phone trade. In this step, you will manually enter the phone trade details for following trade requests:

- Trade Request ID (backend) - Back-to-Back Trading MM 2

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Prerequisite

An external trade request has been created in SAP trading platform integration for the intercompany trade request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades Requests app in SAP trading platform integration. | A list of all external transactions imported from external trading platforms is displayed. |  |
| 2 | Enter Filters | On the Manage Trade Requests screen, enter following data and choose Go.Trade Request ID (Back End): for example, <Trade Request ID (backend) - Back-to-Back SB Trading MM 2> | The external trade request of the following intercompany trade request is displayed：Trade Request ID (backend) - Back-to-Back SB Trading MM 2 |  |
| 3 | Go to Detailed Page | Select the checkbox before one trade request, and choose Details (arrow >) to go to detailed page.Confirm the following field:Request Category: Cash ManagementCompany ID: 1010Instrument Category: Money Market Fixed TermTechnical Status: Mapping successful (domain format) | Go to the detailed page of the trade requests and note down the trade request ID and name it as External - Trade Request ID (SAP trading platform integration) - Back-to-Back SB Trading MM 2 |  |
| 4 | Create Phone Trade | Select the checkbox of the trade request, choose Create Phone Trade, and the Manage Trades screen is displayed. Enter the following data and choose Save:Counterparty: for example, 10537001Interest Rate: for example, 2.0Interest Calculation Method Code: for example, ACT/360 | The external trade request of the following intercompany trade request is fulfilled:Trade Request ID (backend) - Back-to-Back SB Trading MM 2 |  |
| 5 | Display the MM Trade | On the Manage Trades screen, enter following data and choose Go to refresh the page.Trade Request ID: <External - Trade Request ID (SAP trading platform integration) - Back-to-Back SB Trading MM 2> | The new MM trade is displayed in the first row. |  |

###### Generate Intercompany MM Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. In the Back-to-Back Trading scenario, once the external trade request is fulfilled, an intercompany Money Market trade will be created in each company code automatically.

You may follow the steps below to display the intercompany MM trades.

Procedure

First get the intercompany trade request ID.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Enter Filter | Enter following data and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) - Back-to-Back SB Trading MM 1> | The intercompany trade request is displayed.The status of the intercompany trade request is CompletedThe Fulfillment Status is Fulfilled. |  |
| 3 | Go to Detailed Screen | Select the checkbox of the trade request and choose Details (arrow >) to go to detailed page. | The detailed screen of the intercompany trade request is displayed.Note down the intercompany trade request ID (SAP trading platform integration) XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX and name it as Intercompany Trade Request ID (SAP trading platform integration) – Back-to-Back SB Trading MM 1. |  |
| 4 | Repeat the Above Steps for More Trade Request | Repeat the above steps for<Trade Request ID (backend) - Back-to-Back SB Trading MM 2> | The detailed screen of the intercompany trade request is displayed.Note down the intercompany trade request ID (SAP trading platform integration) XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX and name it as Intercompany Trade Request ID (SAP trading platform integration) – Back-to-Back SB Trading MM 2. |  |

Check Intercompany Trade

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go:Trade Request ID: Intercompany Trade Request ID (SAP trading platform integration) - Back-to-Back Trading MM 1/2 | For each intercompany trade request ID, two intercompany trades are displayed.Note down the Financial Transaction:XXXX / XXXXXXXXXXXXXNote The first 4 chars XXXX is the company code in the SAP S/4HANA Cloud Public Edition system.The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

###### Create Money Market Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the MM transaction information in the SAP S/4HANA Cloud Public Edition system.

Procedure

Please follow the following section of this test script to check the MM transactions in SAP S/4HANA Cloud Public Edition.

- Treasury Trading via Trading Platforms - MM Inbound
    - [Create Money Market Transaction in SAP S/4HANA Cloud Public Edition](#unique_70) [page ] 101

###### Decline MM Trade Requests in SAP Trading Platform Integration (Optional)

Purpose

You may reject the intercompany trade requests if it doesn’t follow your company’s trading rules or policies.

Prerequisite

An intercompany trade request has been imported into SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

###### Decline External MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you decline the external trade request which is created when importing the intercompany trade request. Once declined, the external trade request can no longer be further processed.

After you decline the external trade request, you have two options to further process the intercompany trade request in the SAP trading platform integration application on SAP BTP:

- Decline the intercompany trade request

If you choose to decline the intercompany trade request, then the intercompany trade request status will change to Declined and the trade request in the SAP S/4HANA Cloud Public Edition system will be canceled. No further process could be done for the intercompany trade request.

- Reprocess the intercompany trade request

If you choose to reprocess the intercompany trade request, then the intercompany trade request status will change to Processed and another external trade request will be created in the SAP trading platform integration application and you may further process the external trade request, for example, fulfill it.

Prerequisite

Please recreate and release intercompany MM Back-to-Back trade requests and note down the trade request IDs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the Automatically Generated External Trade Requests | On the Manage Trade Requests screen, enter following data, and choose Go:Trade Request ID (Back End):<Trade request IDs (back end) you noted down in the previous step> | The trade requests that you’ve noted down in the previous step are displayed on the screen. |  |
| 3 | Decline The External Trade Request | On the Manage Trade Requests screen, select the checkbox in the front of the trade request you want to decline, and choose Additional Options > Decline. | The Reason for Declining dialog box is displayed. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined.Now the trade request’s status is Declined. |  |

###### Decline Intercompany MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the external trade request of an intercompany Back-to-Back MM trade request has been declined, you can decline the intercompany trade request.

In this step, you decline the intercompany trade requests. Once the intercompany trade request is declined in the Trading Platform Integration application, the status of the corresponding trade request in SAP S/4HANA Cloud Public Edition will be automatically changed to Canceled and the whole process is done.

Prerequisite

The external trade request of an intercompany Back-to-Back MM trade request has been declined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Display the Intercompany Trade Requests | Choose Go. | A list of intercompany trade requests is displayed.Check the status of the intercompany trade requests. |  |
| 3 | Decline the Intercompany Trade Request | Select the checkbox in the front of the trade request that you want to decline.Choose Additional Options > Decline . | The Reason for Declining dialog box displays. |  |
| 4 | Enter Reason for Declining | On the Reason for Declining screen, select a reason, for example, Incorrect amount. | On the Decline Trade Request - Result screen the following message is displayed: XXX-XXXXXXXXXXXXXXXXXXXXXXXXX Trade requests are being declined. |  |
| 5 | Refresh to check the Status of the Intercompany Trade Request | Choose Go to refresh the list | Now the intercompany trade request’s status is Declined. |  |

###### Update the Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition

Purpose

Once the intercompany trade request is declined in the Trading Platform Integration application, the status of the corresponding trade request in the SAP S/4HANA Cloud Public Edition system is automatically updated to Canceled and the whole process is done.

This is an automatic step. Please follow the following section of this test script to check the status of the intercompany trade requests.

- Review External MM Trade Request Status in SAP trading platform integration

|  |
| --- |
| Note The status of the intercompany trade request should be Canceled. |

Prerequisite

You have declined the intercompany trade request in the Trading Platform Integration application.

###### Reprocess Intercompany MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reprocess the intercompany Back-to-Back trade requests. Once the intercompany trade request is reprocessed, the status will be changed to Processed and the corresponding external trade request will be automatically created again and ready for further processing.

Prerequisite

You have declined the related external trade request.

Procedure

Table 8: Reprocess the intercompany trade request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | The Manage Intercompany Trade Requests screen is displayed. |  |
| 2 | Display the Intercompany trade requests | Choose Go.Note You may use Trade Request ID (Back End) as the filter. | A list of intercompany trade requests is displayed.The status of the intercompany trade request should be Technical error. |  |
| 3 | Decline the intercompany trade request | Select the checkbox in front of the trade request that you want to reprocess.Choose Reprocess.A warning message shows up. Choose OK to confirm. |  |  |
| 4 | Refresh to Check the Status of the intercompany Trade Request | Choose Go to refresh the list | Now the intercompany trade request’s status is ProcessedNote down the trade request ID (backend). |  |

Table 9: Check the Status of External Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Display the Automatically Generated External Trade Requests | On the Manage Trade Requests screen, enter following data:Trade Request ID (Backend):<Trade request IDs (back End) that you’ve noted down in previous step>Choose Go. | A new line of the external trade request is displayed and the status is Initiated. |  |

#### Money Market Intercompany scenario 2: Manual Trading

##### Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany MM trade requests in the SAP S/4HANA Cloud Public Edition system for the Manual Trading scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request is identified as an intercompany trade request scenario 2: Manual Trading. You can refer to the following section in the Appendix for examples:

[Business Rules Settings Example](#unique_126) [page ] 159

Procedure

Perform the following section in the Advanced Cash Operations (J78) test script to create an MM Trade Request.

- Cash Trade Request
    - Create and Submit Cash Trade Request for Money Market
    - Release Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Create Money Market Request (MM) | Choose Create Memo Record and choose Create Cash Trade Request (MM) from the dropdown list. | The Memo Record screen is displayed. |  |
| 4 | Enter Cash Trade Request Data | On the Cash Trade Request Data section, make following mandatory fields and choose Enter:Instrument Category: MM (Money Market Undefined)Invest / Borrow: <Invest or Borrow>Term Start Date: <Current date>Term End Date: <Current date+1 year>Company Code: 1710Requested Amount: for example, 1,000,000 USDText: for example, cash request for SAP trading platform integration – MM Manual Trading scenario |  |  |
| 5 | Save Cash Trade Request | Choose Save.Before submitting, you can edit or delete the cash trade request by choosing Edit or Delete. | The following message is displayed:Memo record XXXXXXXXXX is created.The Cash Trade Request is created with status Created.Note down the memo record ID. |  |
| 6 | Submit Cash Trade Request | Choose Submit.After Submitting, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated as Submitted. |  |
| 7 | Create More Cash Requests | Repeat the above steps to create more cash requests. |  |  |

Release Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 1710Certainty Level: Cash Trade RequestCash Trade Request Status: S(Submitted) | The cash trade requests are displayed. |  |
| 4 | Release Cash Trade Request | Select a cash trade request and choose Release. | The cash trade request is released, and a trade request is created automatically in the Treasury and Risk Management (TRM). |  |
| 5 | Go to Detailed Page | Choose the entry to go to the detailed page of the cash trade request. | Note down the MM Trade Request ID under General Information and name it as Trade Request ID (backend) – Manual Trading MM 1 |  |

##### Review Intercompany MM Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany MM trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go：Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) - Manual Trading MM 1>Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade requests are displayed:Trade Request ID (backend) – Manual Trading MM 1This means these Trade requests got imported into SAP trading platform integration. |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow >) to go to detailed page.Confirm the following:Status: InitiatedFulfillment Status: InitialInstrument Category: Money Market UndefinedScenario: Blank | The status of the MM trade request is Initiated.The fulfillment status of the trade request is Initial.Note down the following MM Trade Request ID name it as Trade Request ID (SAP trading platform integration) - Manual Trading MM 1 |  |

##### Update the Instrument Category of the Intercompany MM Trade Requests in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the MM trade requests are imported into SAP trading platform integration, the instrument category is Money Market Undefined. You need to update this field to the right instrument category first. In this step, you update this field for all of the intercompany MM trade requests created in the previous step.

Prerequisite

An intercompany MM trade request has been transferred to SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app on SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) - Manual Trading MM 1> | The following trade requests are displayed：Trade Request ID (backend) - Manual Trading MM 1 |  |
| 3 | Go to Detailed Page | Select the checkbox of one trade request, choose Details (arrow >) to go to detailed page.Confirm the following fields:Instrument Category: Money Market UndefinedScenario: Blank |  |  |
| 4 | Change Instrument Category | Choose Change Instrument Category. The Select Instrument Category dialog box is displayed.Choose MM Fixed Term Deposit/Loan. | The following message is displayed:Instrument category is being changedThe Status of MM trade requests is Edited. |  |
| 5 | Reprocess the Trade Request | On the Manage Intercompany Trade Requests detailed screen, choose More (symbol …) , choose Reprocess and choose OK to confirm the following warning:Do you want to reprocess trade request XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX? | The following message is displayed:Trade Request is being reprocessed. |  |
| 6 | Reload the page | Reload the page, and confirm the following:Status: Process ManuallyInstrument Category: MM Fixed Term Deposit/LoanScenario: Manual Trading |  |  |

##### Create Intercompany Manual Trade in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you manually create intercompany MM transactions for the intercompany trade requests of intercompany scenario 2: Manual Trading in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration, and choose Go. | A list of intercompany trade requests is displayed. |  |
| 2 | Enter Filter | On the Manage Intercompany Trade Requests screen, enter the following data, and choose Go:Trade Request ID (Back End): <Trade Request ID (backend) - Manual Trading MM 1> | The intercompany trade request is displayed and the status is Initiated. |  |
| 3 | Create Manual Trade | Select the checkbox in front of the trade request, choose Create Manual Trade. | The Manage Intercompany Trades screen is displayed.New Manual Intercompany Trade is displayed right under the header. |  |
| 4 | Enter the Manual Trade Details | On the Manage Intercompany Trades screen, fill out all mandatory fields and choose Create.Interest Rate: for example,1.2Interest Calculation Method: ACT/360Note Depending on the instrument type, different trade information need to be entered. | The Manage Intercompany Trades screen is displayed. And the following message is displayed:Trade Created |  |
| 5 | Display the Intercompany Trades | On the Manage Intercompany Trades screen, enter following data and choose Go:Trade Request ID: < Trade Request ID (SAP trading platform integration) - Manual Trading MM 1>Note If the filters section is not displayed, please choose Show Filter to display it. | Two intercompany MM Transactions are displayed. |  |

##### Create Money Market Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the MM transaction information in the SAP S/4HANA Cloud Public Edition system.

Procedure

Please follow the following section of this test script to check the MM transactions in SAP S/4HANA Cloud Public Edition.

- Treasury Trading via Trading Platforms - MM Inbound
    - [Create Money Market Transaction in SAP S/4HANA Cloud Public Edition](#unique_70) [page ] 101

#### Money Market Intercompany scenario 4: Trading via Trading Platform

With this intercompany trading scenario, you can make use of an external platform for the creation and processing of your intercompany trades.

##### Create Intercompany MM Trade Requests in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and release intercompany MM trade requests in the SAP S/4HANA Cloud Public Edition system for the Trading via Trading Platform Scenario. Once released, these trade requests are automatically pushed into SAP trading platform integration.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for DE. Substitute the country/region-specific values provided by SAP Best Practices or use master data values you have created for this purpose. |

Prerequisite

Make sure that you’ve made relevant business rule settings so that the trade request is identified as an intercompany trade request scenario 4: Trading via Trading Platform. You can refer to the following section in the Appendix for examples:

- Business Rules Settings Example

Procedure

Perform the following section in the Advanced Cash Operations (J78) test script to create an MM Trade Request.

- Cash Trade Request
    - Create and Submit Cash Trade Request for Money Market
    - Release Cash Trade Request

Please follow below steps to create external trade requests for Money Market Instruments as an example.:

- Create and submit Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Create Money Market Request (MM) | Choose Create Memo Record and choose Create Cash Trade Request (MM) from the dropdown list. |  |  |
| 4 | Enter Cash Trade Request Data | On the Cash Trade Request Data section, make the following mandatory fields and choose Enter:Instrument Category: MM (Money Market Undefined)MM (Money Market Undefined)Invest / Borrow: <Invest or Borrow>Term Start Date: <Current date>Term End Date: <Current date+1 year>Company Code: 1710Requested Amount: for example, 1000,000JPYText: for example, cash request for SAP trading platform integration – MM Trading via Trading Platform scenario |  |  |
| 5 | Save Cash Trade Request | Choose Create.Note Before submitting, you can edit or delete the cash trade request by choosing Edit or Delete. | The following message occurs:Memo record XXXXXXXXXX is created.The Cash Trade Request is created with status Created.Note down the memo record ID. |  |
| 6 | Submit Cash Trade Request | Choose Submit.After Submiting, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated as Submitted. |  |
| 7 | Create More Cash Requests | Repeat the above steps to create more cash requests. |  |  |

Release Cash Trade Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). | The Manage Memo Records screen is displayed. |  |
| 3 | Search Cash Trade Request | Make the following data and choose Go:Company Code: 1710Certainty Level: Cash Trade RequestCash Trade Request Status: S (Submitted) | The cash trade requests are displayed. |  |
| 4 | Release Cash Trade Request | Select a cash trade request and choose Release. | The cash trade request is released. And a trade request is created automatically in the Treasury and Risk Management (TRM). |  |
| 5 | Go to detailed page | Choose the entry to go to the detailed page of the cash trade request. | Note down the MM Trade Request ID under General Information and name it as Trade Request ID (backend) – Trading via Trading Platform MM 1. |  |

##### Review Intercompany MM Trade Request in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the intercompany MM trade requests sent from SAP S/4HANA Cloud Public Edition into SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. |  |  |
| 2 | Refresh the List | Choose Go. | A list of trade requests is displayed. |  |
| 3 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter the following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) – Trading via Trading Platform MM 1>Note If your trade requests are not showed up automatically, choose Go to refresh the list. | The following trade request is displayed:Trade Request ID (backend) – Trading via Trading Platform MM 1 |  |
| 4 | Go to Detailed Page | Select the checkbox of the trade request and choose Details (arrow >) to go to detailed page.Confirm the following:Status: InitiatedFulfillment Status: InitialInstrument Category: Money Market UndefinedScenario: Blank | The status of the MM trade request is Initiated.The fulfillment status of the trade request is Initial.Note down the following MM Trade Request ID name it as Trade Request ID (SAP trading platform integration) - Manual Trading MM 1 |  |

##### Update the Instrument Category of the Intercompany MM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the MM trade requests are imported into the SAP trading platform integration, the instrument category is Money Market Undefined. You need to update this field to the right Instrument category first. In this step, you update this field for all the intercompany MM trade requests created in the previous step.

Prerequisite

An intercompany MM trade request has been transferred to SAP trading platform integration from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app on SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Enter Filters | On the Manage Intercompany Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Enter the Trade Request ID (backend) – Trading via Trading Platform MM 1> | The following trade requests are displayed.Trade Request ID (backend) – Trading via Trading Platform MM 1 |  |
| 3 | Go to Detailed Page | Select the checkbox of one trade request and choose Details (arrow >) to go to the detailed page.Confirm the following field:Instrument Category: Money Market UndefinedScenario： <Blank> |  |  |
| 4 | Change Instrument Category | Choose Change Instrument Category. The Select Instrument Category dialog box is displayed.Choose MM Fixed Term Deposit/Loan. | The following message is displayed:Instrument category is being changedThe Status of MM trade requests is Edited. |  |
| 5 | Reprocess the Trade Request | On the Manage Intercompany Trade Requests screen, choose More (symbol …), choose Reprocess and choose OK to confirm the warning:Do you want to reprocess trade request XXX - XXXXXXXXXXXXXXXXXXXXXXXXXX? | The following message is displayed:Trade Request is being reprocessed. |  |
| 6 | Reload the Page | Reload the page, and confirm the following:Status: Process ManuallyInstrument Category: MM Fixed Term Deposit/LoanScenario: Trading via Trading Platform |  |  |

##### Send Intercompany MM Trade Requests from SAP Trading Platform Integration to External Trading Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the intercompany trade requests are valid, you may send the intercompany trade requests to External Trading Platforms (for example, iTEX of 360T) for further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Roles prerequisite table lists only Treasury Specialist Front Office, Middle Office, Cash Management Specialist and Cash Manager, yet the Overview Table and MM test steps use the role Treasury Specialist - Back Office (TM00 Process MM Transactions).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-02]]
- related-to :: [[05-treasury-and-cash-management/treasury-correspondence-integration-with-swift-network-3qm-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx` — lines 1–3618 of the extracted text · extracted with `mammoth` · 302,966 chars in the whole document
