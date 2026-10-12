---
id: 13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510
title: Crear un producto EHS - MDS (660) (660_S4CLD2608_Master_Data_ES_XX)
description: Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating an EHS product in Manage Product Master Data (F1602) for waste management.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [660_S4CLD2608_Master_Data_ES_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, ehs products, product master data, waste management, business roles, master data scripts, 660]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-510
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear un producto EHS - MDS (660) (660_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear un producto EHS - MDS (660) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894866)

[2 Requisitos previos 3](#_Toc233894867)

[2.1 Acceso al sistema 3](#_Toc233894868)

[2.2 Roles 3](#_Toc233894869)

[3 Tabla de resumen 4](#_Toc233894870)

[4 Procedimientos 5](#_Toc233894871)

[4.1 Crear datos maestros de producto EHS - Datos generales 5](#_Toc233894872)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un registro de datos maestros de producto EHS para su sistema S/4 HANA. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance de la entrega de contenido de S/4 HANA por parte de SAP Best Practices no se describen en este documento, aunque pueden aparecer en la IU.

Un registro maestro de productos EHS que se crea como se describe aquí se puede utilizar para emplearse posteriormente en procesos de gestión de residuos.

Este documento proporciona un procedimiento detallado para probar este elemento de alcance después de la activación de la solución, reflejando el alcance predefinido de la solución. Cada paso, informe o posición de proceso se trata en su propia sección, proporcionando las interacciones del sistema (pasos de test) en una vista de tabla. Los pasos que no están dentro del alcance del proceso pero que son necesarios para las pruebas se marcan en consecuencia. Deben añadirse pasos específicos del proyecto.

|  |
| --- |
| Nota Los valores en este script de test (notación decimal, formatos de fecha, etc.) se presentan en la notación estándar de EE. UU. Si su sistema de prueba está configurado para utilizar una notación diferente, introduzca valores según corresponda. |

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

| Nombre | ID |
| --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de producto EHS - Datos generales](#unique_6) [página ] 5 | Especialista en datos maestros - Datos de producto | Gestionar datos maestros de producto ( F1602 ) | Se crea un producto EHS. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear datos maestros de producto EHS - Datos generales

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un producto EHS que se puede utilizar posteriormente para procesos de gestión de residuos EHS.

Procedimiento (mediante Fiori Launchpad)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Fiori Launchpad con sus credenciales de usuario. | El Iniciar Aparece la página. |  |
| 2 | Navegar a los datos maestros de producto | Abra la Aplicación Gestionar datos maestros de producto ( F1602 ) | El Gestionar datos maestros de producto Se abre la aplicación y se visualiza un informe de lista. |  |
| 3 | Crear un producto | En la Crear cuadro de diálogo, seleccione Producto . | El Crear registro de datos maestros de un producto. |  |
| 4 | Seleccionar registros de datos maestros de un producto | En la misma pantalla:Introduzca un <Número de producto> en el Campo Número de producto .Seleccione un <Tipo de producto> en el Producto Tipo campo.Seleccione un <Grupo de productos> en el Producto Grupo campo.Introduzca un <Descripción> en el Descripción campo.Seleccione un <Unidad base> mediante la ayuda para entradas para Unidad base campo.Seleccionar OK . | El producto contiene información del registro de datos maestros. |  |
| 5 | Guardar información | Seleccionar Grabar . | El Producto se ha creado. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-511]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-chinese-513]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 8,288 chars in the whole document
