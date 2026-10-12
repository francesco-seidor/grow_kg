---
id: 03-financial-accounting-and-close/steps-to-create-bai2-format-file-207
title: Steps to Create BAI2 Format File (Steps_To_Create_BAI2_File)
description: "Guide to manually building a BAI2 bank statement text file for lockbox upload in SAP S/4HANA; the format must match SAP's BAI2 or the file cannot be processed."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/cash-application]
aliases: [Steps_To_Create_BAI2_File]
keywords: [Cash Application with Machine Learning, bai2 file, lockbox, bank account details, micr number]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Steps_To_Create_BAI2_File.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-207
topic: 03-financial-accounting-and-close/cash-application
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Steps to Create BAI2 Format File (Steps_To_Create_BAI2_File)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Steps_To_Create_BAI2_File.docx`, extracted with `mammoth`. Grouped under **Cash Application with Machine Learning** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP S/4HANAMay 2018EnglishEnglish |  |
|  | Steps to Create BAI2 Format File |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany |  |

Copyright

© 2018 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. Please see [http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark](http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark) for additional trademark information and notices.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP SE or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP SE or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business outlined in this document or any related presentation, or to develop or release any functionality mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’ strategy and possible future developments, products, and/or platform directions and functionality are all subject to change and may be changed by SAP SE or its affiliated companies at any time for any reason without notice. The information in this document is not a commitment, promise, or legal obligation to deliver any material, code, or functionality. All forward-looking statements are subject to various risks and uncertainties that could cause actual results to differ materially from expectations. Readers are cautioned not to place undue reliance on these forward-looking statements, which speak only as of their dates, and they should not be relied upon in making purchasing decisions.

**Steps to Create BAI2 Format File**

## Purpose

The purpose of this document is to describe steps required to manually set up the Bank Administration Institute (BAI) file format for lockbox. The BAI2 format is a cash management balance reporting specification.

For the preparation of uploading files for lockbox, a specific BAI2 format is required. If the BAI2 format received from the issuing bank does not match the SAP BAI2 format, the file cannot be processed.

## Procedure

Use the following code to create your BAI2 format. Copy the code into a text editor application and follow the instructions for creating a file for your requirements.

100**LOCKBOXDESLOCKBOXORI**1702142103

58000001234567170214**LOCKBOXDESLOCKBOXORI**

600100100000357860038001081234567890010123035

4001001560**1**9400000154 00000193930000000000GH

4001001560**9**9400000165 00000163930000000000GH

8000000123456717021400010000035786

9999900

1. Using the provided code block, make the following changes:
    1. In the first line of the file, change the red number to reflect the correct date and time. The file uses the format of *yymmddhhmm*.
    2. On the second line, change the red number to match the date on the first line.
    3. On the third line, make the following changes:
        1. change the blue number to the sum total of all invoices with 2 decimal places and change the orange number to the check number.
        2. Numbers in the light green color indicate the **Bank Key** number of the business partner. That number is usually a 9-digit number that can be found in the payment transactions tab of the business partner.
        3. Numbers in the dark green color indicate the **Bank Account** number of the business partner. This number can be up to 10 digits long and is found in the payment transactions tab of the business partner. When this number is shorter than 10 digits, leave blank spaces after the end of the number. The two (**Bank Key** and **Bank** **Account**) numbers, together, form your business partner's Magnetic Ink Character Recognition (MICR) number and is transmitted by the bank.
    4. On the fourth line, make the following changes:
        1. The yellow number is the 1st to second to last record
        2. Change the red number to the invoice number
        3. Change the blue number to the invoice amount
    5. On the fifth line, make the following changes if the file contains more than one invoice for the customer:

**Caution**: If there is only 1 invoice, skip this step and go to step f.

-
    -
        1. The yellow number is the last record
        2. Change the red number to the invoice number
        3. Change the blue number to the invoice amount
    1. On the sixth line, change the red number to match the date on the first line and change the blue number to the sum total of invoices.

1. LOCKBOXDES – is your SAP S/4HANA *bank account*number. Enter the number into your configuration when you receive it from the bank. For unit test purpose, don’t change it in the file.
2. LOCKBOXORI – is your SAP S/4HANA *bank routing* number. Enter the number into your configuration when you receive it from the bank. For unit test purpose, don’t change it in the file.
3. Save the file as txt.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-cash-application-integration-1mv-740]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Steps_To_Create_BAI2_File.docx` — full document · extracted with `mammoth` · 5,753 chars in the whole document
