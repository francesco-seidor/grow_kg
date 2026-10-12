---
id: 12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-01
title: Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 1 of 3
description: "SAP Best Practices test script for the AE Consumer Products planning-to-fulfillment scenario (5OI, 5W3, 5HK, 5W4, 5HL, 61V): prerequisites, setup, step-by-step Fiori test procedures."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: []
keywords: [End-to-End Produce-and-Sell Scenarios, consumer products scenario, business roles, master data, production capacity leveling, planned independent requirements, pmrp simulation, work center capacity, procurement of production components, purchase orders]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx#lines-1-3041"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1156
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 1/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 1 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx`, part 1 of 3 (lines 1–3041 of the extracted text), extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | From Planning to Fulfillment – Consumer Products (6AA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 8](#_Toc232858252)

[2 Prerequisites 9](#_Toc232858253)

[2.1 System Access 9](#_Toc232858254)

[2.2 Roles 9](#_Toc232858255)

[2.3 Master Data, Organizational Data, and Other Data 11](#_Toc232858256)

[2.4 Business Conditions 17](#_Toc232858257)

[2.5 Additional Manual Configuration 18](#_Toc232858258)

[2.5.1 Manual Configuration for EDI Setup 18](#_Toc232858259)

[2.5.2 Additional Return Reason “Delivery Refusal” 19](#_Toc232858260)

[2.5.3 Define Item Category Determination in Deliveries 21](#_Toc232858261)

[2.6 Preliminary Steps 22](#_Toc232858262)

[2.6.1 Production Capacity Evaluation and Leveling – Consumer Products (5OI) 22](#_Toc232858263)

[2.6.1.1 Create Work Center Group 22](#_Toc232858264)

[2.6.1.2 Check Available Capacity in Work Center 23](#_Toc232858265)

[2.6.1.3 Check Formulas in Work Center 24](#_Toc232858266)

[2.6.1.4 Check Routings 25](#_Toc232858267)

[2.6.1.5 Check Production Version 27](#_Toc232858268)

[2.6.2 Procurement of Production Components – Consumer Products (5W3) 28](#_Toc232858269)

[2.6.2.1 Create Purchasing Info Record 28](#_Toc232858270)

[2.6.2.2 Check Flexible Workflow for Purchase Order Approval 31](#_Toc232858271)

[2.6.2.3 Configure Flexible Workflow for Purchase Order 32](#_Toc232858272)

[2.6.2.4 Manage Conditions to Restart Flexible Workflow for Purchase Orders 33](#_Toc232858273)

[2.6.2.5 Master Data Update for Automatic Purchase Order Creation from Purchase Requisition 35](#_Toc232858274)

[2.6.2.5.1 Change Material Master Data - Purchasing Data 35](#_Toc232858275)

[2.6.2.5.2 Change Supplier Master Data - Purchasing Organization Data 36](#_Toc232858276)

[2.6.2.5.3 Generate Source List 37](#_Toc232858277)

[2.6.2.6 Expand Inspection Method Long Text (Optional) 39](#_Toc232858278)

[2.6.2.7 Change Inspection Plan for Raw Material 40](#_Toc232858279)

[2.6.2.8 Create Quality Info Record in Procurement (Optional) 41](#_Toc232858280)

[2.6.2.9 Create Batch (Optional) 42](#_Toc232858281)

[2.6.3 Quality Management in Discrete Manufacturing – Consumer Products (5HK) 43](#_Toc232858282)

[2.6.3.1 Attach Document to Inspection Method (Optional) 43](#_Toc232858283)

[2.6.3.2 Adopt Routings for Packed Roasted Coffee Beans 45](#_Toc232858284)

[2.6.3.2.1 Routings for Packed Medium Roasted Coffee Beans 45](#_Toc232858285)

[2.6.3.2.2 Routings for Packed Dark Roasted Coffee Beans 47](#_Toc232858286)

[2.6.3.3 Change Inspection Plan for Finished Materials 48](#_Toc232858287)

[2.6.3.4 Create Initial Material Stock 51](#_Toc232858288)

[2.6.4 Subcontracting – Consumer Products (5W4) 52](#_Toc232858289)

[2.6.4.1 Define Item Category Determination in Deliveries 52](#_Toc232858290)

[2.6.4.2 Create Purchasing Info Record (Optional) 53](#_Toc232858291)

[2.6.4.3 Check Flexible Workflow for Purchase Order Approval 55](#_Toc232858292)

[2.6.4.4 Configure Flexible Workflow for Purchase Order 56](#_Toc232858293)

[2.6.4.5 Change Master Inspection Characteristic Visual Pack Check 57](#_Toc232858294)

[2.6.4.6 Create Initial Material Stock 58](#_Toc232858295)

[2.6.4.7 Create Batch 60](#_Toc232858296)

[2.6.5 Sell from Stock – Consumer Products (5HL) 61](#_Toc232858297)

[2.6.5.1 Set Initial Stock for Material 61](#_Toc232858298)

[2.6.5.2 Maintain Product Hierarchy to Distribution Chain (Optional) 63](#_Toc232858299)

[2.6.5.3 Create Customer Hierarchy 64](#_Toc232858300)

[2.6.5.4 Create Condition Records (Optional) 67](#_Toc232858301)

[2.6.5.5 Set a Credit Limit (Optional) 68](#_Toc232858302)

[2.6.5.6 Set Relevance for Sell from Stock with VSiT 69](#_Toc232858303)

[3 Overview Table 71](#_Toc232858304)

[4 Test Procedures 85](#_Toc232858305)

[4.1 Production Capacity Evaluation and Leveling - Consumer Products (5OI) 85](#_Toc232858306)

[4.1.1 Anonymous Forecast and MRP 86](#_Toc232858307)

[4.1.1.1 Option 1: Create Planned Independent Requirements 86](#_Toc232858308)

[4.1.1.2 Option 2: Create Planned Independent Requirements by Upload File 88](#_Toc232858309)

[4.1.1.3 Schedule pMRP Simulation Creation 90](#_Toc232858310)

[4.1.1.4 Process pMRP Simulations 92](#_Toc232858311)

[4.1.1.5 Check Planned Independent Requirements 95](#_Toc232858312)

[4.1.1.6 Material Requirements Planning 96](#_Toc232858313)

[4.1.2 Evaluate Capacity Situation 97](#_Toc232858314)

[4.1.2.1 Check Capacity Situation 98](#_Toc232858315)

[4.1.2.2 Apply Changes to Available Capacity 99](#_Toc232858316)

[4.1.3 Production Capacity Leveling 101](#_Toc232858317)

[4.1.3.1 Production Scheduling 102](#_Toc232858318)

[4.1.3.2 Review Work Center Schedules 104](#_Toc232858319)

[4.1.3.3 Review Capacity Situation 105](#_Toc232858320)

[4.2 Procurement of Production Components – Consumer Products (5W3) 107](#_Toc232858321)

[4.2.1 Procurement of Stock Material with QM - Raw Material 108](#_Toc232858322)

[4.2.1.1 Create Purchase Requisition 108](#_Toc232858323)

[4.2.1.1.1 Option 1: Create Purchase Requisition via MRP Run 108](#_Toc232858324)

[4.2.1.1.2 Option 2: Create Purchase Requisition manually 114](#_Toc232858325)

[4.2.1.2 Create Purchase Order 116](#_Toc232858326)

[4.2.1.2.1 Option 1: Convert Purchase Requisitions to Purchase Orders 116](#_Toc232858327)

[4.2.1.2.2 Option 2: Create Purchase Order Manually 117](#_Toc232858328)

[4.2.1.3 Preview Purchase Order (Optional) 120](#_Toc232858329)

[4.2.1.4 Change Purchase Order (Optional) 121](#_Toc232858330)

[4.2.1.5 Monitor Purchase Order Items (Optional) 122](#_Toc232858331)

[4.2.1.6 Execute Mass Changes to Purchase Orders (Optional) 123](#_Toc232858332)

[4.2.2 Source Inspection Process (Optional) 125](#_Toc232858333)

[4.2.2.1 Review Quality Settings in Material Master (Optional) 125](#_Toc232858334)

[4.2.2.2 Review Quality Info Record (Optional) 126](#_Toc232858335)

[4.2.2.3 Display Inspection Plan for Inspection Characteristics (Optional) 127](#_Toc232858336)

[4.2.2.4 Quality Inspection (Inspection before Goods Receipt) 128](#_Toc232858337)

[4.2.2.4.1 Create Inspection Lot 128](#_Toc232858338)

[4.2.2.4.2 Display Quality Technician Overview (Optional) 130](#_Toc232858339)

[4.2.2.4.3 Change Inspection Lot and Assign Batch 130](#_Toc232858340)

[4.2.2.4.4 Record Inspection Results 132](#_Toc232858341)

[4.2.2.4.5 Display Quality Engineer Overview (Optional) 133](#_Toc232858342)

[4.2.2.4.6 Make Usage Decision 135](#_Toc232858343)

[4.2.3 Post Goods Receipt 136](#_Toc232858344)

[4.2.4 Preview Goods Receipt Slip and Label (Optional) 137](#_Toc232858345)

[4.2.5 Check Goods Receipt Details (Optional) 139](#_Toc232858346)

[4.2.6 Quality Inspection (Goods Receipt Inspection) 140](#_Toc232858347)

[4.2.6.1 Display Material Stock Before Quality Inspection (Optional) 140](#_Toc232858348)

[4.2.6.2 Display Inspection Plan for Inspection Characteristics (Optional) 141](#_Toc232858349)

[4.2.6.3 Display Quality Technician Overview (Optional) 142](#_Toc232858350)

[4.2.6.4 Display Open Inspection Lots (Optional) 143](#_Toc232858351)

[4.2.6.5 Record Inspection Results 145](#_Toc232858352)

[4.2.6.6 Display Quality Engineer Overview (Optional) 148](#_Toc232858353)

[4.2.6.7 Make Usage Decision 149](#_Toc232858354)

[4.2.6.8 Display Material Stock after Quality Inspection (Optional) 151](#_Toc232858355)

[4.2.6.9 Display Inspection Results History (Optional) 152](#_Toc232858356)

[4.2.7 Procurement of Stock Material without QM – Packaging 153](#_Toc232858357)

[4.2.7.1 Create Purchase Requisition 153](#_Toc232858358)

[4.2.7.1.1 Option 1: Create Purchase Requisition via MRP run 153](#_Toc232858359)

[4.2.7.1.2 Option 2: Create Purchase Requisition manually 154](#_Toc232858360)

[4.2.7.2 Approve Purchase Requisition 156](#_Toc232858361)

[4.2.7.3 Automatic Conversion of Purchase Requisition to Purchase Order 157](#_Toc232858362)

[4.2.7.4 Approve Purchase Order (Optional) 159](#_Toc232858363)

[4.2.7.5 Post Goods Receipt 160](#_Toc232858364)

[4.2.8 Evaluations 161](#_Toc232858365)

[4.2.8.1 Batch Information Cockpit – Top-Down and Bottom-Up Analysis 161](#_Toc232858366)

[4.3 Quality Management in Discrete Manufacturing - Consumer Products (5HK) 162](#_Toc232858367)

[4.3.1 Anonymous Forecast and MRP 163](#_Toc232858368)

[4.3.1.1 Option 1: Create Planned Independent Requirements 163](#_Toc232858369)

[4.3.1.2 Option 2: Create Planned Independent Requirements by Upload File 165](#_Toc232858370)

[4.3.1.3 Material Requirements Planning at Plant Level 167](#_Toc232858371)

[4.3.1.4 Evaluate Stock/Requirements Situation 169](#_Toc232858372)

[4.3.2 Production Order Conversion and Available-to-Promise Check for Packed Roasted Coffee Beans 172](#_Toc232858373)

[4.3.2.1 Convert Planned Orders to Production Orders 172](#_Toc232858374)

[4.3.2.2 Review Material Availability Status for Production Orders 174](#_Toc232858375)

[4.3.3 Production Order Processing for Packed Roasted Coffee Beans 176](#_Toc232858376)

[4.3.3.1 Execute Material Staging 176](#_Toc232858377)

[4.3.3.2 Release Production Order 177](#_Toc232858378)

[4.3.3.3 Goods Issue of Batch-Managed Raw Materials via Pick List 179](#_Toc232858379)

[4.3.4 Quality Management – Overview Inspection Lots for Packed Roasted Coffee Beans 180](#_Toc232858380)

[4.3.4.1 Display Open Inspection Lots 180](#_Toc232858381)

[4.3.5 Quality Inspection – In-Process Control (Operation Roasting) for Packed Roasted Coffee Beans 182](#_Toc232858382)

[4.3.5.1 Display Routing for Inspection Characteristics 182](#_Toc232858383)

[4.3.5.2 Display Quality Technician Overview (Optional) 184](#_Toc232858384)

[4.3.5.3 Display Open Inspection Lots (Optional) 184](#_Toc232858385)

[4.3.5.4 Execute Quality Inspection with Inspection Points for Operation Roasting 186](#_Toc232858386)

[4.3.5.5 Display Inspection Results History (Optional) 188](#_Toc232858387)

[4.3.6 Production Order Confirmation of Roasting and Cooling Process for Packed Roasted Coffee Beans 189](#_Toc232858388)

[4.3.6.1 Confirm Production for Operation Roasting 189](#_Toc232858389)

[4.3.6.2 Confirm Production for Operation Cooling 190](#_Toc232858390)

[4.3.6.3 Monitor Order Progress (Optional) 192](#_Toc232858391)

[4.3.7 Quality Inspection – Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt) 193](#_Toc232858392)

[4.3.7.1 Display Inspection Plan for Inspection Characteristics 193](#_Toc232858393)

[4.3.7.2 Display Quality Technician Overview (Optional) 194](#_Toc232858394)

[4.3.7.3 Display Open Inspection Lots (Optional) 195](#_Toc232858395)

[4.3.7.4 Record Inspection Results (Option 1: Before Goods Receipt) 197](#_Toc232858396)

[4.3.7.5 Display Inspection Results History (Optional) 199](#_Toc232858397)

[4.3.8 Quality Inspection – In-Process Control (Operation Packaging) and Usage Decision for Packed Roasted Coffee Beans 200](#_Toc232858398)

[4.3.8.1 Record Inspection Results (Hierarchical Worklist) 200](#_Toc232858399)

[4.3.8.2 Display Inspection Results History (Optional) 203](#_Toc232858400)

[4.3.8.3 Display Quality Engineer Overview (Optional) 204](#_Toc232858401)

[4.3.8.4 Make Usage Decision 205](#_Toc232858402)

[4.3.9 Production Order Confirmation for Packaging Process of Packed Roasted Coffee Beans 208](#_Toc232858403)

[4.3.9.1 Confirm Production incl. Component-Backflush for Operation Packaging 208](#_Toc232858404)

[4.3.9.2 Post Goods Receipt for Production Order 209](#_Toc232858405)

[4.3.9.3 Evaluate Stock/Requirements Situation after Goods Receipt for Production Order 210](#_Toc232858406)

[4.3.10 Quality Inspection – Early Goods Receipt Inspection/ End-Product-Control and Usage Decision (After Goods Receipt) 212](#_Toc232858407)

[4.3.10.1 Display Material Stock Before Usage Decision 212](#_Toc232858408)

[4.3.10.2 Display Open Inspection Lots 213](#_Toc232858409)

[4.3.10.3 Record Inspection Results (Option 2: After Goods Receipt) 214](#_Toc232858410)

[4.3.10.4 Display Quality Engineer Overview (Optional) 215](#_Toc232858411)

[4.3.10.5 Make Usage Decision 216](#_Toc232858412)

[4.3.10.6 Display Material Stock after Usage Decision 218](#_Toc232858413)

[4.3.11 Production Order Processing and Quality Inspection for Packed Roasted Coffee Beans (Dark) 219](#_Toc232858414)

[4.3.11.1 Option 1: Create Initial Material Stock for Packed Roasted Coffee Beans (Dark) 219](#_Toc232858415)

[4.3.11.2 Option 2: Execute Process Steps described for Packed Roasted Coffee Beans (Medium) also for Packed Dark Roasted Coffee Beans (Dark) 221](#_Toc232858416)

[4.3.12 Production Order Conversion for Coffee Display 223](#_Toc232858417)

[4.3.12.1 Create and Release Production Order 223](#_Toc232858418)

[4.3.13 Production Order Processing for Coffee Displays 225](#_Toc232858419)

[4.3.13.1 Goods Issue of Batch-Managed Components 225](#_Toc232858420)

[4.3.13.1.1 Option 1: Goods Issue of Batch-Managed Components via Pick List 225](#_Toc232858421)

[4.3.13.1.2 Option 2: Manual Goods Issue (Instead of Picking List) 226](#_Toc232858422)

[4.3.13.2 Review Production Order (Optional) 227](#_Toc232858423)

[4.3.13.3 Confirm Production Order and Post Goods Receipt 229](#_Toc232858424)

[4.3.14 Quality Inspection – Goods Receipt Inspection and Usage Decision for for Coffee Displays 231](#_Toc232858425)

[4.3.14.1 Display Material Stock Before Quality Inspection (Optional) 231](#_Toc232858426)

[4.3.14.2 Display Inspection Plan for Inspection Characteristics 232](#_Toc232858427)

[4.3.14.3 Display Quality Technician Overview (Optional) 233](#_Toc232858428)

[4.3.14.4 Display Open Inspection Lots 234](#_Toc232858429)

[4.3.14.5 Record Inspection Results (Hierarchical Worklist) 235](#_Toc232858430)

[4.3.14.6 Display Quality Engineer Overview (Optional) 237](#_Toc232858431)

[4.3.14.7 Make Usage Decision 238](#_Toc232858432)

[4.3.14.8 Display Material Stock After Usage Decision 240](#_Toc232858433)

[4.3.15 Evaluations 241](#_Toc232858434)

[4.3.15.1 Review Scrap Report (Optional) 241](#_Toc232858435)

[4.3.15.2 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 242](#_Toc232858436)

[4.4 Subcontracting - Consumer Products (5W4) 244](#_Toc232858437)

[4.4.1 Anonymous Forecast and MRP 245](#_Toc232858438)

[4.4.1.1 Option 1: Create Planned Independent Requirements 245](#_Toc232858439)

[4.4.1.2 Option 2: Create Planned Independent Requirements by Upload File 247](#_Toc232858440)

[4.4.1.3 Material Requirements Planning at Plant Level 249](#_Toc232858441)

[4.4.1.4 Evaluate Stock/Requirements Situation and Prepare Planned Order for Subcontracting 251](#_Toc232858442)

[4.4.1.5 Convert Planned Order to Purchase Requisiton 252](#_Toc232858443)

[4.4.2 Subcontracting 253](#_Toc232858444)

[4.4.2.1 Create Purchase Order 253](#_Toc232858445)

[4.4.2.1.1 Option 1: Convert Purchase Requisition to Purchase Order 253](#_Toc232858446)

[4.4.2.1.2 Option 2: Create Purchase Order manually 255](#_Toc232858447)

[4.4.2.1.3 Option 3 : Create Purchase Order manually with Inbound Delivery 256](#_Toc232858448)

[4.4.2.2 Approve Purchase Orders (Optional) 258](#_Toc232858449)

[4.4.2.3 Monitor Subcontracting Documents (Optional) 259](#_Toc232858450)

[4.4.2.4 Material Requirements Planning at Plant Level 259](#_Toc232858451)

[4.4.2.5 Evaluate Stock/Requirements Situation (Optional) 261](#_Toc232858452)

[4.4.2.6 Transfer Components to the Subcontractor 262](#_Toc232858453)

[4.4.2.7 Batch Transfer Posting 263](#_Toc232858454)

[4.4.2.8 Batch Traceability 265](#_Toc232858455)

[4.4.2.9 Evaluate Stock/Requirements Situation 266](#_Toc232858456)

[4.4.2.10 Create Inbound Delivery for Subcontracting Purchase Order (Optional) 266](#_Toc232858457)

[4.4.2.11 Goods Receipt for Subcontracting Purchase Order 267](#_Toc232858458)

[4.4.2.11.1 Option 1: Receive Goods for Subcontracting Purchase Order 267](#_Toc232858459)

[4.4.2.11.2 Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery 269](#_Toc232858460)

[4.4.2.12 Evaluate Stock/Requirements Situation 270](#_Toc232858461)

[4.4.3 Quality Inspection 271](#_Toc232858462)

[4.4.3.1 Display Material Stock Before Quality Inspection (Optional) 272](#_Toc232858463)

[4.4.3.2 Display Inspection Plan for Inspection Characteristics (Optional) 273](#_Toc232858464)

[4.4.3.3 Display Quality Technician Overview (Optional) 274](#_Toc232858465)

[4.4.3.4 Display Open Inspection Lots (Optional) 274](#_Toc232858466)

[4.4.3.5 Record Inspection Results 276](#_Toc232858467)

[4.4.3.6 Display Quality Engineer Overview (Optional) 277](#_Toc232858468)

[4.4.3.7 Make Usage Decision 279](#_Toc232858469)

[4.4.3.8 Display Material Stock after Usage Decision (Optional) 280](#_Toc232858470)

[4.4.4 Invoicing 281](#_Toc232858471)

[4.4.4.1 Create Supplier Invoice 281](#_Toc232858472)

[4.4.4.2 Review Supplier Invoice (Optional) 283](#_Toc232858473)

[4.4.5 Batch Traceability 284](#_Toc232858474)

[4.4.5.1 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 284](#_Toc232858475)

[4.5 Sell from Stock - Consumer Products (5HL) 286](#_Toc232858476)

[4.5.1 Sell from Stock 286](#_Toc232858477)

[4.5.1.1 Create Sales Order 286](#_Toc232858478)

[4.5.1.2 Review and Release or Reject a Sales Order (Optional) 288](#_Toc232858479)

[4.5.1.2.1 Review Sales Order (Optional) 289](#_Toc232858480)

[4.5.1.2.2 Release Sales Order (Optional) 290](#_Toc232858481)

[4.5.1.2.3 Reject Sales Order (Optional) 291](#_Toc232858482)

[4.5.1.3 Advanced Available-to-Promise Processing (Optional) 292](#_Toc232858483)

[4.5.1.4 Create Delivery 293](#_Toc232858484)

[4.5.1.5 Execute Picking 294](#_Toc232858485)

[4.5.1.6 Check Batches (Optional) 296](#_Toc232858486)

[4.5.1.7 Post Goods Issue 296](#_Toc232858487)

[4.5.1.8 Confirm Proof of Delivery 298](#_Toc232858488)

[4.5.1.9 Create Billing Document 299](#_Toc232858489)

[4.5.1.10 Send Invoice - EDI Relevant 301](#_Toc232858490)

[4.5.1.11 Check Invoice in AIF (Message Dashboard) - EDI relevant 302](#_Toc232858491)

[4.5.1.12 Create Invoice List 302](#_Toc232858492)

[4.5.2 Sell from Valuated Stock in Transit 304](#_Toc232858493)

[4.5.2.1 Create Sales Order 304](#_Toc232858494)

[4.5.2.2 Create Delivery 307](#_Toc232858495)

[4.5.2.3 Execute Picking 308](#_Toc232858496)

[4.5.2.4 Check Batches (Optional) 310](#_Toc232858497)

[4.5.2.5 Post Goods Issue 311](#_Toc232858498)

[4.5.2.6 Confirm Proof of Delivery 312](#_Toc232858499)

[4.5.2.7 Create Billing Document 313](#_Toc232858500)

[4.6 Customer Returns Management – Consumer Products (61V) 315](#_Toc232858501)

[4.6.1 Goods are Returned to Seller 316](#_Toc232858502)

[4.6.1.1 Create Returns Order 316](#_Toc232858503)

[4.6.1.2 Execute Picking 319](#_Toc232858504)

[4.6.1.3 Post Goods Receipt 320](#_Toc232858505)

[4.6.1.4 Perform Material Inspection 321](#_Toc232858506)

[4.6.1.5 Determine Refund 323](#_Toc232858507)

[4.6.1.6 Display Returns Overview 324](#_Toc232858508)

[4.6.1.7 Credit Memo 326](#_Toc232858509)

[4.6.1.7.1 Create Credit Memo 326](#_Toc232858510)

[4.6.2 Scheduling Job (Alternative) 328](#_Toc232858511)

[4.6.2.1 Job Scheduling for Goods Issue Deliveries (Alternative) 328](#_Toc232858512)

[4.6.2.2 Job Scheduling for Billing Creation (Alternative) 329](#_Toc232858513)

[4.6.2.3 Job Scheduling for Billing Release (Alternative) 330](#_Toc232858514)

[4.6.2.4 Job Scheduling for Billing Output (Alternative) 331](#_Toc232858515)

[5 Appendix 333](#_Toc232858516)

[5.1 Succeeding Processes 333](#_Toc232858517)

## Purpose

Overview

The following scope items are incorporated in a scenario that can be executed with the same set of master data for all areas:

- Production Capacity Evaluation and Leveling – Consumer Products (5OI)
- Procurement of Production Components – Consumer Products (5W3)
- Quality Management in Discrete Manufacturing – Consumer Products (5HK)
- Subcontracting – Consumer Products (5W4)
- Sell from Stock – Consumer Products (5HL)
- Advanced Returns Management – Consumer Products (61V)

Additional Consumer Products satellite scenarios consume the same master data and use the transactional data of this scenario or have own master data with a similar structure. These scope items are:

- Supplier Evaluation and Performance Monitoring – Consumer Products (6A6)
- Product Cost Related Master Data Changes – Consumer Products (61W)

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT |  |  |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
|  |  |  |  |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0502 | Display Med + Dark 48 * 1kg Arabica | Batch Managed Finished Material MTS, QM, Manufacturing Date |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch Managed Finished Material, MTS with Maximum Lot Size, QM |
| Material | FG0512 | Carton 12 x 1kg Bags Dark Beans Arabica | Batch Managed Finished Material, MTS with Maximum Lot Size, QM |
| Material | PK0501 | Coffee Bag "Medium" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0502 | Coffee Bag "Dark" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0504 | PK0504 | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0507 | Carton for 12 x 1kg Bags | Packaging Material, MRP and Costing Relevant |
| Material | PK0508 | Display Carton Coffee Beans 48 x 1 kg | Packaging Material, MRP and Costing Relevant |
| Material | RM0501 | Raw Coffee Beans- Arabica | Batch Managed Raw Material |
| Material | TG0501 | Thermo Coffee Cup 0,4l | No serial number, no batch |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331R | Storage Location Returns |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Shipping Point | 331R | Shipping Point 331R |  |
| Company code | 3310 | Company Code 3310 |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- |
| FG0502 | 0 | FERT | PC | Finished Good for MTS processing with Batch Management |
| FG0511 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS |
| PK0501 | 2 | VERP | PC | Packaging Material, Batch Managed, External Procurement |
| PK0504 | 2 | VERP | PC | Label |
| PK0507 | 2 | VERP | PC | Packaging Material |
| RM0501 | 2 | RAW | PC | Raw Material, Batch Managed, External Procurement |
| FG0512 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS |
| PK0502 | 2 | VERP | PC | Packaging Material, Batch Managed, External Procurement |
| PK0504 | 2 | VERP | PC | Label |
| PK0507 | 2 | VERP | PC | Packaging Material |
| RM0501 | 2 | RAW | PC | Raw Material, Batch Managed, External Procurement |
| PK0508 | 1 | VERP | PC | Packaging Material |
| PK0504 | 1 | VERP | PC | Label |

Work Center

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| DP050001 | 3310 | 0001 | Display Packaging 1 |
| DR050001 | 3310 | 0001 | Drum Roasting Machine 1 |
| PM050001 | 3310 | 0001 | Packaging Machine 1 |
| CS050001 | 3310 | 0001 | Cooling Sieve 1 |
| DR050002 | 3310 | 0001 | Drum Roasting Machine 2 |
| PM050002 | 3310 | 0001 | Packaging Machine 2 |
| CS050001 | 3310 | 0001 | Cooling Sieve 2 |
| DP050002 | 3310 | 0001 | Display Packaging 2 |

Available capacity for work center

This overview shows predefined shifts (Shift Sequence: Capacity Group PP):

| Shift | Start time | End time | Length of break |
| --- | --- | --- | --- |
| YS1, Early Shift | 06:00:00 | 14:00:00 | 00:30:00 |
| YS2, Late Shift | 14:00:00 | 22:00:00 | 00:30:00 |
| YS3, Night Shift | 22:00:00 | 06:00:00 | 00:30:00 |

Quality Master Inspection Characteristics

| Master data | Value | Plant | Master. data details | Comments |
| --- | --- | --- | --- | --- |
| Master Inspection Characteristic | YQM00001 | 3310 | Roast Color (Medium) |  |
| Master Inspection Characteristic | YQM00002 | 3310 | Roast Color (Dark) |  |
| Master Inspection Characteristic | YQM00003 | 3310 | Temperature |  |
| Master Inspection Characteristic | YQM00004 | 3310 | Weight |  |
| Master Inspection Characteristic | YQM00005 | 3310 | Sensory |  |
| Master Inspection Characteristic | YQM00006 | 3310 | Relative Humidity |  |
| Master Inspection Characteristic | YQM00007 | 3310 | Rebrand |  |
| Master Inspection Characteristic | YQM00008 | 3310 | Visual Pack Check |  |
| Master Inspection Characteristic | YQM00009 | 3310 | Label Check |  |
| Master Inspection Characteristic | YQM00010 | 3310 | Pest Control |  |
| Master Inspection Characteristic | YQM00011 | 3310 | Defect Grade Raw Coffee Beans (NYBOT) |  |
| Master Inspection Characteristic | YQM00012 | 3310 | Sensory Raw Coffee Beans (SCAA) |  |
| Master Inspection Characteristic | YQUALI01 | 3310 | Surface |  |

QM Work Center

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| QMCP | 3310 | 0001 | QM Check Point |
| QMLABS | 3310 | 0001 | QM Check Point |

Suppliers:

Below mentioned Suppliers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Plant | Comments |
| --- | --- | --- | --- | --- |
| Supplier | 33305001 | Domestic AE Supplier CP | 3310 |  |
| Supplier | 33300002 | Domestic Supplier 2 | 3310 |  |
| Company Code | 3310 | Company Code 3310 | 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 | 3310 |  |

Customer:

Below mentioned Customers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33105001 | Domestic CP Customer 01 |  |
| Ship-to Party | 33105001 | Domestic CP Customer 01 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105002 | Domestic CP Customer 02 |  |
| Ship-to Party | 33105002 | Domestic CP Customer 02 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105005 | Domestic CP Customer 05 |  |
| Ship-to Party | 33105005 | Domestic CP Customer 05 |  |
| Payer | 33105005 | Domestic CP Payer Customer 05 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BND | Create Customer Master - MDS |
| BNY | Create Quality Management Attributes for Material/Product Master - MDS |
| 2ZW | Create Batch Management Master Data - MDS |
| BET | Create Sales Pricing Condition - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:● Run through the Procurement of Direct Materials (J45) test script process.● Or create stock using Post Goods Movement app (refer to Preliminary Steps section for details). |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BNU - Create Costing Run - MDS | Complete all steps in the test script. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Inspection type 03 and 04 are already provided for all relevant materials. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FIN_FSCM_REBUILD_DCD | Rebuild DCD functionality |

### Additional Manual Configuration

#### Manual Configuration for EDI Setup

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b3c61b5831551bdcfbd95d460e071143)

|  |
| --- |
| Note Please ensure while doing the set up use the Business partner (Bill to party as required example 33105001 or 33105002) and relevant Settings for Billing Document (Supplier Invoice). |

#### Additional Return Reason “Delivery Refusal”

In the CP industry it often occurs that customers refuse to accept the goods shipped to them, for example if the agreed delivery window agreed upon was missed. In such a case the truck returns to the delivering plant without having the goods unloaded. It is then a 100% return of the complete delivery. Still one wants to at least briefly inspect the goods if there has been damaged during transport. For this process a special return reason “delivery refusal” shall be created.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the additional return reason.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Configure Your Solution | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Claims, Returns, and Refund Management | All entries display in All Items section. |  |
| 5 |  | Find the entry with item name Customer Returns and choose arrow at the item end. | Configure Your Solution – Customer Returns screen displays. |  |
| 6 |  | In Configuration Steps section, choose Configure in column Actions for step Define Return Reasons for Customer Returns | Change View “Define Return Reasons for Customer Returns”: Change screen displays. |  |
| 7 |  | Choose New Entries, enter the following data and choose Save.Ret.Reason: for example: ZC1Return Reason Description: for example: Delivery Refusal | Return reason is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Return Reasons for Customer Returns | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Return Reasons for Customer Returns.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View Define Return Reasons for Customer Returns screen displays. |  |
| 3 |  | Choose New Entries, enter the following data and choose Save.Return Reason: ZC1Description: Delivery Refusal | Return reason is defined. |  |

#### Define Item Category Determination in Deliveries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: Supply ChainSub Application Area: Delivery Management | All entries are displayed in All Items section. |  |
| 5 | Item Name | Choose Item Deliveries and choose arrow at the item end. | A List of configuration steps displays. |  |
| 6 | Choose Configuration Step | For Deliveries, Choose the as action step Define Item Category Determination in Deliveries and press Configure. | The Configuration opens. |  |
| 7 | New Entries | Add a new entry for following combination:Delivery Type: ELItem category Group: ERLAUsage: VDefault Item category : ELN |  |  |
| 8 | Save your data | Choose Save. | The Delivery Type is enhanced for Item Category. |  |

### Preliminary Steps

#### Production Capacity Evaluation and Leveling – Consumer Products (5OI)

##### Create Work Center Group

In this business process, you are responsible for the capacity planning of some coffee roasting and packaging machines. With the function of work center groups you are able to combine them to one group an use this group as simplified entry for selected capacity apps instead of entering work center individually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The Manage Work Center Groups screen is displayed. |  |
| 3 | Enter Data | On the Manage Work Center Groups screen, choose Create. In the Selection Conditions area, enter the following data and press Enter.In the Create Group dialog box, make the following entries and choose Create:Group: 05_CoffeeDescription: Coffee ProductionGroup Type: ALTERNATIVPlant: 3310 |  |  |
| 4 | Manage Work Center Groups | On the Manage Work Center Groups screen, choose Assign Work Center.In the Work Center dialog box, select the following work center and choose OK:Work Center: DR050001, DR050002, CS050001, CS050002, PM050001, PM050002, DP050001, DP050002 |  |  |

##### Check Available Capacity in Work Center

Purpose

Standard available capacity is applied to the work centers and no shifts are assigned initially. In case these values have been adjusted during testing, we recommend that you have a check to better understand the current available capacity for work centers DR050001, PM050001, CS050001, and DP050001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The Manage Work Center Groups screen is displayed. |  |
| 3 | Enter Work Center Group | On the Manage Work Center Groups screen, select the following entries and choose the details arrow:Name: 05_COFFEEPlant: 3310 |  |  |
| 4 | Choose Work Center | On the Manage Work Center Groups screen, in section Assigned Work Centers click on one of the work centers. A pop up appears where you choose Change Work Center.Work Center: DR050001, PM050001, CS050001 and DP050001 |  |  |
| 5 | Choose Capacity Category 001 | Choose Capacities tab. There, you can find two Capacity categories defined: 001 and 002.Double-click Capacity category: 001. | The Change Work Center: Capacity Overview screen displays.Note Capacity Category 002 is not available for work center CS050001. |  |
| 6 | Check Standard Available Capacity | On the Change Work Center Capacity: Header screen for capacity 001, check standard available capacity. Following values are preset in this scenario:Start time: 06:00:00End time: 22:00:00Length of break: 01:00:00Capacity Utilization: 80No. Ind. Capacities: 1For testing purpose, we recommend using the same values as above. |  |  |
| 7 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner (If you cant see this option then click Menu > Goto > Intervals and Shifts ).On the Change Work Center Capacity: Intervals of Available Capacity screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next 6 weeks.Choose any line you want to delete, then choose Delete line icon in the upper right.Choose Back twice to screen Change Work Center Capacity: Overview. |  |  |
| 8 | Choose Capacity Category 002 | Under Capacities tab, double-click Capacity category: 002. | The Change Work Center: Capacity Overview screen displays.Note Capacity Category 002 is not available for work center CS050001. Hence skip steps #8 and #9 for this work center. |  |
| 9 | Check Default Settings for Capacity Category 002 | Repeat step #6 and #7 for category 002. |  |  |
| 10 | Save | Choose Save. | Work center XXX in plant 3310 was changed. |  |

##### Check Formulas in Work Center

Purpose

This process step shows you how to check and set the formulas used in work centers for critical operation. Formula under Capacities tab is used to calculate the capacity requirements of the operation segments; while formula under Scheduling tab is used to calculate execution time of the operation. You need to check and set formulas for following work centers: DR050001, PM050001, CS050001 and DP050001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center: Initial Screen, make the following entries and press Enter:Plant: 3310Work Center: <Work Center>, e.g. DR050001, PM050001, CS050001 and DP050001. |  |  |
| 4 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 001. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP006 |  |  |
| 5 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 002. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP007 | Note Capacity Category 002 is not available for work center CS050001. |  |
| 6 | Check Formulas under Scheduling Tab | Choose Scheduling tab, check following settings. For test purpose, we recommend using the same values as below:Scheduling basis section:Capacity category: 001Execution time section:Duration of Setup: SAP001Processing Duration: SAP002 |  |  |
| 7 | Exit | Choose Save or Cancel. |  |  |

##### Check Routings

Purpose

If you want to use SAP pre-delivered demo data to run through this scenario, you need to check Routing settings in your system. We recommend to be consistent with what is described in section Routing in chapter Master Data. If it is not consistent, you need to manually change it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). |  |  |
| 3 | Select Finished Material | On the Change Routing: Initial Screen screen, enter the following data and choose Continue:Plant: 3310Material: FG0511 |  |  |
| 4 | Check Routing for Finished Material (Cartons with Coffee Bags) | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: DR050001Operation 0020 - Work Center: CS050001Operation 0030 - Work Center: PM050001GrC: 2Operation 0010 - Work Center: DR050002Operation 0020 - Work Center: CS050002Operation 0030 – Work Center: PM050002If the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |
| 5 | Select Finished Material (Carton with Coffee Bags) | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: FG0512 |  |  |
| 6 | Check Routing for Finished Material (Carton with Coffee Bags) | Check listed Routing versions for Finished Material FG0512 as mentioned in step #4. |  |  |
| 7 | Select Finished Material (Display) | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: FG0502 |  |  |
| 8 | Check routing for Finished Material (Display) | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: DP050001Operation 0020 - Work Center: DP050001GrC: 2Operation 0010 - Work Center: DP050002Operation 0020 - Work Center: DP050002If the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |

##### Check Production Version

Purpose

Production Versions are used as source of supply during production scheduling. This process step shows you how to check the alternative work centers which are assigned to the critical operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Select Finished Material (Carton with Coffee Bean Bags) | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG0511 |  |  |
| 4 | Check Production Version for Finished Materials (Carton with Coffee Bean Bags) | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: Drum Roast 1Production Version: 0002Production Line: Drum Roast 2 |  |  |
| 5 | Repeat Steps | Repeat steps #3 and #4 for Finished Material FG0512. |  |  |
| 6 | Select Finished Material (Display) | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG0502 |  |  |
| 7 | Check Production Version for Finished Materials (Display) | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: Display Packaging 1Production Version: 0002Production Line: Display Packaging 2 |  |  |

#### Procurement of Production Components – Consumer Products (5W3)

##### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create Purchasing Info Records for Raw Material RM0501 and Supplier 33300002 and for the Packaging Materials PK0501, PK0502, PK0504, PK0507 and PK0508 and Supplier 33305001.

|  |
| --- |
| Note If the Purchasing Info Records for the materials already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300002Material: RM0501Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From: Select value from F4 helpNote When the TDT (time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.Order Unit: KGStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 31.12.9999Amount: 4.44Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |
| 11 | Repeat Steps | Repeat the above steps to create the Info Record for the packaging materials using the following data:PK0501: Supplier 33305001, Purchasing Group 002, net price: 45 AED per 100 PC.PK0502: Supplier 33305001, Purchasing Group 002, net price: 45 AED per 100 PC.PK0504: Supplier 33305001, Purchasing Group 002, net price: 5 AED per 100 PC.PK0507: Supplier 33305001, Purchasing Group 002, net price: 1,30 AED per 1 PC.PK0508: Supplier 33305001, Purchasing Group 002, net price: 47,50 AED per 1 PC. |  |  |

##### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

##### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 002Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

##### Manage Conditions to Restart Flexible Workflow for Purchase Orders

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Manage Conditions to Restart Flexible Workflow, then choose Search.Select the line of the item for Item Name Purchase Order Processing, and go to the next screen.On the Purchase Order Processing screen, search for Manage Conditions to Restart Flexible Workflow for Purchase Orders and choose Configure. | The Manage Conditions to Restart Flexible Workflow for POs screen is displayed. |  |
| 5 | Conditions to Restart Flexible Workflow | You can see that the Purchase Order Attributes have been enabled for the Restart Flexible Workflow for PO and Always Restart for Restart Type. | The conditions to Restart Flexible Workflow for Purchase Order have been verified. |  |

SAP Central Business Configuration:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Check Define Rules for Determination of Master Form Template | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Manage Conditions to Restart Flexible Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Conditions to Restart Flexible Workflow | You can see that the Purchase Order Attributes have been enabled for the Restart Flexible Workflow for PO and Always Restart for Restart Type. | The conditions to Restart Flexible Workflow for Purchase Order have been verified. |  |

Result

The conditions to Restart Flexible Workflow for Purchase Order has been verified.

##### Master Data Update for Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note If you want to perform the step Procurement of Stock Material without QM - Packaging, run these Preliminary steps. |

Prerequisite

By default, you have completed the creation of master data, including material master data, supplier master data and Info Record.

You can find general information on how to create master data objects in the Master Data Scripts (MDS) BNF and BNE.

###### Change Material Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing material master data for the materials used for automatic purchase order creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Master Data Specialist - Product Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Material (MM02). | The Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: PK0501Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entries:Plant: 3310Choose Continue. | The Change Material XXXXX (Material general) displays. |  |
| 6 | Select Autom.PO | Scroll down to the General Data section and select the following:Autom.PO: <selected> | Autom.PO is selected. |  |
| 7 | Save your data | Choose Save. | The material master data is updated. |  |
| 8 | Repeat Steps | Repeat the steps above for the other packaging materials PK0502, PK0504, PK0507 and PK0508. |  |  |

Result

The Autom.PO checkbox is selected.

###### Change Supplier Master Data - Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing supplier master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Master Data Specialist - Business Partner Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Find: Business PartnerBy: Supplier NumberSupplier Number: 33305001Choose Start. The Supplier row displays.Double-click the Supplier Partner row. | The Supplier information screen displays. |  |
| 4 | Switch to Change mode | Ensure you are in Change mode. Otherwise, select Switch Between Display and Change. | The Change mode screen displays. |  |
| 5 | Change BP role | In the Change in BP role field, choose the following value: Supplier (defined) |  |  |
| 6 | Open Purchasing Organization Data | Choose the Purchasing tab at the top of the screen. | The Purchasing Organization sub section screen displays. |  |
| 7 | Enter Purchasing Data | Choose Switch Organization.Make the following entry and choose Enter:Purch. Organization: 3310 |  |  |
| 8 | Select Automatic PO checkbox | From the Purchasing Data section, scroll down to the Additional Purchasing Data section, make the following entry:Automatic Purchase Order: <selected> | The Automatic PO checkbox is selected. |  |
| 9 | Save your data | Choose Save. | The Supplier change is saved. |  |

###### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating source list.

|  |
| --- |
| Note If you have more than one supplier, choose one fixed supplier in the source list. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Source Lists (F1859). | The Manage Source Lists screen displays. |  |
| 3 | Create Source List | Choose Create. | The Source List screen displays. |  |
| 4 | Enter General Information | Go to General Information area and make the following entries:Material: PK0501Plant: 3310Choose Generate. |  |  |
| 5 | Search these Sources for the Material and Plant | On the Generated Sources sceen, make the following entries:Valid From: <Current Date>Valid To: <31.12.9999>Choose Go, | The Sources are displayed. |  |
| 6 | Choose Sources | Go to Sources (X) area.Choose all lines of items.Choose Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Choose a fixed Source | Go to Supplier 33305001 and make the following entries:Materials Planning: Record Relevant for MRP (1)Status: Fixed Status (Fixed) | The Supplier has been assigned to Fixed Supplier. |  |
| 8 | Save your Data | Choose Create. | The Source List is created. |  |
| 9 | Repeat Steps | Repeat previous steps for the other packaging materials PK0502, PK0504, PK0507 and PK0508. |  |  |

##### Expand Inspection Method Long Text (Optional)

Purpose

Furthermore, you can expand the long text of inspection method for detailed description.

Prerequisite

Inspection Methods GRADE_RB Defect Grade (NYBOT) and SCORE_RB Sensory of Raw Coffee Beans (SCAA) are already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App. | Choose Change Inspection Method (QS33). | The Change Inspection Method Version: Initial Screen appears. |  |
| 3 | Enter Initial Data. | Make the following entries:Plant: 3310Inspect. Method: GRADE_RBChoose Inspection Method. | The Change Inspection Method Version: General Data screen appears. |  |
| 4 | Expand General Data. | Open the existing entry for more details by clicking the Change long text button next to the short text field under General Information:Defect Grade (NYBOT).A sample of 300 g is analyzed to assess the defects.Go back to General Data screen. | The Change Inspection method long text: Language XX screen appears. |  |
| 5 | Save Data. | To save your data, choose Save. |  |  |
| 6 | Check next inspection method. | Repeat steps 1–3 for Inspection Method SCORE_RB. |  |  |
| 7 | Expand General Data. | Open the existing entry for more details and check, if the following long text appears:Sensory of Raw Coffee Beans (SCAA)Specialty Coffee Cupping according SCAA. |  |  |

##### Change Inspection Plan for Raw Material

Purpose

To run through this business scenario, the inspection plans for raw material RM0501 needs to be adapted regarding some master specific limits of quantitative master inspection characteristics.

Prerequisite

Master Inspection Characteristics and inspection plan are already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Change Inspection Plan (QP02). | Change Inspection Plan (Initial Screen) appears. |  |
| 3 | Enter Data | In the Change Inspection Plan (Initial screen), make the following entries:Material: RM0501Plant: 3310Key Date: <today>Choose Continue. | The Change Inspection Plan: Operation Overview view appears. |  |
| 4 | Select Entry Instruction | In the Inspection Plan Change: Task List Overview screen, select the row with Raw Coffee Beans Arabica and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Select Inspection Characteristic | Mark the operation line 0010 Physical Inspection and choose Inspection Characteristics.Select Master Inspection Characteristic YQM00006 Relative Humidity and choose Control Indicators. | Master Inspection Characteristic is selected in the inspection plan. |  |
| 6 | Change Control Indicator for Inspection Characteristic | In the Edit Characteristic Control Indicators view, change the following options: flagLower Specif. Limit and Upper Specif. LimitChoose Continue without further changes.Choose Continue to exit edit.Replace Lower and Upper Limit with: 11-12% | The control indicators for MIC are changed. |  |
| 7 | Save the Changes | Choose Save. |  |  |

##### Create Quality Info Record in Procurement (Optional)

Purpose

If you want to perform source inspection before goods receipt as an additional procurement process step, the quality Info Record in Procurement must be maintained for the relevant material - supplier - plant combination.

This step is only relevant for source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Quality Info Record - Procurement (QI01). | The Create Q-Info Record view displays. |  |
| 3 | Enter General Data | Make the following entries:Material: RM0501Supplier: 33300002Plant: 3310Choose Continue. |  |  |
| 4 | Enter Release Data | In the Release section, enter the following data:Release Until: 31.12.9999 |  |  |
| 5 | Enter Inspection Control Data | In the Inspection Control section, enter the following data:Source Inspection: 0102Lead Time (In Days) Source: 0Source Insp. – No GR: No (Uncheck tickbox) | There are different constellations, which can be used for performing a source inspection. In this example, both a source inspection and a goods receipt inspection shall be done.Note Please confirm upcoming warning message. |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

##### Create Batch (Optional)

Purpose

If you want to perform source inspection before goods receipt, a SAP batch should be created before, containing the object which is to be inspected, e.g. supplier batch.

This step is only relevant for source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Batch (MSC1N). | The Create Batch view displays. |  |
| 3 | Enter General Data | Make the following entries:Material: RM0501Batch: <no entry>Plant: 3310Choose Continue. | Note Please confirm message Caution! Internal number assignment for materials handled in batches. |  |
| 4 | Enter Basic Data | In the Basic Data 1 section, scroll down to Trading Data and enter a supplier batchSupplier Batch: e.g. 1234 |  |  |
| 5 | Save Your Data | Choose Save. | Your data is saved.Note down the batch: ________________ |  |

#### Quality Management in Discrete Manufacturing – Consumer Products (5HK)

##### Attach Document to Inspection Method (Optional)

Purpose

Optionally, you can attach documents to inspection methods for detailed information while quality inspection process.

Furthermore, you can expand the long text of inspection method for detailed description of differences between medium and dark roasted coffee beans.

Prerequisite

Inspection Methods COLOR_RB Color Check of Roasted Beans and SENS_RB Sensory of Roasted Coffee Beans are already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Change Inspection Method (QS33). | The Change Inspection Method Version: Initial Screen appears. |  |
| 3 | Enter Initial Data | Make the following entries:Plant: 3310Inspect. Method: e.g., SENS_RBChoose Inspection Method. | The Change Inspection Method Version: General Data screen appears. |  |
| 4 | Navigate to General Data | Select Change Long Text button besides Short text Textbox :Long Text: Please check sensory attributes for fragrance, flavor, sweetness, acidity, body and aftertaste.Go back to General Data screen. | The Change Inspection method long text: Language XX screen appears. |  |
| 5 | Choose a Document to Attach | Choose Documents from General Information. |  |  |
| 6 | Create Attachment for Document | Choose Create Document.In the Change Inspection Method Version: General Data dialog box, choose Continue/Enter without entering data.Confirm the file upload message by choosing OK and select a file from your file system via double-click.Choose Transfer to navigate back to the Change Inspection Method Version: General Data screen. | Document is assigned to inspection method. |  |
| 7 | Save Data | To save your data, choose Save. |  |  |
| 8 | Check next inspection method | Repeat steps 1–3 for Inspection Method COLOR_RB. |  |  |
| 9 | Navigate to General Data | Select Change Long Text button besides Short text Textbox and check, if the following long text appears.Long Text: Color check of roasted beans. Please use color scale of coffee beans (SCAA) |  |  |
| 10 | Create Attachment | Repeat steps 5–7 for Inspection Method COLOR_RB. |  |  |

##### Adopt Routings for Packed Roasted Coffee Beans

To run through this business scenario, the routings for FG0511 and FG0512 need to be enhanced with the allocation of components to routing operations other than operation 0010. Moreover relevant QM inspection data must be maintained in the routing headers and operations 0010 and 0030.

Prerequisite

The routings for the semifinished materials FG0511 and FG0512 are already available in the system.

###### Routings for Packed Medium Roasted Coffee Beans

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing: Initial Screen is displayed. |  |
| 3 | Enter Allocation Data | On the Change Routing: Initial Screen, make the following entries and choose Continue:Material: FG0511Plant: 3310On the Change Routing: Overview mark the routing with following Group Counter and choose button Allocation:GrC: 1On the Routing Change: Material Component Overview, select the following materials and choose button New Assignment.Material: PK0501, PK0504, PK0507.If the pop up Choose Alternative BOM should appear, select the following BOM and choose OK:Usage: 1Alt BOM: 1On the New Assignment pop up, make the following entries and choose Continue:Activity: 0030 | The allocation of component PK0501, PK0504 and PK0507 to operation 0030 is done. |  |
| 4 | Maintain Header Details | Go Back.On the Change Routing: Overview view, choose button Header.Define Inspection Points Identifier: Y01 Free Insp.Point (Last Sample is valid) | The Change Routing: Header Details view is displayed. |  |
| 5 | Enter Operation Data (Overview) | Choose Header.On the Change Routing: Header Details view, choose button Operations. | The Change Routing: Operation Overview is displayed. |  |
| 6 | Enter Operation Data (Details) for operation 0010 | On the Change Routing: Operation Overview mark the following Operation and choose button Detail:Operation: 0010 | The Change Routing: Operation Details is displayed. |  |
| 7 | Change Operation Data (Details) | On the Change Routing: Operation Details view, scroll to review the Quality Management: Inspection Points section.Select No ReferenceInsp.point Completion: Automatic valuation based on insp. point definitionChoose Back to return to the Operation Overview view. | Note The Reference influences the inspection point creation in results recording later. |  |
| 8 | Enter Operation Data (Details) for operation 0030 | Repeat steps 5 to 7 for the below operation.Operation: 0030 |  |  |
| 9 | Enter Inspection Characteristics for operation 0010 | Mark the operation line 0010 and choose Inspection Characteristics.Assign Master Inspection Characteristic Roast Color (Medium).Master Inspection Characteristic: YQM00001Sampling Procedure: YFIXFIP1Assign Master Inspection Characteristic Temperature.Master Inspection Characteristic: YQM00003Sampling Procedure: YFIXFIP2Replace Lower and Upper Limit with: 210 - 212 °C .Choose Enter.Choose Back to return to Operations Overview screen. | Master Inspection Characteristics are assigned to the routing. |  |
| 10 | Enter Inspection Characteristics for operation 0030 | Mark the operation line 0030 and choose Inspection Characteristics.Assign Master Inspection Characteristic WeightMaster Inspection Characteristic: YQM00004Sampling Procedure: YFIXFIP3Replace Lower Limit with: 1050 gChoose Enter. | Master Inspection Characteristics are assigned to the routing. |  |
| 11 | Save Your Data | Choose Save.Note If Check Task List pop-up appears, click Yes to continue. | Your data is saved. |  |

Repeat steps 1 to 11 for following routing: material/plant combination:

| Material | Plant | GrC | Component to be assigned | Assignment to operation (OpAc) |
| --- | --- | --- | --- | --- |
| FG0511 | 3310 | 2 | PK0501PK0504PK0507 | 0030 |

###### Routings for Packed Dark Roasted Coffee Beans

Procedure

Repeat steps 1 to 11 from previous chapter, but with changed data in steps 3 and 9:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 3 | Enter Allocation Data | On the Change Routing: Initial Screen, make the following entries and choose Continue:Material: FG0512Plant: 3310On the Change Routing: Overview mark the routing with following Group Counter and choose button Allocation:GrC: 1On the Routing Change: Material Component Overview, select the following material and choose button New Assignment.Material: PK0502If the pop up Choose Alternative BOM should appear, select the following BOM and choose OK:Usage: 1Alt BOM: 1On the New Assignment pop up, make the following entries and choose Continue:OpAc: 0030 | The allocation of component PK0502 to operation 0030 is done. |  |
| 9 | Enter Inspection Characteristics for operation 0010 | Mark the operation line 0010 and choose Inspection Characteristics.Assign Master Inspection Characteristic Roast Color (Dark).Master Inspection Characteristic: YQM00002Sampling Procedure: YFIXFIP1Assign Master Inspection Characteristic Temperature.Master Inspection Characteristic: YQM00003Sampling Procedure: YFIXFIP2Replace Lower and Upper Limit with: 225 - 230 °C .Choose Enter. | Master Inspection Characteristics are assigned to the routing. |  |

Also repeat steps 1 to 11 from previous chapter with changed data in steps 3 and 9 for following routing: material/plant combination:

| Material | Plant | GrC | Component to be assigned | Assignment to operation (OpAc) |
| --- | --- | --- | --- | --- |
| FG0512 | 3310 | 2 | PK0502 | 0030 |

##### Change Inspection Plan for Finished Materials

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Create Inspection Plan (QP01) tile. | Create Inspection Plan (Initial view) appears. |  |
| 3 | Enter Data | In the Create Inspection Plan (Initial view), make the following entries:Material: FG0511Plant: 3310Key Date: <today>Choose Continue. | The Create Inspection Plan: Header Details view appears when there is no plan available for the specified material/plant combination.Note If there is a plan available, choose a group from the dialog box and Inspection Plan Create: Task List Overview appears. Choose New Entries to create a new inspection plan. |  |
| 4 | Maintain Header Details | Create Inspection Plan (Header Details) appears. Enter the following data:Usage: Choose from the value help list for usage purpose 5 Goods receiptStatus: Choose from the value help list 4 Released (General)Lot size: Within 1 to 99,999Choose Operations. | Inspection Plan Create: Operation Overview appears. |  |
| 5 | Enter Operation Data (Overview) | On the Inspection Plan Create: Operation Overview view, enter the following:Operation Number: 0010Work Center: QMLABSControl Key: QM01Description: End-Product-ControlMark the operation line item, then choose Operation.Note If the Operation button is not available, choose Menu > Operation . | Create Inspection Plan: Operation Details appears.Note The Control Key influences the planning and processing of inspection operation, for example whether or not inspection characteristics must be maintained for an inspection operation. |  |
| 6 | Operation Data (Details) | On the Create Inspection Plan: Operation Details view, scroll to review the Recording View: single values and summarized result (default view)Choose Back to return to the Operation Overview view. |  |  |
| 7 | Enter Inspection Characteristics | Mark the operation line 0010 and choose Inspection Characteristics.Assign Master Inspection Characteristic Sensory Roasted Beans:Master Inspection Characteristic: YQM00005Sample Procedure: YFIX1Assign Master Inspection Characteristic Relative Humidity and change the tolerances as follows:Master Inspection Characteristic: YQM00006Sample Procedure: YFIX2Replace Upper Limit with: 5%Assign Master Inspection Characteristic RebrandMaster Inspection Characteristic: YQM00007Sample Procedure: YFIX2Replace Lower and Upper Limit with: 14 – 17%Choose Enter. | Master Inspection Characteristics are assigned to inspection plan. |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

Repeat steps 1 to 8 but with changed step 7 for following inspection plan: material/plant combination:

| Material | Plant | GrC |
| --- | --- | --- |
| FG0512 | 3310 | 1 |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 7 | Enter Inspection Characteristics | Mark the operation line 0010 and choose Inspection Characteristic.Assign Master Inspection Characteristic Sensory Roasted Beans:Master Inspection Characteristic: YQM00005Sample Procedure: YFIX1Assign Master Inspection Characteristic Relative Humidity and change the tolerances as follows:Master Inspection Characteristic: YQM00006Sample Procedure: YFIX2Replace Upper Limit with: 5%Assign Master Inspection Characteristic RebrandMaster Inspection Characteristic: YQM00007Sample Procedure: YFIX2Replace Lower and Upper Limit with: 18 – 20%Choose Enter. | Master Inspection Characteristics are assigned to inspection plan. |  |

##### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Make the following entry and choose Enter.Trans./Event: Goods ReceiptReference Document for MIGO Transaction: OtherInit.entry of stBal. :561 |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Plant: 3310Storage Location: 331C for RMXXXX (Raw Materials) materials and PKXXXX (Packaging Materials)On the Quantity tab:Quantity: <Quantity>, for example, <1000> (for RM0501, PK0501, PK0502, PK0507 and PK0504 add 40000 PC/kg and for PK0508, 5000 PC)On the Material tab:Material: <BOM Material>, refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure. You must create initial stock for all materials except for FG0511, FG0512 and FG0502.Ensure that Item OK is selected and choose Next Item to maintain entries for the next material. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

We recommend that you check stock level for FG0511, FG0512 and FG0502. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. Use Post Goods Movement (MIGO) app with movement type 562 resp. for Init.entry of stBal. 562 without any stock indicator to remove stock and run the test again.

#### Subcontracting – Consumer Products (5W4)

##### Define Item Category Determination in Deliveries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: Supply ChainSub Application Area: Delivery Management | All entries are displayed in All Items section. |  |
| 5 | Item Name | Choose Item Deliveries and choose arrow at the item end. | A List of configuration steps displays. |  |
| 6 | Choose Configuration Step | For Deliveries, Choose the as action step Define Item Category Determination in Deliveries and press Configure. | The Configuration opens. |  |
| 7 | New Entries | Add a new entry for following combination:Delivery Type: ELItem category Group: ERLAUsage: VDefault Item category : ELN |  |  |
| 8 | Save your data | Choose Save. | The Delivery Type is enhanced for Item Category. |  |

##### Create Purchasing Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 3 | Enter Initial Data | Make the following entries:Supplier: 33305001Material: FG0502Purchasing Organization: 3310Plant: 3310Select Subcontracting, then press Enter. | The Create Info Record: General Data screen displays. |  |
| 4 | Choose Purch. Org. Data 1 | Choose Purch.Org.Data 1. | The Create Info Record: Purch. Organization Data1 screen displays. |  |
| 5 | Enter Item Data | Enter the following values:Pl. Deliv. Time: 10 DayPurch.Group: 001Tol. Underdl: 10%Tol. Overdl: 10%Standard Qty: 100Net Price: 25,00Price unit: PCTax Code: <Input Tax Code>Version: 0003Press Enter. |  |  |
| 6 | Save your data | Choose Save. | A purchasing info record for subcontracting procurement is saved. |  |

##### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

##### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, make sure that the flexible workflow for purchase document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entries:Name: Test Workflow for Purchase OrderSelect Start Conditions, and in the Start Conditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 001Choose Add another condition and make the following entries:Total Net Amount of Purchase Order is greater than: SelectedAmount: For example, 500Currency: AEDIn Steps area, choose Create and make the following entries:Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipientsChoose Create.Choose Save. | The workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

##### Change Master Inspection Characteristic Visual Pack Check

Purpose

To run through this business scenario, master inspection characteristic YQM00008 Visual Pack Check and YQM00009 Label Check need to be changed to enable classed results recording.

Prerequisite

Master Inspection Characteristic is already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Master Inspection Characteristic (QS23). | Change Master Insp. Characteristic Version: Initial Screen appears. |  |
| 3 | Change Data for Master Inspection Characteristic | In the Change Master Insp. Characteristic Version: Initial Screen make the following entries:Plant: 3310Master Inspection Characteristic: YQM00008 Visual Pack CheckChoose Master Inspection Characteristic. | Change Master Insp. Characteristic Version: General Data view appears. |  |
| 4 | Change Control Indicator for Master Inspection Characteristic | In the Edit Characteristic Click Control Indicators, Change the following option: flagClassed RecordingChoose Continue without further changes.Choose Continue to exit edit. | The control indicator for MIC is changed. |  |
| 5 | Save Your Data | Choose Save. | Your data is saved. |  |
| 6 | Change next Master Inspection Characteristic | Repeat steps 1 - 5 for Master Inspection Characteristic YQM00009 Label Check. |  |  |

##### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. Select for Init.entry of stBal. 561 without any stock indicator and press Enter. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Plant: 3310Storage Location: 331C for PK05XX (Packaging Materials), 331A for FG05XX (Finished Materials)On the Quantity tab:Quantity: <Quantity>, for example, <1000 PC>On the Material tab:Material: <BOM Material>, refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure. You must create initial stock for all materials except for FG0502.On the Batch tab (only available when materials are batch managed):Batch: <batch number> (optional)For FG05XX materials enter Date of Manufacturing: <today´s date>Ensure that Item OK is selected and choose Next Item to maintain entries for the next material. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

|  |
| --- |
| Note We recommend that you check stock level for FG0502. To do that, log on to the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. Use Post Goods Movement (MIGO) app with movement type 562 resp. for Init.entry of stBal. 562 without any stock indicator to remove stock and run the test again. |

##### Create Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even most batches are automatically created during goods receipt it's also necessary to create batches manually. The DRAFT framework enables the creation of a draft instance that can be converted to an active instance at any point in time.

For the subcontracted finished good the batch which will be ordered will be created in advance. The batches from the Finished goods defines the shelf-life expiration date of the subcontracted finished good. In our example, the earliest shelf-life expiration date of the batches of the Finished goods will be used as shelf-life expiration date to the finished good.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Create a Draft Version of a Master Batch Record | Choose Create in the header area. | The Batch screen displays and a new draft master batch record is created. |  |
| 4 | Maintain the Master Batch Record | Make following entries in the Header Data section and choose Enter:Material : FG0502Batch: <batch number for the finished good>Shelf-life expiration date:<earliest shelf life expiration date of the components>Date of Manufacture: <Current date>Country/Region of Origin: AE | The classification of the batch displays when the material field valuted.When you select enter the draft version of the master batch record is saved and the respective information displays in the bottom status bar.Depending on the configuration of the classification the characteristics can be valuated or are displayed as read only fields. |  |
| 5 | Leave the Page | Leave the page without choosing Create.Choose Back. | The Home screen displays. |  |
| 6 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 7 | Search the Draft Master Batch Record | Make following entries:Material Number: FG0502Editing Status: Own DraftChoose Go. | The list of suitable draft Master Batch Records displays. You should also find the one created in step 4. |  |
| 8 | Save the Daft Master Batch Record | Choose the line with the draft master batch record and choose Create on the Batch screen. | The draft master batch record is opened and is converted to a persistent one. If the batch number is configured to be assigned automatically, it will be populated.The batch fact sheet is shown in display mode.Make a note of the batch number ____________________. |  |

#### Sell from Stock – Consumer Products (5HL)

##### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays.Note It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : FG0502 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |
| 9 | Repeat all steps from above | Use Material: FG0512, FG0511, TG0501 |  |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&Fin Bal |
| Finished Goods (FERT) | 13400000Inventory FinishedGd | 39912000Inv Init SF&Fin Bal |

##### Maintain Product Hierarchy to Distribution Chain (Optional)

Purpose

This process helps you to maintain Product Hierarchy to Distribution Chain if you are using Product Hierarchy relevant materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Product Hierarchy Assignments (F4240). | The Manage Product Hierarchy Assignments (F4240) screen displays. |  |
| 3 | Create New Object | Choose Create. | The Create Product Hierachy Assignment Screen displays. |  |
| 4 | Enter General Information | On the Create Product Hierachy Assignment screen, in the General Information tab, make the following entries:Purpose: 02 SalesSales Organization: 3310Distribution Channel: 10Valid From: <For example, Current Date>Valid To: <For example, Current Date + 1 Year>Note If there exists an active product hierarchy assignment, then proceed to the next step.And if necessary, the user may change the valid dates.Product Hierachy: HOTDRINKS |  |  |
| 5 | Save the Entry | Choose Create. |  |  |

##### Create Customer Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a customer hierarchy for the existing customers. The customers in this script will belong to the same hierarchy.

|  |
| --- |
| Note In case a customer hierarchy already exists from script 6V0 this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Hierarchies (F5794) app. | The Manage Customer Hierarchies screen opens. |  |
| 3 | Create new Hierarchy | Choose Create. | The screen to create a new customer hierarchy is displayed. |  |
| 4 | Enter new Hierarchy | Make the following entries:Type: Customer Hierarchy – SalesHierarchy ID: AE05_0001Hierarchy Description: CP Customer CorporationStart Date: <First of current month>Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create. | The Hierarchy List shows the new hierarchy with status Draft. |  |
| 5 | Create Customer Hierarchy Nodes | Click on the details (>) chevron on the right side of the list entry for the newly created customer hierarchy. | The view pane for the Hierarchy AE05_0001 appears on the right side of the screen. |  |
| 6 | Add new Nodes | Choose Edit. | The pane switches to Edit Mode. |  |
| 7 |  | Choose the Fast Entry Icon on the right hand side of the line for the top-node in the Nodes section. | Fast Entry Screen for Nodes appears.. |  |
| 8 | Fast Entry of Nodes | Choose Subnodes and mark them as pricing relevant:ID: RE_WEST_HQ ; Description: Headquarter Region WestID: RE_SOUTH_HQ ; Description: Headquarter Region SouthID: RE_MIDDLE_HQ ; Description: Headquarter Region MiddleChoose OK. | The subnodes are created. |  |
| 9 | Enter the next level nodes | On the line for RE_WEST_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 10 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 11 | Enter the next level nodes | On the line for RE_SOUTH_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 12 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 13 | Enter the next level nodes | On the line for RE_MIDDLE_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 14 |  | Enter the following data:ID:Description:Price Relevant: CheckedChoose OK. | Subnode is created. |  |
| 15 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 16 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105005Choose OK. | Business Partner Subnode is created. |  |
| 17 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 18 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105001Choose OK. | Business Partner Subnode is created. |  |
| 19 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 20 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105002Choose OK. | Business Partner Subnode is created. |  |
| 21 | Save your data | Choose Save. | The hierarchy is saved with status Draft. |  |
| 22 | Activate the Hierarchy | Choose Activate. | The hierarchy status changes from Draft to Active. |  |

##### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Prices - Sales (F4111) app. | The Manage Prices – Sales screen is displayed. |  |
| 3 | Enter Condition Type | Make the following entries and Enter:ConditionType: <Customer Hierarchy>Key Combination: Choose <4BN DCH1 010> from the help list.Sales Organization: 3310Distribution Channel: 10Choose Go. | The list of existing condition records is displayed. If there are no conditions created yet, the list will be empty. |  |
| 4 | Create new condition record | Choose Create. | An entry line on top of the list appears, condition table, Sales Organization, Distribution Channel are pre-filled from the entered filter values. |  |
| 5 |  | Make the following entries:Sales Organization: 3310Distribution Channel: 10Customer Hierarchy Root Node ID: AE05_0001Customer Hierarchy Node ID: RE_SOUTH_HQValid From: enter todays dateCondition Amount or Ratio: <-7,500>Choose Save.Valid To: leave default value | The condition record is created. |  |

##### Set a Credit Limit (Optional)

Purpose

In this activity, you set a credit limit for the customer. The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency that is defined when the solution is activated. |

|  |
| --- |
| Note If you use the Create Credit Segment configuration step, if you want to set the Credit Segment 1000 in the FLEXIBLE_CHECK field to a value of 3 on the Main Segment and Segment levels, you must also enter a credit limit for Credit Segment 0000. |

Prerequisite

Business partner master record 33105005 is already created with credit management profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts (F4596) view is displayed. |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33105005For the row in the Worklist, choose Details (>). |  |  |
| 4 | Maintain Credit Profile | Choose the Scoring tab.Choose Edit.Make the following entries:Calculation Rule: Standard rule without Automatic calculationRisk Class: Medium Default RiskCredit Check Rule: 01 Default - All Checks Active |  |  |
| 5 | Maintain Credit Segment | Choose the Credit Segments tab. Review or enter the following values in the Credit Segment field:Credit Segment: 1000 Credit Segment 1000 (Maintained)Credit Limit: 5.00Go to the Credit Segment line and make the following entry and choose Apply:Limit Valid To: <End of Year>Note If the Valid To field is not visible, you can go into View Settings and select it to display it.Note Repeat this step to set a credit limit on Credit Segment 0000 to avoid the sales order being blocked at headquarter credit check. | The amount and validity date are set for the credit limit. |  |
| 6 | Save | Save your entries. | Changes have been saved. |  |

##### Set Relevance for Sell from Stock with VSiT

Purpose

You need to set relevance for item category, sales org, plant and incoterm with VSiT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Set Version | Choose Set Local Version in the end of the screen.In the pop-up window, choose Local Country Version and Set Local Version. |  |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 5 | Choose SSCUI | On the Configure Your Solution: Realize Phase screen, search for SSCUI named Set Relevance for Sell-from-Stock with VSiT Process (105504) under Sales Application Area. |  |  |
| 6 | Access SSCUI | Click the line of the SSCUI, and choose Configure. |  |  |
| 7 | Set Relevance for Sell-from-Stock with VSiT | On the Change View "Set Relevance for Sell from Stock with VSiT": Overview screen, choose New Entries and make the following entries:Item Category: TANSOrg: 3310Plant: 3310Incoterm: DAPRelevance for SFS VSiT Process: Relevant for SFS VSiT ProcessChoose Save. | The relevant entries have been set for SFS VSiT Process. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Production Capacity Evaluation and Leveling - Consumer Products (5OI) |  |  |  |
| Anonymous Forecast and MRP |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_48) | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_49) [page ] 88 | Production Planner | Maintain PIRs (F3445) |  |
| [Schedule pMRP Simulation Creation](#unique_50) [page ] 90 | Production Planner | Schedule pMRP Simulation Creation (F3968) | Application job is finished with no error. |
| [Process pMRP Simulations](#unique_51) [page ] 92 | Production Planner | Process pMRP Simulations (F3934) | The capacity issues are reduced. |
| [Check Planned Independent Requirements](#unique_52) [page ] 95 | Production Planner | Maintain PIRs (F3445) | The PIRs for top level materials are updated into requirement plan version 00. |
| [Material Requirements Planning](#unique_53) [page ] 96 | Production Planner | Schedule MRP Runs (F1339) | MRP Run is executed. |
| Evaluate Capacity Situation |  |  |  |
| [Check Capacity Situation](#unique_54) [page ] 98 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is identified. |
| [Apply Changes to Available Capacity](#unique_55) [page ] 99 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is resolved. |
| Production Capacity Leveling |  |  |  |
| [Production Scheduling](#unique_56) [page ] 102 | Production Planner | Capacity Scheduling Table (F3770) | Order is rescheduled and dispatched. |
| [Review Work Center Schedules](#unique_57) [page ] 104 | Production Planner | Capacity Scheduling Board (F3951) | Capacity situation has been reviewed and adopted (optional). |
| [Review Capacity Situation](#unique_58) [page ] 105 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity situation is finally reviewed. |
| Procurement with and without QM - Consumer Products (5W3) |  |  |  |
| Procurement of Stock Material with QM - Raw Material |  |  |  |
| Create Purchase Requisition |  |  |  |
| Option 1: Create Purchase Requisition via MRP Run |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_59) [page ] 108 | Production Planner. | Maintain PIRs (F3445). |  |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_60) [page ] 110 | Production Planner. | Maintain PIRs (F3445). |  |
| [Material Requirements Planning at Plant Level](#unique_61) [page ] 113 | Production Planner. | Open Schedule MRP Runs (F1339). |  |
| [Option 2: Create Purchase Requisition manually](#unique_62) | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisitions are created manually. |
| Create Purchase Order |  |  |  |
| [Option 1: Convert Purchase Requisitions to Purchase Orders](#unique_63) | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | A purchase order is created. |
| [Option 2: Create Purchase Order manually](#unique_64) | Purchaser | Manage Purchase Orders (F0842A) | A purchase order is created. |
| [Preview Purchase Order (Optional)](#unique_65) | Purchaser | Manage Purchase Orders (F0842A) | The preview of an existing purchase order is done. |
| [Change Purchase Order (Optional)](#unique_66) | Purchaser | Manage Purchase Orders (F0842A) | An existing purchase order is changed. |
| [Monitor Purchase Order Items (Optional)](#unique_67) | Purchaser | Monitor Purchase Order Items (F2358) | The purchase order items are monitored. |
| [Execute Mass Changes to Purchase Orders (Optional)](#unique_68) | Purchaser | Mass Changes to Purchase Orders (F2593) | Changes to multiple selected Purchase Orders in bulk are done. |
| Source Inspection Process (Optional) |  |  |  |
| [Review Quality Settings in Material Master (Optional)](#unique_69) | Master Data Specialist - Product Data | Display Material (MM03) | The material master is displayed. |
| [Review Quality Info Record (Optional)](#unique_70) | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_71) | Quality Planner | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| Quality Inspection (Inspection before Goods Receipt) |  |  |  |
| [Create Inspection Lot](#unique_72) | Quality Engineer | Source Inspections - Worklist (QI07) | Inspection Lot is created. |
| [Display Quality Technician Overview (Optional)](#unique_73) | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Change Inspection Lot and Assign Batch](#unique_74) | Quality Technician | Manage Inspection Lots (F2343) | The Quality Technician opens the created source inspection lot and assigns relevant batch with supplier batch information. |
| [Record Inspection Results](#unique_75) | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_76) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_77) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Post Goods Receipt](#unique_78) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The goods receipt to a purchase order is posted. |
| [Preview Goods Receipt Slip and Label (Optional)](#unique_79) | Warehouse Clerk | Material Documents Overview (F1077) | The material document is reviewed. |
| [Check Goods Receipt Details (Optional)](#unique_80) | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt fact sheet is displayed. |
| Quality Inspection (Goods Receipt Inspection) |  |  |  |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_81) | Inventory Manager | Stock - Single Material (F1076) | Material stock is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_82) | Quality Technician | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| [Display Quality Technician Overview (Optional)](#unique_83) | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Display Open Inspection Lots (Optional)](#unique_84) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot for which he or she wants to record inspection results. |
| [Record Inspection Results](#unique_85) | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_86) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_87) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Display Material Stock after Quality Inspection (Optional)](#unique_88) | Inventory Manager | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted use stock or in another storage location. |
| [Display Inspection Results History (Optional)](#unique_89) | Quality Engineer | Display Results History (F2428) | Ths inspection results history is reviewed. |
| Procurement of Stock Material without QM – Packaging |  |  |  |
| Create Purchase Requisition |  |  |  |
| [Option 1: Create Purchase Requisition via MRP run](#unique_90) [page ] 153 | Production Planner | Multiple Apps | Purchase requisitions are created by MRP run. |
| [Option 2: Create Purchase Requisition manually](#unique_91) | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisitions are created manually. |
| [Approve Purchase Requisition](#unique_92) [page ] 156 | Manager - Procurement | My Inbox - All Items (F5331) | Purchase Requisition is approved. |
| [Automatic Conversion of Purchase Requisition to Purchase Order](#unique_93) | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | Purchase orders are released automatically via job. |
| [Approve Purchase Order](#unique_94) | Purchasing Manager | My Inbox - All Items (F5331) | A purchase order is released. |
| [Post Goods Receipt](#unique_95) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The receipt of goods with reference to an existing purchase order is posted. |
| Evaluations |  |  |  |
| [Batch Information Cockpit – Top Down and Bottom-Up-Analysis](#unique_96) | Quality Technician | Batch Information Cockpit (BMBC) | Batch usage is reviewed. |
| Quality Management in Discrete Manufacturing - Consumer Products (5HK) |  |  |  |
| Anonymous Forecast and MRP |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_97) | Production Planner. | Maintain PIRs (F3445). |  |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_98) | Production Planner. | Maintain PIRs (F3445). |  |
| [Material Requirements Planning at Plant Level](#unique_99) | Production Planner. | Open Schedule MRP Runs (F1339). |  |
| [Evaluate Stock/Requirements Situation](#unique_100) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| Production Order Conversion and Available-to-Promise Check for Packed Roasted Coffee Beans |  |  |  |
| [Convert Planned Orders to Production Orders](#unique_101) | Production Planner | Manage Material Coverage - New Version (F0251A) | Planned Orders for Finished Materials are converted to Production Orders. |
| [Review Material Availability Status for Production Orders](#unique_102) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Missing parts for the production order are displayed. |
| Production Order Processing for Packed Roasted Coffee Beans |  |  |  |
| [Execute Material Staging](#unique_103) | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The components needed for the Finished Material production order are moved from various storage locations to the production storage location. |
| [Release Production Order](#unique_104) [page ] 177 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production order for Finished Material is released. |
| [Goods Issue of Batch-Managed Raw Materials via Pick List](#unique_105) | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods movements are posted. |
| Quality Management – Overview Inspection Lots for Packed Roasted Coffee Beans |  |  |  |
| [Display Open Inspection Lots](#unique_106) | Quality Technician | Manage Inspection Lots (F2343) | Inspection lots after release of production order are reviewed. |
| Quality Inspection – In-Process Control (Operation Roasting) for Packed Roasted Coffee Beans |  |  |  |
| [Display Routing for Inspection Characteristics](#unique_107) | Production Engineer - Discrete Manufacturing | Display Routing (CA03) | The routing setup is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_108) | Quality Technician | Quality Technician Overview (F2361) | An overview of open inspection lots is given. |
| [Display Open Inspection Lots (Optional)](#unique_109) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are checked. |
| [Execute Quality Inspection With Inspection Points for Operation Roasting](#unique_110) | Quality Technician | Record Results for Inspection Points (F2689) | Quality Inspection with Inspection Points is executed. |
| [Display Inspection Results History (Optional)](#unique_111) | Quality Technician | Display Results History (F2428) | Inspection results are reviewed. |
| Production Order Confirmation of Roasting and Cooling Process for Packed Roasted Coffee Beans |  |  |  |
| [Confirm Production for Operation Roasting](#unique_112) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production Order Operation 0010 is confirmed. |
| [Confirm Production for Operation Cooling](#unique_113) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production Order Operation 0020 is confirmed. |
| [Monitor Order Progress (Optional)](#unique_114) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The production order progress is reviewed. |
| Quality Inspection – Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt) |  |  |  |
| [Display Inspection Plan for Inspection Characteristics](#unique_115) | Quality Technician | Display Inspection Plan (QP03) | The Inspection Plan is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_116) | Quality Technician | Quality Technician Overview (F2361) | An overview of open Inspection Lots is given. |
| [Display Open Inspection Lots (Optional)](#unique_117) | Quality Technician | Manage Inspection Lots (F2343) | Open Inspection Lots are reviewed. |
| [Record Inspection Results (Option 1: Before Goods Receipt)](#unique_118) | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded. |
| [Display Inspection Results History (Optional)](#unique_119) | Quality Technician | Display Results History (F2428) | Inspection Results are reviewed. |
| Quality Inspection – In-Process Control (Operation Packaging) and Usage Decision for Packed Roasted Coffee Beans |  |  |  |
| [Record Inspection Results (Hierarchical Worklist)](#unique_120) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Inspection Results History (Optional)](#unique_121) | Quality Engineer | Display Results History (F2428) | Inspection Results are reviewed. |
| [Display Quality Engineer Overview (Optional)](#unique_122) | Quality Engineer | Quality Engineer Overview (F2360) | The Inspection lots without Usage Decision are displayed. |
| [Make Usage Decision](#unique_123) | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is made. |
| Production Order Confirmation for Packaging Process of Packed Roasted Coffee Beans |  |  |  |
| [Confirm Production incl. Component Backflush for Operation Packaging](#unique_124) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Final confirmation of the last operation is carried out. |
| [Post Goods Receipt for Production Order](#unique_125) | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | The goods receipt for the production order is posted. |
| [Evaluate Stock/Requirements Situation after goods receipt for Production Order](#unique_126) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Stock/Requirements situation after goods receipt is analyzed. |
| Quality Inspection – Early Goods Receipt Inspection/ End-Product-Control and Usage Decision (After Goods Receipt) |  |  |  |
| [Display Material Stock before Usage Decision](#unique_127) | Inventory Manager | Stock - Single Material (F1076) | Stock situation is reviewed. |
| [Display Open Inspection Lots](#unique_128) | Quality Technician | Manage Inspection Lots (F2343) | The Inspection Lots are reviewed. |
| [Record Inspection Results (Option 2: After Goods Receipt)](#unique_129) | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_130) | Quality Engineer | Quality Engineer Overview (F2360) | The Inspection lots without Usage Decision are displayed. |
| [Make Usage Decision](#unique_131) | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is executed. |
| [Display Material Stock after Usage Decision](#unique_132) | Warehouse Clerk | Stock - Single Material (F1076) | Stock situation is reviewed. |
| Production Order Processing and Quality Inspection for Packed Roasted Coffee Beans (Dark) |  |  |  |
| [Option 1: Create Initial Material Stock for Finished Material Packed Roasted Coffee Beans (Dark)](#unique_133) | Warehouse Clerk | Post Goods Movement (MIGO) | Stock for Finished Material is created. |
| [Option 2: Execute Process Steps described for Packed Roasted Coffee Beans (Medium) also for Packed Dark Roasted Coffee Beans (Dark)](#unique_134) | various | various | Finished Material is produced and stock is available. |
| Production Order Conversion for Coffee Displays |  |  |  |
| [Create and Release Production Order](#unique_135) | Production Planner | Convert Planned Orders - to Production Orders (CO41) | Production Order for Finished Material is created and released. |
| Production Order Processing for Coffee Displays |  |  |  |
| Goods Issue of Batch-Managed Components |  |  |  |
| [Goods Issue of Batch-Managed Components - Option 1: Goods Issue of Batch-Managed Components via Pick List](#unique_136) | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods Issue of components is posted. |
| [Goods Issue of Batch-Managed Components - Option 2: Manual Goods Issue (Instead of Picking List)](#unique_137) | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Issue of components is posted. |
| [Review Production Order (Optional)](#unique_138) | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | The production order is reviewed. |
| [Confirm Production Order and Post Goods Receipt](#unique_139) | Production Operator - Discrete Manufacturing | Confirm Production Order (CO15) | Final confirmation of production order and goods receipt of finished material is posted. |
| Quality Inspection – Goods Receipt Inspection and Usage Decision for Coffee Displays |  |  |  |
| [Display Material Stock before Quality Inspection (Optional)](#unique_140) | Inventory Manager | Stock - Single Material (F1076) | Stock Situation is reviewed. |
| [Display Inspection Plan for Inspection Characteristics](#unique_141) | Quality Technician | Display Inspection Plan (QP03) | The inspection plan setup is reviewed. |
| [Display Quality Technician Overview (Optional)](#unique_142) | Quality Technician | Quality Technician Overview (F2361) | An overview of open inspection lots is given. |
| [Display Open Inspection Lots](#unique_143) | Quality Technician | Manage Inspection Lots (F2343) | Open Inspection Lots are checked. |
| [Record Inspection Results (Hierarchical Worklist)](#unique_144) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_145) | Quality Engineer | Quality Engineer Overview (F2360) | Inspection results without Usage Decision are reviewed. |
| [Make Usage Decision](#unique_146) | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is executed. |
| [Display Material Stock after Usage Decision](#unique_147) | Inventory Manager | Stock - Single Material (F1076) | Stock Situation is reviewed |
| Evaluations |  |  |  |
| [Review Scrap Report (Optional)](#unique_148) | Production Supervisor - Discrete Manufacturing | Material Scrap - Maximum Deviation (F2035) | The scrap analysis is done. |
| [Batch Information Cockpit - Top Down and Bottom-Up Analysis](#unique_149) | Quality Technician | Batch Information Cockpit (BMBC) | The batch traceability is executed. |
| Subcontracting - Consumer Products (5W4) |  |  |  |
| Anonymous Forecast and MRP |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_150) | Production Planner. | Maintain PIRs (F3445). |  |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_151) | Production Planner. | Maintain PIRs (F3445). |  |
| [Material Requirements Planning at Plant Level](#unique_152) [page ] 249 | Production Planner. | Open Schedule MRP Runs (F1339). |  |
| [Evaluate Stock/ Requirements Situation and Prepare Planned Order for Subcontracting](#unique_153) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Convert Planned Order to Purchase Requisition](#unique_154) | Production Planner | Convert Planned Orders - to Purchase Requisitions (MD15) | A subcontracting purchase requisition is created. |
| Subcontracting |  |  |  |
| Create Purchase Order |  |  |  |
| [Create Purchase Order - Option 1: Convert Purchase Requisition to Purchase Order](#unique_155) | Purchaser | Create Purchase Order via Purchase Requisition Assignment List (ME58) | A Purchase Order is created. |
| [Create Purchase Order - Option 2: Create Purchase Order manually](#unique_156) | Purchaser | Create Purchase Order - Advanced (ME21N) | A Purchase Order is created. |
| [Option 3 : Create Purchase Order manually with Inbound Delivery](#unique_157) [page ] 256 | Purchaser | Create Purchase Order - Advanced (ME21N) | A Purchase Order is created that requires after-wards the creation of an inbound delivery. |
| [Approve Purchase Order (Optional)](#unique_158) | Purchasing Manager | My Inbox - All Items (F0862) | A purchase Order is released. |
| [Monitor Subcontracting Documents (Optional)](#unique_159) | Purchaser | Monitor Subcontracting Documents (F3095) | The subcontracting documents are reviewed. |
| [Execute Material Requirements Planning at Plant Level (Optional)](#unique_61) | Production Planner | Schedule MRP Runs (F1339) | Planned Independent Requirements for Finished Materials and also the components are planned. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_160) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Transfer Components to the Subcontractor](#unique_161) | Inventory Manager | Subcontracting Cockpit (F2948) | The components are delivered to the subcontractor. |
| [Batch Transfer Posting](#unique_162) | Warehouse Clerk | Post Goods Movement (MIGO) | Batches are transferred to delivery batch. |
| [Batch Traceability](#unique_163) | Quality Technician | Batch Information Cockpit (BMBC) | Batch analysis is executed. |
| [Evaluate Stock/Requirements Situation](#unique_164) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Create Inbound Delivery for Subcontracting Purchase Order (Optional)](#unique_165) [page ] 266 | Receiving Specialist. | Create Inbound Delivery (VL31N) | An inbound delivery is created. |
| Goods Receipt for Subcontracting Purchase Order |  |  |  |
| [Option 1: Receive Goods for Subcontracting Purchase Order](#unique_166) [page ] 267 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt from subcontracting material is posted.The goods receipt from subcontracting material is posted. |
| [Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery](#unique_167) [page ] 269 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt from subcontracting material is posted. |
| [Evaluate Stock/Requirements Situation](#unique_168) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| Quality Inspection |  |  |  |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_169) | Inventory Manager | Stock - Single Material (F1076) | Material stock is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_170) | Quality Technician | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| [Display Quality Technician Overview (Optional)](#unique_171) | Quality Technician | Quality Technician Overview (F2361) | Ths inspection results history is reviewed. |
| [Display Open Inspection Lots (Optional)](#unique_172) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot for which he or she wants to record inspection results. |
| [Record Inspection Results](#unique_173) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_174) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_175) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Display Material Stock after Usage Decision (Optional)](#unique_176) | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted use stock or in another storage location. |
| Invoicing |  |  |  |
| [Create Supplier Invoice](#unique_177) | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice verification is done. |
| [Review Supplier Invoice (Optional)](#unique_178) | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Invoice verification is done using document list. |
| Batch Traceability |  |  |  |
| [Batch Information Cockpit - Top-Down and Bottom-Up Analysis](#unique_179) | Quality Technician | Batch Information Cockpit (BMBC) | Batch Analysis is executed. |
| Sell from Stock - Consumer Products (5HL) |  |  |  |
| Sell from Stock |  |  |  |
| [Create Sales Order](#unique_180) [page ] 286 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| Review and Release or Reject a Sales Order (Optional) |  |  |  |
| [Review Sales Order (Optional)](#unique_181) [page ] 289 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The blocked sales order is reviewed. |
| [Release Sales Order (Optional)](#unique_182) [page ] 290 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is released. |
| [Reject Sales Order (Optional)](#unique_183) [page ] 291 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is rejected. |
| [Advanced Available-to-Promise Processing (Optional)](#unique_184) [page ] 292 |  |  |  |
| [Create Delivery](#unique_185) [page ] 293 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Execute Picking](#unique_186) [page ] 294 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_187) [page ] 296 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch updated for outbound delivery. |
| [Post Goods Issue](#unique_188) [page ] 296 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| [Confirm Proof of Delivery](#unique_189) [page ] 298 | Shipping Specialist. | Deliveries Worklist - Proof of Delivery (VLPODL). |  |
| [Create Billing Document](#unique_190) [page ] 299 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created for billing document - Invoice is created and sent from the SAP S/4HANA system (supplier side) to the Buyer system. |
| [Send Invoice - EDI Relevant](#unique_191) [page ] 301 |  |  | Supplier Invoice is automatically sent to the Buyer system. |
| [Check Invoice in AIF (Message Dashboard) - EDI relevant](#unique_192) [page ] 302 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (Invoice) is checked in dashboard. |
| [Create Invoice List](#unique_193) [page ] 302 | Billing Clerk | Manage Invoice Lists (F2740) | Invoice list document number created. |
| Sell from Valuated Stock in Transit |  |  |  |
| [Create Sales Order](#unique_194) [page ] 304 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Delivery](#unique_195) [page ] 307 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_196) | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_197) | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Issue](#unique_198) [page ] 311 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Confirm Proof of Delivery](#unique_199) | Shipping Specialist. | Deliveries Worklist - Proof of Delivery (VLPODL). |  |
| [Create Billing Document](#unique_200) | Billing Clerk | Create Billing Documents (F0798) |  |
| Customer Returns Management – Consumer Products (61V) |  |  |  |
| Goods are Returned to Seller |  |  |  |
| [Create Return Order](#unique_201) | Customer Returns | Open Manage Customer Returns (F1708) | Return order is created, return delivery is generated in the background. |
| [Execute Picking](#unique_202) | Shipping | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for the return delivery. |
| [Post Goods Receipt](#unique_203) | Shipping | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted for return delivery. |
| [Perform Material Inspection](#unique_204) | Receiving | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_205) | Customer Returns | Manage Customer Returns (F1708) | Refund determination is checked or triggered. |
| [Display Return Overview](#unique_206) | Customer Returns | Manage Customer Returns (F1708) | Document flow is displayed. |
| Credit Memo |  |  |  |
| [Create Credit Memo](#unique_207) | Billing | Create Billing Documents (F0798) | Credit memo is created. |
| Scheduling Job (Alternative) |  |  |  |
| [Job Scheduling for Goods Issue Deliveries (Alternative)](#unique_208) | Shipping | Schedule Goods Issue for Deliveries (F2259) | Job for goods issue posting with reference to outbound deliveries is scheduled. |
| [Job Scheduling for Billing Creation (Alternative)](#unique_209) | Billing | Schedule Billing Creation (F1519) | Job for creating billing documents is scheduled. |
| [Job Scheduling for Billing Release (Alternative)](#unique_210) | Billing | Schedule Billing Release (F1518) | Job for release billing documents to accounting is scheduled. |
| [Job Scheduling for Billing Output (Alternative)](#unique_211) | Billing | Schedule Billing Output (F1510) | Job for billing document outputs is scheduled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Production Capacity Evaluation and Leveling - Consumer Products (5OI)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The end-to-end scenario starts with the production capacity planning and evaluation.

The planning process covers a two-stage production process for coffee displays. The first stage reflects the roasting and packaging process of medium resp. dark roasted coffee beans under consideration of a fixed capacity of the roasting drums. The second stage reflects a display packaging process where two different finished products (medium and dark roasted coffee beans bags) are packed into a coffee display.

First step is the creation of a demand forecast for finished material (coffee display) represented by Planned Independent Requirements (PIRs). Predictive Material and Resource Planning (pMRP) is used to create, schedule and evaluate pMRP simulations that support you in making informed decisions for your production planning. The results can be taken over and will be released to your operational data as planned independent requirements.

Based on PIRs, material requirements planning (MRP) creates a production plan for finished materials and explodes the entire bill of material structure. As a result, component production and raw material demands are planned. Production planners can analyze and manually change the planned order-based production plan to resolve upcoming bottleneck situations in their defined area of responsibility.

The process of production capacity leveling represents a central part of preparation for the manufacturing process of components. Production planners can assign orders and operations from the production plan to available timeslots of capacities. Additionally, the planners can simulate and choose other alternatives for production by assigning other available production versions, letting the planners schedule the best option for their manufacturing.

#### Anonymous Forecast and MRP

##### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements (PIRs) to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 1 these PIRs will be created manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case leave this app and access the app Create PIR, make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and continue with step #4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Select the material item, and choose Edit in the upper right. |  |  |
| 7 | Edit PIRs | On the screen, enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 600 PCWeek 2 (current week + 3 weeks): 300 PCWeek 3 (current week + 4 weeks): 400 PCWeek 4 (current week + 5 weeks): 400 PCWeek 5 (current week + 6 weeks): 300 PCWeek 7 (current week + 7 week): 100 PCVersion is Active: YES | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can logon to the SAP Fiori launchpad as a Production Planner and open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

##### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements (PIRs) to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2 these PIRs will be loaded by Upload File.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case leave this app and access the app Create PIR, make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and continue with step #4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Afterward choose Back without saving. |  |  |
| 7 | Edit PIRs | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 600 PCWeek 2 (current week + 3 weeks): 300 PCWeek 3 (current week + 4 weeks): 400 PCWeek 4 (current week + 5 weeks): 400 PCWeek 5 (current week + 6 weeks): 300 PCWeek 7 (current week + 7 week): 100 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducible capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can log on to the SAP Fiori launchpad as a Production Planner and open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

##### Schedule pMRP Simulation Creation

Purpose

This process step shows you how to create pMRP simulation.

|  |
| --- |
| Note Besides of creating a pMRP simulation via top level materials, there are two more job templates for creating pMRP simulations. One is Creation of pMRP Data via Work center and the other is Creation of pMRP Data via Components. In this test script, we only focus on the pMRP simulation creation via top level materials. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: <Creation of pMRP Data via Top Level Materials>Job Name: <Creation of pMRP Data via Top Level Materials - FG0502> |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entry:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries and choose OK.Start Immediately: <select>Recurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the Parameter Section area, make the following entries:ID for Reference Plan: 5OI_PMRP_<MMDD>_XXBucket Category: WStart Date of Reference: <Today’s date + 1 day>End Date of Reference: <Today’s date + 16 weeks>Simulation ID: 5OI_PMRP_SIM_<MMDD>_XXSimulation Description: 5OI_PMRP_SIM_<MMDD>_XXFor Object Selection sub-area:Plant: 3310Material: FG0502MRP Controller: 001For Document Data sub-area:Opening Stock: <blank> | MMDD is today’s date, for example, if the date is August 1st, then MMDD = 0801. XX is a running number, eg 01, 02 etc. |  |
| 7 | Schedule New Job | Choose Check.If there are no error messages, choose Schedule.A new job is created and displays in the Application Jobs table. | Confirm that the application job is finished with no error. Warning can be accepted for production versions 0003 and 0099 of material FG0502. |  |

##### Process pMRP Simulations

Purpose

This process step shows you how to process the created pMRP Simulation to handle bottlenecks and constraints.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 5OI_PMRP_<MMDD>_XX | The simulation displays. |  |
| 4 | Copy the Simulation | Choose the check-box of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entries and choose Copy.Copy from Current Simulation: XNew Simulation ID: 5OI_PMRP_SIMU_<MMDD>_CNew Simulation Description: 5OI_PMRP_SIMU_<MMDD>_COPYOverload Tolerance: 2% | It shows Simulation Copied.You can repeat this step to create several copies of one pMRP Simulation to figure out the best adjusted simulation. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose against the row of the new copied simulation with simulation ID: 5OI_PMRP_SIMU_<MMDD>_C | The Demand Plan Simulation screen displays. |  |
| 6 | Check the Demand-Plan Simulation | On the Demand Plan Simulation screen, you can check the Capacity Issues, Delivery Performance, and Violated Constraints.You can check the demand plan simulation quantities for materials in each period, you can switch the displayed mode, for example:Simulation Table Selection: Reference /Simulation | In our scenario, we would only focus to reduce the capacity issue from top-level material FG0502If there is no capacity issue or violated constraints, skip step 7 - 15. |  |
| 7 | Check Issue Worklist | On the top of screen, choose the Capacity Issues Quantity, the Capacity Issues page displays.Choose Show in Issue List, the Issue List screen displays.In the Issues area, you could see Issue Category, Affected Objects, Affected Weeks, Affected Demands, Impact Score, Impact Cause By and Impact Cause.You could choose Clear Filter icon after Filterd by: Capacity Issues, then you could get the overall issue lists, including Violated Constraints if applicable.Optionally, you can choose one Capacity Overload issue, choose Disregard Capacity Issues. On the pop-up Disregard Capacity Issues screen, choose OK.Choose Demand Plan Simulation on the top of screen and navigate back. | The selected issues have been disregarded in this simulation.And the capacity issue quantites are reduced. |  |
| 8 | Check Capacity Plan Simulation | On the Demand Plan Simulation screen.Choose the <600> (simulation quantity) in the red box for FG0502, the Inspector area displays the relevant capacity overload issues.In the Issues area, choose Capacity Plan Simulation.On the Capacity Plan Simulation screen, you can check the Demand/Remaining Capacity in Hours in table view by default.Choose Show Work Center Overview near the top right corner of Capacity Plan Simulation screen, then it shows in graphic view.Check the overload demand in red for work center whose remaining capacity is less than zero, it indicates the capacity issue. | Continue to reduce the capacity issues or violated constraints in step 9-15. |  |
| 9 | Shift Demand | Choose one of the demands (in red if available) for the work center, for example, DP050001.In Top-Level Materials area, navigate to FG0502 for the latest week, choose Shift Demand on the right.On the Shift Top-Level Demand screen, maintain the following entry:Shift Demand To: <the earliest week>Choose Adopt Proposal, the Quantity is automatically updated with the Proposed Quantity.Choose Apply. | The capacity issues are reduced.You can choose Undo or Redo icon to withdraw or resume your changes of simulation.You can choose Show Change History icon to review all your changes in the Global Hisotry area. |  |
| 10 | Check Multi-Level Material Simulation | Choose the next demand in red for a work center, for example, DP050001.In the Top-Level Materials area, navigate to FG0502, and choose Multi-Level Material Simulation. | The Multi-Level Material Simulation screen displays. |  |
| 11 | Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for BOM components in Bill of Material area.Choose Finished good FG0502, then you choose Change Source of Supply to distribute demand into different production versions to balance workload.On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution, choose Apply. | The capacity issues are reduced. |  |
| 12 | Check Simulation Component | Choose Simulation Views at the top and choose Simulation Components.On the Simulation Components screen, you could see simulation quantities for both head materials and components. You can change display mode from Materials to Supply. | The Simulation Components screen displays. |  |
| 13 | Check Simulation Summary | Choose Simulation Summary at the top.On the Simulation Summary screen, you could check Change in Demand Change in Capacity, Production, Change of Source of Supply, Unresolved Issues, and Disregarded Capacity Issues. | The Simulation Summary screen displays. |  |
| 14 | Check Demand Plan Simulation Again | Choose Simulation Views at the top and navigate back to Demand Plan Simulation. | The Demand Plan Simulation screen displays. |  |
| 15 | Release Simulation | Choose Navigation Menu icon at the top left and navigate to Process pMRP Simulations.On the Process pMRP Simulations screen, filter the simulation with the reference ID and choose Go.Reference Data : 5OI_PMRP_<MMDD>_XXChoose Release for the copied simulation with less capacity issues.On the Release screen, make following entries and choose Release.Create PIRs for Demand-Driven MRP Components: unmarkedCreate PIRs for Top-Level Materials: <X>Create PIRs for Subassembly Components: <X>Requirement Version for Top-Level Materials: 00 REQUIREMENTS PLANVersion Active for Top-Level Materials: YesRequirement Version for Subassembly Components: 00 REQUIREMENTS PLANVersion Active for Subassembly Components: Yes | The simulation status is changed into Released. |  |

##### Check Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the adjusted PIRs for top level material FG0502. They are adjusted to ensure less capacity issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: FG0502Plant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Check PIRs | Select the filtered material items whose last modified date is today, and choose Edit in the upper-right corner.On the Edit PIRs screen, check the generated PIRs for FG0502. | The PIRs for top level materials are updated into requirement plan version 00. |  |

##### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The finished material (FG0502) is planned at plant level. There is now a requirement for the finished material (FG0502) in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG0502>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Option screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG0502Changed BOM Components: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Capacity Situation

All orders and operations that are planned with the MRP are allocated to the required capacities. Production planners can evaluate the capacity utilization for a defined time horizon and execute manual changes in orders to resolve upcoming bottleneck situations in the defined area of responsibility.

To solve the bottleneck situation the available capacities will be adopted.

##### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. This process step shows you how to check the capacities for overload on bottleneck resources.

The Work center group is used as selection criterion to cover all coffee production resources the planner is responsible for.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the user icon, and select App Settings.In the App Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if only following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 001.Choose AOR status button of this entry if not assigned, click AOR status button of the corresponding entry to unassign any other entry then choose Back.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80%Note You add Work Center Group as a filter by choosing Adapt Filters > More Filters (Master Data). Select Work Center Group, choose OK, and then choose Go. |  |  |
| 4 | Filter | Choose following entries as filter, and choose Go.Editing Status: AllLoad Type: OverLoadEvaluation Horizon: From today to 8 weeks afterWork Center Group: 05_COFFEEWe here only focus on capacity requirement due to PIRs we just created. | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined timeframe/ help checking utilization for the past.A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Section “Create Planned Independent Requirements”, increase the PIRs for FG0502 in step 7. Then rerun the whole process.Note If you want to check all work center of the work center group 05_COFFEE, choose Load Type: All |  |
| 5 | Check Bottleneck Work Centers | Choose button Settings above table. From Columns, you can choose different KPIs.KPIs on Capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. Red/Yellow/Green bar shows different percentage level of capacity utilization, with color coding according to the Critical Load/Normal Load settings. The red bar indicates the available capacity exceeds Critical Load percentage, thus there is bottleneck with the work center.Note If the button Show Details is displayed on top of the table, click on it to display all selected columns. |  |  |
| 6 | Next Step | After identifying the bottleneck work center(s), stay on this page and go on with the test as described in the next section. |  |  |

##### Apply Changes to Available Capacity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the bottleneck work centers, you may need to optimize capacity utilization by changing available capacity, e.g., via adding/changing shifts.

|  |
| --- |
| Note If you want to apply changes to multiple work centers at once, please use the app Mass Maintenance of Work Center Capacities (F5381). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check Capacity Situation | Check capacity utilization to identify bottleneck work center, as described in last section Check Capacity Situation. |  |  |
| 4 | Choose Bottleneck Work Center | Use the Work Center filter to filter bottleneck work centers with value help. From the displayed list, choose one of the work centers, for example:Work center: DR050001( Drum Roasting Machine 1)Capacity Category: Machine (001) |  |  |
| 5 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In Operations section, the list provides details on related source orders, e.g. Planned Order for FG0512 resp. FG0511.The Shift section provides a review of available capacity for the specific work center. Check the shifts on bottleneck dates and consider which shifts can be added on these dates to increase available capacity. For example, if shift YS3 is not arranged, you might consider adding YS3 on these dates for this work center. | Bottleneck dates and possible additional shifts are identified. |  |
| 6 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 7 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | Add Shift screen pops up. |  |
| 8 | Check Shift is Added | Check items in Shift section, choose More at the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter e.g., Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 9 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under section Shift, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 150%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 10 | Check Bottleneck | Check capacity utilization in Overview section. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 11 | Check Bottleneck for all the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity.Note If you already solve all bottlenecks here, you will not have bottleneck situations available for the following Production Capacity Leveling Process. Even though you can execute capacity leveling without bottleneck situation we recommend to partly keep the bottlenecks. | The bottleneck for all resources is resolved. |  |

#### Production Capacity Leveling

The process of production capacity leveling represents a central part of preparation for the manufacturing process of components. This process enables production planners to assign orders and operations from the production plan to available timeslots of capacities. Additionally, the planners can simulate and choose other alternatives for production by assigning other available production versions, letting the planners schedule the best option for their manufacturing.

##### Production Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In preliminary steps, the planned orders are generated after MRP Run, and the capacity situation is evaluated and adjusted. This process step shows you how to assign orders and operations from the initially created production plan to available timeslots of capacities.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Table (F3770). |  |  |
| 3 | Check App Settings | In the App Settings dialog box, check if only below entry is assigned:For Industry Type, select the following value and choose OK:Industry Type: DiscreteIn the Basis Controls section, select Area for Responsibility. Select Plant and MRP Controller and choose Assign. Check if only below entries are assigned:Plant 1 AE (3310)MRP Controller 001 (001) |  |  |
| 4 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose the following entries as filter and choose Go.Work Center Group: 05_COFFEEEvaluation Horizon: for example, next 1 monthStatus: Not Dispatched and Dispatched | Critical operation for orders which fulfill the search criteria are displayed.If the tested products are MTO relevant, choose the settings to check Sales Orders and Sales Order Items. |  |
| 5 | Choose Order | Orders for FG0511, FG0512 and FG0502 are displayed in the list. Choose the desired order you want to dispatch. | The Capacity Scheduling Table screen displays. |  |
| 6 | Check Operation Information | In the top section of the detailed screen, check the detailed information about the critical operation.. |  |  |
| 7 | Check Available Time Buckets | In the below area of the right panel, the available source of supply would display under the grid table.Use the calendar selection box to adjust the date bucket in which you need to dispatch the order.For orders producing FG0511 and FG0512, the work centers DR050001 and DR050002 can be used as alternative work centers.For orders producing FG0502, the work centers DP050001 and DP050002 can be used as alternative work centers. | The available capacity (XX H) for each day displays in the time bucket table. |  |
| 8 | Check Strategy | Choose Set Strategy in the upper right corner of the left panel. You can check relevant settings here and adjust if necessary.Planning ModeScheduling ControlDirectionIn this case, we choose the Bucket mode as an example. | There are two planning modes:Bucket: Allocate orders to first available timeslot.Sequence: Define an exact time for the order to start/end (depending on the planning direction). |  |
| 9 | Check Order Information | Under Sourcing & Scheduling section, on the right panel, choose the tab page Additional Information to check detailed order information. |  |  |
| 10 | Check Source of Supply | Under Available Sources of Supply in the bucket table, relevant production version displays. Check the production version marked as Assign. If you want to adopt some other production version instead, you can check the relevant line in the Assign column. |  |  |
| 11 | Choose Available Time Bucket | In the bucket table, choose the radio button before the available capacity (XX H) you want to assign. You may view the available capacity (XX H) by Day, Week or Shift, as well as select the date range. |  |  |
| 12 | Dispatch and Review the Dispatched Orders | Choose Dispatch.Mark the radio button in front of the available capacity once again.Choose Review Dispatched Orders to review the dispatched orders. | A message displays: Dispatch of Order XXXX Operation XXXX scheduled from XXX to XXX was successful. |  |
| 13 | Cancel Dispatch (Optional) | If you need to cancel the dispatch process, select the corresponding operation and choose Deallocate. | The Status becomes Not Dispatched. |  |
| 14 | Realign Schedules (Optional) | If you need to realign the schedule, select corresponding items and choose Realign Schedules.Note Realigning the schedule is only available on the overview screen. Choose back to return to this screen from the details view.Enter the off-set number of days and time, choose Realign (choose Save and Realign if you want to set the day and time as default). | A message Realign Schedules executed appears. For details, see Message Manager.You could choose Insert Operation for Future or Past. The offset threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 15 | Choose Save | Choose Save at the bottom of the left panel. |  |  |

Result

The planned orders are rescheduled according to the available timeslot you choose.

##### Review Work Center Schedules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step enables production planner to monitor schedule status by the visualization of Gantt chart.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Board (F3951). |  |  |
| 3 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose following entries as filter and choose Go.Horizon: for example, next 1 monthWork Center Group: 05_COFFEEStatus: Dispatched |  |  |
| 4 | Monitor Status | Monitor the schedule status in dashboard.View detailed information by selecting an operation and choosing Operation Info. |  |  |
| 5 | Adopt Planning for Work Center (Optional) | If you want to execute further adoptions in capacity planning, mark the work center you want to change capacity planning for and choose button Schedule Production. You will be moved to the Capacity Scheduling table and do further adoptions as already mentioned in previous step. |  |  |
| 6 | Adopt Planning for Operation (Optional) | If you need to execute further adoptions for an operation, select the operations on a resource you want to execute rescheduling for and choose button Manage Operation. On the Manage Operation screen, you can reschedule, deallocate and allocate operations by selecting the corresponding operations in the scheduling board and choosing an appropriate activity button on top of scheduling board.Note Only the actions which are executable with this operation are selectable.As an alternative, you can manually add a rescheduling date for the corresponding operation in the header section and choose the button Reschedule.Note The button Reschedule is only selectable when the scheduling date is changed and Enter is pressed on the keyboard. |  |  |

##### Review Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you have solved all capacity bottlenecks, you finally check the capacity situation of the work centers you are responsible for.

After this final check you can internally produce the planned orders for goods (not part of this scope item - see succeeding processes).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the button, App Settings above the table.In the App Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if only following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 001.Choose AOR status button of this entry if not assigned, click AOR status button of the corresponding entry to unassign any other entry then choose Back.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80%Choose OK, twice. |  |  |
| 4 | Filter | If not already available, add the Work Center Group as filter, by choosing Adapt Filters. Select Work Center Group and choose OK.Choose following entries as filter, and choose Go.Editing Status: AllLoad Type: AllEvaluation Horizon: From today to 8 weeks afterWork Center Group: 05_COFFEE | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined timeframe/ help checking utilization for the past.A list of all work centers of the work center group 05_COFFEE are displayed. |  |
| 5 | Check Work Centers | Choose Settings from above table. From Columns, you can choose different KPIs.KPIs on Capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Check capacity utilization in Overview section. Capacity changes and capacity leveling should result in a better match between requirement capacity and available capacity. Check if the bottlenecks are resolved (all the bars are green).If there are still red bars available, you can repeat the steps in the section Apply changes to Available Capacity or Production Capacity Leveling and check again. You can follow this logic until all bottlenecks are resolved. |  |  |

### Procurement of Production Components – Consumer Products (5W3)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the planning process for the materials has been finished, the procurement of batch-managed raw materials (for example, coffee beans) and packaging materials (for example, bags, cartons) that are needed for production of coffee displays is executed.

The process is realized as a procure-to-stock scenario that uses purchase requisitions that are generated either by the Material Requirements Planning (MRP) process or manually by a requester. The conversion from a purchase requisition to a purchase order can either be done manually or automatically. Alternatively, the purchase orders can be created manually.

The purchase requistions and/or the purchase order can be subject to an approval before being transferred to a purchase order (approval of purchase requisition on line item level) or issued to a supplier (purchase order approval on header level). Goods are shipped from the supplier and the goods receipt is created with reference to the corresponding purchase order.

For some materials, quality inspection activities may be relevant upon goods receipt. For the raw coffee beans, a quality inspection is performed, packaging materials will be handled without quality inspection.

At goods receipt, the material is posted to quality inspection stock and an inspection lot is created based on an inspection plan. The quality technician records the inspection results via selection of the relevant work center. Based on the results, the quality engineer makes a usage decision, such as accepting or rejecting the material, posting the material to unrestricted stock or blocked stock, or triggering return to the supplier, with the option of posting as a consumed sample.

Optionally an additional procurement process step can be performed for a rough visual inspection of raw coffee bean bags before posting the goods receipt and doing the physical and sensory quality inspection. Dependent from inspection results, uploading of tanker shall be approved or rejected by warehouse clerk.

#### Procurement of Stock Material with QM - Raw Material

##### Create Purchase Requisition

The components which need to be purchased in this process are raw materials for the production of the finished materials FG0502, FG0511 or FG0512. The MRP run done earlier for material FG0502 has resulted in requirements for the raw material RM0501 which needs to be purchased.

The creation of purchase requisitions can be done either via MRP run (option 1) or manually (option 2).

Option 1 is already covered by previous steps and can be checked in the Stock-/Requirements List (logon as production planner and choose app Monitor Stock / Requirements List - Old Version (MD04). If a purchase requisition is available in the stock-/requirements list, note down the purchase requisition number. This one can be used to create a purchase order in the overnext section.

Option 2 can be used independently from the creation of purchase requsition by MRP.

###### Option 1: Create Purchase Requisition via MRP Run

###### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates. In Option 1 these PIRs will be loaded by manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0502Choose Save and restart with step 1. |  |
| 5 | Edit PIRs. | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 40 PCWeek 2 (current week + 2 weeks): 80 PCWeek 3 (current week + 3 weeks): 80 PCWeek 4 (current week + 4 weeks): 100 PCWeek 5 (current week + 5 weeks): 80 PCWeek 6 (current week + 6 weeks): 80 PCVersion is Active: YES | Note If already stock for FG0502 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

###### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2, these PIRs will be loaded by Upload File.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and restart with step 4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download Template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Then choose Back without saving. |  |  |
| 7 | Edit PIRs. | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 40 PCWeek 2 (current week + 3 weeks): 80 PCWeek 3 (current week + 4 weeks): 80 PCWeek 4 (current week + 5 weeks): 100 PCWeek 5 (current week + 6 weeks): 80 PCWeek 6 (current week + 7 weeks): 80 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can Log on to the SAP Fiori Launchpad as a Production Planner and Open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs. | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved |  |

###### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

###### Option 2: Create Purchase Requisition manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisition can be created via MRP run (see Option 1) or they can be created manually (Option 2).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen displays. |  |
| 3 | Create New Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | From the Document Type drop-down, select Purchase Requisition (NB). |  |  |
| 5 | Add Item | In the Items section, choose Create then choose Material. | The Purchase Requisition Item screen appears. |  |
| 6 | Enter Detail Data | Enter the following values in General Information section:Item Category: StandardMaterial: RM0501Plant: 3310Enter the following values in Quantity and Date section:Quantity: 10Delivery Date: default valueRequisition Date: default valueRelease Date: default valueEnter the following values in Contact Information section:Requirement Tracking Number: For example, TestTrackPurchasing Organization: 3310Purchasing Group: 002Choose Apply and you will automatically go back to the Purchase Requisition screen. |  |  |
| 7 | Create your Entries | Choose Create. | The purchase requisition is created.Note down the purchase requisition number ___________. |  |

Result

The Purchase Requisition is created.

##### Create Purchase Order

###### Option 1: Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert assigned Purchase Requisitions to Purchase Orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Select material RM0501 and plant 3310. Choose Go.Note If the field material is not displayed by default, choose Adapt Filters and select the field Material ID. Choose OK. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition you created in previous step or select one created by MRP run earlier. Then click on Show More per Row. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | If the Purchase Requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Assign Source of Supply, and select the source from a category present in the Assign Source of Supply window. | The assignment of one source to the requisition is done.Note If the purchase requisition runs into an approval process, please execute the chapter [Approve Purchase Requisition](#unique_92) [page ] 156 and then continue. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Manage Purchase Requisitions screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Doc Type: Standard PO.Choose Order. | The purchase order is created.Note down the purchase order number ___________. |  |
| 8 | Back to Manage Purchase Requisition | Once the order is saved, the Message toast Purchase order has been created is displayed. Click on Back button. | The Processing Status of Purchase Requisition has been changed to PO created. |  |

###### Option 2: Create Purchase Order Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.On the General Information tab, make the following entries:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300002Company Code: 3310Purchasing Organization: 3310Purchasing Group: 002Currency: AEDOn the Delivery and Invoice tab, make the following entries and choose Enter:Payment Terms: 0003Go to Supplier Contact Data tab, the Supplier Address, Telephone, Fax, Contact Person are shown.On the Notes tab, choose > or < to search for Header Text. On the Header text column, enter the free text: xxx for testing.On the Items tab, from the Purchase Order Items screen, choose Create and make the following entries:Material: RM0501Plant: 3310Order Quantity: <quantity>Net Order Price: <price>Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.On the General Information tab, make the following entry:Storage Location: 331CGo to the Delivery Address tab and then navigate to the Address field. Click on the F4 value help to select the Address Number, and then choose Enter.Note This step is optional. If there is no appropriate Address Number in the system for usage, please skip this step.From the Purchase Order Item section, choose Process Flow tab.The following entries display:Goods Receipt: yesInvoice Receipt: <selected>Verify Goods-Receipt-Based Invoice Verification is selected.On the tab Tax, check the following entries:Tax Code: <Default Value>Tax Date: <Default Value>On the Schedule Lines tab, make the following entry:Delivery date: <a date in the future>From the Purchase Order Item section, choose Attachments tab.Select Doc. Type to Upload: For External UseChoose Upload to upload an attachment.Choose Apply to go back to the Purchaser Order screen.Note If you want your purchase order to be assigned to an approver, choose a quantity and total net amount of purchase order higher than 500AED (for Purchase Groups = 002) | The Purchase Order screen is displayed. |  |
| 5 | Generate Output Preview (Optional) | Click the Output Preview button on the header of the purchase order and select the output option as required.Note The Output Preview button is only avaliable when your purchase order is in status Draft, In Approval, Not Yet Sent, or Output Error. | An output preview in PDF format is generated. |  |
| 6 | Verify Purchase Order for Completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box.Note down the purchase order number________ and its Delivery Date________. |  |
| 7 | Check the Purchase Order | Open the created purchase order in display mode and check if the values are displayed as text (code). | The relevant values are displayed as text and code. |  |
| 8 | Check the 6 Column Facet in the Tab | Click on the tab (General Information, Delivery and Invoice, Supplier Contact Data). | The tab (General Information,Delivery and Invoice, Supplier Contact Data) will be having the 6 column facet. |  |

|  |
| --- |
| Note If you do not know who should approve the purchase orders you created, then you can use App Manage Purchase Orders to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. |

##### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can preview an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to check the PO detail. | The Purchase Order screen is displayed. |  |
| 4 | Preview the Purchase Order | If you have selected a purchase order in the purchase order overview list without an 'Advanced' Purchase Order indicator, then continue.Go to the Output Management tab. In the Output Management section, choose Show More per Row and then click on the PDF icon at Display.If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, which means the the purchase order was created by the app Create Purchase Order - Advanced (ME21N), then you will be forwarded to the ME23N. There is no print preview available.Note When the Relevant and Merge are both selected for the document type SL1 and channel print in SSCUI: 103542 (Define Output Settings for Document Type), you upload the attachments of SL1 document type in Attachments Tab at the item level in App: Manage Purchase Orders, then the output should contain the Attachments as Document along with PO output.At the Output line item, the number of attachments for the Line item should match the number of attachments we attached. | The Purchase Order is opened in PDF format. |  |

##### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to change and use the little arrow on the right side to enter the PO detail, then choose Edit, if you have selected a purchase order in the purchase order overview list without an 'Advanced' Purchase Order indicator.If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, which means the the purchase order was created by the app Create Purchase Order - Advanced (ME21N), then change in the change mode by pressing the button Display/Change. | The Purchase Order screen is shown.The Purchase order is opened in change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 5 | Check Purchase Order for completeness | Choose Order, if you have selected a purchase order in the purchase order overview list without 'Advanced' Purchase Order indicator. If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, then choose Save to save the purchase order. | The Purchase Order is complete. |  |
| 6 | Messages (Optional) | Choose Messages (if possible). | If a message is displayed, you must correct the Purchase Order. If no message is displayed, the Purchase Order is complete. |  |
| 7 | Save Purchase Order | Choose Order to save the Purchase Order, if you have selected a purchase order in the purchase order overview list without 'Advanced' Purchase Order indicator. If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, then choose Save to save the purchase order. | The Purchase Order has been saved. The system displays a success message Purchase order has been saved. |  |

##### Monitor Purchase Order Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in purchase orders, but by default only overdue items would be listed in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Monitor Purchase Order Items (F2358). | The Monitor Purchase Order Items screen is displayed. |  |
| 3 | Search for Purchase Orders | The basic filters are displayed.Purchase Order, Display Currency, Material Group, Material, Supplier, Plant, and so on.Make the above entries accordingly, then choose Go. | The search results show the details with the respective filter criteria.You can choose Adapt Filters to select filters. |  |
| 4 | Display Purchase Order | Choose the individual line item of the Purchase Order for which you want to display the PO details. | The Purchase Order Item screen is shown. |  |
| 5 | Verify data | Verify the data displayed on the object page. | The data should correspond to the Purchase Order. |  |

##### Execute Mass Changes to Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can apply changes to multiple selected Purchase Orders in bulk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Mass Changes to Purchase Orders (F2593) app. | The Mass Changes to Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Orders Items | Set values to some filters to search Purchase Orders. For example,Material GroupPurchasing OrganizationPurchasing GroupPlantThen choose GO. | The search results show the details with the respective filter criteria. |  |
| 4 | Select Purchase Order | Select several POs by clicking the checkbox beside the purchase order number. | Purchase Order has been selected. |  |
| 5 | Choose Mass Edit | After selecting an individual purchase order, choose Mass Edit. | A dialog box will open displaying fields for 2 categories – Header fields, Item fields for which values can be changed. |  |
| 6 | Apply Mass Changes | Set new values in the given desired fields.For example: Terms of Payment: Replace Field Value: 0002.Choose Apply Mass Changes. Choose Apply to confirm the Apply Mass Changes screen. Choose Close to close the Success screen. | New values will be set to desired fields for selected Purchase Orders / Items. |  |
| 7 | Check Application Jobs | Choose Monitor Mass Changes.On the Monitor Mass Changes screen, enter the Created At with Today and remove Created By filter as blank. Choose Go and then choose Mass Change Jobs tab. Navigate to the selected Mass Change Job by clicking on the Chevron (>) or by directly clicking on the Mass Change Job line. | It will navigate to Monitor Mass Changes screen.Verify if the job is successful for the selected Purchase Orders. |  |

#### Source Inspection Process (Optional)

Purpose

If you want to perform source inspection before goods receipt as an additional procurement process step, you can run through the following steps. This step is only relevant for source inspection.

With this setup, it is possible to inspect the raw material before goods receipt to decide whether the material shall be unloaded from tanker. In case of approval, the warehouse clerk posts the goods receipt to quality inspection stock creating a further inspection lot for the physical and sensory quality inspections by QM Labs and Sensory Experts. If the material is rejected, the process ends without receiving material but with sending back to the supplier.

##### Review Quality Settings in Material Master (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Material (MM03) app. | The Display Material (Initial Screen) displays. |  |
| 3 | Enter Material | Enter RM0501 in the field Material and choose Continue. | The Select View(s) pop-up is displayed. |  |
| 4 | Open Quality Management View | Select Quality Management view. Choose Org.Levels button and enter 3310 for Plant. Choose Continue button or choose Enter. | The Display MaterialRM0501(Raw Materials) screen is displayed. |  |
| 5 | Review Quality Management in Procurement Settings | The following settings are done:QM in Procur. Active: flaggedQM Control Key: 0000 |  |  |
| 6 | Review Inspection Setup | Choose button Insp. Setup and review the inspection types assigned to the material. | Inspection type 0102 Source Inspection is assigned additionally to goods receipt inspection with inspection type 01 (Goods Receipt Inspection for Purchase Order). |  |

##### Review Quality Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Quality info record has been set up to influence procurement functions. In this example the source inspection and goods receipt inspection shall be performed.

If a quality inspection is needed for a specific material supplier combination before goods receipt is posted, you can enable supplier source inspection by maintaining the source inspection type, lead time and indicator Source Insp. – No GR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Quality Info Records (F2256A) app. | The Manage Quality Info Records screen displays. |  |
| 3 | Enter Search Fields | Make the following entries and choose GoPlant: 3310Material: RM0501Supplier: 33300002Click on the quality info record. |  |  |
| 4 | Review Release Data | In the Release section, review the following data:Release Until: 31.12.9999 |  |  |
| 5 | Review Inspection Control Data | In the Inspection Control section, review the following data:Source Inspection: 0102Lead Time (In Days): 0Source Inspection Instead of GR Inspectn: No (unchecked) | Source Inspection Instead of GR Inspectn: If you do not set this indicator, the system creates one inspection lot for same purchase order item before goods receipt AND another inspection lot after goods receipt. |  |

##### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related to the raw material. The inspection plan defines all inspection characteristics used in the source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Manage Inspection Plans screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: RM0501Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview screen, select the row with Source Inspection Raw Coffee Beans and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and choose either Inspection Characteristics or Menu > Go To > Inspection Characteristic Overview (F7) . | The Display Inspection Plan: Characteristics Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There is one Master Inspection Characteristic which is Qualitative:Pest Control | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure and catalog can be reviewed in detail. |  |

##### Quality Inspection (Inspection before Goods Receipt)

###### Create Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The raw material undergoes a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the quality engineer creates inspection lots per worklist. Then, the quality technician records the inspection results for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

|  |
| --- |
| Note Usually, this inspection lot creation is done by a job. |

Prerequisite

The inspection is processed based on inspection lot. In this business process, a purchase order item for the material exists and QM in procurement is active with control key 0000 and an additional inspection type of inspection lot origin 01 (Goods Receipt). Furthermore, a quality info record is maintained with inspection type and lead time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Source Inspections - Worklist (QI07). | The Worklist of Source Inspections screen displays.You can get an overview of the purchase order items where a source inspection is planned dependent from their delivery time. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Supplier: 33300002Material: RM0501Plant: 3310Delivery Date: <delivery date> (from previous steps)Opening Period: 0Inspect w/o batch: flagged | Note A list of purchase orders for materials with source inspection is displayed. The system selects all purchase order items whose delivery date lies before the delivery date entered on the selection screen.The opening period controls the traffic light display in the selected list after executing:The light is green, if the delivery date from the purchase order item minus the lead time from the quality info record lies before the current date plus the opening period.The light is red, if the above does not apply.Note Causes the system to create a (source) inspection lot, although there is no batch defined in the purchasing document. |  |
| 4 | Create Inspection Lot | Select line and choose Inspection Lot:Purch.Doc: <purchase order> (from previous steps) |  |  |
| 5 | Save Inspection Lot | Choose Save. | Line disappears from worklist because source inspection lot is created. |  |

###### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

###### Change Inspection Lot and Assign Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the source inspection in reference to the relevant purchase order.

Prerequisite

In this business process, the inspection lot is created via source inspection worklist. A batch was prepared before with assignment to the supplier batch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: RM0501Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt | Alternatively, you can search for the Purch.Doc <Purchase Order ID> (from previous step)If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purchasing Document: <purchase order> (from previous steps). | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____________________ |  |
| 5 | Check Inspection Lot | Under Origin, verify the referenced Purchasing Document/Item. | The purchase order item from which the source inspection lot originates is displayed. |  |
| 6 | Choose Operations (Optional) | In Results, choose operation Inspection before Goods Receipt (10). | For checking the relevant inspection data, e.g. characteristic Pest Control |  |
| 7 | Change Inspection Lot | Exit and go back to Manage Inspection Lots list. Click the hyperlink of inspection lot and select Change Inspection Lot. | The Change Inspection Lot: Supplier Data screen displays. |  |
| 8 | Add Batch | Assign batch to inspection lot and choose Save.Batch: <batch ID> (from preliminary steps) | Inspection Lot XXXX was changed appears and the batch is assigned to the inspection lot. |  |

###### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The results are recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Order: <Purchase Order ID> (from previous steps). | If Purchase Order isn't displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the Inspection Lot. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results on top of the list. Choose Edit. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultPest Control: Code Group - Code QUAL01 OKNegative ResultPest Control: Code Group - Code QUAL01 NOK | For qualitative characteristics (Pest Control) the value help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step.In case of negative inspection results, a general defect is created in the background, if auto-defect recording is planned for the inspection characteristic.If needed, you can add a remark with further details.For the inspection characteristic Pest Control, a short documentation is required if it is rejected, e.g. Beetles or Grubs. |  |
| 7 | Create Defects (Optional) | Optionally, you can add a defect code from list.Select relevant Inspection Characteristics and choose Create Defect. Select Defect Level from list, e.g. for inspection characteristic.Select Defect Code Group - Code, e.g. DEFPEST 0001 Beetles.Choose Create. | The Select Defect Code Group screen displays. |  |
| 8 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM source inspection has been performed and results recorded. |  |

###### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision | You can process further as described in the chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional) | Alternative Entry to chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 8 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 9 | In Card: Top Defective Materials (Optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 10 | In Card: Top Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

###### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the goods receipt depending on the inspection result. If you don't want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

|  |
| --- |
| Note In case of positive recorded results (in previous step), immediate auto-usage decision with "Accepted-unrestricted stock (A1)" is performed in background if respective plant specific settings are prepared in customizing. In this case, you can skip this chapter. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchasing Document: <Purchase Order> (from previous steps). | If Purchase Document isn't displayed in the filters, choose Adapt Filters. On the dialog box Adapt Filters, select Purchase Document and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Select Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a negative result with defect. For a pest control rejection, a pest infestation type defect will be displayed. |  |
| 6 | Choose Edit and Add Document (Optional) | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Go to Usage Decision tab.Depending on the inspection result, select one of the following two options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210 (Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears. | Note For source inspection, you can use the same UD codes as for inspection lots which are created from goods receipt posting.Because source inspection lots are not stock relevant, the follow-up-action behind the codes are not relevant.Note If the material is batch managed, you must assign a batch to the inspection lot before saving.One way is described in this test script by preparing a batch for assignment.Another way of working with source inspection, the batch can be prepared due to close alignments with supplier. In this case, the batch can be assigned to the purchase order during purchase order creation or by changing the purchase order ideally when the tanker leaves the supplier side respective latest when the tanker arrives at customer side. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the raw material. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID from previous step and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: <Delivery Note>Printing: Individual slip |  |  |
| 5 | Enter batch (Optional) | If source inspection was performed with acceptance before:Batch: <batch ID> (from previous steps) | Batch is manually determined at goods receipt by assigning the batch which was inspected before (while additional source inspection). |  |
| 6 | Select Item | From the Items section, select the goods receipt item to be posted. | You can see that the Post button is activated. |  |
| 7 | Post | Choose Post. | The system displays the message Material Document xxx posted. |  |

#### Preview Goods Receipt Slip and Label (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, the material document is previewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Material Documents Overview (F1077). | The Material Documents Overview is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose the Go button.Plant: 3310Material Document: <Material document> from previous step | The relevant Material Document item displays. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The Material Document screen displays. |  |
| 5 | Check Goods Receipt Details | Check the General Information, Attachments, Item, Document Flow and Process Flow. | In the General Information section, you can see the Posting Date, Document Date. |  |
| 6 | Select the Material Document Item | In the Items section, select the row of material document item that you want to preview. | The Material Document Item screen displays. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose Show More per Row, and choose Display Document icon in the item of which Output Type is GOODS_RECEIPT_PO_SLIP. | The Goods Receipt Slip is opened in PDF format.Note In case Display Document is not visible on screen, switch layout to Show More per row |  |
| 8 | Back to Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods receipt fact sheet is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Material Documents Overview (F1077) . | The Material Documents Overview screen is displayed. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purchase order approval threshold for purchasing group 002 appears inconsistent: the 5W3 workflow configuration example uses total net amount greater than 10 AED, while the 5W3 manual purchase order note says an approver is assigned above 500 AED (for Purchase Groups = 002); 5W4 uses group 001 with 500 AED.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx` — lines 1–3041 of the extracted text · extracted with `mammoth` · 604,664 chars in the whole document
