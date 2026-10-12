---
id: 12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630
title: Creación de hoja de ruta - MDS (BNL) (BNL_S4CLD2608_Master_Data_ES_XX)
description: Spanish machine-translated SAP S/4HANA Cloud 2608 master data script (BNL) for creating a production routing (hoja de ruta) with operations and component assignment in discrete manufacturing.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_ES_XX]
keywords: [Routings and Reference Operation Sets, routing, production operations, control keys, component assignment, work centers, external processing, task list usage, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-630
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Creación de hoja de ruta - MDS (BNL) (BNL_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de hoja de ruta - MDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894967)

[2 Requisitos previos 3](#_Toc233894968)

[2.1 Acceso al sistema 3](#_Toc233894969)

[2.2 Roles 3](#_Toc233894970)

[2.3 Unidades organizativas necesarias 3](#_Toc233894971)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894972)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894973)

[2.5.1 Utilización 5](#_Toc233894974)

[3 Tabla de resumen 6](#_Toc233894975)

[4 Procedimientos de prueba 7](#_Toc233894976)

[4.1 Creación de hoja de ruta 7](#_Toc233894977)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Una hoja de ruta de producción define el proceso de producción para un material. Contiene el operaciones o pasos de trabajo que se llevarán a cabo durante la producción. Define el uso de materiales y puestos de trabajo. Forma un modelo para una orden de fabricación y es la base para el cálculo del coste del producto.

Se define una hoja de ruta para un producto terminado o semielaborado y es específica de un centro de producción (conocido como centro). Se aplica a un tamaño de lote determinado y consta de un número de operaciones con cada una asignada a un puesto de trabajo.

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
| Todos los datos | Centro |  | Todos los datos de una hoja de ruta dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de hoja de ruta pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se deben utilizar en una hoja de ruta.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material |  | Obligatorio | Complete el siguiente script de test como requisito previo antes de ejecutar pasos de proceso:Creación de maestro de productos de tipo "Materia prima" - MDS (BNR)Creación de maestro de productos de tipo "Producto semielaborado" - MDS (BNS)Creación de maestro de productos de tipo "Producto terminado" - MDS (BNT) |
| Puesto de trabajo | En Crear hoja de ruta: resumen de operación pantalla, Seleccione un puesto de trabajo para una operación interna | Obligatorio, (opcional) | Para una operación externa, el puesto de trabajo no es una entrada obligatoria campo.Si es necesario, ejecute el Crear hoja de ruta - MDS (BNL) script de test. |
| Lista de materiales |  | Opcional | Ejecute el Crear lista de materiales para material para producción y ventas - MDS (BNK) Script de test. |
| Registro info de compras |  | (Obligatorio) | Para una operación externa, puede utilizar un registro info de compras para capturar todos los datos relevantes para el suministro |
| Grupo de materiales |  |  |  |
| Clase de coste |  |  |  |

### Parámetros principales para la creación de datos

En esta sección se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear una hoja de ruta:

#### Utilización

| Clase de puesto de trabajo | Descripción |
| --- | --- |
| 1 | Producción |
| 2 | Ingeniería/Diseño |
| 3 | Universal |

## Tabla de resumen

Este elemento de alcance consta del paso del proceso enumerado en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de hoja de ruta](#unique_10) [página ] 7 | Ingeniero de producción - Fabricación discreta | Gestión de hojas de ruta (F5425) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de hoja de ruta

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de hojas de ruta (F5425) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | Se abre una ventana nueva en la que se muestra Crear hoja de ruta pantalla. |  |
| 4 | Configurar la pantalla Crear hoja de ruta | Introduzca los siguientes datos en el campo Crear hoja de ruta pantalla:Material : <Material terminado/semielaborado número>Centro : <Su número de centro>Seleccionar Continuar . | El Crear hoja de ruta: Detalles de cabecera se visualiza. |  |
| 5 | Configurar la pantalla Crear hoja de ruta: Detalles de cabecera | Introduzca los siguientes datos en el campo Crear hoja de ruta: Detalles de cabecera pantalla:Utilización : <1 para producción>Estado : <4 liberado-general>De tamaño de lote - a tamaño de lote : <Introduzca el intervalo de tamaño de lote y la unidad de medida> |  |  |
| 6 | Configurar la pantalla Crear hoja de ruta: Resumen de operaciones | Seleccionar Operación y el Crear hoja de ruta: Pantalla de resumen de operación muestra.Introduzca los siguientes datos en el campo Crear hoja de ruta: Pantalla de resumen de operación :Puesto de trabajo : necesario para operaciones internas, (en blanco) para operaciones externasClave de control : <YBP1/YBP2/YBP3/YBP5>YBP1 para operación interna sin entrada de mercancías automáticaYBP2 para operación externa (subcontratación PP)YBP3 para operación interna con entrada de mercancías automáticaYBP4 para hito de fabricación por procesosDescripción : <Introduzca un descripción para la operación>A continuación, haga doble clic en la operación introducida. |  |  |
| 7 | Configuración de operación externa para la sección Procesamiento externo | Introduzca los siguientes datos en el campo Crear hoja de ruta: Detalles de operación pantalla:Registro info de compras : obligatorio para operaciones internas, (en blanco) para operaciones operacionesGrupo de artículos : L002/L003Clase de coste : <clase de coste relevante para su país>Organización de compras : <organización de compras> . |  |  |
| 8 | Configuración de operación interna para sección de valor estándar | Introduzca los siguientes datos en el campo Crear detalles de operación de hoja de ruta pantalla:Configuración : <tiempo de preparación>Máquina : <Tiempo de operación de máquina>Mano de obra : <tiempo de mano de obra> |  |  |
| 9 | Añadir más operaciones | Repita los pasos anteriores para cada operación. |  |  |
| 10 | Seleccionar un componente | Seleccionar Asignación de componentes desde la parte superior de la vista y, a continuación, seleccione un componente. | El Resumen de componentes de material se visualiza. |  |
| 11 | Crear una nueva asignación | Seleccionar Nueva asignación . | A Nueva asignación se visualiza la ventana de diálogo. |  |
| 12 | Asignar a lista oper./act. | Seleccionar Lista oper./act. . |  |  |
| 13 | Seleccionar operación | Seleccione una operación y pulse Intro . |  |  |
| 14 | Asignar otros componentes | Repita los pasos anteriores para otros componentes. |  |  |
| 15 | Guardar los datos | Guarde las entradas. | Se ha creado la hoja de ruta. |  |

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
> Flagged while digesting this document, not verified: Control key list in step 6 names YBP1/YBP2/YBP3/YBP5 but the explanation lists YBP4 (process manufacturing milestone) and no YBP5; the step 7 text also says the purchasing info record is mandatory for internal operations, contradicting the prerequisite table (external operations).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]
- related-to :: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]
- related-to :: [[12-production-and-manufacturing/mds-bnl-631]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 12,807 chars in the whole document
