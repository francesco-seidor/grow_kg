---
id: 09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b
title: Script de datos maestros - Crear condición de determinación de precios basada en clase de servicio – MDS (3GD) (3GD_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script (3GD) for SAP S/4HANA Cloud: creating service-class-based pricing conditions PST0, PST1, PST2 via VK12."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_ES_XX]
keywords: [Consumption Items and Service-Type-Based Rating, pricing conditions, service class pricing, master data scripts, condition records, convergent billing, business roles, sales organization, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-318
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear condición de determinación de precios basada en clase de servicio – MDS (3GD) (3GD_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear condición de determinación de precios basada en clase de servicio - MDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894609)

[2 Requisitos previos 3](#_Toc233894610)

[2.1 Acceso al sistema 3](#_Toc233894611)

[2.2 Roles 3](#_Toc233894612)

[2.3 Datos maestros obligatorios y opcionales 3](#_Toc233894613)

[3 Tabla de resumen 4](#_Toc233894614)

[4 Procedimientos de prueba 5](#_Toc233894615)

[4.1 Crear condición de precio de PST0 5](#_Toc233894616)

[4.2 Crear condición de precio de PST1 6](#_Toc233894617)

[4.3 Crear condición de precio de PST2 7](#_Toc233894618)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Las condiciones de determinación de precios basadas en servicios se utilizan para almacenar la información necesaria para llevar a cabo la determinación de precios automática en la valoración de Convergent Facturación. Incluyen precios y recargos basados en las diferentes variantes. Pueden ser específicos de un cliente en particular o material o una combinación de parámetros. Una condición de determinación de precios basada en servicios contiene información como un precio en una moneda específica para un material. Esta información se utiliza y almacena en las posiciones facturables, las posiciones del plan de facturación, los documentos de facturación y la facturación documentos.

Por lo general, la información es específica de una unidad de ventas concreta dentro de su organización.

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

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Especialista en determinación de precios | SAP_BR_PRICING_SPECIALIST | Gestión de precios | SAP_BR_PRICING_SPECIALIST |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un maestro registro de datos.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Organización de ventas | Pantalla inicial | Obligatorio | <Número de organización de ventas> |
| Canal de distribución | Pantalla inicial | Obligatorio | <Número de canal de distribución> |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear condición de precio de PST0](#unique_7) [página ] 5 | Especialista en determinación de precios | Fijar precios de material - Ventas (VK12) | La condición de precio de material está actualizada. |
| [Crear condición de precio de PST1](#unique_8) [página ] 6 | Especialista en determinación de precios | Fijar precios de material - Ventas (VK12) | La condición de precio de material está actualizada. |
| [Crear condición de precio de PST2](#unique_9) [página ] 7 | Especialista en determinación de precios | Fijar precios de material - Ventas (VK12) | La condición de precio de material está actualizada. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear condición de precio de PST0

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este procedimiento describe la creación de una condición de precio de venta: PST0

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar precios de material - Ventas (VK12) . | El Modificar registros de condición se visualiza. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , realice las siguientes entradas como se indica a continuación y seleccione Intro .Clase de condición : PST0 |  |  |
| 4 | Selección | En la Modificar condición de precio basado en clase de servicio (PST0): Selección , realice las siguientes entradas como se indica a continuación y seleccione Ejecutar .Organización de ventas : <Organización de ventas>Canal de distribución : <Canal de distribución> |  |  |
| 5 | Modificar condición de precio | En la Modificar condición de precio basado en clase de servicio (PST0): Resumen , realice las siguientes entradas como se indica a continuación y seleccione Grabar .Material : CBPTS002Cantidad : <importe>UM : <UN>Inicio de validez : <la fecha actual>Válido hasta : por ejemplo, <la fecha actual + un año> | La condición de precio de material está actualizada. |  |

### Crear condición de precio de PST1

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este procedimiento describe la creación de una condición de precio de venta: PST1

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar precios de material - Ventas (VK12) . | El Modificar registros de condición se visualiza. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , realice las siguientes entradas y seleccione Intro .Clase de condición : PST1 |  |  |
| 4 | Selección | En la Modif.var.bas.tp.serv.(PST1): Selección , realice las siguientes entradas como se indica a continuación y seleccione Ejecutar .Organización de ventas : Organización de ventasCanal de distribución : Canal de distribución |  |  |
| 5 | Modificar condición de precio | En la Modif.var.bas.cl.serv.(PST1): Resumen , realice las siguientes entradas como se indica a continuación y seleccione Grabar .Material : CBPTS001Variante : HIGH_ENDCantidad : <importe>UM : UNInicio de validez : <la fecha actual>Válido hasta : por ejemplo, <la fecha actual + un año> | La condición de precio de material está actualizada. |  |

### Crear condición de precio de PST2

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este procedimiento describe la creación de una condición de precio de venta: PST2

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar precios de material - Ventas (VK12) . | El Modificar registros de condición se visualiza. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , realice las siguientes entradas y seleccione Intro .Clase de condición : PST2 |  |  |
| 4 | Selección | En la Cl.serv.-% var.basad.(PST2): Selección , realice las siguientes entradas como se indica a continuación y seleccione Ejecutar .Organización de ventas : Organización de ventasCanal de distribución : Canal de distribución |  |  |
| 5 | Modificar condición de precio | En la Modificar % var.bas.cl.serv.(PST2): Resumen , realice las siguientes entradas como se indica a continuación y seleccione Grabar .Material : CBPTS001Variante : HIGH_ENDCantidad : <importe>Inicio de validez : <la fecha actual>Válido hasta : por ejemplo, <la fecha actual + un año> | La condición de precio de material está actualizada. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 13,539 chars in the whole document
