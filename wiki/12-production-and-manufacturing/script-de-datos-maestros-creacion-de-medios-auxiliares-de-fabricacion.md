---
id: 12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion
title: Script de datos maestros - Creación de medios auxiliares de fabricación - MDS (5CP) (5CP_S4CLD2608_Master_Data_ES_XX)
description: Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (5CP) for creating production resources/tools (MAF) and assigning them to routings and production orders.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_ES_XX]
keywords: [Production Resources/Tools (PRTs), production resources tools, material prt creation, miscellaneous prt creation, document prt creation, equipment prt creation, prt assignment to routing, prt assignment to production order, prt status, prt control key]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-438
topic: 12-production-and-manufacturing/production-resources-tools
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de medios auxiliares de fabricación - MDS (5CP) (5CP_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de medios auxiliares de fabricación - MDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894778)

[2 Requisitos previos 3](#_Toc233894779)

[2.1 Acceso al sistema 3](#_Toc233894780)

[2.2 Roles 3](#_Toc233894781)

[2.3 Unidades organizativas necesarias 4](#_Toc233894782)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894783)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894784)

[2.5.1 Status MAF 4](#_Toc233894785)

[2.5.2 Clave de control MAF 5](#_Toc233894786)

[3 Tabla de resumen 6](#_Toc233894787)

[4 Procedimientos 7](#_Toc233894788)

[4.1 Crear medios auxiliares de fabricación 7](#_Toc233894789)

[4.1.1 Crear MAF de material 7](#_Toc233894790)

[4.1.2 Crear MAF varios 8](#_Toc233894791)

[4.1.3 Crear documento MAF 10](#_Toc233894792)

[4.1.4 Crear MAF de equipo 11](#_Toc233894793)

[4.2 Asignar MAF en hoja de ruta (opcional) 12](#_Toc233894794)

[4.3 Asignar MAF en orden de fabricación (opcional) 14](#_Toc233894795)

[5 Apéndice 16](#_Toc233894796)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un registro de datos maestros de medios auxiliares de fabricación para su SAP S/4HANA Cloud Private Edition sistema. A diferencia de las máquinas y Activos fijos, MAF (medios auxiliares de fabricación) son recursos operativos móviles (no estacionarios) necesarios para realizar un actividad y se puede utilizar repetidamente.

Hay varias categorías de medios auxiliares de fabricación disponibles. La categoría determina las características y el negocio funciones que puede tener un MAF.

Puede crear su propio MAF siguiendo las instrucciones de este script de datos maestros.

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
| Ingeniero de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC | Ingeniería de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC |  |
| Supervisor de producción - Fabricación discreta | SAP_BR_PRODN_SUPERVISOR_DISC | Gestión de producción - Fabricación discreta | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Ingeniero de diseño | SAP_BR_DESIGN_ENGINEER | Gestión de documentos | SAP_BR_DESIGN_ENGINEER |  |
| Planificador de mantenimiento | SAP_BR_MAINTENANCE_PLANNER | Planificación de mantenimiento | SAP_BR_MAINTENANCE_PLANNER |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de material dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos dependen del centro. | Centro:____________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de hoja de ruta de referencia pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en una Referencia hoja de ruta.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Hoja de ruta | Asignar MAF en hoja de ruta | Opcional | Supongamos que tiene una hoja de ruta y desea asignarle MAF. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear un registro de datos maestros de MAF:

#### Status MAF

El estado MAF controla el uso de medios auxiliares de fabricación. En función de su estado, un el medio auxiliar de fabricación se puede liberar para varias tareas en la actualización de MAF.

| Status MAF | Descripción |
| --- | --- |
| 01 | Creado el |
| 02 | Liberado para planificación de utilización MAF |
| 03 | Liberado para producción |

#### Clave de control MAF

La clave de control MAF determina si los MAF están asignados a una hoja de ruta o a una orden. incluidas en las siguientes funciones empresariales:

| Perfil de control MAF | Descripción |
| --- | --- |
| 1 | Todas las funciones |
| 2 | Imprimir |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear MAF de material](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) |  |
| [Crear MAF varios](#unique_12) [página ] 8 | Ingeniero de producción - Fabricación discreta | Gestionar medios auxiliares de fabricación (F7653) |  |
| [Crear documento MAF](#unique_13) [página ] 10 | Ingeniero de diseño | Gestionar documentos (F2733) |  |
| [Crear MAF de equipo](#unique_14) [página ] 11 | Planificador de mantenimiento | Crear objeto técnico (W0029) |  |
| [Asignar MAF en hoja de ruta (opcional)](#unique_15) [página ] 12 | Ingeniero de producción - Fabricación discreta | Modificar hoja de ruta (CA02) |  |
| [Asignar MAF en orden de fabricación (opcional)](#unique_16) [página ] 14 | Supervisor de producción - Fabricación discreta | Modificar orden de fabricación (CO02) |  |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear medios auxiliares de fabricación

#### Crear MAF de material

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este capítulo se muestra cómo crear un MAF de material.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Aparece la página. |  |
| 2 | Abrir la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una ventana nueva que muestra Crear material (inicial) Pantalla) . |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , realice lo siguiente entradas:Material : <Número de material> , para ejemplo, PRT_01Tipo de material : Producción Recursos/herramientasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione vista:Vista básicaMedios auxiliares de fabricaciónOtras vistas necesariasSeleccione Continuar . |  |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en la Sección Nivel de organización, realice las siguientes entradas:Centro : <Código de centro> , por ejemplo, 1010Pulsar Intro . |  |  |
| 6 | Introducir datos de vista básica | El Datos básicos 1 introduzca la etiqueta datos siguientes:Descripción : <Finalizado MAF de montaje>Unidad de medida base : <EA>Seleccione el Medios auxiliares de fabricación tab. | Se graban los datos básicos. |  |
| 7 | Introducir datos de medios auxiliares de fabricación | El Medios auxiliares de fabricación introduzca lo siguiente datos:Utilización MAF : <009>Perfil de control MAF : <1>Seleccionar Grabar . | La pantalla vuelve a la pantalla inicial.Se crea el material PRT_01. |  |

#### Crear MAF varios

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este capítulo le muestra cómo crear un MAF variado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar medios auxiliares de fabricación (F7653) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | Se abre una ventana nueva en la que se muestra Crear MAF pantalla. |  |
| 4 | Introducir nombre | Realice las siguientes entradas:Medio auxiliar de fabricación : <Nombre> , por ejemplo, PRT_02Seleccionar Datos básicos . | El Crear medio auxiliar de fabricación: Datos básicos se visualiza. |  |
| 5 | Introducir datos básicos | Proporcione una descripción para el MAF que ha creado:Buscar el Descripción del medio auxiliar de fabricación texto quick info e introduzca: <MAF varios 02>En la Datos básicos , realice las siguientes entradas:Estado : <03>Utilización MAF : <009>Unidad de medida base : <EA>Seleccionar Grabar . | La pantalla vuelve a la pantalla inicial.Se ha creado el medio auxiliar de fabricación. |  |

#### Crear documento MAF

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este capítulo se muestra cómo crear un MAF de documento.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de diseño . | El Iniciar Aparece la página. |  |
| 2 | Abrir la aplicación SAP Fiori | Abierto Gestionar documentos (F2733) . | Se abre una ventana nueva que muestra Gestionar Documentos . |  |
| 3 | Crear el documento | Seleccionar Crear .El Documento , realice lo siguiente entradas:Clase de documento : <SPP>Descripción de documento : <PRT_03>Seleccionar Crear . | Se crea el documento.Anote el número de documento. |  |
| 4 | Editar el documento | Seleccionar Editar en la esquina superior derecha.En la Datos de documento la sección, cambie la Documento Estado en En curso .En la Originales sección, seleccione Cargar , y adjunte un documento MAF desde su PC.Seleccionar Grabar . | Se graba el documento. |  |
| 5 | Liberar el documento | Seleccionar Editar en la esquina superior derecha.En la Datos de documento la sección, cambie la Documento Estado int Liberado .Seleccionar Grabar . | Se graba el documento. |  |

#### Crear MAF de equipo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este capítulo se muestra cómo crear MAF de equipo.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de mantenimiento . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear objeto técnico (W0029) . | Se abre la aplicación. |  |
| 3 | Crear equipo | El Crear objeto técnico , seleccione el botón de selección Tipo de objeto técnico: Equipo .En la siguiente pantalla, introduzca lo siguiente:Tipo de objeto técnico : EquipoObjeto técnico : dejar en blancoInicio de validez : fecha de hoyCategoría de objeto técnico : P (medios auxiliares de fabricación)Seleccionar Continuar . |  |  |
| 4 | Actualizar datos generales | El Crear objeto técnico: <ID de equipo> en la pantalla Datos generales sección, introduzca lo siguiente:Descripción : <Por ejemplo, equipo MAF>Opcionalmente, actualice otros datos generales y, a continuación, navegue al MAF Datos sección. | El Crear objeto técnico: Datos generales Aparece la pantalla. |  |
| 5 | Actualizar datos MAF | En la Datos MAF introduzca lo siguiente:Utilización de hoja de ruta : 009 (todos los tipos de hoja de ruta)Clave de control : 1 (todas las funciones)Opcionalmente, actualice más detalles. Por ejemplo, puede crear un punto de medición asignado con algunas características y, a continuación, adjunte el Punto de medida en campo Punto de medición , y marque la casilla de selección para el campo Cargar Registros . | El Crear objeto técnico: Datos de ubicación aparece la pantalla. |  |
| 6 | Guardar equipo | Opcionalmente, puede actualizar información adicional para otras secciones.Seleccionar Grabar . | Se ha creado el equipo. Anote el número de equipo. |  |

### Asignar MAF en hoja de ruta (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este capítulo se muestra cómo asignar MAF de material, MAF varios, MAF de documento o MAF de equipo en la hoja de ruta. Puede asignar diferentes tipos de medios auxiliares de fabricación a las hojas de ruta y órdenes de fabricación para las que son necesarias. MAF asignados a la hoja de ruta se copiará automáticamente en la orden de fabricación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | El Iniciar Aparece la página. |  |
| 2 | Abrir la aplicación SAP Fiori | Abierto Modificar hoja de ruta (CA02) . | Se abre una ventana nueva que muestra Modificar hoja de ruta: Inicial Pantalla . |  |
| 3 | Introducir material | Realice las siguientes entradas y seleccione Continuar :Material : <Material número>Centro : <Código de centro> , por ejemplo, 1010 | El Modificar hoja de ruta: Resumen de operaciones Aparece la pantalla. |  |
| 4 | Seleccionar operación | Marque una posición y seleccione Operaciones .Seleccione una operación que desee asignar a MAF. A continuación, seleccione MAF . | El Modificar hoja de ruta: Resumen MAF Aparece la pantalla. |  |
| 5 | Asignar MAF de material | Cuando no exista ningún MAF en la operación, realice lo siguiente: entradas en el diálogo: Modificar hoja de ruta: Nueva MAF .Si ya hay alguno, seleccione Material , realice las siguientes entradas y pulse la marca de verificación verde:Número de posición MAF : <0010>Material : <Material número> , por ejemplo, PRT_01Centro : <Centro código> , por ejemplo, 1010 | El MAF de material está asignado a la operación. |  |
| 6 | Asignar MAF varios | Seleccionar Otros , realice las siguientes entradas y pulse la marca de verificación verde:Número de posición MAF : <0020>Medios auxiliares de fabricación : <Nombre> , por ejemplo, PRT_02 | Hay varios MAF asignados a la operación. |  |
| 7 | Asignar MAF de documento | Seleccionar Documento , realice las siguientes entradas y pulse la marca de verificación verde:Número de posición MAF : <0030>Documento : <Número de documento creado en paso anterior>Clase de documento : <SPP>Parte de documento : <000>Versión de documento : <00>Cantidad : <1 EA>Perf.ctrl. : <1> | El documento MAF está asignado a la operación. |  |
| 8 | Asignar MAF de equipo | Seleccionar Equipo , realice las siguientes entradas y seleccione el verde marca de verificación:Equipo : <Número de equipo creado en el paso anterior> |  |  |
| 9 | Grabar las modificaciones | Seleccionar Grabar . | Se ha guardado la hoja de ruta. |  |

### Asignar MAF en orden de fabricación (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este capítulo se muestra cómo asignar MAF de material, MAF varios, MAF de documento o MAF de equipo para una operación en una orden de fabricación. Marca Asegúrese de que tiene una orden de fabricación creada por adelantado. También puede asignar MAF en la pestaña Resumen de operaciones durante la creación de la orden.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Supervisor de producción - Fabricación discreta . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Modificar orden de fabricación (CO02) . | Se abre una ventana nueva que muestra Modificación de orden de fabricación: Acceso . |  |
| 3 | Introducir información de orden | Realice las siguientes entradas y seleccione Continuar :Orden : <Número de orden> | El Creación de orden de fabricación: Modificar Aparece la pantalla. |  |
| 4 | Seleccionar una operación | Seleccionar Operaciones .En la Resumen de operaciones tabla, marque la casilla de selección de uno operación, por ejemplo, Operación 0010 , y seleccione MAF . | Un nuevo diálogo Modificación de orden de fabricación: MAF nuevo Entradas aparece si no existe ningún MAF en la operación.Si ya hay alguno, Resumen de medios auxiliares de fabricación se mostrará la tabla. |  |
| 5 | Asignar MAF de material | Cuando no exista ningún MAF en la operación, realice las siguientes entradas en el diálogo Modificación de orden de fabricación: MAF nuevo Entradas :Si ya existe una, seleccione la + a las la parte inferior de Medios auxiliares de fabricación Resumen y realice las siguientes entradas:Número de posición : por ejemplo, 0010Material : por ejemplo, PRT_01Centro : por ejemplo, 1010Seleccione la marca de verificación verde. | El MAF de material está asignado a la operación. |  |
| 6 | Asignar MAF varios | Seleccione el + en la parte inferior de Producción Resumen de recursos/herramientas y seleccione Otros . A continuación, realice lo siguiente entradas:Número de posición : por ejemplo, 0020MAF : por ejemplo, PRT_02Seleccione la marca de verificación verde. | Hay varios MAF asignados a la operación. |  |
| 7 | Asignar MAF de documento | Seleccione el + en la parte inferior de Producción Resumen de recursos/herramientas y seleccione Documento . Luego, haga lo siguiente entradas:Número de posición : <0030>Documento : <Número de documento creado en anterior Paso>Clase de documento : <SPP>Parte de documento : <000>Versión de documento : <00>Cantidad : <1 EA>Clave de control : <1>Seleccione la marca de verificación verde. | El documento MAF está asignado a la operación. |  |
| 8 | Asignar MAF de equipo | Seleccione el + en la parte inferior de Resumen de medios auxiliares de fabricación y seleccionar Equipo . A continuación, realice las siguientes entradas:Equipo : <Número de equipo creado en el paso anterior>Perfil de control : 1 (todas las funciones)Seleccione la marca de verificación verde. |  |  |

## Apéndice

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Objetivo refers to SAP S/4HANA Cloud Private Edition while the document is for Public Edition

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]
- related-to :: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]
- related-to :: [[12-production-and-manufacturing/mds-5cp-441]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 25,167 chars in the whole document
