---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate
title: "Script de datos maestros: Creación de maestro de productos de tipo \"Material no de almacén\" - MDS (31Y) (31Y_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (31Y): test steps to create a non-stock material via MM01 or F1602 (basic, sales, purchasing, accounting)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-non-stock-and-service]
aliases: [31Y_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Non-Stock Materials and Service Products", non-stock material, material master data, basic data, sales data, purchasing data, accounting data, business roles, organizational units, material types]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-312
topic: 02-business-partner-and-product-master-data/product-master-non-stock-and-service
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Creación de maestro de productos de tipo "Material no de almacén" - MDS (31Y) (31Y_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Non-Stock Materials and Service Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Material no de almacén" - MDS (31Y) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894596)

[2 Requisitos previos 3](#_Toc233894597)

[2.1 Acceso al sistema 3](#_Toc233894598)

[2.2 Roles 3](#_Toc233894599)

[2.3 Unidades organizativas necesarias 3](#_Toc233894600)

[2.4 Datos maestros obligatorios y operativos 4](#_Toc233894601)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233894602)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233894603)

[2.5.2 Ramo 5](#_Toc233894604)

[3 Tabla de resumen 6](#_Toc233894605)

[4 Procedimientos de prueba 7](#_Toc233894606)

[4.1 Crear datos maestros de material (no de almacén) - Datos básicos 7](#_Toc233894607)

[4.2 Crear datos maestros de material (no de almacén) - Datos de ventas (datos de IVA) 10](#_Toc233894608)

[4.3 Crear datos maestros de material (no de almacén) - Datos de compras 13](#_Toc233894609)

[4.4 Crear datos maestros de material (no de almacén) - Datos de contabilidad (datos de área de valoración) 16](#_Toc233894610)

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
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. Su administrador del sistema proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

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
| Datos básicos | Independiente de las unidades organizativas | Descripción de material (texto breve), Número de material, Grupo de artículos, unidad de medida base, y así on. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales, Grupo de tipos de posición, Tipo de Grupo, carga Grupo, tiempo de preparación, etc. | Pueden existir datos de ventas para cada organización de ventas de su estructura empresarial para la que el material se utiliza el registro maestro. | Centro:____________Organización de ventas:__________Canal de distribución:__________ |
| Datos de compras | Centro | Grupo de compras, grupo de artículos, procesamiento de EM hora, etc. | Pueden existir datos de compras para cada organización de compras para qué material se debe utilizar en compras procesos. | Centro:__________ |
| Datos de contabilidad | Área de valoración (=centro), clase de valoración | Clase de valoración, por precio por unidad, precio Control, etc. | Pueden existir datos de área de valoración para cada ID de centro de su estructura de la empresa para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, valoración diferente). precio de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y operativos

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un maestro de materiales registro de datos.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un registro maestro y siempre son necesarios para crear un registro de datos maestros de material.

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizados o qué campos son obligatorios u opcionales. En función de los tipos de material, el el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos Los tipos de material utilizan la misma definición de rango de números.

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe ser más de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un Número numérico de un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M . Actualmente, solo es visible en SAP GUI.

## Tabla de resumen

En esta sección, se proporciona una lista de pasos por los que pasa un usuario al crear un registro de datos maestros. Cada segmento lógico y significativo de un objeto de datos maestros debe llevar a un paso separado (por ejemplo, segmentos de datos dependientes de la unidad organizativa, etc.).

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de material (no de almacén) - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos básicos. |
| [Crear datos maestros de material (no de almacén) - Datos de ventas (datos de IVA)](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de ventas. |
| [Crear datos maestros de material (no de almacén) - Datos de compras](#unique_13) [página ] 13 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de compras. |
| [Crear datos maestros de material (no de almacén) - Datos de contabilidad (datos de área de valoración)](#unique_14) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Datos de contabilidad (datos de área de valoración). |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este alcance posición.

### Crear datos maestros de material (no de almacén) - Datos básicos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material (MM01) . | El Crear material (MM01) se visualiza. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial)Material : Número de materialRamo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : Material no de almacénHaga clic en Seleccionar vista(s) . | Aparece una ventana nueva, Seleccionar vista(s) . |  |
| 4 | Seleccionar vistas | En Seleccionar vista(s) , seleccione Datos básicos 1 y seleccione continuar . | Crear material... (material no de almacén) se abre. |  |
| 5 | Introducir datos básicos | De Material...(Material no de almacén) , en la Datos básicos 1 introduzca un Descripción de material (texto breve) . |  |  |
| 6 | Introducir datos básicos | Desde el Datos básicos 1 en la pestaña Datos generales introduzca las descripciones para lo siguiente:Unidad de medida baseGrupo de materialesGr.tp.pos.gen. |  |  |
| 7 | Guardar los datos | En la parte inferior derecha de la pantalla, seleccione Grabar para guardar los datos. | El Crear material (pantalla inicial) aparece.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Crear nuevo maestro de productos. | Seleccionar Crear . | El Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir datos para campos obligatorios | En la Crear registro de datos maestros inicial, efectúe las siguientes entradas:Número de producto : por ejemplo, Z …Puede introducir cualquier ID alfanumérico externo y ese ID debe empezar por un carácter alfanumérico o, si no proporciona ninguna entrada, el sistema asignará automáticamente un ID numérico.Para obtener más información sobre el número de producto, consulte el anterior Tipo de material y rangos de números sección.Tipo de producto : NLAGGrupo de productos : por ejemplo, YBPM01Unidad base : por ejemplo, UNDescripción : cualquier descripción |  |  |
| 5 | Seleccione OK. | En la Gestionar maestro de productos , seleccione OK . | El Gestionar maestro de productos se visualiza. |  |
| 6 | Introducir datos básicos | En la Gestionar maestro de productos > DATOS BÁSICOS > Vista Datos básicos , realice la siguiente entrada:Sector : por ejemplo 00 |  |  |
| 7 | Seleccione Añadir (+) | En la Gestionar maestro de productos > DATOS BÁSICOS > Vista Descripciones , pantalla, seleccione + (Añadir) . | El Maestro de productos: Descripción Aparece la vista.Algunos campos ya se han rellenado con datos del paso anterior. |  |
| 8 | Introducir datos de descripciones | En la Descripciones , efectúe las siguientes entradas:Idioma : por ejemplo, AlemánDescripción de producto : <su descripción> |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que el objeto se ha guardado. |  |

### Crear datos maestros de material (no de almacén) - Datos de ventas (datos de IVA)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear el material ( Material no de almacén ) datos maestros. Las aplicaciones disponibles son en función de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, Creación de material (no gestionado en stock) Material) Datos maestros: Datos básicos , antes de continuar con esto sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) se visualiza. |  |
| 3 | Introducir datos básicos de material | En la Crear material (vista inicial) hacer el siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo no está se ofrece para la entrada, el campo se rellena con en el oscuro .Tipo de material : NLAG no gestionado en stock MaterialHaga clic en Seleccionar vista(s) . | Después de completar las entradas, se abre una ventana nueva, Seleccionar Vista(s) |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) selección de ventana Ventas: Datos org.ventas 1 , Ventas: Org.ventas Datos 2 y Ventas: General/Centro Datos y seleccione continuar .Nota Solo para Polonia: seleccione también Comercio exterior: Exportación Datos para introducir el número de clasificación PKWiU. | Una ventana con Niveles de organización muestra |  |
| 5 | Introducir datos de niveles de organización | En Niveles de organización , en la Nivel de organización sección, introduzca descripciones para lo siguiente:CentroOrg.ventasCanal distrib.Seleccionar Continuar .Nota La información aparece en la parte inferior de la vista: El El material ya existe y se ampliará . | Crear material... (material no de almacén) ver muestra... |  |
| 6 | Introducir datos de ventas | En Material...(Material no de almacén) , del Ventas: org.ventas 1 en la pestaña Datos generales sección, haga lo siguiente entrada:Unidad de medida baseCentro suministrador |  |  |
| 7 | Introducir datos de ventas | En Material…(Material no de almacén) , del Ventas: org.ventas 1 en la pestaña Impuesto Datos , realice las siguientes entradas:Clasificación fiscal : 1Nota El valor introducido indica que el material es (normalmente) completamente sujeto a impuestos.Solo para Brasil: en el Datos fiscales haga que la sección siguientes entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : Cualquiera 1 para material o 2 para servicios | Ventas: org.ventas 2 muestra la pestaña |  |
| 8 | Introducir datos de ventas | El Ventas: org.ventas 2 en la pestaña Conceptos de agrupación sección, haga lo siguiente entradas:Gr.tp.pos.gen.Grupo de tipos de posiciónMat.gr.imputación | La siguiente pestaña, Ventas: General/Centro muestra. |  |
| 9 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos de expedición , introduzca lo siguiente datos:Gr.carga |  |  |
| 10 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Parámetros generales de centro sección, introduzca Datos siguientes:Centro de beneficio |  |  |
| Solo para Polonia | Introducir datos de ventas | En la Comercio internacional: Exportación sección, introduzca los siguientes datos:Código de control : por ejemplo, 26.70.13.0 | Se actualiza el código PKWiU para Polonia. |  |
| 11 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto (F1602) se visualiza. |  |
| 3 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que navegue hasta Producto vista.Haga clic en Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar cadenas de distribución | En la Producto , seleccione Cadenas de distribución pestaña. | El Cadenas de distribución se visualiza. |  |
| 5 | Seleccione Añadir (+) | En la Cadenas de distribución , seleccione + (Añadir) | Cadenas de distribución abre en Editar Modo . |  |
| No relevante para Brasil | Introducir datos de cadenas de distribución | En Cadenas de distribución , haga lo siguiente entradas:En la DATOS GENERALES - Información general sección:Organización de ventas : Org.ventas númeroNota El valor de la unidad organizativa viene determinado por lo que se ofrece en el Ayuda para entradas.Canal de distribución : por ejemplo 10Centro de entrega : Centro númeroEn la TÉRMINOS DE AGRUPACIÓN sección:Grupo de tipos de posición : por ejemplo, NLAGEn la IMPUESTO SOBRE VENTAS sección de vista:País : país códigoCategoría fiscal : por ejemplo, TTX1Clasificación fiscal : por ejemplo, o 1 para material o 2 para servicios. Impuesto Clasificación ejemplo: 1 lleno impuesto al utilizar la condición para determinación de impuestos UTXJ para los EE. UU.Nota La clasificación fiscal depende de los requisitos específicos de la país/región. Clasificación fiscal en el maestro de materiales y las tablas maestras de cliente determinan las entradas de porcentaje. |  |  |
| 6 | Volver a la vista principal | Seleccionar Aplicar para volver al Producto vista. | El Producto Aparece la vista. |  |
| 7 | Guardar los datos | Seleccionar Grabar . | Aparece un mensaje del sistema que indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (no de almacén) - Datos de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear el material ( Material no de almacén ) datos maestros. Las aplicaciones disponibles son en función de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior, Creación de material (no gestionado en stock) Material) Datos maestros: Datos básicos , antes de continuar con esto sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo no está se ofrece para la entrada, el campo se rellena con en el oscuro .Tipo de material : NLAG no gestionado en stock MaterialSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Compras y seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Nivel de organización sección, realice la siguiente entrada:Centro : Centro númeroSeleccionar Continuar .Nota Aparece un mensaje en la parte inferior de la pantalla: El material ya existe y se ampliará. | El Crear material... (material no de almacén) se visualiza. |  |
| 6 | Introducir datos de compras | El Material…(Material no de almacén) pantalla, en la pantalla Compras en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida base : por ejemplo, HGrupo de materiales : por ejemplo, YBPM02Grupo de compras : por ejemplo, 001Ind.impto.p.material : por ejemplo, 1 |  |  |
| No relevante para Brasil | Introducir datos de compras | El Material…(Material no de almacén) pantalla, en la pantalla Compras en la pestaña Otros datos / datos del fabricante , realice la siguiente entrada:Tiempo de procesamiento EM : por ejemplo, 1 |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el producto de la lista que le llevará a la Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccione Editar cabecera | En la Editar cabecera , seleccione Actualizar grupo de productos .Seleccionar OK . |  |  |
| 5 | Introducir datos de compras | En la Compras , realice la siguiente entrada:Clave de valor de compras : por ejemplo, 1 |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de material (no de almacén) - Datos de contabilidad (datos de área de valoración)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear material ( Material no de almacén ) datos maestros. Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior, Crear datos maestros de material (no de almacén) - Datos básicos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) se visualiza. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial) efectúe las siguientes entradas:Material : Número de materialRamo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para entrada, el campo se rellena con en el oscuro .Tipo de material : NLAG Material no de almacénHaga clic en Seleccionar vista(s) . | Seleccionar vista(s) se abre. |  |
| 4 | Seleccionar vistas | En Seleccionar vista(s) , seleccione las siguientes vistas:Contabilidad 1Contabilidad 2Seleccionar Continuar . | Niveles de organización se abre. |  |
| 5 | Introducir datos de niveles de organización | En la Niveles de organización en la pantalla Nivel de organización , realice las siguientes entradas:CentroNota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliará. | Crear material... (material no de almacén) se abre. |  |
| 6 | Introducir datos de contabilidad | En la Crear material... (material no de almacén) pantalla, en la pantalla Contabilidad 1 en la pestaña Datos de valoración actuales , realice la siguiente entrada:Categoría de valoración : por ejemplo, YB01Control de precio : por ejemplo, SPrecio variable : por ejemplo, 1Unidad de precio : por ejemplo, 1 |  |  |
| No relevante para Brasil | Confirmar entradas | No es necesario realizar entradas en Contabilidad 2 pestaña. |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | El Datos maestros: Producto Aparece la ventana.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto (F1602) se visualiza. |  |
| 3 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista a la que accederá Producto vista.Haga clic en Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar datos de área de valoración | En la Producto , seleccione Áreas de valoración pestaña. | El Áreas de valoración se visualiza. |  |
| 5 | Seleccione Añadir (+) | En la Áreas de valoración sección, seleccione + (Añadir) . | Valoración abre en Modo de edición. |  |
| 6 | Introducir datos de área de valoración | En Valoración , efectúe las siguientes entradas:Área de valoración : número de área de valoraciónCategoría de valoración : por ejemplo, YB01 |  |  |
| No relevante para Brasil | Introducir datos de área de valoración actual | En ÁREAS DE VALORACIÓN > Valoración > Período actual , efectúe las siguientes entradas:Precio de inventarioControl de precio : por ejemplo, S |  |  |
| 7 | Volver a la pantalla principal | Seleccionar Aplicar para volver a Producto vista. | Gestionar maestro de productos se visualiza. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto se ha guardado. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-non-stock-material-md]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-creating-non-stock-material-product-master-data-31y]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31y-313]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-nao-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 34,590 chars in the whole document
