---
id: 11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic
title: Script de datos maestros - Actualizar ubicaciones y asignaciones de ubicación fija (3KR) (3KR_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP master data script 3KR: create, change, display, mass-change warehouse storage bins and assign fixed bins in EWM via Fiori, release 2608."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_ES_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, bin mass change, master data scripts, warehouse management, business roles, business partner, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-336
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Actualizar ubicaciones y asignaciones de ubicación fija (3KR) (3KR_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Actualizar ubicaciones y asignaciones de ubicación fija - MDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894628)

[2 Requisitos previos 3](#_Toc233894629)

[2.1 Acceso al sistema 3](#_Toc233894630)

[2.2 Roles 3](#_Toc233894631)

[2.3 Unidades organizativas necesarias 3](#_Toc233894632)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894633)

[3 Tabla de resumen 5](#_Toc233894634)

[4 Procedimientos de prueba 6](#_Toc233894635)

[4.1 Crear ubicaciones 6](#_Toc233894636)

[4.2 Modificar ubicaciones 7](#_Toc233894637)

[4.3 Visualizar ubicaciones 8](#_Toc233894638)

[4.4 Efectuar modificación en masa de ubicaciones 9](#_Toc233894639)

[4.5 Asignar ubicaciones fijas 10](#_Toc233894640)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, puede aprender a realizar las siguientes actividades para crear un almacén. Ubicaciones y asignaciones de ubicación fija:

- [Crear ubicaciones](#unique_2) [página ] 6
- [Modificar ubicaciones](#unique_3) [página ] 7
- [Visualizar ubicaciones](#unique_4) [página ] 8
- [Efectuar modificación en masa de ubicaciones](#unique_5) [página ] 9
- [Asignar ubicaciones fijas](#unique_6) [página ] 10

La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema normal. Principalmente aprende qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance de SAP S/4HANA La entrega de contenido de SAP Best Practices no se describe en este documento, aunque pueden aparecer en la pantalla.

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

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todo | Número de almacén |  |  |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros <tipo>.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Interlocutor comercial | Asignar ubicaciones fijas | Obligatorio | Interlocutor comercial como persona autorizada a disponer para el almacén |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear ubicaciones](#unique_2) [página ] 6 | Jefe de almacén (EWM) | Crear ubicaciones (/SCWM/LS01) | Se crean las ubicaciones en almacén. |
| [Modificar ubicaciones](#unique_3) [página ] 7 | Jefe de almacén (EWM) | Editar ubicaciones (/SCWM/LS02) | Se han modificado las ubicaciones. |
| [Visualizar ubicaciones](#unique_4) [página ] 8 | Jefe de almacén (EWM) | Visualizar ubicaciones (/SCWM/LS03) | Se visualizan las ubicaciones. |
| [Efectuar modificación en masa de ubicaciones](#unique_5) [página ] 9 | Jefe de almacén (EWM) | Edición en masa de ubicaciones (/SCWM/LS11) | Se realizan modificaciones en masa en las ubicaciones. |
| [Asignar ubicaciones fijas](#unique_6) [página ] 10 | Jefe de almacén (EWM) | Asignar ubicaciones fijas (/SCWM/BINMAT) | Se crea la asignación de ubicación fija. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear ubicaciones

Objetivo

En esta sección encontrará una descripción de cómo crear ubicaciones en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Crear ubicaciones (/SCWM/LS01) . |  |  |
| 3 | Introducir ID de ubicación | El Crear ubicaciones (/SCWM/LS01) introduzca los siguientes datos:Número de almacén : <Su número de almacén>Ubicación : <ID de ubicación>Seleccionar Intro . |  |  |
| 4 | Introducir atributos de ubicación | El Ubicación introduzca los siguientes datos:Tipo de almacén : <Tipo de almacén>Nota Solo el Tipo de almacén El campo es obligatorio. Todos los demás campos siguientes son opcionales:Peso máximoVolumen máx.Pasillo de ubicaciónCoordenada XPilaCoordenada YNivel de ubicaciónCoordenada ZÁngulo de ubicación |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que la ubicación se ha guardado. |  |

### Modificar ubicaciones

Objetivo

En esta sección se modifican las ubicaciones en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Editar ubicaciones (/SCWM/LS02) . |  |  |
| 3 | Introducir ID de ubicación | El Editar ubicaciones (/SCWM/LS02) introduzca los siguientes datos:Número de almacén : <Su número de almacén>Ubicación : <ID de ubicación>Seleccionar Intro . |  |  |
| 4 | Modificar atributos de ubicación | El Ubicación modifique los siguientes valores si es necesario.Nota Solo se pueden modificar los siguientes campos:Peso máximoVolumen máx.Pasillo de ubicaciónCoordenada XPilaCoordenada YNivel de ubicaciónCoordenada ZÁngulo de ubicación |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que la ubicación se ha guardado. |  |

### Visualizar ubicaciones

Objetivo

En esta sección se visualizan las ubicaciones en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como el Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Visualizar ubicaciones (/SCWM/LS03) . |  |  |
| 3 | Introducir ID de ubicación | El Visualizar ubicaciones (/SCWM/LS03) introduzca los siguientes datos:Número de almacén : <Su número de almacén>Ubicación : <ID de ubicación>Seleccionar Intro . | Se visualizan los atributos de ubicación. |  |

### Efectuar modificación en masa de ubicaciones

Objetivo

En esta sección se realiza una modificación en masa de las ubicaciones en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Edición en masa de ubicaciones (/SCWM/LS11) . |  |  |
| 3 | Introducir criterios de filtro | El Modificación en masa de ubicaciones en número de almacén XXXX introduzca los siguientes datos:Número de almacén : <Su número de almacén>Puede introducir los siguientes valores como criterios de selección/filtro:Ubicación : <ID de ubicación> hasta <ID de ubicación>Tipo de almacén : <ID de tipo de almacén> hasta <ID de tipo de almacén>Estado bloqueadoNota Si selecciona la Delimitaciones opcionales puede seleccionar varios filtros para la selección de ubicaciones.Seleccionar Ejecutar . | Se visualiza la lista de ubicaciones que coinciden con los criterios de selección. |  |
| 4 | Modificación en masa de ubicaciones | Seleccione las entradas que desee marcando las casillas de selección correspondientes.Seleccionar Borrar para eliminar varias ubicaciones a la vez.o bienSeleccionar Editar para modificar varias ubicaciones al mismo tiempo. Podrá realizar modificaciones en los siguientes atributos de las ubicaciones.Peso máximoVolumen máx.Pasillo de ubicaciónPilaNivel de ubicaciónÁngulo de ubicación |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que se han guardado las modificaciones en la ubicación. |  |

### Asignar ubicaciones fijas

Objetivo

En esta sección se realiza una asignación de ubicación fija en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Asignar ubicaciones fijas (/SCWM/BINMAT) . |  |  |
| 3 | Introducir criterios de filtro | El Actualizar ubicaciones fijas introduzca los siguientes datos:Número de almacén : <Su número de almacén>Producto : <ID de producto> hasta <ID de producto>Persona autorizada a disponer : <ID de interlocutor comercial> hasta <ID de interlocutor comercial>Nota La persona autorizada a disponer es el socio comercial actualizado para el número de almacén.Ubicación : <ID de ubicación> hasta <ID de ubicación>Tipo de almacén : <ID de tipo de almacén> hasta <ID de tipo de almacén>Seleccionar Ejecutar . | Se visualiza la lista de ubicaciones fijas asignadas que coinciden con los criterios de selección. |  |
| 4 | Crear asignación de ubicación fija | El Número de almacén XXXX: Visualizar ubicación fija , seleccione Editar .El Número de almacén XXXX: Actualizar ubicación fija , seleccione Crear .En la fila recién creada, introduzca los siguientes valores:Eliminación : <ID de interlocutor comercial para la parte autorizada a disponer>Ubicación : <ID de ubicación fija>Tp. : <ID de tipo de almacén de ubicación fija>Producto : <ID de producto>Ctd.máx. : <Cantidad>UM visualiz. : <UM para cantidad máxima> por ejemplo, PCCtd.mín. : <Cantidad>UM visualiz. : <UM para cantidad mínima> por ejemplo, PCSi ha actualizado los valores para los siguientes campos en los datos maestros de producto de almacén:Ctd.máx.ubic.Cantidad máximaCantidad mínimaVisualizar UM para las cantidades máximas/mínimasEl Ctd.máx. y Ctd.mín. valores en la asignación de ubicación fija se calcularán en función de los valores de Cantidad máxima , Cantidad mínima y Ctd.máx.ubic. en los datos maestros de producto de almacén. El Visualizar UM también se completará a partir de los datos maestros de producto de almacén. |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que las ubicaciones se han guardado. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-337]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-339]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 15,838 chars in the whole document
