---
id: 09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-02
title: "Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "Test script (part 2 of 2): SAP Entitlement Management jobs, provisioning/decommissioning responses via SoapUI, Subscription Billing checks, end-of-contract."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: []
keywords: [Subscription Products and Rate Plans, entitlement management, license decommissioning, tenant decommissioning, provisioning requests, provisioning response testing, tenant provisioning, license provisioning, subscription billing, subscription termination]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx#lines-3327-3917"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1122
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3327–3917 of the extracted text), extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

##### Display Entitlements in SAP Entitlement Management

Procedure

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | The entitlements for Tenant phases and for Licenses from the old contract, have now been set to status Expired. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Run Job in SAP Entitlement Management to Create License Decommissioning Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job will create a license decommissioning process, for licenses which have expired, and which are licenses with a specific metric, and not licenses to activate individual capabilities – those will be decommissioned using event SI 5SW Licenses Expired, as explained earlier in chapter At End of Trial Period, Perform Decommissioning for Capability “CAD 3D”.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job name | Choose job name 5SW License Decommissioning.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the JOB LOGS. | Check the job log to see that multiple license decommissioning processes were created. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the decommissioning processes to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app. |  |  |
| 3 | Execution of the job name | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the provisioning requests. | Check the sent provisioning and decommissioning requests to the productive tenant |  |

##### Send Response for the License Decommissioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different decommissioning requests for tenants have been sent to the provisioning system, the decommissioning of the licenses is performed by the provisioning system, reducing the license quantities. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License DecommissioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the message log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the process log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/ then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license decommissioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement has status Expired. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationMetricQuantityCAD ApplicationUsers30CAD ApplicationDocuments60CAD ApplicationDocuments90CAD ApplicationDocuments100 |  |  |

Payload for CAD Users Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : false,
"Application" : "CAD",
"Quantity" : 20
}
} ]

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : false,
"Application" : "CAD",
"Quantity" : 30
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : false,
"Application" : "CAD",
"Quantity" : 60
}
} ]

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : false,
"Application" : "CAD",
"Quantity" : 90
}
} ]

Payload for Document License from CAD Documents

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : false,
"Application" : "CAD",
"Quantity" : 100
}
} ]

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the decommissioning processes to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app. |  |  |
| 3 | Execution of the job name | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the provisioning requests. | Check the sent provisioning requests to the provisioning system. |  |

##### Send Response for the Tenant Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the Tenant Entitlement | Select the view Commercial Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: Tenant PhaseApplication: Analytics ApplicationSystem Type: Productive SystemChoose View Phase Detail.Choose tab Provision.Choose Expand for SI 5SW Tenant ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose Send Provisioning Request.Choose the icon in the middle, View Log.On pop-up window Send Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/ then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI.. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The tenant provisioning process has status Completed. |  |
| 8 | Return to Entitlements Tenants Overview | Choose Back.Choose Back.In Maintain Customer Entitlements, choose View Commercial Tenants. | The entitlement for Tenant Phases and Tenants for Application CAD and System Type Productive System have status Active.The Tenant entitlement shows the Tenant ID, Tenant Name, Tenant URL based on the provisioning feedback. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationSystem TypeAnalyticsTest System |  |  |

Payload for Analytics Productive Tenant:

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.prod.cad.com",
"Tenant_ID" : "ANALYTICS_10001_PRD",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM ANALYTICS PROD"
}
} ]

Payload for Analytics Test Tenant:

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.test.cad.com",
"Tenant_ID" : "ANALYTICS_10002_TST",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM ANALYTICS TEST"
}
} ]

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/ then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license decommissioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityCAD ApplicationCAD 2D EssentialsCAD ApplicationCAD 2D AdvancedCAD ApplicationCAD 3DCollaboration ApplicationCollaboration BasicCollaboration ApplicationCollaboration AdvancedCollaboration ApplicationCollaboration Realtime |  |  |

Payload for CAD Users Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 100
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for CAD 2D Advanced

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ADV",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for CAD 3D

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_3D",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

Payload for Collaboration Advanced

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_ADV",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

Payload for Collaboration Realtime

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_REAL",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

