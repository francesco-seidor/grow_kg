---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2
title: "Script de datos maestros - Creación de maestro de productos de tipo \"Producto terminado\" (MDS BNT) (BNT_S4CLD2608_Master_Data_ES_XX)"
description: Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 test script for creating finished-product (FERT) material master data via MM01 or F1602.
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNT_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, finished product creation, sales data, mrp planning data, storage data, accounting valuation data, configurable products, product attachments, repetitive manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-672
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos de tipo "Producto terminado" (MDS BNT) (BNT_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Producto terminado" - MDS (BNT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895074)

[2 Requisitos previos 3](#_Toc233895075)

[2.1 Acceso al sistema 3](#_Toc233895076)

[2.2 Roles 3](#_Toc233895077)

[2.3 Unidades organizativas necesarias 3](#_Toc233895078)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895079)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233895080)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233895081)

[2.5.2 Ramo 5](#_Toc233895082)

[3 Tabla de resumen 6](#_Toc233895083)

[4 Procedimientos de prueba 7](#_Toc233895084)

[4.1 Crear datos maestros de producto - Datos básicos 7](#_Toc233895085)

[4.2 Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas 10](#_Toc233895086)

[4.3 Crear datos maestros de producto - Datos de planificación MRP / Datos de centro 14](#_Toc233895087)

[4.4 Crear datos maestros de producto - Datos de almacén 17](#_Toc233895088)

[4.5 Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración 20](#_Toc233895089)

[4.6 Crear datos maestros de producto - Producto configurable y variantes 23](#_Toc233895090)

[4.7 Crear datos maestros de producto - Guardar anexos 26](#_Toc233895091)

[4.8 Crear datos maestros de producto - Ventas de centro / Datos generales 28](#_Toc233895092)

[4.9 Crear datos maestros de producto - Centro / Fabricación repetitiva 30](#_Toc233895093)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

El maestro de materiales o productos contiene información sobre todos los materiales físicos que se aprovisionan, producen, almacenan y venden. Pos también se utiliza para gestionar información sobre servicios, por ejemplo, para comprar y vender servicios en horas.

El maestro de materiales contiene información como el número de material unívoco, el nombre, el tipo de material, la unidad de medida, las descripciones, el peso y dimensiones. Esta información de material se utiliza y almacena en transacciones como pedidos de cliente, entregas, pedidos y mercancías. movimientos.

Como toda la información de un material se almacena centralmente, la información del maestro de materiales se organiza en diferentes vistas. Por ejemplo, ventas, almacenamiento, MRP, cálculo de costes y contabilidad.

Parte de la información de cada material es específica de determinadas unidades organizativas. Por ejemplo, una descripción de ventas es específica de un unidad de ventas (conocida como área de ventas), un planificador de necesidades es específico de un sitio específico (conocido como centro) o alguna información puede ser específico de un almacén.

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
| Datos básicos | Independiente de unidades organizativas | Descripción de material (texto breve), número de material, grupo de materiales, unidad base de Medida, etc. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales, Grupo de tipos de posición, Tipo de Grupo, grupo de carga, tiempo de preparación, etc. on. | Pueden existir datos de ventas para cada organización de ventas de su estructura empresarial para la que el material se utiliza el registro maestro. | Centro:____________Organización de ventas:__________Canal de distribución:__________ |
| Datos de planificación/MRP (datos de centro) | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Plazo de entrega previsto, etc. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función de la necesidad de almacenar Planificación específica de ubicación. | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. Rest. Estante, etc. |  | Centro:____________Almacén:__________ |
| Datos de contabilidad (datos de valoración) | Área de valoración (=centro), clase de valoración | Clase de valoración, Precio por unidad, Control de precio, etc. | Pueden existir datos de área de valoración para cada ID de centro de su estructura de la empresa para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, diferente precio de valoración de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un material registro de datos maestros.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

Esta sección describe algunos parámetros básicos que influyen en el comportamiento de un registro maestro y siempre son necesarios para crear un registro de datos maestros de material:

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizar o qué campos son obligatorios u opcionales. En función de los tipos de material, el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos los tipos de material utilizan la misma definición de rango de números

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe tener más de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un número numérico a un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M . Actualmente esto solo es visible en SAP GUI.

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos básicos. |
| [Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material - Datos de ventas (datos de IVA). |
| [Crear datos maestros de producto - Datos de planificación MRP / Datos de centro](#unique_13) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material - Datos de planificación/MRP (datos de centro). |
| [Crear datos maestros de producto - Datos de almacén](#unique_14) [página ] 17 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean los datos de almacén. |
| [Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración](#unique_15) [página ] 20 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Datos de contabilidad (datos de valoración) creados. |
| [Crear datos maestros de producto - Producto configurable y variantes](#unique_16) [página ] 23 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Crear producto configurable y variantes. |
| [Crear datos maestros de producto - Guardar anexos](#unique_17) [página ] 26 | Especialista en datos maestros - Datos de producto | Modificar material (MM02) / Gestionar datos maestros de producto (F1602) | Grabar anexos en el registro maestro de materiales. |
| [Crear datos maestros de producto - Ventas de centro / Datos generales](#unique_18) [página ] 28 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |
| [Crear datos maestros de producto - Centro / Fabricación repetitiva](#unique_19) [página ] 30 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear datos maestros de producto - Datos básicos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas y seleccione Seleccionar vista(s) :Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo es rellenado con En la oscuridad .Tipo de material : FERT | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) vista, seleccionar Datos básicos 1 y Datos básicos 2 y seleccione Continuar . | El Crear material (producto terminado) se visualiza. |  |
| 5 | Introducir datos básicos | En la Material (producto terminado) vista, en la Datos básicos 1 introduzca la etiqueta descripción de material (texto breve). |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida base : <Unidad de medida base>Grupo de materiales : <Grupo de artículos>Gr.tp.pos.gen. : <GenItemCatGroup> |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN , realice las siguientes entradas y pulse Intro :Peso bruto : <Peso bruto>Unidad de peso : <Unidad de peso>Peso neto : <Peso neto> | El Datos básicos 2 se visualiza. |  |
| 8 | Introducir datos básicos | El Datos básicos 2 no es necesario realizar ninguna entrada. | Una ventana nueva Última vista de datos alcanzada se abre con el mensaje Está a punto de salir. ¿Desea grabe primero sus datos para este material? . |  |
| 9 | Guardar los datos | En la Última vista de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear nuevo maestro de productos. | Seleccionar Crear producto . | El Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir datos para campos obligatorios | En la Crear registro de datos maestros vista, haga el siguientes entradas:Número de producto : por ejemplo, Z …Nota Aquí puede introducir cualquier ID alfanumérico externo … (al menos esto debe empezar con un carácter). Si no realice cualquier entrada aquí, el sistema asignará un ID numérico automáticamente.Para obtener más información sobre el número de producto, consulte la Tipo de material y rangos de números sección en Parámetros principales para la creación de datos .Tipo de producto : FERTGrupo de productos : por ejemplo, L004Unidad base : por ejemplo, UNDescripción : <Descripción> |  |  |
| 5 | Seleccione OK. | En la Gestionar maestro de productos , seleccione OK . | El Gestionar maestro de productos se visualiza. |  |
| 6 | Introducir datos básicos | Ir a Gestionar maestro de productos > DATOS BÁSICOS > Datos básicos visualice y realice la siguiente entrada:Sector : por ejemplo, 00 |  |  |
| 7 | Ir a la vista Descripciones | Vaya a Descripciones vista. | La descripción en el idioma predeterminado (por ejemplo, inglés) ya se ha rellenado. |  |
| 8 | Seleccione Crear. | En la DESCRIPCIONES , seleccione Crear . | El Maestro de productos: Descripción se visualiza.Algunos campos ya se han rellenado. |  |
| 9 | Introducir datos de descripciones | En la Maestro de productos: Descripción , efectúe las siguientes entradas:Idioma : por ejemplo, AlemánDescripción de producto : <Descripción de producto> | Las descripciones se pueden actualizar en diferentes idiomas. |  |
| 10 | Volver al maestro de productos | Seleccione la flecha hacia atrás para volver al Maestro de productos vista. | El Maestro de productos se visualiza. |  |
| 11 | Seleccionar unidad de medida base | En la Maestro de productos vista, vaya a DATOS BÁSICOS y seleccione Unidad de medida base . | El Unidad de medida base se visualiza. |  |
| 12 | Introducir datos de unidad de medida base | Seleccionar Mostrar más y realice las siguientes entradas para los campos relacionados con el peso:Unidad de peso : por ejemplo, KGPeso bruto : por ejemplo, 2Peso neto : por ejemplo, 1Nota Si el Bruto Peso , Unidad de peso , o Peso neto campos no se muestran como campos de entrada, actualice/vuelva a cargar la vista. Después de actualizar/volver a cargar, puede realizar las entradas indicadas para esos campos. |  |  |
| 13 | Volver a la pantalla principal | Seleccione la flecha hacia atrás para volver al Maestro de productos vista. | El Maestro de productos se visualiza. |  |
| 14 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas

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

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Ventas: Datos org.ventas 1 , Ventas: Datos org.ventas 2 , y Ventas: Datos generales/de centro .Seleccionar Continuar .Nota Solo para Polonia : para introducir el número de clasificación PKWiU, también debe seleccionar Comercio internacional: Exportación . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas y seleccione Continuar :Centro : Por ejemplo, 1710 .Org.ventas : Por ejemplo, 1710 .Canal distrib. : Por ejemplo, 10 . | El Crear material (producto terminado) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará . |  |
| 5 | Introducir datos de ventas | El Material (producto terminado) pantalla, en la pantalla Ventas: org.ventas 1 pestaña, introduzca un valor adecuado para el Clasificación fiscal campo. Por ejemplo, 1 para imponible en su totalidad. | El Ventas: org.ventas 2 se visualiza.El valor introducido indica que el material está (normalmente) totalmente sujeto a impuestos. |  |
| 6 | Introducir datos de ventas | El Ventas: org.ventas 2 en la pestaña Conceptos de agrupación la sección, haga entrada siguiente:Grupo de tipos de posición : <Grupo de tipos de posición> | El Ventas: General/Centro se visualiza. |  |
| 7 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos generales la sección, haga entrada siguiente:Verificación de disponibilidad : Por ejemplo, PE . |  |  |
| 8 | Introducir datos de ventas | En la Datos de expedición (tiempos en días) , realice las siguientes entradas:Gpo.transp. : Por ejemplo, 0001 .Gr.carga : Por ejemplo, 0001 . |  |  |
| 9 | Introducir datos de ventas | En la Parámetros generales de centro , realice las siguientes entradas:Centro de beneficio : Por ejemplo, YB110 o bien YB111 .SerialNoProfile : seleccione un perfil de número de serie válido que se haya asignado con el perfil tipo de equipo para su empresa. | El Última vista de datos alcanzada con el mensaje: Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| Solo para Polonia | Introducir datos de ventas - solo para Polonia | En la Comercio internacional: Exportación , realice la siguiente entrada:Código de control : Por ejemplo, 26.70.13.0 . | Se actualiza el código PKWiU para Polonia. |  |
| 10 | Guardar los datos | El Última vista de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar cadenas de distribución | El Maestro de productos , seleccione CADENAS DE DISTRIBUCIÓN . | El CADENAS DE DISTRIBUCIONES se visualiza. |  |
| 4 | Seleccione Crear. | Ir a CADENAS DE DISTRIBUCIÓN > Cadenas de distribución y seleccione Crear . | El Cadena de distribución se visualiza en modo de edición. |  |
| 5 | Introducir datos de cadenas de distribución | El Cadena de distribución , efectúe las siguientes entradas:DATOS GENERALES - Información generalOrganización de ventas : <Número de organización de ventas> , por ejemplo, 1710Canal de distribución : Por ejemplo, 10 .Centro de entrega : <Número de centro> , por ejemplo, 1710TÉRMINOS DE AGRUPACIÓNGrupo de tipos de posición : Por ejemplo, NORM .Grupo de imputación : Por ejemplo, 03 Productos terminados .IMPUESTO SOBRE VENTASPaís : <Código de país> , por ejemplo, DECategoría fiscal : TTX1Clasificación fiscal : Cualquiera 1 para material o 2 para Servicios.Clasificación fiscal : Por ejemplo, 1 Impuesto completo al utilizar el impuesto UTXJ condición para EE. UU.Nota La clasificación fiscal depende de los requisitos específicos del país/región. Clasificación fiscal en el maestro de materiales y las tablas maestras de cliente determinan las entradas de porcentaje fiscal.Solo para Brasil :En la Clasificación fiscal , realice las siguientes entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : Cualquiera 1 para material o 2 para los Servicios. |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de planificación MRP / Datos de centro

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

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione MRP1 , MRP2 , MRP3 , y MRP4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : <Código de centro> , por ejemplo, 1710Almacén : Por ejemplo, 171A . | El Crear material (producto terminado) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará . |  |
| 5 | Introducir datos de planificación/MRP | El Material (producto terminado) pantalla, en la pantalla Planif.necesidades 1 en la pestaña Datos generales , realice la siguiente entrada:Grupo de compras : <Grupo de compras> |  |  |
| 6 | Introducir datos de planificación/MRP | En la Método de planificación de necesidades , realice las siguientes entradas:Caract.planif.nec. : Por ejemplo, PD .Planificador de necesidades : Por ejemplo, 001 . |  |  |
| 7 | Introducir datos de planificación/MRP | En la Cálculo del tamaño del lote , realice la siguiente entrada:Cálculo del tamaño del lote : EX | El Planif.necesidades 2 se visualiza. |  |
| 8 | Introducir datos de planificación/MRP | El Crear material (producto terminado) pantalla, en la pantalla Planif.necesidades 2 tabulador, hacer entradas en función de sus necesidades o, al menos, introduzca valores para los campos obligatorios. Por ejemplo, el Interna producción tiempo en días. | El Planif.necesidades 3 se visualiza. |  |
| 9 | Introducir datos de planificación/MRP | El Crear material (producto terminado) pantalla, en la pantalla Planif.necesidades 3 en la pestaña Planificación , realice las siguientes entradas:Grupo de estrategias : Por ejemplo, 40 .Modo de consumo : Por ejemplo, 2 .Per.consumo anter. : <Per.consumo ant.>Intervalo de consumo a plazo : <Período de consumo futuro> |  |  |
| 10 | Introducir datos de planificación/MRP | En la Verificación de disponibilidad , realice las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Plazo reaprov.total : Por ejemplo, 3 . | El Planif.necesidades 4 se visualiza. |  |
| 11 | Introducir datos de planificación/MRP | El Crear material (producto terminado) pantalla, en la pantalla Planif.necesidades 4 ficha, usted hace no es necesario realizar ninguna entrada. | El Última vista de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 12 | Grabar | El Última vista de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Maestro de productos , seleccione CENTROS . | El CENTROS se visualiza. |  |
| 4 | Seleccione Crear. | El CENTROS , seleccione Crear . | El Centro se visualiza en modo de edición. |  |
| 5 | Introducir centros: Datos de información general | Ir a Centro > INFORMACIÓN GENERAL , y realice las siguientes entradas:Centro : <Número de centro> , por ejemplo, 1710Centro de beneficio : Por ejemplo, YB110 o bien YB111 . |  |  |
| 6 | Introducir centros - Datos de planificación de necesidades | El Maestro de productos , seleccione DATOS MRP .En la DATOS MRP > Datos MRP , realice las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Caract.planif.nec. : Por ejemplo, PD .Planificador de necesidades : Por ejemplo, 001 . |  |  |
| 7 | Introducir centros - Datos de tamaño de lote | El DATOS MRP , seleccione Datos de tamaño de lote .El Datos de tamaño de lote , realice la siguiente entrada:Cálculo del tamaño del lote : Por ejemplo, EX . |  |  |
| 8 | Introducir centros - Datos de aprovisionamiento | Ir a Datos de planificación de necesidades > Aprovisionamiento , y realice las siguientes entradas:Plazo de entrega previsto : Por ejemplo, 3 .Tiempo de procesamiento de entrada de mercancías : Por ejemplo, 1 . |  |  |
| 9 | Seleccionar centros - Datos de previsión | Ir a Gestionar maestro de productos > CENTROS y seleccione PREVISIÓN . | El PREVISIÓN se visualiza. |  |
| 10 | Introducir centros - Datos de previsión | El PREVISIÓN , realice la siguiente entrada:Tipo de período : Por ejemplo, M . |  |  |
| 11 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Maestro de productos se visualiza. |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de producto - Datos de almacén

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

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2 | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : Por ejemplo, 1710 .Almacén : Por ejemplo, 171A . | El Crear material (producto terminado) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará . |  |
| 5 | Introducir datos de almacén | El Crear material (producto terminado) pantalla, en la pantalla Dat.ce./almacén 1 en la pestaña Datos generales , realice la siguiente entrada:Número de vales de entrada de mercancías : Por ejemplo, 1 . | El Dat.ce./alm.2 se visualiza. |  |
| 6 | Confirmar entradas | El Dat.ce./Almacén 2 no es necesario realizar ninguna entrada.Nota Para el SerialNoProfile seleccione un perfil de número de serie válido que se haya asignado con el tipo de equipo adecuado para su empresa. | El Última vista de datos alcanzada con el mensaje: Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 7 | Grabar | El Última vista de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Gestionar maestro de productos , seleccione CENTROS .Nota Si no hay ningún registro de datos de centro, siga los pasos del capítulo anterior: [Crear datos maestros de producto - Datos de planificación MRP / Datos de centro](#unique_13) [página ] 14. | El CENTROS se visualiza. |  |
| 4 | Seleccionar detalles de centro | El CENTROS utilice el icono de flecha para seleccionar los datos de centro que ha creado en el anterior paso. | El Maestro de productos: Centro se visualiza. |  |
| 5 | Navegar a Centro: Almacén | El Maestro de productos: Centro pantalla, vaya a CENTROS > UBICACIONES DE ALMACENAMIENTO . | El Maestro de productos: CENTROS se visualiza en modo de edición. |  |
| 6 | Seleccione Crear. | Ir a UBICACIONES DE ALMACENAMIENTO > Almacenes y seleccione Crear . | El Centro - Almacén se visualiza en modo de edición. |  |
| 7 | Introducir centro: Datos de almacén | El Almacenes , realice la siguiente entrada:Almacén : <Número de almacén> , por ejemplo, 171A |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar dos veces para volver al Producto pantalla. | El Maestro de productos se visualiza. |  |
| 9 | Grabar | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración

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

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Contabilidad 1Contabilidad 2 | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : <Código de centro> | El Crear material (producto terminado) se visualiza.El mensaje del sistema muestra que El material ya existe y se ampliará . |  |
| 5 | Introducir datos de contabilidad | El Crear material (producto terminado) pantalla, en la pantalla Contabilidad 1 ficha, en el Datos de valoración generales , realice la siguiente entrada:Categoría de valoración : 7920 |  |  |
| 6 | Introducir datos de contabilidad | En la Precios y valores , realice las siguientes entradas:Precio estándar : <Precio estándar>Precio por unidad : Por ejemplo, 20 .Control de precio : Por ejemplo, S . | El Contabilidad 2 se visualiza. |  |
| 7 | Confirmar entradas | El Contabilidad 2 no es necesario realizar ninguna entrada. | El Última vista de datos alcanzada con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 8 | Guardar los datos | El Última vista de datos alcanzada , seleccione Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de área de valoración | El Maestro de productos de gestor , seleccione ÁREAS DE VALORACIÓN . | El ÁREAS DE VALORACIÓN se visualiza. |  |
| 4 | Seleccione Crear. | El ÁREAS DE VALORACIÓN , seleccione Crear . | El ÁREAS DE VALORACIÓN se visualiza en modo de edición. |  |
| 5 | Introducir datos de área de valoración | Ir a ÁREAS DE VALORACIÓN > Área de valoración , y realice las siguientes entradas:Área de valoración : <Área de valoración> , por ejemplo, 1710Determinación de control de precio : 2Categoría de valoración : Por ejemplo, 7920 . |  |  |
| 6 | Introducir datos de área de valoración actual | El Valoración , seleccione Período actual , y realice lo siguiente entradas:Precio medio variable : Por ejemplo, 20 .Control de precio : Por ejemplo, S . |  |  |
| 7 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Maestro de productos se visualiza. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Producto configurable y variantes

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar un procedimiento anterior, Crear datos maestros de producto - Datos básicos , antes de continuar con este procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una ventana nueva que muestra la Crear material (pantalla inicial) . |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : Número de materialRamo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : FERTHaga clic en Seleccionar vista(s) . | Se abre una ventana nueva que muestra la Seleccionar vista(s) vista. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos básicos 1Datos básicos 2Clasificación |  |  |
| 4 | Introducir datos básicos | El Material (producto terminado) vista, en la Datos básicos 1 introduzca la etiqueta Descripción de material (texto breve) y Unidad de medida base.Pulsar Introduzca. | Datos básicos 2 se visualiza. |  |
| 5 | Introducir datos básicos | En la Datos básicos 2 , verifique la El material es configurable casilla de selección.Pulsar Intro . | Clasificación muestra las pestañas y Categoría de clase Se abre la ventana emergente. |  |
| 6 | Seleccionar categoría de clase | En la Categoría de clase Ventana emergente, seleccione el tipo de clase 300 (Variante) y seleccione Continuar . | Clasificación se visualiza. |  |
| 7 | Asignar clase | En la Asignación asigne una clase y pulse Intro. | Las características correspondientes se visualizan debajo de la Asignación sección. |  |
| 8 | Seleccionar valores de característica | Seleccione los valores necesarios de las características. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Se crea el material configurable. Ahora debe crear la variante. |  |
| 10 | Crear variante | Para crear Variante , de nuevo abierto Crear material (MM01) y siga los pasos anteriores para crear un nuevo material con Datos básicos 1 y Datos básicos 2 . |  |  |
| 11 | Crear variante | En Datos básicos 2 ir a Configuración específica de cliente e introduzca el material configurable creado anteriormente en la Mat.conf.vál.p.tod.ce. y haga clic en Configurar variante y, a continuación, seleccione el valor de característica necesario para configurar variantes. | Se crea la variante. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le llevará a Producto vista.Haga clic en Editar . | Producto se visualiza en edición modo (los campos están listos para su entrada). |  |
| 3 | Hacer que el producto sea configurable | En la Producto vista, vaya a Configuración y verifique la El producto es configurable casilla de selección. |  |  |
| 4 | Asignar clase de variante | En la Producto vista, vaya a Clasificación y seleccione Haga clic en aquí para asignar una clase y, a continuación, seleccione una clase del tipo 300 (Variante). | Se visualizarán las características de la clase asignada. |  |
| 5 | Seleccionar características | Seleccione los valores de característica necesarios para cada una de las características. |  |  |
| 6 | Ir a la pestaña Variantes | En la Producto vista, vaya a Variantes y seleccione Seleccionar Variantes de producto . | Se visualizará un árbol/tabla con las diferentes características. |  |
| 7 | Seleccionar características y crear variantes | Seleccione la combinación de valores de característica y haga clic en Aplicar . | Se crearán variantes. |  |
| 8 | Grabar | Seleccionar Grabar . | El sistema emite una notificación de que el objeto se ha guardado. |  |

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

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Modificar material

Siga este procedimiento cuando su acceso de usuario le presente el Modificar material (MM02) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Modificar material (MM02) . | El Modificar material (pantalla inicial) se visualiza. |  |
| 2 | Introducir número de material | Realice la siguiente entrada y seleccione Seleccionar vista(s) :Número de material : <Número de material> | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 .Seleccionar Continuar . | El Modificar material (producto terminado) se visualiza. |  |
| 4 | Seleccionar servicios para objeto | En la barra de herramientas de la aplicación, vaya a Servicios para objeto > Crear anexo . | El Importar archivo se visualiza. |  |
| 5 | Seleccione Cargar. | El Importar archivo , seleccione Cargar . | Se muestra una pantalla de carga de archivos. |  |
| 6 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se carga el archivo. |  |
| 7 | Grabar | Seleccionar Seleccionar y luego Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le lleva a la Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar anexos | El Producto vaya a la pantalla Anexos pestaña. | El Anexos se visualiza. |  |
| 4 | Seleccione Cargar. | En el Sistema de gestión de documentos sección, seleccione Cargar . | Se muestra una pantalla de carga de archivos. |  |
| 5 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se carga el archivo. |  |
| 6 | Grabar | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Ventas de centro / Datos generales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un maestro de materiales (productos) datos. Las aplicaciones disponibles dependen de su rol asignado, por lo que hay dos opciones Se proporcionan .

Requisito previo

Debe completar el procedimiento anterior, Creación de material (producto) Datos maestros - Datos básicos , antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de datos básicos, como se describe en la Procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | Crear material (pantalla inicial) se abre. |  |
| 2 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Material número>Ramo : MNota Si el Ramo introduzco el campo está oculto, no se requiere ninguna entrada. Cuando el No se ofrece el ramo para la entrada, el campo se rellena con en la oscuridad.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | Seleccionar vista(s) Se abre la pantalla. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) selección de ventana Básico Datos y Ventas: General/Centro Datos y seleccione continuar . | Niveles de organización aparece |  |
| 4 | Introducir datos de niveles de organización | En la pantalla Niveles de organización, en el Nivel de organización sección, realice las siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (producto terminado) Se abre la pantalla. |  |
| 5 | Introducir datos en Datos básicos 1 | En la vista Datos básicos 1, efectúe las siguientes entradas y seleccione Intro :Descripción : Actualizar descripción para productoUnidad base : Actualizar unidad base "EA" por ejemplo 1 |  |  |
| 6 | Introducir datos en Ventas: General/Centro | En la Datos de expedición (tiempos en días) Sección realice la siguiente entrada:Gr.carga : elegir cualquiera valor de la ayuda para entradas |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) | El Gestionar datos maestros de producto (F1602) aplicación se abre y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto por introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | En la Producto , seleccione Centros | El Centros se visualiza. |  |
| 4 | Seleccione Crear. | En la Centros , seleccione Crear . |  |  |
| 5 | Introducir centros - Datos generales | En la sección Datos generales, efectúe las siguientes entradas:Centro : Centro número por ejemplo, 1710 |  |  |
| 6 | Introducir datos de planificación de necesidades | En la Sección MRP , haga lo siguiente entradas:Caract.planif.nec. : ejemplo ND |  |  |
| 7 | Introducir centro - ventas | En la Sección Ventas hacer seguimiento entradas:Grupo de carga : seleccionar del valor ayuda |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver a Producto vista. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto es grabado . |  |

### Crear datos maestros de producto - Centro / Fabricación repetitiva

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de producto. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el El ramo no se ofrece para la entrada, el campo está atenuado.Tipo de material : FERTSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 , MRP 1 , y Planif.necesidades 4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice las siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos en Datos básicos 1 | El Datos básicos 1 , efectúe las siguientes entradas y pulse Intro :Descripción : <Descripción del producto>Unidad base : Actualizar unidad base UN , por ejemplo, 1 . |  |  |
| 6 | Introducir datos en MRP 1 | En la Método de planificación de necesidades , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
| 7 | Introducir datos en MRP 4 | En la Fabricación repetitiva/montaje/estrategia de despliegue sección, haga lo siguiente entradas:Fabricación repetitiva : marque la casilla de selección.Perfil fabricación repetitiva : <Seleccione cualquier valor de la ayuda para entradas> |  |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto , seleccione Centros . | El Centros se visualiza. |  |
| 4 | Seleccione Crear. | El Centros , seleccione Crear . |  |  |
| 5 | Introducir centros - Datos generales | En la Datos generales , realice la siguiente entrada:Centro : <Número de centro> , por ejemplo, 1710 |  |  |
| 6 | Introducir datos de planificación de necesidades | En la MRP , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
| 7 | Introducir datos de fabricación repetitiva | En la Fabricación repetitiva , realice las siguientes entradas:Fabricación repetitiva activada : marque la casilla de selección para activar el Perfil de fabricación repetitiva campo.Perfil de fabricación repetitiva : <Seleccione cualquier valor del valor ayuda> | Si marca la casilla de selección Fabricación repetitiva activada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser editable.Si desmarca la casilla de selección Fabricación repetitiva activada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser de solo lectura. |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

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
> Flagged while digesting this document, not verified: Machine-translated text has errors (e.g. 'Pos también', 'En la oscuridad' for dimmed/greyed out field); some steps say field is filled/dimmed inconsistently

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document title in batch metadata is 'Objetivo' (a heading), real title taken from cover

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnt-675]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnt-673]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 64,008 chars in the whole document
