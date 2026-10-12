---
id: 14-maintenance-service-and-projects/crear-punto-de-medicion-mds-5mi-468
title: Crear punto de medición - MDS (5MI) (5MI_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script (5MI): create measuring points and measuring counters for maintenance, with measuring point type setup."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/measuring-points-and-counters]
aliases: [5MI_S4CLD2608_Master_Data_ES_XX]
keywords: [Measuring Points and Counters, measuring points, measuring counters, maintenance master data, master data scripts, measuring point category, condition-based maintenance, technical objects, fiori launchpad roles, 5MI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-468
topic: 14-maintenance-service-and-projects/measuring-points-and-counters
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear punto de medición - MDS (5MI) (5MI_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Measuring Points and Counters** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear punto de medición - MDS (5MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894769)

[2 Requisitos previos 3](#_Toc233894770)

[2.1 Acceso al sistema 3](#_Toc233894771)

[2.2 Roles 3](#_Toc233894772)

[2.3 Unidades organizativas necesarias 3](#_Toc233894773)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894774)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894775)

[2.5.1 Tipo de punto de medición 4](#_Toc233894776)

[3 Tabla de resumen 7](#_Toc233894777)

[4 Procedimiento 8](#_Toc233894778)

[4.1 Crear punto de medición 8](#_Toc233894779)

[4.2 Crear contador de medición 9](#_Toc233894780)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear datos maestros de un punto de medición. para su sistema S/4HANA. La descripción incluye los segmentos de datos que relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector principalmente aprende qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance de la entrega de contenido de S/4HANA por parte de SAP Best Las prácticas no se describen en este documento, aunque pueden aparecer en el usuario interfaz de usuario (IU).

## Requisitos previos

En esta sección se resumen todos los requisitos previos para crear un punto de medición.

### Acceso al sistema

El ensayo debe realizarse con el siguiente sistema:

Tabla 1:

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. Su administrador del sistema le proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio) | ID (espacio) |
| --- | --- | --- | --- |
| Especialista en datos maestros - Gestión de mantenimiento | SAP_BR_MD_SPECIALIST_EAM | Datos maestros: Gestión de mantenimiento | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de los diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Datos maestros obligatorios y opcionales

Los registros de datos de punto de medición pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en una medición punto.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Objeto técnico |  | Obligatorio | Equipo o Ubicación técnica. |
| Característica |  | Obligatorio | Las características describen las propiedades de los objetos. Los valores de un la característica especifica las propiedades. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear un punto de medición.

#### Tipo de punto de medición

El tipo de punto de medición determina los datos que se pueden actualizar en el registro maestro para el punto de medición. Los puntos de medición se distinguen en el sistema por punto de medición categoría. Cada tipo de punto de medición se identifica mediante una clave, que es lo primero asigne al punto de medición cuando lo cree en el sistema.

Tabla 2:

| Tipo de punto de medición | Descripción |
| --- | --- |
| M | Punto de medida (general) |

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El objetivo de esta actividad es configurar el tipo de punto de medición.

Procedimiento

En función de su entorno de configuración para SAP S/4HANA Cloud Public Edition, seleccione una de las siguientes opciones:

Configurar su solución :

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración de proceso empresarial . | El Rampa de lanzamiento SAP Fiori se visualiza. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar su solución ( F1241 ). | Gestionar su solución la pantalla es visualizado. |  |
| 3 | Abrir Configurar su solución | Seleccionar Configurar su solución .Nota Para crear opciones dependientes de país/región para la versión local prevista, seleccione Fijar versión local .Seleccione el área de aplicación como Gestión de activosSeleccione el área de subaplicación como Gestión de mantenimientoSeleccione la fila con el nombre de artículo: Datos maestros | Se muestra la pantalla Configure Your Solution. |  |
| 4 | Abra Definir categorías de punto de medición | Por debajo de Pasos de configuración , seleccione el nombre del paso " Definir categorías de punto de medición " y haga clic en Configurar | Tipos de puntos de medida Se visualizará la pantalla |  |
| 5 | Activar condiciones para CBM (opcional) | Seleccione la categoría de punto de medición "M"Intro Ámbito de medida Mensaje como “W”Marque la casilla de selección de Crear notificacionesHaga clic en Grabar | Se han establecido las condiciones para CBM |  |

SAP Central Business Configuration

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Experto en configuración - Proceso empresarial Configuración . | El Rampa de lanzamiento SAP Fiori se visualiza. |  |
| 2 | Acceder a la aplicación | Abierto Actividades de implementación | El Gestionar su solución la pantalla es visualizado. |  |
| 3 | Configuración de acceso | Para localizar la actividad en la vista de árbol, haga clic en el icono de búsqueda y seleccionar la extensión Búsqueda opciónIntroduzca el Texto de nodo/Descripción de actividad: " Definir Tipos de punto de medida " y haga clic en continuar | Se visualiza la actividad en la vista de árbol. |  |
| 4 | Abra Definir categorías de punto de medición | Por debajo de Pasos de configuración , seleccione el paso nombre " Definir categorías de punto de medición " y haga clic en Configurar | Tipos de puntos de medida la pantalla será visualizado |  |
| 5 | Activar condiciones para CBM (opcional) | Seleccione la categoría de punto de medición "M"Intro Ámbito de medida Mensaje como “W”Marque la casilla de selección de Crear NotificacionesHaga clic en Grabar | Se han establecido las condiciones para CBM |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la tabla.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear punto de medición](#unique_10) [página ] 8 | SAP_BR_MD_SPECIALIST_EAM | Crear punto de medición (EAMS_WDA_MP_OIF) aplicación | Se ha creado el punto de medición. |

## Procedimiento

En esta sección se describen los procedimientos para cada paso del proceso que pertenece a este elemento de alcance. Usted puede utilizar estos procedimientos también para probar la creación de datos maestros.

### Crear punto de medición

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como especialista en datos maestros SAP_BR_MD_SPECIALIST_EAM . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abra la Crear punto de medición (EAMS_WDA_MP_OIF) aplicación. | Se abre una ventana nueva que muestra la Crear punto de medición pantalla. |  |
| 3 | Introducir detalles | Introduzca lo siguiente:Punto de medición/Contador : <Punto de medición>Tipo de objeto de referencia : <Objeto técnico> | Aparece una nueva pantalla que muestra el objeto de referencia. |  |
| 4 | Introducir detalles de objeto de referencia | Introduzca lo siguiente:Objeto técnico : <Número de equipo/ubicación>Pulse Intro o seleccione Continuar . | Crear punto de medición |  |
| 5 | Datos generales | El Datos generales introduzca lo siguiente:Descripción : <Descripción del punto de medición>Característica : Por ejemplo, OPERATING_HOUR/PRESSURETipo de punto de medición : M (punto de medida general) |  |  |
| 6 | Introducir límites de destino y datos de contador | El Límites de destino y Datos de contador introduzca lo siguiente:Valor de destino : Por ejemplo, 10 PALímite de rango superior : Por ejemplo, 15 PALímite de rango inferior : Por ejemplo, 5 PA |  |  |
| 7 | Introducir tolerancia de medición (opcional) | El Sección Tolerancia de medición , introduzca lo siguiente:Tolerancia de medición superior : Por ejemplo, 12 PATolerancia de medición inferior : Por ejemplo, 7 PA |  |  |
| 8 | Actualizar condición (solo para actualización basada en condiciones) | En la sección Actualizar condición,Haga clic en la casilla de selección para Activar condición, seleccione cualquier condición : Por ejemplo, Para condición : LECTURA DE MEDIDAS > LÍMITE SUPERIORIntroduzca los siguientes detalles:Tipo de objeto (clase de aviso) : Por ejemplo, Trabajo reactivoPrioridad : seleccione la prioridad necesaria para crear el aviso, por ejemplo, 1 Muy altaActivo : haga clic en la casilla de selección para activar esta condiciónTexto explicativo : introduzca el texto explicativo para el aviso que se va a crearDescripción : introduzca la descripción para el aviso que se va a crear |  |  |
| 9 | Verificar entradas | Seleccionar Verificar entradas . | Se verifican las entradas. |  |
| 10 | Grabe los datos | Guarde las entradas. | Se ha creado el punto de medición. |  |

### Crear contador de medición

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como datos maestros especialista SAP_BR_MD_SPECIALIST_EAM . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abra la Crear punto de medición ( EAMS_WDA_MP_OIF ) | Se abre una ventana nueva que muestra la Crear punto de medición pantalla. |  |
| 3 | Introducir detalles | Introduzca lo siguiente:Punto de medición/Contador : <Contador>Tipo de objeto de referencia : <Objeto técnico> | Aparece una nueva pantalla que muestra el objeto de referencia. |  |
| 4 | Introducir objeto de referencia | Introduzca lo siguiente:Objeto técnico : <Número de equipo/ubicación>Pulsar Intro o seleccione Continuar . | Crear punto de medición (contador) Se abre la pantalla. |  |
| 5 | Introducir datos generales | El Datos generales introduzca lo siguiente:Descripción : <Descripción del contador de medición>Tipo de punto de medición : M (punto de medida general)Característica : Por ejemplo, OPERATING_HOUR/PRESSURE | Datos generales actualizados |  |
| 6 | Introducir límites de destino y datos de contador | El Límites de destino y datos de contador introduzca lo siguiente:Lectura de desbordamiento : <Lectura de desbordamiento de contador>Estimación anual : <Estimación anual de objeto técnico>Unidad de ámbito de medida | Se actualizan los límites de destino |  |
| 7 | Verificar entradas | Seleccionar Verificar entradas . | Se verifican las entradas. |  |
| 8 | Grabe los datos | Guarde las entradas. | Se ha creado el punto de medición. |  |

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
- related-to :: [[14-maintenance-service-and-projects/5mi-469]]
- related-to :: [[14-maintenance-service-and-projects/create-measuring-point-mds-5mi-467]]
- related-to :: [[14-maintenance-service-and-projects/criar-ponto-de-medicao-mds-5mi-470]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mi-471]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 17,246 chars in the whole document
