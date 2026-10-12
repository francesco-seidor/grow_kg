---
id: 12-production-and-manufacturing/crear-recurso-mds-3x8-378
title: Crear recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script 3X8 for creating a production resource (app F6176) in SAP S/4HANA Cloud 2608, with a pointer to script 3X9."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X8_S4CLD2608_Master_Data_ES_XX]
keywords: [Process Manufacturing Resources and Master Recipes, resource master data, resource category, standard value key, capacity planning, cost center, master recipe, business roles, master data scripts, 3X8]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-378
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear recurso - MDS (3X8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894653)

[2 Requisitos previos 3](#_Toc233894654)

[2.1 Acceso al sistema 3](#_Toc233894655)

[2.2 Roles 3](#_Toc233894656)

[2.3 Unidades organizativas necesarias 3](#_Toc233894657)

[2.4 Datos maestros obligatorios y opcionales 3](#_Toc233894658)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894659)

[2.5.1 Categoría de recurso 4](#_Toc233894660)

[3 Tabla de resumen 5](#_Toc233894661)

[4 Procedimientos de prueba 6](#_Toc233894662)

[4.1 Creando recurso 6](#_Toc233894663)

[5 Apéndice 9](#_Toc233894664)

[5.1 Crear receta de planificación 9](#_Toc233894665)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un medio de recursos de producción y personas implicadas en un proceso de producción que tienen capacidades asignadas a ellas. Los recursos se dividen en categorías de recursos, como línea de producción, mano de obra, almacenamiento.

Con los recursos, puede:

- Crear una estructura de red de recursos para definir la secuencia de los recursos utilizado
- Definir una jerarquía de recursos para agrupar recursos para la evaluación
- Clasificar los recursos para definir su idoneidad para un fin o uso en un operación

## Requisitos previos

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
| Ingeniero de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC | Ingeniería de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizativas necesarias

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos para el recurso dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de recursos pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un recurso.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Clave de valor prefijado | En la IU de recursos, etiqueta de datos básicos, encontrará la entrada de clave de valor prefijado en estándar Actualización de valores sección. | Obligatorio | El sistema utiliza valores estándar como parámetros con estándar de origen. valor en fórmulas para calcular el tiempo de ejecución, necesidades de capacidad y costes.La clave de valor estándar se utiliza para asignar un ID de parámetro al estándar. valores. Este ID de parámetro identifica el valor estándar en un fórmula. Puede utilizar el ID de parámetro para determinar la palabra clave para un valor estándar, como configuración, máquina o mano de obra. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear un recurso.

#### Categoría de recurso

La categoría de recurso determina el tipo de datos que se deben actualizar en el maestro de recursos registro. Clave que diferencia los recursos según su categoría (por ejemplo, recurso) grafo, unidad de proceso).

| Categoría de recurso | Descripción |
| --- | --- |
| 0008 | Unidad de procesamiento |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Creando recurso | Ingeniero de producción - Fabricación por procesos | Gestionar recursos (F6176) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este alcance posición.

### Creando recurso

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación por procesos | El Iniciar Se muestra la página. |  |
| 2 | Abrir la aplicación SAP Fiori | Seleccionar Gestionar recursos (F6176) . |  |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | Se muestra una nueva pantalla que muestra el Crear recurso: Inicial Pantalla . |  |
| 4 | Introducir código de centro | Intro Código de centro . | El Crear organización se visualiza. |  |
| 5 | Introducir ID de recurso | Intro ID de recurso .Nota La longitud del campo del ID de recurso es inferior a 8. |  |  |
| 6 | Categoría de recurso | Seleccione la categoría de recurso:<0008> Unidad de procesamiento |  |  |
| 7 | Seleccionar datos básicos | Seleccionar Datos básicos en la esquina superior izquierda de la pantalla. | El Crear recurso: Datos básicos pantalla muestra. |  |
| 8 | Introducir datos | El Datos básicos introduzca los siguientes datos:Descripción : <introduzca la descripción>Responsable : <persona responsable o responsable del centro>Utilización : <008>Clave de valor prefijado : <YBP1> |  |  |
| 9 | Introducir los valores predeterminados | El Valores propuestos introduzca los siguientes datos:Clave de control : <YBP4>Unidad de valor prefijado de la máquina : <H>Unidad de trabajo de valor estándar : <H> |  |  |
| 10 | Configurar las fórmulas de capacidad y procesamiento | El capacidades introduzca los siguientes datos:Clase de capacidad : <001(Máquina/002(Persona)>configurar fórmula : <YBPI01>Fórmula de procesamiento : <YBPI02> | Seleccionar Intro . El Crear recurso Capacidad: Cabecera se visualiza. |  |
| 11 | Configurar capacidad de recursos | En la Capacidad de recursos: Cabecera sección, introduzca los siguientes datos:Descripción de categoría de capacidad : <añada una descripción>Responsable de capacidad : Seleccione F4 para buscar la persona responsable del centro.ID de calendario de fábrica : <Calendario para su país>Versión activa : <1>Unidad base de capacidad. : por ejemplo, DHora de inicio :Hora de fin :Duración de las pausas :Tiempo de operación :Utilización de capacidad : <100>Ctd.cap.indiv. : <10>Relevante para programación finita : <X>Planificación a largo plazo : <X>Se puede utilizar en varias operaciones : <X>Seleccionar Intro . | Seleccionar Intro . La pantalla vuelve al resumen de capacidad. |  |
| 12 | Introducir datos de programación | El Programación introduzca los siguientes datos:Categoría de capacidad : <001(Máquina/002(Persona)>Duración de la preparación : <YBPI01>Duración de procesamiento : <YBPI02> |  |  |
| 13 | Introducir datos de cálculo del coste | El Cálculo de costes introduzca los siguientes datos:Centro de coste : <Centro de coste de Fabricación para su sociedad>Clase de actividad (máquina) : <3>Fórmula (máquina) : <YBPI01>Tipo de actividad - Mano de obra) : <11>Fórm. mano de obra (mano de obra) : <YBPI02>Unidad de actividad : Seleccione la UM necesaria, por ejemplo, H |  |  |
| 14 | Guardar los datos | Guarde las entradas. |  |  |

## Apéndice

### Crear receta de planificación

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Receta de planificación |  |  | Para ejecutar esta actividad, ejecute el script de test Crear receta de planificación (3X9). |

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
- related-to :: [[12-production-and-manufacturing/master-data-script-create-resource-mds-3x8-377]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-379]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-381]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-recurso-mds-3x8-380]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 12,388 chars in the whole document
