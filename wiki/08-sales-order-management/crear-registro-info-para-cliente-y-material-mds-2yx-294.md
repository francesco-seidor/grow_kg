---
id: 08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294
title: Crear registro info para cliente y material - MDS (2YX) (2YX_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script 2YX: create customer-material info record via Gestionar materiales de cliente (F2499) in S/4HANA Cloud 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_ES_XX]
keywords: [Customer-Material Info Records, customer-material info record, sales unit conversion, sales master data, business roles, test procedures, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-294
topic: 08-sales-order-management/customer-material-info-records
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear registro info para cliente y material - MDS (2YX) (2YX_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear registro info para cliente y material - MDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894576)

[2 Requisitos previos 3](#_Toc233894577)

[2.1 Acceso al sistema 3](#_Toc233894578)

[2.2 Roles 3](#_Toc233894579)

[2.3 Datos maestros obligatorios y opcionales 3](#_Toc233894580)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894581)

[3 Tabla de resumen 5](#_Toc233894582)

[4 Procedimientos de prueba 6](#_Toc233894583)

[4.1 Crear información cliente-material 6](#_Toc233894584)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear información cliente-material para su SAP S/4HANA Cloud Public Edición sistema. El La descripción incluye los segmentos de datos que son relevantes para el SAP S/4HANA Cloud Public Edición aplicación. Campos que no son relevantes para el alcance del SAP S/4HANA Cloud Public Edición contenido no se describen en este documento.

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

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Empleado del departamento de ventas del servicio interno | SAP_BR_INTERNAL_SALES_REP | Ventas internas / Devoluciones de cliente / Facturación | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Datos maestros obligatorios y opcionales

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Cliente | Pantalla inicial | Obligatorio |  |
| Organización de ventas | Pantalla inicial | Obligatorio |  |
| Canal de distribución | Pantalla inicial | Obligatorio |  |
| Material | Pantalla inicial | Opcional |  |

### Datos maestros obligatorios y opcionales

En esta sección encontrará algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear una determinación de precios. condición:

Organización de ventas : <Organización de ventas>

Canal de distribución : <Canal de distribución>

Cliente : <Cliente>

Material : <Número de material>

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación SAP Fiori / Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear información cliente-material](#unique_8) [página ] 6 | Empleado del departamento de ventas del servicio interno | Gestionar materiales de cliente (F2499) | Se ha creado el registro info para material y cliente. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear información cliente-material

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Empleado del departamento de ventas del servicio interno . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar materiales de cliente (F2499) . | Se abre la aplicación. |  |
| 3 | Acceder a la creación de materiales de cliente | Seleccionar Crear . | El Material de cliente se visualiza. |  |
| 4 | Introducir información básica de cliente-material | Realice las siguientes entradas:Cliente : <Cliente>Producto : <Número de material>Organización de ventas : <Organización de ventas>Canal de distribución : <Canal de distribución>Descripción de material de cliente : proporcione una descripción para el cliente y el material. | Se actualiza la información básica de cliente y material. |  |
| 5 | Introducir unidad de ventas | En la Conversión de unidades , realice la siguiente entrada:1 PAL (unidad de cliente) : 2 UN (básico) Unidad) | Se actualiza la unidad de ventas para la combinación de cliente-material.NotaPara actualizar la unidad de ventas y la conversión en esta pantalla, los datos maestros de material de la unidad de medida y se debe actualizar la conversión. Puede hacer referencia a otros scripts de datos maestros, por ejemplo, Creación de maestro de productos de tipo "Mercadería" - MDS - BNF para mercaderías.Una vez actualizada la unidad de ventas en esta pantalla, se visualiza en el documento de ventas. |  |
| 6 | Seleccione Crear. | Seleccionar Crear . | El material de cliente se ha creado correctamente. |  |

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
- related-to :: [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293]]
- related-to :: [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296]]
- related-to :: [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292]]
- related-to :: [[08-sales-order-management/mds-2yx-295]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 9,690 chars in the whole document
