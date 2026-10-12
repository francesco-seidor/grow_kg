---
id: 11-inventory-warehouse-and-transportation/crear-datos-maestros-de-almacen-para-recurso-mds-3y2-396
title: Crear datos maestros de almacén para recurso - MDS (3Y2) (3Y2_S4CLD2608_Master_Data_ES_XX)
description: Spanish (machine-translated) SAP master data script for creating and deleting warehouse resources via Warehouse Monitor (/SCWM/MON) in S/4HANA Cloud Public Edition 2608.
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-resources]
aliases: [3Y2_S4CLD2608_Master_Data_ES_XX]
keywords: [EWM Warehouse Resources, warehouse resource, warehouse resource deletion, warehouse monitor, master data creation, business roles, warehouse management, test procedures, 3Y2]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-396
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-resources
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear datos maestros de almacén para recurso - MDS (3Y2) (3Y2_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Resources** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear datos maestros de almacén para recurso – MDS (3Y2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894673)

[2 Requisitos previos 3](#_Toc233894674)

[2.1 Acceso al sistema 3](#_Toc233894675)

[2.2 Roles 3](#_Toc233894676)

[2.3 Unidades organizativas necesarias 3](#_Toc233894677)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894678)

[3 Tabla de resumen 5](#_Toc233894679)

[4 Procedimientos de prueba 6](#_Toc233894680)

[4.1 Crear recurso de almacén 6](#_Toc233894681)

[4.2 Borrar recurso de almacén 7](#_Toc233894682)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, aprenderá a crear datos maestros para recursos de almacén. Puede actualizar los recursos de almacén con el almacén Supervisar (/SCWM/MON). Este documento incluye los segmentos de datos que son relevantes para que los datos maestros funcionen en un sistema regular entorno. Principalmente aprenderá qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance de la entrega de contenido de SAP S/4HANA por parte de SAP Best Practices no se describe en este documento, aunque pueden aparecer en la pantalla. Utilice estos datos maestros para todos los procesos empresariales de Gestión de almacenes.

Este documento proporciona un procedimiento detallado para probar este elemento de alcance después de la activación de la solución, reflejando el alcance predefinido de la solución. Cada paso, informe o posición de proceso se trata en su propia sección, proporcionando las interacciones del sistema (pasos de test) en una vista de tabla. Los pasos que no están dentro del alcance del proceso pero que son necesarios para las pruebas se marcan en consecuencia. Deben añadirse pasos específicos del proyecto.

|  |
| --- |
| Nota Los valores en este script de test (notación decimal, formatos de fecha, etc.) se presentan en la notación estándar de EE. UU. Si su sistema de prueba está configurado para utilizar una notación diferente, introduzca valores según corresponda. |

## Requisitos previos

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
| Jefe de almacén (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Oficina de almacén | SAP_BR_WAREHOUSE_CLERK_EWM |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todo | Número de almacén |  |  |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros <tipo>.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
|  |  |  |  |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear Recurso de almacén | Jefe de almacén (EWM) | Monitor de almacén (/SCWM/MON) | Se lleva a cabo la creación del recurso en el almacén. |
| Borrar Recurso de almacén | Jefe de almacén (EWM) | Monitor de almacén (/SCWM/MON) | Se lleva a cabo el borrado del recurso en el almacén. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear recurso de almacén

Objetivo

En esta sección se crea el recurso de almacén mediante la Monitor de almacén (/SCWM/MON) aplicación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM). |  |  |
| 2 | Acceder a la aplicación | Abierto Monitor de almacén (/SCWM/MON) . | El Monitor de gestión de almacén se visualiza la ventana de diálogo. |  |
| 3 | Introducir número de almacén | Si el Monitor de gestión de almacén se abre, indique los siguientes datos:Número de almacén : <Su número de almacén>Seleccionar Ejecute. |  |  |
| 4 | Seleccionar menú | En la jerarquía del área izquierda de la pantalla, seleccione Gestión de recursos > Recurso . |  |  |
| 5 | Visualizar recurso | En la ventana de diálogo de apertura, seleccione Ejecutar . | El sistema muestra todos los recursos que se han creado para el almacén. |  |
| 6 | Crear recurso | Seleccionar Más métodos > Crear recurso . |  |  |
| 7 | Introducir valores | En la ventana de diálogo de apertura, indique los siguientes datos:Recurso : <ID de recurso>Nota El ID de recurso está limitado a 18 caracteres.Seleccionar Ejecute. | Se ha creado un recurso correctamente. |  |

### Borrar recurso de almacén

Objetivo

En esta sección se borra el recurso de almacén mediante la Monitor de almacén (/SCWM/MON) aplicación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM). |  |  |
| 2 | Acceder a la aplicación | Abierto Monitor de almacén (/SCWM/MON) . | El Monitor de gestión de almacén se visualiza la ventana de diálogo. |  |
| 3 | Introducir número de almacén | En la apertura Monitor de gestión de almacén indique los siguientes datos:Número de almacén : <Su número de almacén>Seleccionar Ejecute. |  |  |
| 4 | Seleccionar menú | En la jerarquía del área izquierda de la pantalla, seleccione Gestión de recursos > Recurso . |  |  |
| 5 | Visualizar recurso | En la ventana de diálogo, seleccione Ejecutar . | El sistema muestra todos los recursos que se han creado para el almacén. |  |
| 6 | Borrar recurso | Seleccione el recurso que se va a borrar y, a continuación, seleccione Más métodos > Borrar recurso . |  |  |
| 7 | Confirmar borrado | En la Borrar recurso ventana de diálogo, seleccione Sí .Nota No puede borrar un recurso en particular que aún se utiliza en el almacén. Esto significa que cuando un usuario ha iniciado sesión en el recurso o si un usuario ha fijado el recurso como recurso por defecto. | Se ha eliminado un recurso correctamente. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-warehouse-master-data-for-resource-mds-3y2-3]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-397]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-399]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-deposito-para-recurso-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 11,290 chars in the whole document
