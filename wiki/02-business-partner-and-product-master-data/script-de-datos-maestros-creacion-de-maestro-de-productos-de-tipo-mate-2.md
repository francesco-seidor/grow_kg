---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2
title: "Script de datos maestros - Creación de maestro de productos de tipo \"Materia prima\" (BNR) (BNR_S4CLD2608_Master_Data_ES_XX)"
description: Spanish machine-translated SAP S/4HANA Cloud Public 2608 master data test script (BNR) for creating raw-material (ROH) product masters via MM01 or F1602.
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNR_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", material master, product master creation, basic data, purchasing data, mrp planning data, storage data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-660
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos de tipo "Materia prima" (BNR) (BNR_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Materia prima" - MDS (BNR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895025)

[2 Requisitos previos 3](#_Toc233895026)

[2.1 Acceso al sistema 3](#_Toc233895027)

[2.2 Roles 3](#_Toc233895028)

[2.3 Unidades organizativas necesarias 3](#_Toc233895029)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895030)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233895031)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233895032)

[2.5.2 Ramo 5](#_Toc233895033)

[3 Tabla de resumen 6](#_Toc233895034)

[4 Procedimientos de prueba 7](#_Toc233895035)

[4.1 Crear datos maestros de material - Datos básicos 7](#_Toc233895036)

[4.2 Crear datos maestros de material - Datos de compras 10](#_Toc233895037)

[4.3 Crear datos maestros de material - Datos de planificación/MRP (datos de centro) 12](#_Toc233895038)

[4.4 Crear datos maestros de material - Datos de almacén 16](#_Toc233895039)

[4.5 Crear datos maestros de material - Datos de contabilidad (datos de área de valoración) 19](#_Toc233895040)

[4.6 Crear datos maestros de producto - Producto configurable y variantes 21](#_Toc233895041)

[4.7 Crear datos maestros de producto - Guardar anexos 25](#_Toc233895042)

[4.8 Crear datos maestros de producto - Ventas de centro / Datos generales 27](#_Toc233895043)

[4.9 Crear datos maestros de producto - Centro / Fabricación repetitiva 29](#_Toc233895044)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

El maestro de materiales o productos contiene información sobre todos los materiales físicos que se aprovisionan, producen, almacenan y venden. También se utiliza para gestionar información sobre servicios, por ejemplo, para la compra y venta de servicios en horas.

El maestro de materiales contiene información como el número de material unívoco, el nombre, el material tipo, unidad de medida, descripciones, peso y dimensiones. Esta información de material es utilizado y almacenado en transacciones como pedidos de cliente, entregas, pedidos y movimientos de mercancías.

Como toda la información de un material se almacena centralmente, la información del maestro de materiales se organizados en diferentes vistas. Por ejemplo, ventas, almacenamiento, MRP, cálculo de costes y contabilidad.

Parte de la información de cada material es específica de determinadas unidades organizativas. Para ejemplo, una descripción de ventas es específica de una unidad de ventas (conocida como área de ventas), una planificación de necesidades es específico de un sitio específico (conocido como centro) o alguna información podría ser específico de un almacén.

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
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de material dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Descripción de material (texto breve), número de material, grupo de materiales, unidad base de Medida, etc. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Datos de compras | Centro | Grupo de compras, Grupo de artículos, Tiempo de tratamiento de EM, etc. | Pueden existir datos de compras para cada organización de compras para qué material se debe utilizar en compras procesos. | Centro:__________ |
| Datos de planificación/MRP | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Plazo de entrega previsto, etc. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del es necesario realizar una planificación específica de almacén | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. Rest. Estante, etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para los que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del es necesario realizar una planificación específica de almacén | Centro:____________Almacén:__________ |
| Datos de contabilidad | Área de valoración (=centro), clase de valoración | Clase de valoración, Precio por unidad, Control de precio, etc. | Los datos del área de valoración pueden existir para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales. Cada centro representa una valoración Área (por ejemplo, precio de valoración diferente de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un maestro de materiales registro de datos.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir específico de BR Campos para datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
|  |  | Opcional |  |
|  |  | Obligatorio |  |

### Parámetros principales para la creación de datos

En esta sección, se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear un registro de datos maestros de material:

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizar o qué campos son obligatorios u opcionales. En función de los tipos de material, el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos los tipos de material utilizan la misma definición de rango de números

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe tener más de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un número numérico a un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M .

|  |
| --- |
| Nota Actualmente, esto solo es visible en SAP GUI. |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material básicos. |
| [Crear datos maestros de material - Datos de compras](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de compras. |
| [Crear datos maestros de material - Datos de planificación/MRP (datos de centro)](#unique_13) [página ] 12 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de planificación MRP. |
| [Crear datos maestros de material - Datos de almacén](#unique_14) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se han creado los datos maestros de almacén. |
| [Crear datos maestros de material - Datos de contabilidad (datos de área de valoración)](#unique_15) [página ] 19 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de contabilidad. |
| [Crear datos maestros de producto - Producto configurable y variantes](#unique_16) [página ] 21 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) o bien Modificar material (MM02) si es necesario | Se crean el producto configurable y las variantes. |
| [Crear datos maestros de producto - Guardar anexos](#unique_17) [página ] 25 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Grabe los anexos en el registro maestro de materiales. |
| [Crear datos maestros de producto - Ventas de centro / Datos generales](#unique_18) [página ] 27 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |
| [Crear datos maestros de producto - Centro / Fabricación repetitiva](#unique_19) [página ] 29 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear datos maestros de material - Datos básicos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | Se muestra la rampa de lanzamiento SAP Fiori.Nota La entrada al sistema mediante la rampa de lanzamiento solo es relevante en caso de uso de Web GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 .Seleccionar Continuar . | El Crear material (materias primas) se visualiza. |  |
| 5 | Introducir datos básicos | El Material … (materias primas) pantalla, en la pantalla Datos básicos 1 etiqueta, introduzca descripción para la Descr. campo. |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida base : <Unidad de medida base>Grupo de materiales : <Grupo de artículos>Gr.tp.pos.gen. : <GenItemCatGroup> |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN , realice las siguientes entradas:Peso bruto : <Peso bruto>Unidad de peso : <Unidad de peso>Peso neto : <Peso neto>Pulsar Intro . | El Datos básicos 2 se visualiza. |  |
| 8 | Introducir datos básicos | El Datos básicos 2 no es necesario realizar ninguna entrada. | El Última pantalla de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 9 | Guardar los datos | El Última pantalla de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | En la Maestro de productos catálogo, seleccione el Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | El Gestionar datos maestros de producto , seleccione Crear . | El Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir campos obligatorios | El Crear registro de datos maestros , efectúe las siguientes entradas y seleccione OK :Número de producto : Por ejemplo, Z o cualquier ID alfanumérico externo. Debe empiece con un carácter o sin entrada y, a continuación, el sistema asignará un ID numérico automáticamente.Nota Para obtener más información sobre la creación del número de producto, consulte el anterior [Tipo de material y rangos de números](#unique_8) [página ] 5 capítulo.Tipo de producto : ROHGrupo de productos : Por ejemplo, L002 .Unidad base : Por ejemplo, UN .Descripción : <Cualquier descripción> |  |  |
| 5 | Volver a la pantalla principal | Volver a Gestionar maestro de productos pantalla. | El Gestionar maestro de productos se visualiza. |  |
| 6 | Introducir datos básicos | Ir a Gestionar maestro de productos > DATOS BÁSICOS > Datos básicos , y realice la siguiente entrada:Sector : Por ejemplo, 00 . |  |  |
| 7 | Añadir una descripción | Ir a Gestionar maestro de productos > DATOS BÁSICOS > Descripción y seleccione Crear . | Se muestra la descripción en el idioma predeterminado (por ejemplo, inglés). |  |
| 8 | Introducir datos de descripción | El Descripción , efectúe las siguientes entradas:Idioma : Por ejemplo, Alemán .Descripción de producto : <Descripción del producto> |  |  |
| 9 | Volver a la pantalla principal | Seleccione la flecha hacia atrás para volver a la pantalla principal. | El Maestro de productos se visualiza. |  |
| 10 | Seleccionar unidad de medida base | Ir a Información general > DATOS BÁSICOS y seleccione Unidad de medida base . | El Unidad de medida base se visualiza. |  |
| 11 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que Registro de datos maestros creado , que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material - Datos de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Ha completado y grabado los datos básicos para el material como se describe en la sección anterior. [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Compras y seleccione Continuar .Nota Solo para Polonia : para introducir el código PKWiU, seleccione también Comercio exterior - Importación Datos antes de elegir Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice la siguiente entrada y seleccione Continuar :Centro : <Código de centro> | El Crear material (materias primas) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará. |  |
| 5 | Introducir datos de compras | El Material (materias primas) pantalla, en la pantalla Compras en la pestaña Datos generales , realice las siguientes entradas:Grupo de compras : <Número de grupo de compras>Grupo de materiales : Por ejemplo, L002 . |  |  |
| 6 | Introducir datos de compras | En la Otros datos / datos del fabricante , realice la siguiente entrada:Tmpo.tratam.EM : Por ejemplo, 1 . | El Última pantalla de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| Solo para Polonia | Introducir datos de importación de comercio exterior | Solo para Polonia: en el Datos de comercio exterior introduzca los datos del código PKWiU:Código de control : Por ejemplo, 24.10.32.0 . | Se actualiza el código PKWiU para Polonia. |  |
| 7 | Guardar los datos | El Última pantalla de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccionar Producto (original) de la lista que le lleva a la Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de compras | El Maestro de productos , seleccione Compras . | El Compras se visualiza. |  |
| 4 | Editar cabecera | Seleccionar Editar cabecera en la parte superior de la pantalla y realice la siguiente entrada:Grupo de productos : Por ejemplo, A001 . | El Editar cabecera se visualiza. |  |
| 5 | Introducir datos de compras | El Compras , realice la siguiente entrada:Clave de valor de compras : Por ejemplo, 1 . |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de material - Datos de planificación/MRP (datos de centro)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Ha rellenado los datos para el material como se describe en la sección anterior. [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7 y han completado y grabado los datos maestros de compras.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione MRP1 , MRP2 , MRP3 , y MRP4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : Por ejemplo, 1710 .Almacén : Por ejemplo, 171C . | El Crear material (materias primas) se visualiza. |  |
| 5 | Introducir datos de planificación/MRP | El Material (materias primas) pantalla, en la pantalla Planif.necesidades 1 en la pestaña Método de planificación de necesidades , realice las siguientes entradas:Caract.planif.nec. : Por ejemplo, PD .Planificador de necesidades : Por ejemplo, 001 . | El mensaje del sistema muestra que El material ya existe y se ampliará. |  |
| 6 | Introducir datos de planificación/MRP | En la Datos de tamaño de lote , realice la siguiente entrada:Cálculo del tamaño del lote : Por ejemplo, EX . | El Planif.necesidades 2 se visualiza. |  |
| 7 | Introducir datos de planificación/MRP | El Crear material (materias primas) pantalla, en la pantalla Planif.necesidades 2 en la pestaña Aprovisionamiento , realice las siguientes entradas:Clase de aprovisionamiento : Por ejemplo, F .Almacén de producciónAlmacén p.proc.ext. |  |  |
| 8 | Introducir datos de planificación/MRP | En la Programación , realice las siguientes entradas:Plazo de entrega previsto : Por ejemplo, 3 .Tmpo.tratam.entr.mcía. : Por ejemplo, 1 .Clave de horizonte : Por ejemplo, 000 . | El Planif.necesidades 3 se visualiza. |  |
| 9 | Introducir datos de planificación/MRP | El Crear material (materias primas) pantalla, en la pantalla Planif.necesidades 3 en la pestaña Verificación de disponibilidad , realice las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Plazo reaprovis.total : Por ejemplo, 3 . | El Planif.necesidades 4 se visualiza. |  |
| 10 | Introducir datos de planificación/MRP | El Crear material (materias primas) pantalla, en la pantalla Planif.necesidades 4 en la pestaña Explosión de la lista de materiales / Necesidades secundarias , realice la siguiente entrada:Sol.indiv./colect. : 2 | El Última pantalla de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 11 | Guardar los datos | El Última pantalla de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar centros | El Maestro de productos , seleccione CENTROS . | El CENTROS se visualiza. |  |
| 4 | Seleccione Crear. | En la CENTROS sección, seleccione Crear . | El Centros se visualiza en modo de edición. |  |
| 5 | Introducir centros: Datos de información general | El Centro: Información general , efectúe las siguientes entradas:Centro : <Número de centro>Centro de beneficio : Por ejemplo, YB110 o bien YB111 .En la Ventas , realice la siguiente entrada:Grupo de carga : Por ejemplo, 0001 . |  |  |
| 6 | Introducir centros - Datos de planificación de necesidades | El Datos MRP , efectúe las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Plazo de entrega previsto : Por ejemplo, 3 .Tiempo de procesamiento de entrada de mercancías : Por ejemplo, 1 .Caract.planif.nec. : Por ejemplo, PD .Planificador de necesidades : Por ejemplo, 001 . |  |  |
| 7 | Introducir centros - Datos de tamaño de lote | El DATOS MRP , seleccione Datos de tamaño de lote .El Datos de tamaño de lote , realice la siguiente entrada:Cálculo del tamaño del lote : Por ejemplo, EX . |  |  |
| 8 | Introducir centros - Datos de aprovisionamiento | Ir a Datos de planificación de necesidades > Aprovisionamiento , y realice las siguientes entradas:Plazo de entrega previsto : Por ejemplo, 3 .Tiempo de procesamiento de entrada de mercancías : Por ejemplo, 1 . |  |  |
| 9 | Seleccionar centros - Previsión | El Maestro de productos: CENTROS , seleccione PREVISIÓN . | El Centro - PREVISIÓN se visualiza. |  |
| 10 | Introducir datos de previsión | El PREVISIÓN , realice la siguiente entrada:Tipo de período : Por ejemplo, M . |  |  |
| 11 | Volver a la pantalla principal | Seleccionar Aplicar . | El Gestionar maestro de productos se visualiza. |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de material - Datos de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Ha rellenado los datos para el material como se describe en la sección anterior. [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7 y han completado y grabado los datos de MRP/Planning.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2 |  |  |
| 4 | Introducir datos de niveles de organización | Seleccionar Niveles org. en la parte superior de la pantalla.El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : <Código de centro>Almacén : <Número de almacén> | El Crear material (materias primas) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará. |  |
| 5 | Introducir datos de almacén | El Crear material (materias primas) pantalla, en la pantalla Dat.ce./almacén 1 pestaña, en el Datos generales , realice la siguiente entrada:Número de vales de entrada de mercancías : Por ejemplo, 1 .Pulsar Intro para navegar a la siguiente pantalla. | El Dat.ce./alm.2 se visualiza. |  |
| 6 | Confirmar entradas | El Dat.ce./Almacén 2 en la pestaña Parámetros generales de centro , realice las siguientes entradas:Centro de beneficio : <Centro de beneficio>Perfil de número de serie : <Perfil de número de serie>Seleccione un perfil de número de serie válido que se haya asignado con el tipo de equipo adecuado para su de negocios. | El Última pantalla de datos alcanzada se muestra con el mensaje Está a punto de salir. ¿Desea grabe primero sus datos para este material? . |  |
| 7 | Guardar los datos | El Última pantalla de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar centros | El Gestionar maestro de productos , seleccione CENTROS .Nota Ya se debe haber creado un registro de datos de centro. Si no tiene un registro de centro existente, siga los pasos de la sección anterior. [Crear datos maestros de material - Datos de planificación/MRP (datos de centro)](#unique_13) [página ] 12. | El CENTROS se visualiza. |  |
| 4 | Seleccionar detalles de centro | El Maestro de productos: CENTROS seleccione el icono de flecha para los datos de centro que ha creado en la sección anterior, [Crear datos maestros de material - Datos de planificación/MRP (datos de centro)](#unique_13) [página ] 12. | El Centro de maestro de productos se visualiza. |  |
| 5 | Navegar a Centro: Almacén | El Gestión de maestro de productos - CENTROS pantalla, vaya a CENTROS > UBICACIÓN DE ALMACENAMIENTO . | El Maestro de productos: CENTROS se visualiza en modo de edición. |  |
| 6 | Seleccione Crear. | Ir a CENTROS > UBICACIÓN DE ALMACENAMIENTO > Almacén y seleccione Crear . | El Centro - Almacén se visualiza en modo de edición. |  |
| 7 | Introducir centro: Datos de almacén | El Almacén , realice la siguiente entrada:Almacén : <Número de almacén> | El Nuevo registro - Almacén se visualiza. |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar dos veces para volver al Producto pantalla. | El Gestionar maestro de productos se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de material - Datos de contabilidad (datos de área de valoración)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Ha rellenado los datos para el material como se describe en la sección anterior. [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7 y han completado y guardado los datos de Almacén.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Contabilidad 1Contabilidad 2 | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice la siguiente entrada:Centro : <Centro> | El Crear material (materias primas) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará. |  |
| 5 | Introducir datos de contabilidad | El Crear material (materias primas) pantalla, en la pantalla Contabilidad 1 en la pestaña Datos de valoración generales , realice la siguiente entrada:Categoría de valoración : 3000 |  |  |
| 6 | Introducir datos de contabilidad | En la Precios y valores , realice las siguientes entradas:Precio por unidad : Por ejemplo, 20 .Control de precio : <V> | El Contabilidad 2 se visualiza. |  |
| 7 | Confirmar entradas | El Contabilidad 2 no es necesario realizar ninguna entrada. | El Última pantalla de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 8 | Guardar los datos | El Última pantalla de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar áreas de valoración | El Gestionar maestro de productos , seleccione ÁREAS DE VALORACIÓN . | El ÁREAS DE VALORACIÓN se visualiza. |  |
| 4 | Seleccione Crear. | El ÁREAS DE VALORACIÓN , seleccione Crear . | El Nuevo registro - Área de valoración se visualiza en modo de edición. |  |
| 5 | Introducir datos de área de valoración | El ÁREAS DE VALORACIÓN , efectúe las siguientes entradas:Área de valoración : <Número de área de valoración>Determinación de control de precio: : 2Nota Solo para Brasil : Determinación de control de precio es 2 si Control de precio es V , y así es 3 si Control de precio es S , al abordar los principios de contabilidad de costes de Brasil.Categoría de valoración : <Número de clase de valoración> |  |  |
| 6 | Introducir datos de área de valoración actual | El Valoración pantalla, vaya a Valoración > Período actual , y realice las siguientes entradas:Precio estándar : Por ejemplo, 20 .Control de precio : Por ejemplo, S . |  |  |
| 7 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Gestionar maestro de productos pantalla. | El Gestionar maestro de productos se visualiza. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Producto configurable y variantes

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de producto. Las aplicaciones disponibles dependen de su asignación rol, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | Se muestra la rampa de lanzamiento SAP Fiori.Nota La entrada al sistema mediante la rampa de lanzamiento solo es relevante en caso de uso de Web GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | Nota Si el Categoría de clase se muestra cuando realiza el paso 3, debe seguir el paso 7, 8, 9, y 10 antes del paso 4 y, a continuación, vuelva a abrir el material en el Modificar material (MM02) para ejecutar los pasos 5 y 6.El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos básicos 1Datos básicos 2Clasificación |  |  |
| 5 | Introducir datos básicos | El Material (materias primas) pantalla, en la pantalla Datos básicos 1 , haga el siguientes entradas:Descripción de material (texto breve) : <Descripción de material>Unidad de medida base : <Unidad de medida base>Pulsar Intro . | El Datos básicos 2 se visualiza. |  |
| 6 | Introducir datos básicos | El Datos básicos 2 , verifique la Material configurable casilla de selección.Pulsar Intro . | El Clasificación y la ficha Categoría de clase se visualiza la ventana de diálogo. |  |
| 7 | Seleccionar categoría de clase | En la Categoría de clase seleccione Categoría de clase 300 (variante) y seleccione Continuar . | El Clasificación se visualiza. |  |
| 8 | Asignar clase | En la Asignación sección, asigne una clase y pulse Intro . | Las características correspondientes se visualizan debajo de la Asignación sección. |  |
| 9 | Seleccionar valores de característica | Seleccione los valores necesarios de las características. |  |  |
| 10 | Grabar datos | Seleccionar Grabar . | Se crea el material configurable. |  |
| 11 | Navegar a la transacción CU41 | Navegar a CU41 transacción y realice las siguientes entradas:Nombre de perfil : <Nombre de perfil>Categoría de clase : 300 |  |  |
| 12 | Grabar datos | Seleccionar Grabar . | Se crea el perfil de configuración. |  |
| 13 | Navegar a la transacción CU42 | Navegar a CU42 transacción.Haz doble clic Nombre perfil > Pantalla inicial de configuración > Modo de procesamiento: Configuración de variante avanzada .Seleccionar Grabar . | Se crea el perfil. |  |
| 14 | Crear variante | Para crear una variante, abra la Crear material (MM01) y siga los pasos anteriores para crear un nuevo Material con Datos básicos 1 y Datos básicos 2 . |  |  |
| 15 | Crear variante | En Datos básicos 2 , vaya a Configuración específica de cliente e introduzca el valor creado material configurable en el Mat.conf.vál.p.tod.ce. . Seleccione Configurar variante y, a continuación, seleccione los valores de características necesarios para configurar variantes. | Se crea la variante. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | Se muestra la rampa de lanzamiento SAP Fiori.Nota La entrada al sistema mediante la rampa de lanzamiento solo es relevante en caso de uso de Web GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Buscar y abrir producto para editar | Buscar el creado anteriormente Producto introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le lleva a la Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 4 | Hacer que el producto sea configurable | El Producto vaya a la pantalla Configuración y verifique la El producto es configurable casilla de selección. |  |  |
| 5 | Asignar clase de variante | El Producto vaya a la pantalla Clasificación y seleccione Haga clic aquí para asignar una clase .Seleccione una clase de tipo 300 (variante) . | Las características de la visualización de clase asignada. |  |
| 6 | Seleccionar características | Seleccione los valores de característica necesarios para cada una de las características. |  |  |
| 7 | Ir a la pestaña Variantes | El Producto vaya a la pantalla Variantes y seleccione Seleccionar Variantes de producto . | Se visualiza un árbol/tabla con las diferentes características. |  |
| 8 | Seleccionar características y crear variantes | Seleccione la combinación de valores de característica y seleccione Aplicar . | Se crean las variantes. |  |
| 9 | Grabar | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Guardar anexos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de producto. Las aplicaciones disponibles dependen de su asignación rol, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7, antes de continuar con este procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la sección anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 .Seleccionar Continuar . | El Crear material (materias primas) se visualiza. |  |
| 4 | Seleccionar servicios para objeto | Ir a Servicios para objeto > Crear anexo . | El Importar archivo se visualiza. |  |
| 5 | Seleccione Cargar. | El Importar archivo , seleccione Cargar . | Se muestra una pantalla de carga de archivos. |  |
| 6 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se ha cargado el archivo. |  |
| 7 | Grabar | Seleccionar Seleccionar y luego Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar anexos | El Producto vaya a la pantalla Anexos pestaña. | El Anexos se visualiza. |  |
| 4 | Seleccione Cargar. | En el Sistema de gestión de documentos sección, seleccione Cargar . | Se muestra una pantalla de carga de archivos. |  |
| 5 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se ha cargado el archivo. |  |
| 6 | Grabar | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Ventas de centro / Datos generales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la sección anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el El ramo no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Ventas: General/Centro Datos .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice las siguientes entradas:Centro : <Centro número>Org.ventas : <Número de organización de ventas>Canal distrib. : <Canal de distribución> | El Crear material... (materias primas) se visualiza. |  |
| 5 | Introducir datos en la pantalla Datos básicos 1 | El Datos básicos 1 , efectúe las siguientes entradas y pulse Intro :Descripción : introduzca una descripción para el producto.Unidad base : Actualizar Unidad base EA , por ejemplo, 1 . |  |  |
| 6 | Introducir datos en la pantalla Ventas: Datos generales/de centro | En la Datos de expedición (tiempos en días) , realice la siguiente entrada:Gr.carga : <Seleccione un valor de la ayuda para entradas> |  |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto , seleccione Centros . | El Centros se visualiza. |  |
| 4 | Seleccione Crear. | El Centros , seleccione Crear . |  |  |
| 5 | Introducir centros - Datos generales | En la Datos generales , realice la siguiente entrada:Centro : <Número de centro> , por ejemplo, 1710 |  |  |
| 6 | Introducir datos de planificación de necesidades | En la MRP , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
| 7 | Introducir centro - ventas | En la Ventas , realice la siguiente entrada:Grupo de carga : <Seleccione un valor de la ayuda para entradas> |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Centro / Fabricación repetitiva

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, [Crear datos maestros de material - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la sección anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el El ramo no se ofrece para la entrada, el campo está atenuado.Tipo de material : ROH (materias primas)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 , MRP 1 , y Planif.necesidades 4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice las siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (materias primas) se visualiza. |  |
| 5 | Introducir datos en la pantalla Datos básicos 1 | El Datos básicos 1 , efectúe las siguientes entradas y pulse Intro :Descripción : introduzca una descripción para el producto.Unidad base : Actualizar Unidad base EA , por ejemplo, 1 . |  |  |
| 6 | Introducir datos en la pantalla MRP 1 | En la Método de planificación de necesidades , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
| 7 | Introducir datos en la pantalla MRP 4 | En la Fabricación repetitiva/montaje/estrategia de despliegue , realice la siguiente entrada:Fabricación repetitiva : marque la casilla de selección.Perfil fabricación repetitiva : <Seleccione un valor de la ayuda para entradas> |  |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto búsqueda campo.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto , seleccione Centros . | El Centros se visualiza. |  |
| 4 | Seleccione Añadir (+) | El Centros , seleccione Añadir (+) . |  |  |
| 5 | Introducir centros - Datos generales | En la Datos generales , realice la siguiente entrada:Centro : <Número de centro> , por ejemplo, 1710 |  |  |
| 6 | Introducir datos de planificación de necesidades | En la MRP , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
| 7 | Introducir datos de fabricación repetitiva | En la Fabricación repetitiva , realice las siguientes entradas:Fabricación repetitiva activada : marque la casilla de selección para activar el Fabricación repetitiva Perfil campo.Perfil de fabricación repetitiva : <Seleccione un valor de la ayuda para entradas>Nota Después de verificar el Fabricación repetitiva activada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser editable.Después de desmarcar Fabricación repetitiva activada la casilla de verificación, el Perfil de fabricación repetitiva El campo debe ser de solo lectura. |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

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
> Flagged while digesting this document, not verified: Machine-translated Spanish text, unreviewed; terminology may differ from other-language versions of the same script.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Plant sales and repetitive manufacturing Option 1 tables skip a step number (7) and some fields are blank; table of mandatory/optional master data objects is empty.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-661]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-663]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 62,727 chars in the whole document
