---
id: 12-production-and-manufacturing/script-de-datos-maestros-crear-hoja-de-ruta-estandar-mds-ble-576
title: Script de datos maestros - Crear hoja de ruta estándar - MDS (BLE) (BLE_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script BLE: create a reference (standard) routing with transaction CA11."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BLE_S4CLD2608_Master_Data_ES_XX]
keywords: [Routings and Reference Operation Sets, reference routing, routing operations, work centers, control keys, work center usage, plant organizational data, business roles, master data scripts, BLE]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-576
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear hoja de ruta estándar - MDS (BLE) (BLE_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear hoja de ruta estándar - MDS (BLE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894888)

[2 Requisitos previos 3](#_Toc233894889)

[2.1 Acceso al sistema 3](#_Toc233894890)

[2.2 Roles 3](#_Toc233894891)

[2.3 Unidades organizativas necesarias 3](#_Toc233894892)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894893)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894894)

[2.5.1 Utilización 4](#_Toc233894895)

[3 Tabla de resumen 5](#_Toc233894896)

[4 Procedimientos de prueba 6](#_Toc233894897)

[4.1 Creación de hoja de ruta de referencia 6](#_Toc233894898)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este proceso describe cómo crear una hoja de ruta estándar.

Una hoja de ruta estándar tiene la misma estructura que una hoja de ruta. No puede asignar un material a fabricar a una operación de referencia set. No puede tener secuencias paralelas ni alternativas.

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
| Todos los datos | Centro |  | Todos los datos de una hoja de ruta estándar dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de hoja de ruta de referencia pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en una Referencia hoja de ruta.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material |  | Obligatorio | Complete el siguiente script de test como requisito previo antes de ejecutar pasos de proceso:Creación de maestro de productos de tipo "Materia prima" - MDS (BNR)Creación de maestro de productos de tipo "Producto semielaborado" - MDS (BNS)Creación de maestro de productos de tipo "Producto terminado" - MDS (BNT) |
| Puesto de trabajo | En Crear operación de referencia: resumen de operaciones , seleccione un Puesto de trabajo para una operación interna | Obligatorio, (opcional) | Para una operación externa, el puesto de trabajo no es una entrada obligatoria campo.Si es necesario, ejecute el Crear hoja de ruta estándar - MDS Ensayo (BLE) script. |
| Lista de materiales |  | Opcional | Ejecute el Crear lista de materiales para material para producción y ventas - MDS (BNK) script de test. |
| Registro info de compras |  | (Obligatorio) | Para una operación externa, puede utilizar un registro info de compras para capturar todos los datos relevantes para el suministro |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear una hoja de ruta de referencia:

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
| [Creación de hoja de ruta de referencia](#unique_10) [página ] 6 | Ingeniero de producción - Fabricación discreta | Crear hoja de ruta de referencia (CA11) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de hoja de ruta de referencia

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
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear hoja de ruta de referencia (CA11) . | El Crear hoja de ruta estándar: Acceso es visualizado.. |  |
| 3 | Configurar Crear hoja de ruta estándar inicial Pantalla | El Pantalla inicial Crear hoja de ruta estándar , introduzca el datos.Seleccionar Intro . | El Crear detalles de cabecera de hoja de ruta estándar aparece. |  |
| 4 | Configurar la cabecera de la hoja de ruta estándar Imagen detallada | Indique los siguientes datos en el campo Crear referencia Hoja de ruta estándar: Detalles de cabecera vista:Contador de grupos de hojas de ruta : <1>Centro : <su centro>Utilización : <1 para producción>Estado : <4 liberado-general>De tamaño de lote - a tamaño de lote : <Introducir tamaño de lote intervalo y unidad de medida> |  |  |
| 5 | Configurar Crear hoja de ruta estándar: Operación Resumen | Seleccionar Operación y el Crear Hoja de ruta estándar: Resumen de operaciones Pantalla aparece.Introduzca los siguientes datos en el campo Crear operación de hoja de ruta estándar resumen pantalla.Puesto de trabajo : necesarios para las operaciones internas, (espacio en blanco) para operaciones externasClave de control : <YBP1/YBP2/YBP3/YBP5/YBRW>YBP1 para operación interna sin entrada de mercancías automáticaYBP2 para operación externa (subcontratación PP)YBP3 para operación interna con entrada de mercancías automáticaYBP5 para hito de fabricación por procesosDescripción : <Introduzca una descripción para el operación>A continuación, haga doble clic en la operación introducida. |  |  |
| 6 | Sección Configuración de operación para valor estándar | Introduzca los siguientes datos en el campo Crear referencia Detalles de operación de conjunto de operaciones pantalla.Configuración : <tiempo de preparación>Máquina : <Operación de máquina hora>Mano de obra : <tiempo de mano de obra> |  |  |
| 7 | Añadir más operaciones | Repita los pasos anteriores para cada operación. |  |  |
| 8 | Guardar los datos | Guarde las entradas. | Se ha creado la hoja de ruta estándar. |  |

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
- related-to :: [[12-production-and-manufacturing/master-data-script-create-reference-operation-set-mds-ble-575]]
- related-to :: [[12-production-and-manufacturing/mds-ble-577]]
- related-to :: [[12-production-and-manufacturing/mds-ble-579]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-conjunto-de-operacoes-de-referencia-mds-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 11,463 chars in the whole document
