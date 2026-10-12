---
id: 11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330
title: "Actualizar atributos de productos de almacén - MDS (3KQ) [ES] (3KQ_S4CLD2608_Master_Data_ES_XX)"
description: Spanish machine-translated SAP S/4HANA Cloud master data script 3KQ for updating warehouse product attributes via Warehouse Monitor or Manage Product Master Data (F1602).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_ES_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse monitor, product master data, mass changes, replenishment, storage types, business roles, business partner, warehouse management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-330
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Actualizar atributos de productos de almacén - MDS (3KQ) [ES] (3KQ_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Actualizar atributos de productos de almacén - MDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894616)

[2 Requisitos previos 3](#_Toc233894617)

[2.1 Acceso al sistema 3](#_Toc233894618)

[2.2 Roles 3](#_Toc233894619)

[2.3 Unidades organizativas necesarias 3](#_Toc233894620)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894621)

[3 Tabla de resumen 5](#_Toc233894622)

[4 Procedimientos de prueba 6](#_Toc233894623)

[4.1 Actualizar atributos de producto de almacén con monitor de almacén 6](#_Toc233894624)

[4.2 Actualizar atributos de producto de almacén 7](#_Toc233894625)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, puede aprender a crear atributos relevantes para el almacén para su maestro de materiales/productos. Existen dos opciones para actualizar los atributos de almacén:

- Puede actualizar los atributos de producto de almacén con la Monitor de almacén (/SCWM/MON) aplicación. Esta aplicación se puede utilizar para modificaciones individuales y en masa.
- Puede actualizar los atributos de producto de almacén con la Gestionar datos maestros de producto (F1602) aplicación. Esta aplicación se puede utilizar para modificaciones individuales.

Este documento incluye los segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema normal. El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance de la entrega de contenido de SAP S/4HANA por parte de SAP Best Practices no se describen en este documento aunque puedan aparecer en la IU.

Utilice estos datos maestros para todos los procesos empresariales de Gestión de almacenes.

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Jefe de almacén (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Oficina de almacén | SAP_BR_WAREHOUSE_CLERK_EWM |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todo | Número de almacén |  |  |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros <tipo>.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Interlocutor comercial | Actualizar atributos de producto de almacén | Obligatorio | Interlocutor comercial como persona autorizada a disponer para el almacén |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Actualizar atributos de producto de almacén con monitor de almacén](#unique_7) [página ] 6 | Jefe de almacén (EWM) | Monitor de almacén (/SCWM/MON) | Se realiza una modificación en masa de productos de almacén. |
| [Actualizar atributos de producto de almacén](#unique_8) [página ] 7 | Especialista en datos maestros - Datos de producto | Gestionar datos maestros de producto (F1602) | Se crean atributos de almacén para los datos maestros de material. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Actualizar atributos de producto de almacén con monitor de almacén

Objetivo

En esta sección se actualizan los atributos de producto de almacén mediante la Monitor de almacén (/SCWM/MON) aplicación. Esta aplicación se puede utilizar para modificaciones individuales y en masa.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Monitor de almacén (/SCWM/MON) . | El Monitor de gestión de almacén SAP - Número de almacén XX50 se visualiza. |  |
| 3 | Seleccionar menú | En la jerarquía del área izquierda de la pantalla, seleccione Datos maestros de producto > Atributo de almacén . |  |  |
| 4 | Introducir número de producto | En la /SCWM/SAPLPROD_OVERVIEW indique los siguientes datos:Atributos básicos sección:Número de producto : <Número de producto> hasta <Número de producto>Opciones adicionales sección:Sólo prod.sin datos almacén : XSeleccionar Ejecutar . | El sistema muestra los productos que aún no se han actualizado con datos de almacén en el área derecha de la pantalla. |  |
| 5 | Seleccionar productos | En la Atributos de almacén , seleccione los productos y, a continuación, seleccione Más métodos > Modificación/creación en masa . |  |  |
| 6 | Seleccionar productos | En la /SCWM/SAPLPROD_OVERVIEW introduzca los siguientes datos cuando corresponda.En la Datos de almacén sección:Indicador de control de entrada en stockIndicador de control de salida de stockInd.almacén bloquesIndicador de inventario cíclicoInd.determ.cl.proc.Seleccionar Ejecutar .Nota En Cloud Warehouse Management, el indicador de control de entrada en stock y el indicador de control de salida de stock normalmente se actualizan con el mismo valor. Sin embargo, en el proceso de reaprovisionamiento utilizado en el almacén, estos dos campos deben actualizarse de forma diferente para permitir el proceso. |  |  |
| 7 | Guardar los datos | En la ventana de diálogo, confirme las modificaciones. | Un mensaje del sistema le indica que los productos se han guardado correctamente. |  |

### Actualizar atributos de producto de almacén

Objetivo

En esta sección encontrará una descripción de cómo actualizar los atributos de producto de almacén. con el Gestionar datos maestros de producto (F1602) aplicación. Esta aplicación se puede utilizar para cambios individuales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . |  |  |
| 2 | Acceder a la aplicación | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Introducir número de material | El Gestionar datos maestros de producto (F1602) introduzca los siguientes datos:Producto : <Número de material>Seleccionar Ir . | Los datos maestros de material se visualizan en el Producto sección. |  |
| 4 | Seleccionar material | Seleccione la fila de los datos maestros de material. |  |  |
| 5 | Seleccionar gestión de almacenes | El Producto , seleccione Almacén Gestión y vaya a Gestión de almacenes > Almacén . |  |  |
| 6 | Editar datos maestros de material | El Producto , seleccione Editar . |  |  |
| 7 | Añadir datos de almacén | En la Almacén de almacén, seleccione el almacén para su almacén.Si su número de almacén no existe, seleccione Crear . |  |  |
| 8 | Introducir valores | El Almacén introduzca lo siguiente datos:En la Información general sección:Almacén : <Almacén EWM Número>Persona autorizada a disponer : <Negocio ID de interlocutor para la parte autorizada a disponer>Indicador de determinación de tipo de procesoIndicador de inventario cíclicoNota Solo Almacén y Persona autorizada a Eliminar son obligatorios para la entrada. Los siguientes valores son opcionales.En la Entrada en stock sección:Indicador de control de entrada en stockEn la Salida de stock sección:Indicador de control de salida de almacénNota En la gestión de almacenes en la nube, el indicador de control de entrada en stock y el indicador de control de salida de stock se actualiza con el mismo valor. Sin embargo, en el proceso de reaprovisionamiento utilizado en el almacén, estos dos Los campos deben actualizarse de forma diferente para permitir el proceso. |  |  |
|  | Crear datos de tipo de almacén para reaprovisionamiento | En la Tipos de almacenamiento sección, seleccione Crear .El Nuevo registro – Tipo de almacenamiento , introduzca el Datos siguientes:En la Información general sección:Tipo de almacén : <Almacenamiento Tipo>Cantidad máxima de ubicaciones : <Número de Ubicaciones>En la Reaprovisionamiento sección:Cantidad mínima de reaprovisionamiento/UM de visualización : <Cantidad> / <UM>Cantidad mínima/UM de visualización : <Cantidad> / <UM>Cantidad máxima / UM de visualización : <Cantidad> / <UM> |  |  |
| 9 | Guardar los datos | Seleccionar Aplicar . | Se graban los datos de almacén. |  |
| 10 | Volver a la pantalla Producto | Regrese a la Producto pantalla. |  |  |
| 11 | Seleccionar gestión de almacenes | El Producto , seleccione el botón de selección Centros pestaña. |  |  |
| 12 | Añadir datos de centro | En la Centros seleccione el centro.Si su centro no existe, seleccione Crear . |  |  |
| 13 | Introducir valores | El Centro introduzca los siguientes datos en la sección Información general:Perfil de número de serie: <Perfil de número de serie> |  |  |
| 14 | Guardar los datos | Seleccionar Aplicar . | Se graban los datos del centro. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-331]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-333]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 14,379 chars in the whole document
