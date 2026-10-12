---
id: 08-sales-order-management/script-de-datos-maestros-crear-condicion-de-bonificacion-en-especie-md
title: Script de datos maestros - Crear condición de bonificación en especie - MDS (BEW) (BEW_S4CLD2608_Master_Data_ES_XX)
description: Spanish master data script (MDS BEW) with test steps to create free-goods (bonificación en especie) pricing conditions via app VBN2 in SAP S/4HANA Cloud Public Edition.
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/free-goods]
aliases: [BEW_S4CLD2608_Master_Data_ES_XX]
keywords: [Free Goods and Free-of-Charge Delivery, free goods conditions, pricing conditions, condition key combinations, business roles, sales master data, sales orders, BEW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-546
topic: 08-sales-order-management/free-goods
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear condición de bonificación en especie - MDS (BEW) (BEW_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Free Goods and Free-of-Charge Delivery** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear condición de bonificación en especie - MDS (BEW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894903)

[2 Requisitos previos 3](#_Toc233894904)

[2.1 Acceso al sistema 3](#_Toc233894905)

[2.2 Roles 3](#_Toc233894906)

[2.3 Datos maestros obligatorios y opcionales 3](#_Toc233894907)

[3 Tabla de resumen 5](#_Toc233894908)

[4 Procedimientos de prueba 6](#_Toc233894909)

[4.1 Crear condición de bonificación en especie 6](#_Toc233894910)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Contexto empresarial

Algunos clientes pueden recibir mercancías sin cargo cuando compran una determinada cantidad. A La condición de bonificación en especie permite actualizar este acuerdo para un cliente específico y material. Se utiliza en la transacción de pedido de cliente.

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
| Cliente | Pantalla inicial | Obligatorio | <Número de cliente> |  |
| Material | Pantalla inicial | Opcional | Por ejemplo, TG11 |  |

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región, los datos de muestra del paquete de línea base proporcionan valores localizados para los admitidos países/regiones. |

## Tabla de resumen

Crear condición de bonificación en especie - MDS consta de los pasos del proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación SAP Fiori / Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear condición de bonificación en especie](#unique_7) [página ] 6 | Especialista en determinación de precios | Gestionar bonificación en especie - Ventas (VBN2) | Se ha creado el registro de condición de bonificación en especie. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear condición de bonificación en especie

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento describe la creación de condiciones de determinación de precios.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región. Sustituir los valores específicos de país/región proporcionados por SAP S/4HANA Cloud Public Edición sistema o utilice los valores de datos maestros que ha creado para este propósito. |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se muestra la rampa de lanzamiento SAP Fiori. | Se muestra la rampa de lanzamiento SAP Fiori. |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar bonificación en especie - Ventas (VBN2) . | Se abre una nueva vista, que muestra Modificar bonificación en especie determinación . |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar determinación de bonificación en especie vista, introduzca la siguiente información:Tipo de descuento : por ejemplo, YA00Pulsar Intro . | El Modificar bonificación en especie SD (YA00): Selección Se abre la vista. |  |
| 4 | Combinación de claves | Cliente/MaterialY seleccione Seleccionar . |  |  |
| 5 | Selección | En la Modificar bonificación en especie SD (YA00): Selección , introduzca lo siguiente información:Organización de ventas : <Empresa Código>Canal de distribución : por ejemplo, 10Cliente : <Cliente número>Válido el : <Fecha>Seleccionar Ejecutar . | Modificar bonificación en especie SD (YA00) se visualiza. |  |
| 6 | Modificar condición de precio | En la Modificar bonificación en especie SD (YA00) introduzca los datos abajo:Material : por ejemplo, TG11Ctd.mín. : por ejemplo, 1.000Para : por ejemplo, 500Unidad : por ejemplo, UNCtd.adic. : por ejemplo, 10Un.ctd.adic. : por ejemplo, UNTipo Cacul : por ejemplo, 1Mcía.grat. : por ejemplo, 1 | Se ha actualizado la condición de bonificación en especie. |  |
| 7 | Grabar | Seleccionar Grabar . | Se guarda la condición de bonificación en especie. |  |

Combinación de claves: organización de ventas/canal de distribución/grupo de precios/material

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se muestra la rampa de lanzamiento SAP Fiori. | Se muestra la rampa de lanzamiento SAP Fiori. |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar bonificación en especie - Ventas (VBN2) . | Se abre una nueva vista, que muestra Modificar determinación de bonificación en especie . |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar determinación de bonificación en especie introduzca la siguiente información:Tipo de descuento : por ejemplo, YA00Pulsar Intro . | El Modificar bonificación en especie SD (YA00): Selección Se abre la vista. |  |
| 4 | Combinación de claves | Org.ventas/Canal distrib./Gr.precios/MaterialY seleccione Seleccionar |  |  |
| 5 | Selección | En la Modificar bonificación en especie SD (YA00): Selección introduzca la siguiente información:Organización de ventas : <Sociedad>Canal de distribución : por ejemplo, 10Grupo de precios : <Grupo de precios>Válido el : <Fecha>Seleccionar Ejecutar . | Modificar bonificación en especie SD (YA00) se visualiza. |  |
| 6 | Modificar condición de precio | En la Modificar bonificación en especie SD (YA00) introduzca los datos siguientes:Material : por ejemplo, TG11Ctd.mín. : por ejemplo, 1.000Para : por ejemplo, 500Unidad : por ejemplo, UNCtd.adic. : por ejemplo, 10Un.ctd.adic. : por ejemplo, UNTipo Cacul : por ejemplo, 1Mcía.grat. : por ejemplo, 1 | Se ha actualizado la condición de bonificación en especie. |  |
| 7 | Grabar | Seleccionar Grabar . | Se guarda la condición de bonificación en especie. |  |

Combinación de claves: organización de ventas/canal de distribución/material

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se muestra la rampa de lanzamiento SAP Fiori. | Se muestra la rampa de lanzamiento SAP Fiori. |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar bonificación en especie - Ventas (VBN2) . | Se abre una nueva vista, que muestra Modificar determinación de bonificación en especie . |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar determinación de bonificación en especie introduzca la siguiente información:Tipo de descuento : por ejemplo, YA00Pulsar Intro . | El Modificar bonificación en especie SD (YA00): Selección Se abre la vista. |  |
| 4 | Combinación de claves | Org.ventas/Canal distrib./MaterialY seleccione Seleccionar . |  |  |
| 5 | Selección | En la Modificar bonificación en especie SD (YA00): Selección introduzca la siguiente información:Organización de ventas : <Sociedad>Canal de distribución : por ejemplo, 10Válido el : <Fecha>Seleccionar Ejecutar . | Modificar bonificación en especie SD (YA00) se visualiza. |  |
| 6 | Modificar condición de precio | En la Modificar bonificación en especie SD (YA00) introduzca los datos siguientes:Material : por ejemplo, TG11Ctd.mín. : por ejemplo, 1.000Para : por ejemplo, 500Unidad : por ejemplo, UNCtd.adic. : por ejemplo, 10Un.ctd.adic. : por ejemplo, UNTipo Cacul : por ejemplo, 1Mcía.grat. : por ejemplo, 1 | Se ha actualizado la condición de bonificación en especie. |  |
| 7 | Grabar | Seleccionar Grabar . | Se guarda la condición de bonificación en especie. |  |

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
- related-to :: [[08-sales-order-management/criar-condicao-de-bonificacao-em-mercadoria-mds-bew-548]]
- related-to :: [[08-sales-order-management/master-data-script-create-free-goods-condition-mds-bew-545]]
- related-to :: [[08-sales-order-management/mds-bew-547]]
- related-to :: [[08-sales-order-management/mds-bew-549]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 13,865 chars in the whole document
