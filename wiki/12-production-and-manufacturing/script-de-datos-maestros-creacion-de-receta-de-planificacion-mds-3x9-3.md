---
id: 12-production-and-manufacturing/script-de-datos-maestros-creacion-de-receta-de-planificacion-mds-3x9-3
title: "Script de datos maestros: Creación de receta de planificación - MDS (3X9) (3X9_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish (machine-translated) master data script for scope item 3X9: creating a master recipe in SAP S/4HANA Cloud Public Edition via Fiori app F5426."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X9_S4CLD2608_Master_Data_ES_XX]
keywords: [Process Manufacturing Resources and Master Recipes, master recipe, master recipe creation, process manufacturing, business roles, master data prerequisites, recipe usage key, change management, production version, 3X9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-384
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Creación de receta de planificación - MDS (3X9) (3X9_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de receta de planificación - MDS (3X9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894718)

[2 Requisitos previos 3](#_Toc233894719)

[2.1 Acceso al sistema 3](#_Toc233894720)

[2.2 Roles 3](#_Toc233894721)

[2.3 Unidades organizativas necesarias 3](#_Toc233894722)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894723)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894724)

[2.5.1 Utilización 5](#_Toc233894725)

[3 Tabla de resumen 6](#_Toc233894726)

[4 Procedimientos de prueba 7](#_Toc233894727)

[4.1 Creación de receta de planificación 7](#_Toc233894728)

[5 Apéndice 10](#_Toc233894729)

[5.1 Modificación de receta de planificación con procedimiento de gestión de modificaciones 10](#_Toc233894730)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Puede utilizar la receta de planificación para describir un proceso específico de la empresa en industrias de procesos sin relación con un pedido específico.

Las recetas de planificación se utilizan principalmente para planificar la fabricación de productos. Sin embargo, también puede utilizarlos para describir la limpieza o Cambio de una línea de producción.

Las recetas de planificación se utilizan como referencia para las órdenes de proceso, así como la base para el cálculo del coste del producto.

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
| Ingeniero de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC | Ingeniería de producción - Fabricación por procesos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizativas necesarias

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos de una receta de planificación dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de la receta de planificación pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un maestro Receta.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material |  | Obligatorio | Complete el siguiente script de test como requisito previo antes de ejecutar pasos de proceso:Creación de maestro de productos de tipo "Materia prima" - MDSCreación de maestro de productos de tipo "Producto semielaborado" - MDSCreación de maestro de productos de tipo "Producto terminado" - MDS |
| Recurso | En Crear receta de planificación: resumen de operaciones imagen, seleccione un puesto de trabajo para una operación interna | Obligatorio, (opcional) | Para una operación externa, el puesto de trabajo no es una entrada obligatoria campo.Si es necesario, ejecute el Crear recurso - MDS Test script. |
| Lista de materiales |  | Opcional | Ejecute el Crear lista de materiales para material para producción y ventas - MDS script de test. |
| Registro info de compras |  | (Obligatorio) | Para una operación externa, puede utilizar un registro info de compras para capturar todos los datos relevantes para el suministro |
| Grupo de materiales |  |  |  |
| Clase de coste |  |  |  |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear una receta de planificación.

#### Utilización

| Clave de utilización de hoja de ruta | Descripción |
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
| [Creación de receta de planificación](#unique_10) [página ] 7 | Ingeniero de producción - Fabricación por procesos | Gestión de recetas de planificación (F5426) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de receta de planificación

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación por procesos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de recetas de planificación (F5426) . |  |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | El Crear receta de planificación: Acceso muestra. |  |
| 4 | Configurar la pantalla inicial Crear receta de planificación | El Pantalla inicial Crear receta de planificación , introduzca los siguientes datos:Material : <Material terminado/semielaborado número>Centro : <Su centro número>Perfil : <YPI1>Pulsar Intro . | El Crear detalle de cabecera de receta de planificación se visualiza. |  |
| 5 | Configurar la subpestaña Crear cabecera de receta de planificación | El Crear receta de planificación: Receta introduzca los siguientes datos en la pantalla Receta Cabecera subficha:Utilización : <1 para producción>Estado : <4 liberado-general>Grupo de planificación : <1>Pulsar Intro . |  |  |
| 6 | Añadir una operación | Introduzca los siguientes datos en el campo Operaciones subficha:Recurso : <Recurso>Clave de control : <YBP4>Descripción : <Introduzca un descripción para la operación> .Pulsar Intro . |  |  |
| 7 | Añadir una fase | Empezar en una nueva fila.Introduzca los siguientes datos en el campo Operaciones subficha:Indicador de fase : <X>Operación superior : <ID de operación, por ejemplo, 0010>Recurso : <Recurso>Clave de control : <YBP4>Descripción : <Introduzca un descripción para la operación>.Haga doble clic en la fase que ha creado. | El Crear receta de planificación: Operación se visualiza. |  |
| 8 | Configuración para sección de valor estándar de fase | Introduzca los siguientes datos en el campo Valores estándar subficha y, a continuación, vuelva atrás:Máquina : <Operación de máquina hora>Mano de obra : <Tiempo de trabajo> |  |  |
| 9 | Añadir más operaciones o fase | Repita los pasos anteriores para cada operación o fase.Si desea asignar componentes en este momento, debería continuar los siguientes pasos; de lo contrario, puede grabar sus entradas y salir. |  |  |
| 10 | Seleccionar material | El Crear receta de planificación: Receta seleccione el pulsador Materiales subficha. | El Insertar versión de fabricación se visualiza la ventana de diálogo. |  |
| 11 | Insertar versión de fabricación | En la Insertar versión de fabricación , efectúe las siguientes entradas:Versión de fabricación : <Nueva versión de fabricación>Datos de la lista de materiales – Alternativa de la lista de materiales : <Su AltBOM>Datos de la lista de materiales – Utilización de la lista de materiales : <Utilización>Seleccionar Verificar . Verifique la información relevante y asegúrese de que no exista ningún error y, a continuación, seleccione Cerrar . | El indicador de verificación se muestra en verde para el Datos de lista de materiales sección. |  |
| 12 | Cerrar pantalla y adoptar modificaciones | En la Insertar versión de fabricación ventana de diálogo, seleccionar Cerrar pantalla y adoptar modificaciones . | La lista de materiales se visualiza en Asignaciones de componentes de material en la Materiales subficha. |  |
| 13 | Crear una nueva asignación | Seleccionar Nueva asignación . | El Nueva asignación se visualiza la ventana de diálogo. |  |
| 14 | Asignar a lista oper./act. | Seleccionar Lista oper./act. . |  |  |
| 15 | Seleccionar operación | Seleccione una operación y pulse Intro . |  |  |
| 16 | Asignar otros componentes | Repita los pasos anteriores para otros componentes. |  |  |
| 17 | Guardar los datos | Guarde las entradas. | Se ha creado la receta de planificación. |  |
| 18 | Imprimir (opcional) | Dentro de la Gestión de recetas de planificación (F5426) la aplicación, busque y seleccione la receta de planificación que acaba de creado.El Visualizar receta de planificación: Receta , seleccione Menú > Detalles > Imprimir receta de planificación . | Se descarga un archivo PDF que contiene los detalles de la receta de planificación. |  |

## Apéndice

### Modificación de receta de planificación con procedimiento de gestión de modificaciones

Si utiliza la receta de planificación que requiere autorización, puede consultar el script de test del elemento de alcance 5QC - Gestión de modificaciones de productos con registros de modificaciones – Industrias de proceso , y siga el capítulo Modificar receta de planificación para cualquier cambio.

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
- related-to :: [[12-production-and-manufacturing/create-master-recipe-mds-3x9-383]]
- related-to :: [[12-production-and-manufacturing/criar-receita-mestre-mds-3x9-386]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-385]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-387]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 14,090 chars in the whole document
