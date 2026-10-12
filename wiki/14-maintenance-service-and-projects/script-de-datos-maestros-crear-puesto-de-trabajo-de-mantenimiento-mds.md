---
id: 14-maintenance-service-and-projects/script-de-datos-maestros-crear-puesto-de-trabajo-de-mantenimiento-mds
title: "Script de datos maestros - Crear puesto de trabajo de mantenimiento (MDS, 5MH) (5MH_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish (machine-translated) master data script for scope 5MH: creating a maintenance work center with CR01 in SAP S/4HANA Cloud Public Edition."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_ES_XX]
keywords: [Maintenance Work Centers, maintenance work center, work center class, work center capacity, standard value key, cost calculation, business roles, master data scripts, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-462
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear puesto de trabajo de mantenimiento (MDS, 5MH) (5MH_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear puesto de trabajo de mantenimiento - MDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894782)

[2 Requisitos previos 3](#_Toc233894783)

[2.1 Acceso al sistema 3](#_Toc233894784)

[2.2 Roles 3](#_Toc233894785)

[2.3 Unidades organizativas necesarias 3](#_Toc233894786)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894787)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894788)

[2.5.1 Clase de puesto de trabajo 4](#_Toc233894789)

[3 Tabla de resumen 5](#_Toc233894790)

[4 Procedimiento 6](#_Toc233894791)

[4.1 Crear puesto de trabajo de mantenimiento 6](#_Toc233894792)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un maestro de puestos de trabajo de mantenimiento. registro de datos para su sistema S/4HANA. La descripción incluye los segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector principalmente aprende qué segmentos de datos y campos suelen tener que rellenarse con datos valores. Campos que no son relevantes para el alcance de la entrega de contenido de S/4HANA por SAP Best Practices no se describen en este documento, aunque pueden aparecer en la interfaz de usuario (IU).

Un registro maestro de puesto de trabajo de mantenimiento que se crea como se describe aquí se puede utilizar para procesos de mantenimiento.

## Requisitos previos

Esta sección resume todos los requisitos previos para crear un puesto de trabajo.

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
| Ingeniero de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC | Ingeniería de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa, General Los datos (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos para el puesto de trabajo dependen del centro. | Centro: –––––-- |

### Datos maestros obligatorios y opcionales

Los registros de datos del puesto de trabajo pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un puesto de trabajo.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Clave de valor prefijado | En la pantalla del puesto de trabajo, Datos básicos pestaña, usted encontrar la entrada de la clave de valor prefijado en la actualización del valor prefijado sección. | Obligatorio | El sistema utiliza valores estándar como parámetros con estándar de origen. valor en fórmulas para calcular el tiempo de ejecución, necesidades de capacidad y costes. Utilice la clave de valor estándar para asignar un ID de parámetro a valores estándar. Este ID de parámetro identifica el valor estándar en una fórmula. Puede utilizar el ID de parámetro para determinar la palabra clave para un valor estándar, como configuración, máquina o mano de obra. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear un puesto de trabajo de mantenimiento:

#### Clase de puesto de trabajo

La clase de puesto de trabajo determina qué datos se pueden actualizar en el registro maestro para el puesto de trabajo. Los puestos de trabajo se pueden distinguir por su categoría (por ejemplo, puesto de trabajo de producción, puesto de trabajo de mantenimiento, puesto de trabajo de servicio, etc.)

Tabla 2:

| Clase de puesto de trabajo | Descripción |
| --- | --- |
| 0005 | Mantenimiento |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la tabla.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear puesto de trabajo de mantenimiento](#unique_10) [página ] 6 | SAP_BR_PRODN_ENG_DISC | Crear puesto de trabajo (CR01) | Se ha creado el puesto de trabajo. |

## Procedimiento

En esta sección se describen los procedimientos para cada paso del proceso que pertenece a este elemento de alcance. También puede utilizar estos procedimientos para probar la creación de datos maestros.

### Crear puesto de trabajo de mantenimiento

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
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como SAP_BR_PRODN_ENG_DISC . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear puesto de trabajo (CR01) . | Se abre una ventana nueva que muestra el Crear puesto de trabajo: Acceso . |  |
| 3 | Introducir código de centro | Introduzca el Código de centro : <1010> | El Crear organización la pantalla es visualizado. |  |
| 4 | Introducir ID de puesto de trabajo | Introduzca el ID de puesto de trabajo: <RES-0100>Nota La longitud de campo del ID de puesto de trabajo es inferior a 8. |  |  |
| 5 | Clase de puesto de trabajo | Seleccione la clase de puesto de trabajo: <0005 > Centro Mantenimiento |  |  |
| 6 | Seleccionar datos básicos | Seleccionar Datos básicos en la parte superior izquierda esquina de la pantalla. | Aparece la pantalla Create work center: basic data. |  |
| 7 | Introduzca la descripción del puesto de trabajo, seleccione la persona responsable, la utilización y el estándar Clave de valor | El Datos básicos introduzca lo siguiente datos:Descripción : por ejemplo, RES-0100Responsable : por ejemplo, <YMM> Mecánico de mantenimiento SupervisorUtilización : por ejemplo, <004> Solo tarea de mantenimiento ListasClave de valor prefijado : por ejemplo, <SAP0> Sin estándar Valores |  |  |
| 8 | Introducir clave de control | Seleccionar Valores propuestos introduzca la etiqueta datos siguientes:Clave de control : por ejemplo, <YBM1> Centro Actualización-Interno . |  |  |
| 9 | Configurar la capacidad y otras fórmulas | El Capacidades introduzca lo siguiente datos:Categoría de capacidad : por ejemplo, <002> PersonaOtra fórmula : por ejemplo, <YBPM01> Proy.:Neces.red | Seleccione Intro. La pantalla Crear capacidad de puesto de trabajo: Cabecera aparece. |  |
| 10 | Configurar capacidad de puesto de trabajo | En la sección Capacidad de puesto de trabajo: Cabecera, introduzca los siguientes datos:Descripción de categoría de capacidad : por ejemplo, Mecánica CapacidadResponsable de capacidad : por ejemplo, <A> Planificador Grupo ACalendario de fábrica : Calendario de ID para su país, por ejemplo, <01> Alemania (estándar)Unidad base de capacidad : por ejemplo, <H> HoraHora de inicio : por ejemplo, <06:00:00>Hora de fin : por ejemplo, <14:30:00>Duración de las pausas : por ejemplo, <00:30:00>Utilización de capacidad : por ejemplo, <100>Ctd.capacidades ind. : por ejemplo, <10>Planificación a largo plazo : <X> | Seleccione Intro. La pantalla vuelve al resumen de capacidad. |  |
| 11 | Introducir datos de programación | El Programación introduzca lo siguiente datos:Categoría de capacidad : por ejemplo, <002> Persona |  |  |
| 12 | Introducir datos de cálculo del coste | El Cálculo de costes introduzca la etiqueta datos siguientes:Fecha de inicio : por ejemplo, <01/01/2015>Centro de coste : por ejemplo, < 10101701> Centro y mant. (DE)Cl.actividad tratam.int. : para ejemplo, <11> Personal HorasClave de fórmula para el cálculo del coste : para ejemplo, <YBPM01> Proy.:Neces.actual.red |  |  |
| 13 | Grabe los datos | Grabe sus entradas | Se graban las entradas. |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461]]
- related-to :: [[14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-463]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-465]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 13,070 chars in the whole document
