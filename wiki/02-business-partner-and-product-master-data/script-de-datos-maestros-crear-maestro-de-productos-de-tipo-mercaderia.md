---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia
title: "Script de datos maestros - Crear maestro de productos de tipo \"Mercadería\" (BNF) (BNF_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 test script for creating a Merchandise product master via MM01 or F1602, by data view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-trading-goods]
aliases: [BNF_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Trading Goods", product master data, material master creation, basic data, sales data, purchasing data, mrp planning data, warehouse data, accounting valuation data, configurable products]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-594
topic: 02-business-partner-and-product-master-data/product-master-trading-goods
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear maestro de productos de tipo "Mercadería" (BNF) (BNF_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Trading Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear maestro de productos de tipo "Mercadería" - MDS (BNF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894916)

[2 Requisitos previos 3](#_Toc233894917)

[2.1 Acceso al sistema 3](#_Toc233894918)

[2.2 Roles 3](#_Toc233894919)

[2.3 Unidades organizativas necesarias 3](#_Toc233894920)

[2.4 Datos maestros obligatorios y operativos 5](#_Toc233894921)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233894922)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233894923)

[2.5.2 Ramo 5](#_Toc233894924)

[3 Tabla de resumen 6](#_Toc233894925)

[4 Procedimientos de prueba 7](#_Toc233894926)

[4.1 Crear datos maestros de material (producto) - Datos básicos 7](#_Toc233894927)

[4.2 Crear datos maestros de material (producto) - Datos de ventas (datos de IVA) 10](#_Toc233894928)

[4.3 Crear datos maestros de material (producto) - Datos de compras 14](#_Toc233894929)

[4.4 Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro) 16](#_Toc233894930)

[4.5 Crear datos maestros de material (producto) - Datos de almacén 20](#_Toc233894931)

[4.6 Crear datos maestros de material (producto) - Datos de contabilidad (datos de área de valoración) 22](#_Toc233894932)

[4.7 Crear datos maestros de producto - Producto configurable y variantes 25](#_Toc233894933)

[4.8 Crear datos maestros de producto - Guardar anexos 28](#_Toc233894934)

[4.9 Crear datos maestros de producto - Ventas de centro / Datos generales 30](#_Toc233894935)

[4.10 Crear datos maestros de producto - Centro / Fabricación repetitiva 32](#_Toc233894936)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

El maestro de materiales o productos contiene información sobre todos los materiales físicos que se aprovisionan, producen, almacenan y venden. Pos también se utiliza para gestionar información sobre servicios, por ejemplo, para la compra y venta de servicios en horas.

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

Algunos segmentos de datos maestros de material dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Descripción de material (texto breve), Número de material, Grupo de artículos, unidad de medida base, etc. | Datos básicos solo existe una vez para un registro de datos maestros de material. | n/d |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales, Grupo de tipos de posición, Tipo de Grupo, carga Grupo, tiempo de preparación, etc. | Pueden existir datos de ventas para cada organización de ventas de su estructura empresarial para la que se utiliza el registro maestro de materiales. | Centro:____________Organización de ventas:__________Canal de distribución:__________ |
| Datos de compras | Centro | Grupo de compras, grupo de artículos, procesamiento de EM hora, etc. | Los datos de compras pueden existir para cada organización de compras para la que se debe utilizar el material en los procesos de compras. | Centro:__________ |
| Datos de planificación/MRP | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Entrega planificada hora, etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función de la necesidad de realizar una planificación específica de almacén | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. rest. Estantería, etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para los que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del necesita realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Datos de contabilidad | Área de valoración (=centro), clase de valoración | Clase de valoración, por precio por unidad, precio Control, etc. | Los datos del área de valoración pueden existir para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, un precio de valoración diferente de un material en diferentes centros) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y operativos

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de material.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

En esta sección, se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear un registro de datos maestros de material:

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizar o qué campos son obligatorios u opcionales. En función de los tipos de material, el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos los tipos de material utilizan la misma definición de rango de números

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe ser superior a 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un número numérico a un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M . Actualmente, este es visible solo en SAP GUI.

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos básicos. |
| [Crear datos maestros de material (producto) - Datos de ventas (datos de IVA)](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de ventas. |
| [Crear datos maestros de material (producto) - Datos de compras](#unique_13) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de compras. |
| [Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)](#unique_14) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material - Datos de planificación/MRP. |
| [Crear datos maestros de material (producto) - Datos de almacén](#unique_15) [página ] 20 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean los datos de almacén. |
| [Crear datos maestros de material (producto) - Datos de contabilidad (datos de área de valoración)](#unique_16) [página ] 22 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Datos de contabilidad (datos de área de valoración). |
| [Crear datos maestros de producto - Producto configurable y variantes](#unique_17) [página ] 25 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Crear producto configurable y variantes. |
| [Crear datos maestros de producto - Guardar anexos](#unique_18) [página ] 28 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Grabar anexos en el registro maestro de materiales. |
| [Crear datos maestros de producto - Ventas de centro / Datos generales](#unique_19) [página ] 30 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |
| [Crear datos maestros de producto - Centro / Fabricación repetitiva](#unique_20) [página ] 32 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear datos maestros de material (producto) - Datos básicos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 .Seleccionar Continuar . | El Crear material...(mercaderías) se visualiza. |  |
| 5 | Introducir datos básicos | El Material...(mercaderías) pantalla, en la pantalla Datos básicos 1 introduzca la etiqueta Descripción de material (texto breve) . |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 en la pestaña Datos generales sección, haga lo siguiente entradas:Unidad de medida base : <Unidad de medida base>Grupo de materiales : <Grupo de artículos>Gr.tp.pos.gen. : <GenItemCatGroup> |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN , realice las siguientes entradas:Peso bruto : <Peso bruto>Unidad de peso : <Unidad de peso>Peso neto : <Peso neto>Pulsar Intro . | El Datos básicos 2 se visualiza. |  |
| 8 | Completar datos básicos | El Datos básicos 2 no es necesario realizar ninguna entrada. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar para guardar los datos. | El Crear material (pantalla inicial) se visualiza.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear producto. | El Gestionar datos maestros de producto , seleccione Crear producto . | El Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir datos para campos obligatorios | El Crear datos maestros , efectúe las siguientes entradas:Número de producto : Por ejemplo, Z … o cualquier ID alfanumérico externo. Pos debe empezar con un carácter o sin entrada y, a continuación, el sistema asignará un ID numérico automáticamente.Nota Para obtener más información sobre el número de producto, consulte el anterior [Tipo de material y rangos de números](#unique_8) [página ] 5 capítulo.Tipo de producto : MercaderíasGrupo de productos : Por ejemplo, L001 .Unidad base : Por ejemplo, UN .Descripción : <Cualquier descripción> |  |  |
| 5 | Seleccione OK. | El Gestionar maestro de productos , seleccione OK . | El Gestionar maestro de productos se visualiza. |  |
| 6 | Introducir datos básicos | Vaya a Gestionar maestro de productos > DATOS BÁSICOS > Datos básicos y realice la siguiente entrada:Sector : Por ejemplo 00 . |  |  |
| 7 | Seleccione Crear. | Vaya a Gestionar maestro de productos > DATOS BÁSICOS > Descripciones y seleccione Crear . | Se muestra la descripción en el idioma predeterminado (por ejemplo, inglés). |  |
| 8 | Introducir datos de descripciones | El Descripciones , efectúe las siguientes entradas:Idioma : Por ejemplo, Alemán .Descripción de producto : <Descripción del producto> |  |  |
| 9 | Volver a la pantalla principal | Seleccione la flecha hacia atrás para volver a la pantalla principal. | El Maestro de productos se visualiza. |  |
| 10 | Seleccionar unidad de medida base | Ir a Gestionar maestro de productos > DATOS BÁSICOS y seleccione Unidad de medida base . |  |  |
| 11 | Volver a la pantalla principal | Seleccione la flecha hacia atrás para volver a la pantalla principal. | El Maestro de productos se visualiza. |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (producto) - Datos de ventas (datos de IVA)

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Ventas: Datos org.ventas 1 , Ventas: Datos org.ventas 2 , y Ventas: Datos generales/de centro .Seleccionar Continuar .Nota Solo para Polonia : seleccionar también Comercio exterior: Datos de exportación para introducir Número de clasificación PKWiU. | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:CentroOrg.ventasCanal distrib.Seleccionar Continuar .Nota El mensaje del sistema muestra que El material ya existe y se ampliará . | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos de ventas | El Material...(mercaderías) pantalla, en la pantalla Ventas: org.ventas 1 ficha, en el Datos generales , realice las siguientes entradas:Unidad de medida baseCentro suministrador |  |  |
| 6 | Introducir datos de ventas | El Material...(mercaderías) pantalla, en la pantalla Ventas: org.ventas 1 ficha, en el Datos fiscales , realice la siguiente entrada:Clasificación fiscal : 1Nota El valor introducido indica que el material está (normalmente) totalmente sujeto a impuestos.Solo para Brasil :En la Datos fiscales , realice las siguientes entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : Cualquiera 1 para material o 2 para los Servicios. | El Ventas: org.ventas 2 se visualiza. |  |
| 7 | Introducir datos de ventas | El Ventas: org.ventas 2 en la pestaña Conceptos de agrupación sección, haga lo siguiente entradas:Gr.estadíst.materialGrupo de tipos de posiciónMat.gr.imputación : 01 | El Ventas: General/Centro se visualiza. |  |
| 8 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos generales la sección, haga entrada siguiente:Verificación de disponibilidad : PE |  |  |
| 9 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos de expedición (tiempos en días) , realice las siguientes entradas:Gpo.transp. : <0001>Gr.carga : <0001> |  |  |
| 10 | Introducir datos de ventas | En la Parámetros generales de centro , realice la siguiente entrada:Centro de beneficio : <Centro de beneficio>Nota Para el SerialNoProfile , seleccione un perfil de número de serie válido que se haya asignado con el tipo de equipo adecuado para su empresa. |  |  |
| Solo para Polonia | Introducir datos de ventas | Solo para Polonia :En la Comercio internacional: Exportación , realice la siguiente entrada:Código de control : Por ejemplo, 26.70.13.0 . | Se actualiza el código PKWiU para Polonia. |  |
| 11 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar cadenas de distribución | El Producto seleccione el pulsador Cadenas de distribución pestaña. | El Cadenas de distribución se visualiza. |  |
| 4 | Seleccione + (Añadir) | El Cadenas de distribución , seleccione + (Añadir) . | El Cadenas de distribución se visualiza en modo de edición. |  |
| 5 | Introducir datos de cadenas de distribución | El Cadenas de distribución , efectúe las siguientes entradas:En la DATOS GENERALES - Información general sección:Organización de ventas : <Número de organización de ventas>Nota El valor de Unidad organizativa viene determinado por lo que se ofrece en la ayuda para entradas.Canal de distribución : Por ejemplo 10 .Centro de entrega : <Centro número>En la TÉRMINOS DE AGRUPACIÓN sección:Grupo de tipos de posición : Por ejemplo, NORM .Grupo de imputación : Por ejemplo, 01 Mercaderías .En la IMPUESTO SOBRE VENTAS sección:País : <Código de país>Categoría fiscal : Por ejemplo, TTX1 .Clasificación fiscal : Por ejemplo, 1 para material o 2 para los Servicios.Clasificación fiscal : Por ejemplo, 1 Impuesto completo al utilizar la condición para determinación de impuestos UTXJ para EE. UU.Nota La clasificación fiscal depende de los requisitos específicos del país/región. Clasificación fiscal en el material Las tablas Maestro y Maestro de clientes determinan las entradas de porcentaje.Solo para Brasil :En la Clasificación fiscal , realice las siguientes entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : Cualquiera 1 para material o 2 para Servicios. |  |  |
| 6 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 7 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (producto) - Datos de compras

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Compras y seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice la siguiente entrada:Centro : <Número de centro>Seleccionar Continuar .Nota El mensaje del sistema muestra que El material ya existe y se ampliará . | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos de compras | El Material...(mercaderías) pantalla, en la pantalla Compras en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida base : Por ejemplo KG .Grupo de compras : Por ejemplo, 001 .Grupo de materiales : Por ejemplo, L001 . |  |  |
| 6 | Introducir datos de compras | En la Otros datos/datos del fabricante , realice la siguiente entrada:Tmpo.tratam.EM : Por ejemplo, 1 . |  |  |
| 7 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de compras | El Producto , seleccione Compras . | El Compras se visualiza. |  |
| 4 | Introducir datos de compras | El Compras , efectúe las siguientes entradas:Clave de valor de compras : Por ejemplo, 1 .Estado de unidad de pedido variable : ActivoEn la sección de datos de cabecera, seleccione Editar cabecera y realice la siguiente entrada:Grupo de productos : Por ejemplo, L001 . |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione MRP1 , MRP2 , MRP3 , y MRP4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : <Número de centro>Almacén : <Número de almacén> | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos de planificación/MRP | El Crear material... (mercaderías) pantalla, en la pantalla MRP1 en la pestaña Datos generales , realice las siguientes entradas:Caract.planif.nec. : PDPlanificador de necesidades : <001>Nota El mensaje del sistema muestra que El material ya existe y se ampliará . |  |  |
| 6 | Introducir datos de planificación/MRP | En la Datos de tamaño de lote , realice la siguiente entrada:Cálculo del tamaño del lote : <EX> | El Planif.necesidades 2 se visualiza. |  |
| 7 | Introducir datos de planificación/MRP | El Crear material... (mercaderías) pantalla, en la pantalla Planif.necesidades 2 en la pestaña Programación , realice las siguientes entradas:Plazo de entrega previsto : Por ejemplo, 3 .Tmpo.tratam.entr.mcía. : Por ejemplo, 1 .Clave de horizonte : Por ejemplo, 000 . | El Planif.necesidades 3 se visualiza. |  |
| 8 | Introducir datos de planificación/MRP | El Crear material... (mercaderías) pantalla, en la pantalla Planif.necesidades 3 en la pestaña Planificación , realice la siguiente entrada:Grupo de estrategias : Por ejemplo, 40 . |  |  |
| 9 | Introducir datos de planificación/MRP | En la Verificación de disponibilidad , realice las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Plazo reaprov.total : Por ejemplo, 3 . | El Planif.necesidades 4 se visualiza. |  |
| 10 | Introducir datos de planificación/MRP | El Crear material... (mercaderías) pantalla, en la pantalla Planif.necesidades 4 en la pestaña Explosión de la lista de materiales/necesidades secundarias , realice la siguiente entrada:Sol.indiv./colect. : 1 |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto , seleccione Centros . | El Centros se visualiza. |  |
| 4 | Seleccione Crear. | El Centros , seleccione Crear . | El Centro se visualiza en modo de edición. |  |
| 5 | Introducir datos generales | En la Datos generales , realice las siguientes entradas:Centro : <Número de centro> , por ejemplo, 1710Centro de beneficio : Por ejemplo, YB700 .Gr.carga : Por ejemplo, 0001 . |  |  |
| 6 | Introducir datos de planificación de necesidades | Vaya a Datos de planificación de necesidades > Datos MRP y realice las siguientes entradas:Verificación de disponibilidad : Por ejemplo, PE .Caract.planif.nec. : Por ejemplo, PD .Planificador de necesidades : Por ejemplo, 001 . |  |  |
| 7 | Introducir datos de tamaño de lote | En la Datos MRP > Datos de tamaño de lote , realice la siguiente entrada:Cálculo del tamaño del lote : Por ejemplo EX . |  |  |
| 8 | Introducir datos de aprovisionamiento | Vaya a Datos de planificación de necesidades > Aprovisionamiento y realice las siguientes entradas:Plazo de entrega previsto : Por ejemplo, 3 .Tiempo de procesamiento de entrada de mercancías : Por ejemplo, 1 . |  |  |
| 9 | Seleccionar datos de previsión | El Centro seleccione el pulsador Previsión pestaña. | El Previsión se visualiza. |  |
| 10 | Introducir datos de previsión | El Previsión , realice la siguiente entrada:Tipo de período : Por ejemplo, Mensual . |  |  |
| 11 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (producto) - Datos de almacén

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas:Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, efectúe las siguientes entradas:Centro : <Número de centro>Almacén : <Número de almacén>Nota El mensaje del sistema muestra que El material ya existe y se ampliará . | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos de almacén | El Crear material... (mercaderías) pantalla, en la pantalla Dat.ce./almacén 1 pestaña, en el Datos generales , realice la siguiente entrada:Número de vales de entrada de mercancías : Por ejemplo, 1 . | El Dat.ce./alm.2 se visualiza. |  |
| 6 | Confirmar entradas | El Dat.ce./Almacén 2 no es necesario realizar ninguna entrada.Nota Para el Perfil de número de serie seleccione un perfil de número de serie válido que se haya asignado con la categoría de equipo adecuada para su negocio. |  |  |
| 7 | Guardar los datos | Seleccionar Grabar . | El Datos maestros: Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto seleccione el pulsador Centros pestaña.Nota Si no hay ningún registro de datos de centro, siga los pasos del capítulo anterior. [Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)](#unique_14) [página ] 16. | El Centros se visualiza. |  |
| 4 | Seleccionar detalles de centro | El Centros utilice el icono de flecha para seleccionar los datos de centro que ha creado en el paso anterior. | El Centro se visualiza. |  |
| 5 | Navegar a Centro: Almacenes | El Centro pantalla, vaya a Almacenes > Almacenes . |  |  |
| 6 | Seleccione Crear. | Ir a Almacenes > Almacenes y seleccione Crear . | El Centro - Almacén se visualiza en modo de edición. |  |
| 7 | Introducir centro: Datos de almacén | El Almacenes , efectúe la siguiente entrada:Almacén : <Número de almacén> |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar dos veces para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (producto) - Datos de contabilidad (datos de área de valoración)

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas:Contabilidad 1Contabilidad 2Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice la siguiente entrada:Centro : <Centro>Nota La información se muestra en la parte inferior de la pantalla: El material ya existe y se ampliado . | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos de contabilidad | El Crear material... (mercaderías) pantalla, en la pantalla Contabilidad 1 ficha, en el Datos de valoración generales , realice la siguiente entrada:Categoría de valoración : <número> |  |  |
| 6 | Introducir datos | En la Precios y valores , realice las siguientes entradas:Precio por unidad : por ejemplo, 20Control de precio : por ejemplo, V | El Contabilidad 2 se visualiza. |  |
| 7 | Confirmar entradas | No es necesario realizar ninguna entrada en el Contabilidad 2 pestaña. |  |  |
| 8 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) . | Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto entrando Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le llevará a Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de área de valoración | En la Producto , seleccione la vista Áreas de valoración pestaña. | El Áreas de valoración se visualiza. |  |
| 4 | Seleccione Crear. | En la Áreas de valoración sección, seleccione Crear . | Valoración se abre en modo de edición. |  |
| 5 | Introducir datos de área de valoración | En la Valoración , efectúe las siguientes entradas:Área de valoración : <número de área de valoración>Determinación de control de precio : 2Categoría de valoración : por ejemplo, 3100 |  |  |
| 6 | Introducir datos de área de valoración actual | Ir a ÁREAS DE VALORACIÓN > Valoración y realice las siguientes entradas:Precio de inventario : por ejemplo, 20Indicador de control de precio : por ejemplo, VNota Cuando introduce V como Indicador de control de precio, el valor añadido en Precio de inventario se convierte en Precio medio variable. Cuando introduce S como el Indicador de control de precio, el valor añadido en El Precio de inventario se convierte en Precio estándar. |  |  |
| 7 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto vista. | El Gestionar maestro de productos se visualiza. |  |
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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos básicos 1Datos básicos 2Clasificación |  |  |
| 4 | Introducir datos básicos | El Material (producto terminado) pantalla, en la pantalla Datos básicos 1 introduzca la etiqueta Descripción de material (texto breve) y Unidad de medida base .Pulsar Intro . | El Datos básicos 2 se visualiza. |  |
| 5 | Introducir datos básicos | El Datos básicos 2 , verifique la El material es configurable casilla de selección.Pulsar Intro . | El Clasificación y la ficha Categoría de clase se visualiza la ventana de diálogo. |  |
| 6 | Seleccionar categoría de clase | En la Categoría de clase seleccione Categoría de clase 300 (variante) y seleccione Continuar . | El Clasificación se visualiza. |  |
| 7 | Asignar clase | En la Asignación sección, asigne una clase y pulse Intro . | Las características correspondientes se visualizan en el Asignación sección. |  |
| 8 | Seleccionar valores de característica | Seleccione los valores necesarios para las características. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Se crea el material configurable. |  |
| 10 | Crear variante | Para crear un Variante , abra el Crear material (MM01) de nuevo y siga lo anterior pasos para crear un nuevo material con Datos básicos 1 y Datos básicos 2 . |  |  |
| 11 | Crear variante | El Datos básicos 2 pestaña, vaya a Configuración específica de cliente e introduzca el creado anteriormente Material configurable en la Mat.conf.vál.p.tod.ce. , seleccione Configurar variante y, a continuación, seleccione el valor de Características necesario para configurar las variantes. | Se crea la variante. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Hacer que el producto sea configurable | El Producto vaya a la pantalla Configuración y verifique la El producto es configurable casilla de selección. |  |  |
| 4 | Asignar clase de variante | El Producto vaya a la pantalla Clasificación , seleccione Haga clic en aquí para asignar una clase y, a continuación, seleccione una clase de tipo 300 (variante) . | Se visualizan las características de la clase asignada. |  |
| 5 | Seleccionar características | Seleccione los valores de característica necesarios para cada una de las características. |  |  |
| 6 | Ir a la pestaña Variantes | El Producto vaya a la pantalla Variantes y seleccione Seleccionar Variantes de producto . | Se visualiza un árbol/tabla con las diferentes características. |  |
| 7 | Seleccionar características y crear variantes | Seleccione la combinación de valores de característica y seleccione Aplicar . | Se crean variantes. |  |
| 8 | Grabar | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con este capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria El sector no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 .Seleccionar Continuar . | El Crear material (producto terminado) se visualiza. |  |
| 4 | Seleccionar servicios para objeto | En la barra de herramientas de la aplicación, vaya a Servicios para objeto > Crear anexo . | El Importar archivo se visualiza. |  |
| 5 | Seleccione Cargar. | El Importar archivo , seleccione Cargar . | Se muestra una pantalla de carga de archivos. |  |
| 6 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se ha cargado el archivo. |  |
| 7 | Grabar | Seleccionar Seleccionar y Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo la Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar anexos | El Producto vaya a la pantalla Anexos pestaña. | El Anexos se visualiza. |  |
| 4 | Seleccione Crear. | En el Sistema de gestión de documentos sección, seleccione Crear . | Se muestra una pantalla de carga de archivos. |  |
| 5 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se ha cargado el archivo. |  |
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

El siguiente procedimiento proporciona instrucciones sobre cómo crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el El ramo no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos y Ventas: Datos generales/de centro .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, haga lo siguiente entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos en Datos básicos 1 | El Datos básicos 1 , efectúe las siguientes entradas y pulse Intro :Descripción : <Descripción del producto>Unidad base : Actualizar unidad base UN , por ejemplo, 1 . |  |  |
| 6 | Introducir datos | En la Datos de expedición (tiempos en días) , realice la siguiente entrada:Gr.carga : <Seleccione cualquier valor de la ayuda para entradas> |  |  |
| 7 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

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
| 7 | Introducir centro - ventas | En la Ventas , realice la siguiente entrada:Grupo de carga : <Seleccione de la ayuda para entradas> |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

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

Debe completar el capítulo anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto capítulo.

Siga el procedimiento después de guardar el Datos básicos entradas, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Crear material

Siga este procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | Se abre la aplicación. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el El ramo no se ofrece para la entrada, el campo está atenuado.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 , MRP 1 , y Planif.necesidades 4 .Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice las siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (mercaderías) se visualiza. |  |
| 5 | Introducir datos en Datos básicos 1 | El Datos básicos 1 , efectúe las siguientes entradas y pulse Intro :Descripción : <Descripción del producto>Unidad base : Actualizar unidad base UN , por ejemplo, 1 . |  |  |
| 6 | Introducir datos MRP 1 | En la Método de planificación de necesidades , realice la siguiente entrada:Caract.planif.nec. : Por ejemplo, ND . |  |  |
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
| 7 | Introducir datos de fabricación repetitiva | En la Fabricación repetitiva , realice las siguientes entradas:Fabricación repetitiva activada : marque la casilla de selección para activar el Fabricación repetitiva Perfil campo.Perfil de fabricación repetitiva : <Seleccione cualquier valor de la ayuda para entradas> | Si marca la casilla de selección Fabricación repetitiva activada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser editable.Si desmarca la casilla de selección Fabricación repetitiva activada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser de solo lectura. |  |
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
> Flagged while digesting this document, not verified: Machine-translated and unreviewed; terminology may differ from other SAP documents or the English original

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document title extracted as 'Objetivo' (first heading) rather than real title

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bnf-597]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnf-595]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 67,597 chars in the whole document
