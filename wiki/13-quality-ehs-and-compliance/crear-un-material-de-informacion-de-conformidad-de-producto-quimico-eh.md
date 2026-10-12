---
id: 13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh
title: Crear un material de información de conformidad de producto químico EHS - MDS (65Z) (65Z_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 65Z: create an EHS chemical compliance information material in app F4864 for waste management."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_ES_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, chemical compliance material, material master data, master data scripts, ehs waste management, business roles, test procedures, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-504
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear un material de información de conformidad de producto químico EHS - MDS (65Z) (65Z_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear un material de información de conformidad de producto químico EHS - MDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894804)

[2 Requisitos previos 3](#_Toc233894805)

[2.1 Acceso al sistema 3](#_Toc233894806)

[2.2 Roles 3](#_Toc233894807)

[3 Tabla de resumen 4](#_Toc233894808)

[4 Procedimientos 5](#_Toc233894809)

[4.1 Crear datos maestros de material de información de conformidad de producto químico EHS - Datos generales 5](#_Toc233894810)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un registro de datos maestros de material de información de conformidad química de EHS para su sistema S/4 HANA. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance de la entrega de contenido de S/4 HANA por parte de SAP Best Practices no se describen en este documento, aunque pueden aparecer en la IU.

Un registro maestro de materiales de información de conformidad química de EHS que se crea como se describe aquí se puede utilizar para emplearse posteriormente en procesos de gestión de residuos.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) |
| --- | --- |
| Responsable medioambiental | SAP_BR_EHS_ENV_MGMT |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de material de información de conformidad de producto químico EHS - Datos generales](#unique_6) [página ] 5 | Responsable medioambiental | Gestionar datos de material ( F4864 ) | Se crea un material de información de conformidad química (CCI) EHS. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear datos maestros de material de información de conformidad de producto químico EHS - Datos generales

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un material de información de conformidad de producto químico EHS que se puede utilizar posteriormente para procesos de gestión de residuos EHS.

Procedimiento (mediante Fiori Launchpad)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Fiori Launchpad con sus credenciales de usuario. | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar datos maestros de cliente | Abra la Gestionar datos de material aplicación ( F4864 ). | El Gestionar datos de material Se abre la aplicación y se visualiza un informe de lista. |  |
| 3 | Crear un nuevo material | Seleccionar Crear .En la pantalla:Introducir en un <Nombre> en el Nombre interno campo.Seleccione un <Rol de logística> de la Rol logístico lista desplegable.Seleccionar Grabar . | El Material nuevo y se crea un nuevo material. |  |
| 4 | Añadir un producto | Seleccionar Editar .En la Producto sección, seleccione Añadir y seleccione un producto.Seleccionar Grabar .Nota: Solo se puede asignar un producto a un material. | Se añade un producto al material y se graba la información. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 7,645 chars in the whole document
