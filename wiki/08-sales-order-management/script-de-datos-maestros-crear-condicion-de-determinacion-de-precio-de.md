---
id: 08-sales-order-management/script-de-datos-maestros-crear-condicion-de-determinacion-de-precio-de
title: "Script de datos maestros: Crear condición de determinación de precio de venta - MDS (BET) (BET_S4CLD2608_Master_Data_ES_XX)"
description: Spanish master data script (BET) for creating sales price conditions (e.g. PPR0) in SAP S/4HANA Cloud Public Edition using app VK12.
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-pricing-conditions]
aliases: [BET_S4CLD2608_Master_Data_ES_XX]
keywords: [Sales Price Conditions and Statistical Conditions, sales price condition, pricing, master data script, user roles, mandatory master data, test procedure, BET]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-540
topic: 08-sales-order-management/sales-pricing-conditions
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear condición de determinación de precio de venta - MDS (BET) (BET_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Sales Price Conditions and Statistical Conditions** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear condición de determinación de precio de venta - MDS (BET) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894851)

[2 Requisitos previos 3](#_Toc233894852)

[2.1 Acceso al sistema 3](#_Toc233894853)

[2.2 Roles 3](#_Toc233894854)

[2.3 Datos maestros obligatorios y opcionales 3](#_Toc233894855)

[3 Tabla de resumen 5](#_Toc233894856)

[4 Procedimientos de prueba 6](#_Toc233894857)

[4.1 Crear condición de precio 6](#_Toc233894858)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Las condiciones de precio de venta se utilizan para almacenar la información necesaria para realizar determinación automática de precios en un pedido de cliente. Incluyen precios, descuentos, recargos y impuestos. Pueden ser específicos de un cliente o material en particular o de una combinación de parámetros.

Una condición de precio de venta contiene información como un precio en una moneda específica para un material o un descuento específico de cliente como porcentaje. Esta información se utiliza y almacenado en el pedido de cliente y en los documentos de facturación, como las facturas.

Por lo general, la información es específica de una unidad de ventas en particular dentro de su organización.

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
| Especialista en determinación de precios | SAP_BR_PRICING_SPECIALIST | Gestión de precios | SAP_BR_PRICING_SPECIALIST |  |

### Datos maestros obligatorios y opcionales

La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar al crear condiciones de determinación de precios.

Si ha instalado un paquete de línea base de SAP Best Practices, puede utilizar el paquete de línea base datos de muestra o añada sus propios datos maestros, según sea necesario:

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Valores de muestra | Comentarios |
| --- | --- | --- | --- | --- |
| Organización de ventas | Pantalla inicial | Obligatorio | <Número de organización de ventas> |  |
| Canal de distribución | Pantalla inicial | Obligatorio | <Número de canal de distribución> |  |
| Material | Pantalla inicial | Obligatorio | Por ejemplo, TG11 |  |

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región, los datos de muestra del paquete de línea base proporcionan valores localizados para los admitidos países/regiones. |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear condición de precio](#unique_7) [página ] 6 | Especialista en determinación de precios | Fijar precios de material - Ventas (VK12) | Se crean condiciones de precio de venta. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear condición de precio

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este procedimiento describe la creación de condiciones de determinación de precios de venta.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región. Sustituir los valores específicos de país/región proporcionados por SAP S/4HANA Cloud Public Edición sistema o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar precios de material - Ventas (VK12) . | El Crear mandato: Acceso muestra. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición introduzca la siguiente información:Clase de condición : por ejemplo, PPR0Pulsar Intro . | El Combinación de claves se visualiza. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material con status de liberación y haga clic en Seleccionar . | El Modificar precio (PPR0): Selección se visualiza. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección introduzca la siguiente información:Organización de ventas : <Organización de ventas>Canal de distribución : <Canal de distribución>Material : por ejemplo, TG11Válido el : por ejemplo, <Fecha>Seleccionar Ejecutar . | El Modificar condición de precio (PPR0): Resumen se visualiza. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen introduzca los siguientes datos:Material : por ejemplo, TG11Cantidad : por ejemplo, $17.55$Inicio de validez : por ejemplo, <Fecha actual>Válido hasta : por ejemplo, <Fecha actual + un año> | La condición de precio de material está actualizada. |  |
| 7 | Grabar | Seleccionar Grabar . | La condición de precio se ha guardado. |  |

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
- related-to :: [[08-sales-order-management/create-sales-pricing-condition-mds-bet-539]]
- related-to :: [[08-sales-order-management/mds-bet-541]]
- related-to :: [[08-sales-order-management/mds-bet-543]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 10,351 chars in the whole document