##### Display Active Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615) under Subscriptions and Billing catalog. | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the Solution Order from the result list. | Solution Order details are displayed on the Display Solution Order Page |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Subscription.Choose the subscription ID to navigate to the Subscription in SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status: ActiveValid From: XXX XX, XXXXNote Note down the provider contract ID mentioned in the Processing data tab for further steps. | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Provider Contract | Choose tab Processing Data.Choose the Provider Contract ID under Related Documents.Review the provider contract under General Data.Choose Items: General Data.Choose Item 1 – License.Double click the linked Billing Plan.Choose Plan Items.Choose Item 2 – Activation Fee.Double click the linked Billing Plan.Choose Plan Items.Choose Back.Choose Back.Choose Back. |  |  |
| 9 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

#### End of Contract for Test Tenant

The test processes above already covered decommissioning of a license for one specific capability being decommissioned, after the last of multiple entitlements for the dame capability has expired, and the decommissioning of a license with metric, this chapter describes the decommissioning of a tenant, which is triggered when the last phase of different tenant phase entitlement expires, so that there is no active contract left for the specific tenant.

##### Terminate Subscription early in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Subscription Specialist - Subscription Billing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Subscriptions (F6801). |  |  |
| 3 | Execution of the job name | Activate the check box on the left side of the active subscription for CAD Test Tenant.Choose Mass Changes and then Cancel.Under Desired Expiration Date, <enter the first day of the current month minus 2 months>.Under Cancellation Notice Data, <enter the same date>.Under Cancellation Reason, Contract Termination.Activate the check box for Overrule Subscription Terms.Choose Cancel Subscriptions. | The subscriptions have status Expired. |  |

##### Display Entitlements in SAP Entitlement Management

Procedure

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant Entitlement | Select the views Commercial Tenants and click on Go. | The previously created Tenant and Tenant Phase entitlements for Offering CAD Test Tenant are still Active, but the end date of the Tenant Phase entitlements has been reduced. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Run Job in SAP Entitlement Management to Set Status to Expired

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job will move any entitlement, for which the end date has been passed, to Expired. For the current test process, by running this job, we are simulating that the day, where the contract for the test tenant expires, has arrived, so that tenant phase entitlement is set to status Expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job name | Choose job name 5SW Set Status to Expired Job.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the JOB LOGS. | Check the job log to see that one status were set to Expired. |  |

##### Display Entitlements in SAP Entitlement Management

Procedure

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant Entitlement | Select the views Commercial Tenants and click on Go. | The entitlements for Tenant Phase for Offering CAD Test Tenant has now been set to status Expired. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Run Job in SAP Entitlement Management to Trigger Tenant Decommissioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job will create a tenant decommissioning process, for tenant phase licenses which have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app. |  |  |
| 3 | Execution of the job name | Choose job name 5SW Tenant Phases Provisioning Process Job.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the JOB LOGS. | Check the job log to see that a tenant decommissioning processes was created. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the decommissioning processes to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app. |  |  |
| 3 | Execution of the job name | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the provisioning requests. | Check the sent decommissioning requests to the productive tenant. |  |

##### Send Response for the Tenant Decommissioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different decommissioning requests for tenants have been sent to the provisioning system, the decommissioning of the licenses is performed by the provisioning system, reducing the license quantities. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the Tenant Entitlement | Select the view Commercial Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the Entitlement Number withEntitlement Model: Tenant PhaseApplication: CAD ApplicationOffering: CAD Test TenantStatus: ExpiredClick View Phase Detail.Choose tab Provision.Choose Expand for SI 5SW Tenant Phase DecommissioningNote down the Process Log ID.Choose the Process Log ID.Choose Send Provisioning Request.Choose the icon View Log in the middle.On pop-up Send Provisioning Request window, choose the Message Log ID.On Communication Messages screen, choose the icon under Payload.On Payload pop-up, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your processLogID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter[Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response](#unique_27) [page ] 51.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/):Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On Payload pop up, choose Close and choose Back. | The license decommissioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlements of type Tenant and Tenant Phase for Offering CAD Test Tenant has status Expired. |  |

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.test.cad.com",
"Tenant_ID" : "CAD_10005_TST",
"Tenant_Status" : "EXPIRED",
"Tenant_Name" : "AE1 COM CAD TEST 2"
}
} ]

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx` — lines 3327–3917 of the extracted text · extracted with `mammoth` · 288,298 chars in the whole document
