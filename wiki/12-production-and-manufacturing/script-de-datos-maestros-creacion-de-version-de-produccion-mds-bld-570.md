---
id: 12-production-and-manufacturing/script-de-datos-maestros-creacion-de-version-de-produccion-mds-bld-570
title: "Script de datos maestros: Creación de versión de producción - MDS (BLD) (BLD_S4CLD2608_Master_Data_ES_XX)"
description: Spanish (machine-translated) master data script for creating and editing production versions in SAP S/4HANA Cloud Public Edition via Fiori apps F6400 and F2568.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_ES_XX]
keywords: [Production Versions, create production version, edit production version, bill of materials, routings, material master, business roles, master data scripts, plant organizational unit, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-570
topic: 12-production-and-manufacturing/production-versions
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Creación de versión de producción - MDS (BLD) (BLD_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de versión de producción - MDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894914)

[2 Requisitos previos 3](#_Toc233894915)

[2.1 Acceso al sistema 3](#_Toc233894916)

[2.2 Roles 3](#_Toc233894917)

[2.3 Unidades organizativas necesarias 3](#_Toc233894918)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894919)

[3 Tabla de resumen 5](#_Toc233894920)

[4 Procedimientos de prueba 6](#_Toc233894921)

[4.1 Crear versión de fabricación 6](#_Toc233894922)

[4.2 Editar versión de fabricación (opcional) 9](#_Toc233894923)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Crear versión de fabricación

En este documento encontrará una descripción de cómo crear una versión de fabricación para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye los segmentos de datos que son relevantes para el SAP S/4HANA Cloud Public Edición aplicación. Campos que no son relevantes para alcance de SAP S/4HANA Cloud Public Edición no se describen en este documento.

Una versión de fabricación que se crea como se describe aquí se puede utilizar para el procesamiento procesos de producción.

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
| Ingeniero de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC | Ingeniería de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizativas necesarias

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos para la versión de fabricación dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de la versión de fabricación pueden hacer referencia a otros datos maestros . El La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios utilizado en una versión de fabricación.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material | La versión de fabricación se crea para cada material y centro. | Obligatorio | El Versión de fabricación: Procesamiento en masa pantalla, Material debe introducirse.Para la creación de material, puede seguir los pasos del script de datos maestros: Creación de maestro de productos de tipo "Materia prima" - MDS - BNR , Creación de maestro de productos de tipo "Producto semielaborado" - MDS - BNS , o Creación de maestro de productos de tipo "Producto terminado" - MDS - BNT . |
| Lista de materiales | Los datos maestros de la lista de materiales para el material se asignan en una producción versión | Obligatorio | El Versión de fabricación: Procesamiento en masa pantalla, Lista de materiales alternativa y Utilización de lista de materiales deben introducirse.Para crear una lista de materiales, puede seguir los pasos del script de datos maestros: Crear lista de materiales para material para producción y ventas - MDS - BNK . |
| Hoja de ruta | Se asigna una lista de tomas para el material en una versión de fabricación | Obligatorio | El Versión de fabricación: Procesamiento en masa pantalla, Tipo de hoja de ruta , Grupo , y Contador de grupos de hojas de ruta deben introducirse.Para crear una lista de tareas, puede seguir los pasos del script de datos maestros: Crear hoja de ruta - MDS - BNL o bien Crear receta de planificación - MDS - 3X9 . |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear versión de fabricación](#unique_8) [página ] 6 | Ingeniero de producción - Fabricación discreta o bien Ingeniero de producción - Fabricación por procesos | Procesar versiones de fabricación (F6400) o bien Gestionar versiones de fabricación (F2568) |  |
| [Editar versión de fabricación (opcional)](#unique_9) [página ] 9 | Ingeniero de producción - Fabricación discreta o bien Ingeniero de producción - Fabricación por procesos | Procesar versiones de fabricación (F6400) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear versión de fabricación

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

Es posible realizar este paso con diferentes aplicaciones SAP Fiori. Hay 3 opciones que puede aprovechar. Puede seleccionar una de ellas.

Opción 1

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta o un Ingeniero de producción - Fabricación por procesos . | El Iniciar se visualiza. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Procesar versiones de fabricación (F6400) . | Se abre la aplicación. |  |
| 3 | Indicar campos de selección | Realice las siguientes entradas y seleccione Ir :Material : <Introducir número de material>Centro : <Introducir centro> |  |  |
| 4 | Verificar propuestas de versión de fabricación | El Propuestas de versión de fabricación puede encontrar las propuestas para crear una nueva versión de fabricación si la La combinación de lista de materiales/hoja de ruta correspondiente aún no existe.Puede revisar los detalles de la propuesta seleccionando la propuesta y realizando posibles modificaciones. | Nota Se ha introducido el paso de configuración (ID: 105965) para configurar las reglas para la propuesta de versión de fabricación. |  |
| 5 | Aceptar propuesta | Marque la propuesta de versión de fabricación y seleccione Aceptar propuesta . |  |  |
| 6 | Confirmación | En la Confirmación ventana de diálogo, seleccione OK . | Se crea una nueva versión de fabricación basada en los parámetros propuestos. Puede encontrarlo en Producción existente Versiones pestaña. |  |

Opción 2

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta o un Ingeniero de producción - Fabricación por procesos . | El Iniciar se visualiza. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Procesar versiones de fabricación (F6400) . | Se abre la aplicación. |  |
| 3 | Indicar campos de selección | Realice las siguientes entradas y seleccione Ir :Material : <Introducir número de material>Centro : <Introducir centro> |  |  |
| 4 | Seleccionar etiqueta | Seleccione el Versiones de fabricación existentes pestaña. |  |  |
| 5 | Crear | Seleccionar Crear . En la Crear versión de fabricación , realice las siguientes entradas y seleccionar Crear :Material : <Introducir número de material>Centro : <Introducir centro>Versión de fabricación : <Un número de 4 dígitos>Descripción de versión de fabricación : <Descripción> |  |  |
| 6 | Parámetros de entrada | Introduzca los parámetros necesarios y seleccione Crear :Fecha de inicio de validez : <hoy>Fecha de fin de validez : <31/12/9999>Tamaño de lote mínimo : <1>Tamaño de lote máximo : <999999999>Hoja de ruta sección:Tipo de hoja de ruta : <Seleccione el tipo de hoja de ruta para el material>Grupo de hojas de ruta : <Seleccione el grupo para el material>Contador de hojas de ruta : <Seleccione el contador de grupos de hojas de ruta para el material>Lista de materiales sección:Lista de materiales alternativa : <Seleccione la alternativa de la lista de materiales para el material>Utilización de lista de materiales : <Seleccione la utilización de la lista de materiales del maestro de listas de materiales para el material> | Se crea la versión de fabricación. |  |

Opción 3

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta o un Ingeniero de producción - Fabricación por procesos . | El Iniciar se visualiza. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar versiones de fabricación (F2568) . | El Versión de fabricación: Tratamiento en masa se visualiza. |  |
| 3 | Introducir código de centro | Intro Código de centro . |  |  |
| 4 | Introducir material | Intro Material .Pulsar Intro . |  |  |
| 5 | Versión de fabricación | Introduzca las partidas individuales de la versión de fabricación y pulse Intro .Material : <Introducir material número>Versión de fabricación : <A 4 Número de dígito>Inicio de validez : <hoy>Válido hasta : <31/12/9999>De tamaño de lote : <1>A tamaño de lote : <999999999>Lista de materiales alternativa : Pulse F4 para elegir Lista de materiales alternativa para el materialUtilización de lista de materiales : Pulse F4 seleccionar Lista de materiales uso del maestro de listas de materiales para el materialGrupo : <Introduzca el grupo para el material>Contador de grupos de hojas de ruta : <Introduzca el Contador de grupos de hojas de ruta para el material>Tipo : <Seleccione el tipo de hoja de ruta para el material> |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | Se crea la versión de fabricación. |  |

### Editar versión de fabricación (opcional)

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta o un Ingeniero de producción - Fabricación por procesos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Procesar versiones de fabricación (F6400) . | Se abre la aplicación. |  |
| 3 | Indicar campos de selección | Realice las siguientes entradas y seleccione Ir :Material : <Introducir número de material>Centro : <Introducir centro> |  |  |
| 4 | Navegar a la pestaña Versiones de fabricación existentes | Vaya a Versiones de fabricación existentes pestaña. |  |  |
| 5 | Editar versión de producción | Seleccione la versión de fabricación que desea modificar y seleccione Editar en la Producción Versión pantalla.Realice las modificaciones necesarias en los campos en función de sus necesidades.Nota Si desea realizar modificaciones similares en varias versiones de fabricación, puede realizar una selección múltiple en el Versiones de fabricación existentes y seleccione Edición en masa .En la Edición en masa puede realizar las modificaciones necesarias en los campos enumerados. |  |  |
| 6 | Grabar | Seleccionar Grabar . | La versión de fabricación se ha actualizado correctamente. |  |

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
- related-to :: [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569]]
- related-to :: [[12-production-and-manufacturing/mds-bld-571]]
- related-to :: [[12-production-and-manufacturing/mds-bld-573]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 16,598 chars in the whole document
