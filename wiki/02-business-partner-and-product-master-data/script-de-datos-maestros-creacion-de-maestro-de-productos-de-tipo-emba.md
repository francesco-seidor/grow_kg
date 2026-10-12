---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-emba
title: "Script de datos maestros - Creación de maestro de productos de tipo \"Embalaje\" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_ES_XX)"
description: "SAP S/4HANA Cloud Public Edition master data script (3Y1, Spanish) for creating a packaging material master: basic, sales and WM views via MM01/MM02/F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [3Y1_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", packaging material master, master data scripts, basic data view, sales data view, warehouse management data, manage product master data, material types, number ranges, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-390
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos de tipo "Embalaje" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Embalaje" - MDS (3Y1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894690)

[2 Requisitos previos 3](#_Toc233894691)

[2.1 Acceso al sistema 3](#_Toc233894692)

[2.2 Roles 3](#_Toc233894693)

[2.3 Unidades organizativas necesarias 3](#_Toc233894694)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894695)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894696)

[2.5.1 Tipo de material y rangos de números 4](#_Toc233894697)

[2.5.2 Ramo 5](#_Toc233894698)

[3 Tabla de resumen 6](#_Toc233894699)

[4 Procedimientos 7](#_Toc233894700)

[4.1 Crear datos maestros de material - Vista básica 7](#_Toc233894701)

[4.2 Crear datos maestros de material - Vista de ventas 9](#_Toc233894702)

[4.3 Actualizar datos maestros de material - Vista WM 12](#_Toc233894703)

[5 Apéndice 14](#_Toc233894704)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este script de datos maestros proporciona procedimientos para crear un maestro de material de embalaje/producto utilizado por los elementos de alcance de Gestión de almacenes.

Este documento proporciona un procedimiento detallado para probar este elemento de alcance después de la activación de la solución, reflejando el alcance predefinido de la solución. Cada paso, informe o posición de proceso se trata en su propia sección, proporcionando las interacciones del sistema (pasos de test) en una vista de tabla. Los pasos que no están dentro del alcance del proceso pero que son necesarios para las pruebas se marcan en consecuencia. Deben añadirse pasos específicos del proyecto.

|  |
| --- |
| Nota Los valores en este script de test (notación decimal, formatos de fecha, etc.) se presentan en la notación estándar de EE. UU. Si su sistema de prueba está configurado para utilizar una notación diferente, introduzca valores según corresponda. |

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Unidad de medida baseGrupo de materiales, etc. . |  | n/d |
| Datos de ventas | Independiente de las unidades organizativas | Grupo de transporte, tipo de material de embalaje,Peso embalaje perm.,Volumen de embalaje permitido, etc. |  | n/d |
| Datos WM | Independiente de las unidades organizativas | Tipo de unidad de manipulaciónTipo UMp estándar |  | n/d |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un registro de datos maestros de embalaje.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Unidad de medida base | Datos básicos | Obligatorio |  |

|  |
| --- |
| Nota Los campos específicos de Brasil son necesarios para obtener un cálculo de impuestos adecuado. Verifique la Definir BR Campos específicos para datos maestros capítulo para datos maestros de material en el Crear datos maestros para Brasil (JD0_BR). |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son siempre obligatorio para crear datos maestros de embalaje registro:

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizados o qué campos son obligatorios u opcionales. En función de los tipos de material, el el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos Los tipos de material utilizan la misma definición de rango de números.

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A - ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe tener más de 40 caracteres. |
| Numérico interno | 1–99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un número numérico a un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M .

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| Crear datos maestros de material - Vista básica | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos básicos. |
| Crear datos maestros de material - Vista de ventas | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de ventas. |
| Actualizar datos maestros de material - Vista WM | Especialista en datos maestros - Datos de producto | Modificar material (MM02) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos WM. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear datos maestros de material - Vista básica

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Rampa de lanzamiento SAP Fiori aparece. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (pantalla inicial) aparece. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Material número>Tipo de material : Embalaje | El Seleccionar vista(s) Aparece la pantalla. |  |
| 4 | Elija Seleccionar vista(s) | Seleccionar Seleccione Vista(s). | El Seleccionar vista(s) aparece la ventana de diálogo. |  |
| 5 | Seleccionar vistas | En Seleccionar vista(s) seleccione la ventana de diálogo Datos básicos 1 y la casilla de selección Datos básicos 2 casilla de selección. Seleccionar Continuar (Intro) . | El Crear material <su número de material> (Embalaje), Aparece la pantalla |  |
| 6 | Introducir datos básicos | El Crear material > su número de material > (Embalaje) , efectúe las siguientes entradas:Descr.: <su descripción de material> |  |  |
| 7 | Introducir datos básicos | El Datos básicos 1 en la pestaña Datos generales la sección, haga siguientes entradas:Unidad de medida base: <UM> por ejemplo, UNGr.tp.pos.gen.: VERP |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN , realice las siguientes entradas:Peso bruto: por ejemplo, 20Unidad de peso: por ejemplo, KGPeso neto: por ejemplo, 15Volumen: por ejemplo, 138Unidad de volumen: por ejemplo, CD3Seleccionar Intro . | Una vez completada la entrada, pase a la siguiente pestaña, Datos básicos 2 . |  |
| 8 | Completar datos básicos | No se requieren entradas para el Datos básicos 2 vista. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto (F1602) pantalla muestra. |  |
| 3 | Seleccione Crear nuevo maestro de productos. | El Gestionar datos maestros de producto (F1602) , seleccione Crear y seleccione Producto . | El Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir datos para campos obligatorios | El Crear registro de datos maestros , efectúe las siguientes entradas:Número de producto : por ejemplo, Z …Puede introducir cualquier valor externo ID alfanumérico y ese ID debe empezar por un ID alfanumérico carácter. Si no proporciona ninguna entrada, el sistema automáticamente asigna un ID numérico.Para obtener más información sobre el número de producto, consulte el tipo de material y los rangos de números anteriores sección.Tipo de producto : VERPUnidad base : por ejemplo, UNDescripción : <cualquiera descripción>Seleccionar OK . |  |  |
| 5 | Introducir datos básicos | El Información general etiqueta, realice la siguiente entrada:En Básico Datos sección:Sector : por ejemplo, 00Seleccionar Mostrar más y hacer lo siguiente entrada:Grupo de tipos de posición general : VERP |  |  |
| 6 | Introducir datos de descripciones | En la Descripciones sección, seleccione Crear y hacer lo siguiente entradas:Idioma : por ejemplo, DEDescripción de producto : <su descripción> |  |  |
| 7 | Seleccionar unidad de medida base | En la Unidades de medida base sección, seleccionar Mostrar más para introducir el accesorio de venta datos. |  |  |
| 8 | Introducir otros datos de indicador | En la Peso , realice las siguientes entradas:Peso bruto : por ejemplo, 20 kgPeso neto : por ejemplo, 15 kgEn la Volumen , realice la siguiente entrada:Volumen: por ejemplo, 138 CD3 |  |  |
| 9 | Guardar los datos | Seleccionar Crear . | Aparece un mensaje del sistema que indica que el objeto se ha grabado. |  |

### Crear datos maestros de material - Vista de ventas

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, Creación de datos maestros de material - Datos básicos, antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

|  |
| --- |
| Nota Debido a la restricción de rendimiento en la aplicación Gestionar datos maestros de producto, no todos los campos se pueden ver y editar. Si encuentra algún campo que faltan, seleccione la opción 1 para crear el material o puede añadir estos campos en la aplicación Gestionar datos maestros de producto mediante la directriz en Adaptación de IU de SAP Fiori en tiempo de ejecución - Adaptación de usuario clave \| SAP Help Portal |

Procedimiento: Opción 1 - Crear material

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material (MM01) . | Crear material (vista inicial) muestra. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) efectúe las entradas siguientes:Material : <Número de material> Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena en la oscuridad.Tipo de material : EmbalajeSeleccionar Seleccionar Vista(s) . | Después de completar las entradas, se abre una nueva pantalla, Seleccionar vista(s) . |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Ventas: Datos generales/de centro y seleccione Continuar .Nota Solo para Polonia: Seleccione también Comercio exterior: Datos de exportación para ingresar al PKWiU número de clasificación. | Una pantalla con Niveles de organización muestra. |  |
| 4 | Seleccione Continuar. | El Niveles de organización en la pantalla Nivel de organización sección, hacer no introducir datos para centro, organización de ventas y canal de distribuciónSeleccionar Continuar .La siguiente información aparece en la parte inferior de la vista: El material ya existe y se ampliado .pSolo para Polonia: si ha seleccionado Comercio exterior: Datos de exportación , seleccionar Centro . |  |  |
| 5 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos de expedición (tiempos en días) la sección, haga entrada siguiente:Gpo.transp. : 0001 |  |  |
| 6 | Introducir datos de material de embalaje | En la Datos de material de embalaje sección, hacer las siguientes entradas:Tipo mat.embalajePeso embalaje perm.Tolerancia de exceso de pesoVolumen embalaje perm.Tolerancia vol.exc.Cerrado |  |  |
| 7 | Solo para Polonia Introducir datos de ventas | En la Comercio internacional: Exportación sección, introduzca los siguientes datos:• Código de control : para ejemplo, 26.40.20.0 | Se actualiza el código PKWiU para Polonia. |  |
| 8 | Grabe los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto (F1602) se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que lo guía a la Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccione Ventas. | El Producto , seleccione Ventas .efectúe las siguientes entradas:Grupo de transporte : 0001Embalaje permitido Peso:Volumen de embalaje permitido: |  |  |
| 4 | Guardar los datos | Seleccionar Grabar . | Aparece un mensaje del sistema que indica que el objeto se ha guardado. |  |

### Actualizar datos maestros de material - Vista WM

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior, Creación de datos maestros de material (producto) - Datos básicos, antes de continuar con esta sección.

Inicie el procedimiento después de haber guardado las entradas de datos básicos, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Modificar material (MM02) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Modificar material (MM02) . | Crear material (pantalla inicial) se abre. |  |
| 2 | Introducir datos básicos de material | El Modificar material (pantalla inicial) pantalla, efectúe las siguientes entradas:Material : <Material número>Haga clic en Seleccionar Vista(s) . | Seleccionar vista(s) se abre. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas:Ejecución WMEmbalaje WMSeleccionar Continuar . |  |  |
| 4 | Introducir datos de ejecución WM | El Ejecución WM pestaña, realice lo siguiente entradas:Tipo UMp estándar : por ejemplo, SP1 |  |  |
| 5 | Introducir datos de embalaje WM | El Embalaje WM pestaña, realice lo siguiente entradas:Tipo de unidad de manipulación : por ejemplo, SP1 |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . |  |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto (F1602) Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que lo guía a la Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar ejecución | En la Producto , seleccione la vista Gestión de almacenes pestaña. |  |  |
| 4 | Introducir datos de ejecución | En la Ejecución , realice las siguientes entradas:Tipo de unidad de manipulación estándar: por ejemplo, SP1 |  |  |
| 5 | Introducir datos de embalaje | En la Embalaje , realice las siguientes entradas:Tipo de unidad de manipulación: por ejemplo, SP1 |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/create-product-master-of-type-packaging-mds-3y1-389]]
- related-to :: [[02-business-partner-and-product-master-data/criar-mestre-de-produtos-do-tipo-embalagem-mds-3y1-392]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-391]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-393]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 22,471 chars in the whole document
