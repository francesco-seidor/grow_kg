---
id: 12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj
title: Script de datos maestros - Crear puesto de trabajo de producción - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ES_XX)
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data test script BNJ: create a production work center (F6175) and optionally work center groups (F4044)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_ES_XX]
keywords: [Production Work Centers and Work Center Groups, work centers, work center groups, capacity planning, standard value keys, work center categories, cost calculation, routings, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-618
topic: 12-production-and-manufacturing/production-work-centers
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear puesto de trabajo de producción - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear puesto de trabajo de producción - MDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894989)

[2 Requisitos previos 3](#_Toc233894990)

[2.1 Acceso al sistema 3](#_Toc233894991)

[2.2 Roles 3](#_Toc233894992)

[2.3 Unidades organizativas necesarias 3](#_Toc233894993)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894994)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894995)

[2.5.1 Clase de puesto de trabajo 4](#_Toc233894996)

[3 Tabla de resumen 5](#_Toc233894997)

[4 Procedimientos de prueba 6](#_Toc233894998)

[4.1 Creación de puesto de trabajo 6](#_Toc233894999)

[4.2 Gestión de grupos de puestos de trabajo (opcional) 8](#_Toc233895000)

[4.2.1 Crear grupo de puestos de trabajo (opcional) 8](#_Toc233895001)

[4.2.2 Asignar puesto de trabajo (opcional) 9](#_Toc233895002)

[5 Apéndice 11](#_Toc233895003)

[5.1 Crear hoja de ruta 11](#_Toc233895004)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un puesto de trabajo es donde se llevan a cabo las operaciones de producción. Por ejemplo, un puesto de trabajo puede representar una línea de producción, una máquina, un grupo de máquinas, un empleado o un grupo de empleados.

Un puesto de trabajo contiene información utilizada para la planificación de capacidad (por ejemplo, capacidad disponible), programación (p. ej., fórmula para el tiempo de procesamiento) y cálculo de costos (p. ej., centro de costos). Este la información se utiliza en hojas de ruta y en transacciones como órdenes de trabajo de producción. La información es específica de un sitio de producción (conocido como centro).

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

### Unidades organizativas necesarias

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos para el puesto de trabajo dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos del puesto de trabajo pueden hacer referencia a otros datos maestros . Los siguientes La tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un puesto de trabajo.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Clave de valor prefijado | En la IU del centro de trabajo, etiqueta de datos básicos, encontrará la entrada de clave de valor prefijado en estándar Actualización de valores sección. | Obligatorio | El sistema utiliza valores estándar como parámetros con origen estándar valor en fórmulas para calcular el tiempo de ejecución, la capacidad necesidades y costes.La clave de valor estándar se utiliza para asignar un ID de parámetro al estándar. valores. Este ID de parámetro identifica el valor estándar en un fórmula. Puede utilizar el ID de parámetro para determinar la palabra clave para un valor estándar, como configuración, máquina o mano de obra. |

### Parámetros principales para la creación de datos

En esta sección se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear un puesto de trabajo:

#### Clase de puesto de trabajo

La clase de puesto de trabajo determina qué datos se pueden actualizar en el registro maestro para el puesto de trabajo. Los puestos de trabajo se pueden distinguir por su categoría (por ejemplo, puesto de trabajo de producción, puesto de trabajo de mantenimiento y puesto de trabajo de servicio, etc.)

| Clase de puesto de trabajo | Descripción |
| --- | --- |
| 0001 | Máquina |
| 0007 | Línea de producción |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de puesto de trabajo](#unique_10) [página ] 6 | Ingeniero de producción - Fabricación discreta | Gestionar centros de trabajo (F6175) |  |
| [Crear grupo de puestos de trabajo (opcional)](#unique_11) [página ] 8 | Ingeniero de producción - Fabricación discreta | Gestionar grupos de puestos de trabajo (F4044) |  |
| [Asignar puesto de trabajo (opcional)](#unique_12) [página ] 9 | Ingeniero de producción - Fabricación discreta | Gestionar grupos de puestos de trabajo (F4044) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de puesto de trabajo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Abrir la aplicación SAP Fiori | Seleccionar Gestionar centros de trabajo (F6175) . |  |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | Se muestra una nueva pantalla que muestra el Crear puesto de trabajo: Inicial Pantalla . |  |
| 4 | Introducir código de centro | Intro Código de centro . | El Crear organización se visualiza. |  |
| 5 | Introducir ID de puesto de trabajo | Intro ID de puesto de trabajo .Nota La longitud de campo del ID de puesto de trabajo es inferior a 8. |  |  |
| 6 | Clase de puesto de trabajo | Seleccione la clase de puesto de trabajo:<0001> Máquina<0007> Línea de producción |  |  |
| 7 | Seleccionar datos básicos | Seleccionar Datos básicos en la esquina superior izquierda de la pantalla. | El Crear puesto de trabajo: Datos básicos pantalla muestra. |  |
| 8 | Introducir datos | El Datos básicos introduzca los siguientes datos:Descripción : <introduzca la descripción>Responsable : <persona responsable o responsable del centro>Utilización : <009>Clave de valor prefijado : <SAP1> |  |  |
| 9 | Configurar las fórmulas de capacidad y procesamiento | El capacidades introduzca los siguientes datos:Clase de capacidad : <001(Máquina/002(Persona)>configurar fórmula : <SAP005>Fórmula de procesamiento : <SAP006>Pulsar Intro . | El Crear puesto de trabajo Capacidad: Cabecera se visualiza. |  |
| 10 | Configurar capacidad de puesto de trabajo | En la Capacidad de puesto de trabajo: Cabecera introduzca los siguientes datos:Descripción de categoría de capacidad : <añada una descripción>Responsable de capacidad : Pulse F4 para buscar a la persona responsable del centro.ID de calendario de fábrica : <Calendario para su país>Versión activa : <1>Unidad base de capacidad : por ejemplo, DHora de inicio : <Hora de inicio>Hora de fin : <Hora de fin>Duración de las pausas : <Longitud de las pausas>Tiempo de operación : <Tiempo operativo>Utilización de capacidad : <100>Ctd.cap.indiv. : <10>Relevante para programación finita : <X>Planificación a largo plazo : <X>Se puede utilizar en varias operaciones : <X>Pulsar Intro . | La pantalla vuelve al resumen de capacidad. |  |
| 11 | Introducir datos de programación | El Programación introduzca los siguientes datos:Categoría de capacidad : <001(Máquina/002(Persona)>Duración de la preparación : <SAP001>Duración de procesamiento : <SAP002> |  |  |
| 12 | Introducir datos de cálculo del coste | El Cálculo de costes introduzca los siguientes datos:Centro de coste : <Centro de coste para su sociedad>Clase de actividad ( para configuración) : <3>Fórmula ( para configuración) : <SAP005>Clase de actividad (máquina) : <1>Fórmula (máquina) : <SAP006>Clase de actividad (mano de obra) : <11>Fórmula (Mano de obra) : <SAP007>Unidad de actividad : Seleccione la UM necesaria, por ejemplo, Mín. |  |  |
| 13 | Guardar los datos | Guarde las entradas. |  |  |

### Gestión de grupos de puestos de trabajo (opcional)

Objetivo

Este capítulo le muestra cómo agrupar los puestos de trabajo si es necesario.

#### Crear grupo de puestos de trabajo (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este paso del proceso le muestra cómo crear un grupo de puestos de trabajo.

Puede verificar los grupos de puestos de trabajo de muestra creados mediante la etapa de proceso Crear y asignar grupo de puestos de trabajo en el elemento de alcance 31L .

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar grupos de puestos de trabajo (F4044) . | Se abre la aplicación. |  |
| 3 | Crear grupo | Seleccionar Crear encima de la tabla.El Crear grupo de pantalla, haga siguientes entradas:Grupo : <Introduzca el nombre del grupo>Centro : 1010Tipo de grupo : <ALTERNATIV> o <MISMA LÍNEA> o <RSPONSBLTY>Descripción : <Introduzca la descripción>Seleccionar Crear . | Se crea el grupo de puestos de trabajo. |  |

#### Asignar puesto de trabajo (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Esta etapa de proceso le muestra cómo asignar puestos de trabajo al grupo de puestos de trabajo.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar grupos de puestos de trabajo (F4044) . | Se abre la aplicación. |  |
| 3 | Seleccionar el grupo | Busque el grupo creado en el paso anterior y, a continuación, seleccione el icono > al final de la fila. | La lista de información detallada se muestra en el panel derecho. |  |
| 4 | Asignar centro de trabajo | En la Componentes de grupo sección, seleccione Asignar centro de trabajo .Seleccione uno o varios puestos de trabajo de la ventana de diálogo y seleccione OK .Nota Si un puesto de trabajo ya está asignado a otro grupo, aparecerá un mensaje de error: El puesto de trabajo "XXX" ya está asignado a este Tipo de grupo . | Los puestos de trabajo asignados a la visualización de grupo.Los puestos de trabajo se han asignado correctamente. |  |

## Apéndice

### Crear hoja de ruta

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Hoja de ruta |  |  | Para ejecutar esta actividad, ejecute la Crear hoja de ruta - MDS (BNL) Test script. |

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
- related-to :: [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-619]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-621]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 16,816 chars in the whole document
