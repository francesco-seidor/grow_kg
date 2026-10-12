---
id: 11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-area-de-suministro-de-produccion-m
title: Script de datos maestros - Actualizar área de suministro de producción - MDS (3KS) (3KS_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script (3KS): optionally assigning bin locations to production supply areas (PSA) in warehouse management."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_ES_XX]
keywords: [EWM Production Supply and Receipt, production supply area, storage bin assignment, master data scripts, warehouse production integration, kanban supply, control cycle, business roles, business partner, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-342
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Actualizar área de suministro de producción - MDS (3KS) (3KS_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Actualizar área de suministro de producción - MDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894619)

[2 Requisitos previos 3](#_Toc233894620)

[2.1 Acceso al sistema 3](#_Toc233894621)

[2.2 Roles 3](#_Toc233894622)

[2.3 Unidades organizativas necesarias 3](#_Toc233894623)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894624)

[2.5 Condiciones empresariales 4](#_Toc233894625)

[3 Tabla de resumen 5](#_Toc233894626)

[4 Procedimientos de prueba 6](#_Toc233894627)

[4.1 (OPCIONAL) Asignar ubicación a ASP - Almacén 6](#_Toc233894628)

[4.2 (OPCIONAL) Asignar ubicación a ASP 7](#_Toc233894629)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, puede aprender a realizar las siguientes actividades para crear un almacén. datos maestros para el suministro de producción:

- [(OPCIONAL) Asignar ubicación a ASP - Almacén](#unique_2) [página ] 6
- [(OPCIONAL) Asignar ubicación a ASP](#unique_3) [página ] 7

La creación y replicación del área de suministro de producción, así como la asignación de ubicación a ASP se supone que se realizan mediante la ejecución de pasos relevantes en el script de datos maestros o documentos de script de test mencionados en el Condición empresarial capítulo. Estos datos maestros El script es solo para que los clientes verifiquen las parametrizaciones relevantes y creen parametrizaciones manualmente en caso de que no se cumplan las condiciones empresariales.

La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema normal. Principalmente aprende qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance de SAP S/4HANA La entrega de contenido de SAP Best Practices no se describe en este documento aunque puede que aparezca en la IU.

Utilice estos datos maestros para los procesos empresariales de integración de producción en Gestión de almacenes.

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

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de un unidad organizativa o sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todo | Número de almacén |  |  |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen del maestro opcional y obligatorio objetos de datos que se deben utilizar al crear una asignación de ubicación al registro de datos maestros ASP.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Interlocutor comercial | Asignar ubicación a ASP - Almacén | Obligatorio | Interlocutor comercial como persona autorizada a disponer para el almacén. |
| Área de suministro de producción | Asignar ubicación a ASP - Almacén | Obligatorio | El área de suministro de producción que se crea en SAP S/4HANA. Consulte el capítulo Condición empresarial. |
| Producto | Asignar ubicación a ASP - Almacén | Obligatorio |  |
| Ubicación | Asignar ubicación a ASP - Almacén | Obligatorio |  |

### Condiciones empresariales

Antes de poder probar este elemento de alcance, se deben cumplir las siguientes condiciones empresariales.

| ID de elemento de alcance | Condición empresarial |
| --- | --- |
| 40D: Creación de área de suministro de producción - MDS | Este script de datos maestros es el requisito previo de este documento.Al crear el área de suministro de producción (ASP), utilice el almacén WM en la nube, por ejemplo, 105W .Después de ejecutar este script de datos maestros, ha creado las siguientes opciones:El área de suministro de producción se crea en SAP S/4HANA.El área de suministro de producción relevante se replica automáticamente de SAP S/4HANA a la nube Almacén. |
| 3DV: Integración de producción de almacén | El requisito previo de este documento es el paso Crear ciclo de control en el capítulo Pasos preliminares del test 3DV. script.Después de ejecutar el paso Crear ciclo de control, ha creado las siguientes opciones:El área de suministro de producción relevante se replica automáticamente desde SAP S/4HANA al almacén en la nube.La ubicación está asignada al ASP. |
| 3VT - Suministro kanban de almacén a producción | El requisito previo para este documento es el paso Ciclo de control para kanban: Traslado de stock en el capítulo Pasos preliminares del test 3VT. script.Después de ejecutar el paso Ciclo de control para kanban: Traslado de stock, ha creado lo siguiente: Opciones:El área de suministro de producción relevante se replica automáticamente desde SAP S/4HANA al almacén en la nube.La ubicación está asignada al ASP. |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [(OPCIONAL) Asignar ubicación a ASP - Almacén](#unique_2) [página ] 6 | Jefe de almacén (EWM) | Asignar ubicación a ASP - Almacén (/SCWM/PSASTAGE) | Se crea la asignación de la ubicación a ASP. |
| [(OPCIONAL) Asignar ubicación a ASP](#unique_3) [página ] 7 | Jefe de almacén (EWM) | Asignar ubicación a ASP (/SCWM/PSASTAGE2) | Se crea la asignación de la ubicación a ASP. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### (OPCIONAL) Asignar ubicación a ASP - Almacén

Objetivo

En esta sección se gestionan las asignaciones de ubicación de todas las áreas de suministro de producción del número de almacén en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Este paso es opcional y puede omitirlo si la ubicación se ha asignado a la ASP como estaba previsto. Solo es necesario si aún no se han realizado asignaciones de ubicación para su ASP durante el paso de creación del ciclo de control. Consulte el paso "Crear ciclo de control" en el capítulo Condición empresarial.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Asignar ubicación a ASP - Almacén (/SCWM/PSASTAGE) . |  |  |
| 3 | Crear entrada nueva | El Modificar vista "Asignar ubicación a ASP": Resumen , seleccione Entradas nuevas . |  |  |
| 4 | Introducir valores de asignación | El Entradas nuevas: Detalles de entradas añadidas introduzca los siguientes datos:Eliminación : <ID de interlocutor comercial para la parte autorizada a disponer>Área de suministro : <Área de suministro de producción>Producto : <ID de producto>Ubicación : <ID de ubicación> |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que se ha grabado la asignación de la ubicación a la ASP. |  |

### (OPCIONAL) Asignar ubicación a ASP

Objetivo

En esta sección se gestionan todas las asignaciones de ubicación dentro de un área de suministro de producción concreta en SAP S/4HANA mediante la rampa de lanzamiento SAP Fiori.

Este paso es opcional y puede omitirlo si la ubicación se ha asignado a la ASP como estaba previsto. Solo es necesario si aún no se han realizado asignaciones de ubicación para su ASP durante el paso de creación del ciclo de control. Consulte el paso "Crear ciclo de control" en el capítulo Condición empresarial.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Jefe de almacén (EWM) . |  |  |
| 2 | Acceder a la aplicación | Abierto Asignar ubicación a ASP (/SCWM/PSASTAGE2) . |  |  |
| 3 | Determinar área de trabajo | El Determinar entrada de área de trabajo introduzca los siguientes datos:Persona autorizada a disponer : <ID de interlocutor comercial para la parte autorizada a disponer>Área de suministro : <Área de suministro de producción>Seleccionar Continuar . |  |  |
| 4 | Crear entrada nueva | El Modificar vista "Asignar ubicación a ASP": Resumen , seleccione Entradas nuevas . |  |  |
| 5 | Introducir valores de asignación | El Entradas nuevas: Detalles de entradas añadidas introduzca los siguientes datos:Producto : <ID de producto>Ubicación : <ID de ubicación> |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | Un mensaje del sistema le indica que se ha grabado la asignación de la ubicación a la ASP. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 13,688 chars in the whole document
