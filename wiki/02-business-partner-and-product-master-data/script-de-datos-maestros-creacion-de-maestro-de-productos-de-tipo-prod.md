---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod
title: "Script de datos maestros - Creación de maestro de productos de tipo \"Producto semielaborado\" (MDS BNS) (BNS_S4CLD2608_Master_Data_ES_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (Spanish, machine-translated): test steps to create a HALB semi-finished product master via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNS_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, semi-finished products, basic data, purchasing data, mrp planning data, warehouse data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-666
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos de tipo "Producto semielaborado" (MDS BNS) (BNS_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Producto semielaborado" - MDS (BNS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895014)

[2 Requisitos previos 3](#_Toc233895015)

[2.1 Acceso al sistema 3](#_Toc233895016)

[2.2 Roles 3](#_Toc233895017)

[2.3 Unidades organizativas necesarias 3](#_Toc233895018)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895019)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233895020)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233895021)

[2.5.2 Ramo 5](#_Toc233895022)

[3 Tabla de resumen 6](#_Toc233895023)

[4 Procedimientos de prueba 7](#_Toc233895024)

[4.1 Crear datos maestros de producto - Datos básicos 7](#_Toc233895025)

[4.2 Crear datos maestros de producto - Datos de compras 10](#_Toc233895026)

[4.3 Crear datos maestros de producto - Datos de planificación MRP / Datos de centro 12](#_Toc233895027)

[4.4 Crear datos maestros de producto - Datos de almacén 16](#_Toc233895028)

[4.5 Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración 19](#_Toc233895029)

[4.6 Crear datos maestros de producto – Producto configurable y variantes 22](#_Toc233895030)

[4.7 Crear datos maestros de producto – Grabar anexos 24](#_Toc233895031)

[4.8 Crear datos maestros de producto - Ventas de centro / Datos generales 27](#_Toc233895032)

[4.9 Crear datos maestros de producto - Centro / Fabricación repetitiva 29](#_Toc233895033)

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
| Datos básicos | Independiente de unidades organizativas | Descripción de material (texto breve), Número de material, Grupo de artículos, unidad de medida base etc. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Datos de compras | Centro | Grupo de compras, grupo de artículos, tiempo de procesamiento de EM etc. | Pueden existir datos de compras para cada organización de compras para qué material se debe utilizar en compras procesos. | Centro:__________ |
| Datos de planificación/MRP (datos de centro) | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Entrega planificada hora etc. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del necesita realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. rest. Estantería, etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para los que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del necesita realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Datos de contabilidad | Área de valoración (=centro), clase de valoración | Clase de valoración, precio por unidad, control de precio etc. | Pueden existir datos de área de valoración para cada ID de centro de su estructura de la empresa para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, diferente precio de valoración de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un maestro de materiales registro de datos.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir específico de BR Campos para datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | La asignación de un centro de beneficio a un maestro de materiales es necesaria para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

En esta sección se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro. y siempre son necesarios para crear un registro de datos maestros de materiales.

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizar o qué campos son obligatorios u opcionales. En función de los tipos de material, el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos los tipos de material utilizan la misma definición de rango de números.

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

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de producto - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean datos básicos. |
| [Crear datos maestros de producto - Datos de compras](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean los datos de compras (datos de centro). |
| [Crear datos maestros de producto - Datos de planificación MRP / Datos de centro](#unique_13) [página ] 12 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material – MRP/datos de planificación. |
| [Crear datos maestros de producto - Datos de almacén](#unique_14) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean los datos de almacén. |
| [Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración](#unique_15) [página ] 19 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean los datos de contabilidad (datos de valoración). |
| [Crear datos maestros de producto – Producto configurable y variantes](#unique_16) [página ] 22 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Crear producto configurable y variantes. |
| [Crear datos maestros de producto – Grabar anexos](#unique_17) [página ] 24 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Grabar anexos en el registro maestro de materiales. |
| [Crear datos maestros de producto - Ventas de centro / Datos generales](#unique_18) [página ] 27 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |
| [Crear datos maestros de producto - Centro / Fabricación repetitiva](#unique_19) [página ] 29 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) |  |

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

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles depende de su rol asignado, por lo que se proporcionan dos opciones.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : HALB (semielaborado) Producto)Haga clic en Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Datos básicos 1 y Básico datos 2 y seleccione Continuar . | El Crear material (producto semielaborado) la vista se visualiza. |  |
| 5 | Introducir datos básicos | En la Material... (producto semielaborado) vista, en el Datos básicos 1 introduzca el Descripción de material (breve) texto) . |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 pestaña, en el Datos generales la sección, haga siguientes entradas:Unidad de medida baseGrupo de materialesGr.tp.pos.gen. |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN la sección, haga sig.entradas y confirme dos veces con Intro :Peso brutoUnidad de pesoPeso netoIr a Datos básicos 2 pestaña. | El Datos básicos 2 se visualiza. |  |
| 8 | Introducir datos básicos | El Datos básicos 2 no tiene para realizar cualquier entrada. Confirmar con Intro . | Una nueva vista Última vista de datos alcanzada abre con el aviso Está a punto de salir. ¿Desea ¿Desea grabar primero sus datos para este material? . |  |
| 9 | Guardar los datos | En la Última vista de datos alcanzada seleccione Sí . | El Datos maestros - Producto se visualiza.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con su usuario credenciales. | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar maestro de productos Se abre la vista. |  |
| 3 | Seleccione Crear nuevo maestro de productos. | En la Gestionar maestro de productos , seleccione Crear Producto | El Crear registro de datos maestros se visualiza la ventana. |  |
| 4 | Introducir datos para campos obligatorios | En la Crear registro de datos maestros vista, efectúe las siguientes entradas:Número de producto : por ejemplo, Z …cualquier ID alfanumérico externo … (al menos este debe empezar con un carácter) o ninguna entrada para que el sistema asigna automáticamente un ID numéricoTipo de producto : HALB (semielaborado) Producto)Grupo de productos : por ejemplo, L003Unidad base : por ejemplo, UNDescripción : <cualquiera descripción> |  |  |
| 5 | Seleccione OK. | En la Gestionar maestro de productos , seleccione OK . | El Gestionar maestro de productos ver se visualiza. |  |
| 6 | Introducir datos básicos | En la Gestionar maestro de productos > DATOS BÁSICOS > Datos básicos , realice la siguiente entrada:Sector : por ejemplo 00 |  |  |
| 7 | Seleccione Crear. | El Vista de producto ir a DATOS BÁSICOS > Descripciones faceta, seleccione Crear . | La descripción en el idioma predeterminado (por ejemplo, inglés) ya se ha rellenado |  |
| 8 | Introducir datos de descripciones | En la Descripciones vista, haga el siguientes entradas:Idioma : por ejemplo, AlemánDescripción de producto : <su descripción> | Las descripciones se pueden actualizar en diferentes idiomas. |  |
| 9 | Seleccionar unidad de medida base | En la Gestionar maestro de productos > DATOS BÁSICOS , seleccione Unidad base de Medida | El Unidad de medida base ver se visualiza. |  |
| 10 | Guardar los datos | Seleccionar Grabar . | El sistema emite una notificación que indica que el objeto es grabado. |  |

### Crear datos maestros de producto - Datos de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponible depende de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la sección anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (vista inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | En la Crear material (vista inicial) , efectúe las siguientes entradas:Material : Material númeroSector sector : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : HALB (semielaborado) Producto)Haga clic en Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Compras y seleccione Continuar .Nota Solo para Polonia: para introducir el código PKWiU, seleccione también Comercio exterior: Datos de importación antes de seleccionar Continuar . | El Niveles de organización ver se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización vista, en el Niveles de organización sección, hacer la siguiente entrada y seleccione Continuar :Centro : <Centro número> | El Crear material (producto semielaborado) la vista se visualiza. |  |
| 5 | Introducir datos de compras | En la Material (producto semielaborado) vista, en el Compras pestaña, en el Datos generales la sección, haga siguientes entradas:Grupo de compras : por ejemplo 001Grupo de materiales : por ejemplo, L003 |  |  |
| 6 | Introducir datos de compras | En la Otros datos/datos del fabricante sección, realice la siguiente entrada:Tmpo.tratam.EM : por ejemplo 1 | Una ventana nueva Última vista de datos alcanzada abre con el mensaje Está a punto de salir. ¿Desea ¿Desea grabar primero los datos para este material? . |  |
| Solo para Polonia | Introducir datos de importación de comercio exterior | Para Polonia, en el Datos de comercio exterior sección, introduzca los datos de código PKWiU:Código de control : por ejemplo, 24.10.32.0 | Se actualiza el código PKWiU para Polonia. |  |
| 7 | Guardar los datos | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto ventana se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Gestionar datos maestros de producto Se abre la aplicación y varios campos de búsqueda se visualizan. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Haga clic en Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de compras | En la Maestro de productos , seleccione COMPRA | El COMPRA se visualiza. |  |
| 4 | Introducir datos de compras | El COMPRA vista, realice lo siguiente entrada:• Clave de valor de compras : para ejemplo 1 |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | La notificación del sistema indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de planificación MRP / Datos de centro

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponible depende de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (vista inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | El Crear material (vista inicial) , realice lo siguiente entradas:Material : Material númeroRamo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : HALB (semielaborado) Producto)Haga clic en Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione MRP1 , MRP2 , MRP3 y MRP4 y seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización vista, en el Nivel de organización sección, hacer las siguientes entradas:CentroAlmacén | El Crear material (producto semielaborado) se visualiza. |  |
| 5 | Introducir datos de planificación/MRP | El Material (producto semielaborado) vista, en el Planif.necesidades 1 pestaña, en el Datos generales la sección, haga siguientes entradas:Caract.planif.nec. : PDHorizonte de planificación fijoPlanificador de necesidades : 001 | Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliará . | . |
| 6 | Introducir datos de planificación/MRP | En la Cálculo del tamaño del lote sección, hacer la siguiente entrada:Cálculo del tamaño del lote : EX | El Planif.necesidades 2 se visualiza. |  |
| 7 | Introducir datos de planificación/MRP | En la Crear material (semielaborado) Producto) vista, en la MRP 2 en la pestaña Aprovisionamiento sección, realice las siguientes entradas:Clase de aprovisionamientoAlmacén de producción |  |  |
| 8 | Introducir datos de planificación/MRP | En la Programación la sección, haga siguientes entradas:Fabricación propiaPlazo de entrega previstoTmpo.tratam.EMClave de horizonte | El Planif.necesidades 3 se visualiza. |  |
| 9 | Introducir datos de planificación/MRP | En la Crear material (semielaborado) Producto) vista, en la MRP 3 en la pestaña Planificación sección, realice las siguientes entradas:Grupo de estrategiasModo de consumoPer.consumo anter.Intervalo de consumo a plazo |  |  |
| 10 | Introducir datos de planificación/MRP | En la Verificación de disponibilidad sección, hacer las siguientes entradas:Verificación de disponibilidadPlazo reaprov.total | El Planif.necesidades 4 se visualiza. |  |
| 11 | Introducir datos de planificación/MRP | Nota Para el elemento de alcance Subcontratación - BMY , debe actualizar el Versiones de fabricación para garantizar funcionalidad correcta.El Crear material (semielaborado) Producto) vista, en la MRP 4 en la pestaña Explosión de la lista de materiales/dependiente necesidades sección, haga lo siguiente entrada:Individual/Colectivo | Una ventana nueva Última vista de datos alcanzada se abre con el mensaje: Está a punto de salir. ¿Desea grabar los datos? para este material? |  |
| 12 | Guardar los datos | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto ver se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto Se abre la aplicación y hay varias búsquedas se visualizan los campos. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Haga clic en Editar . | Producto se visualiza en modo de edición (campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | En la Maestro de productos , seleccione CENTROS . | El CENTROS se visualiza. |  |
| 4 | Seleccione Crear. | En la CENTROS , seleccione Crear . | El Centro la vista se abre en Editar Modo . |  |
| 5 | Introducir centros: Datos de información general | En la Centro > INFORMACIÓN GENERAL , efectúe las siguientes entradas:Centro : <Centro número>Centro de beneficio : por ejemplo, YB110 o YB111Gr.carga : por ejemplo, 0001 | El Crear material (producto semielaborado) la vista se visualiza. |  |
| 6 | Introducir centros - Datos de planificación de necesidades | Nota Para el elemento de alcance Subcontratación - BMY , debe actualizar el Grupo de estrategias también.En la Maestro de productos , seleccione MRP DATOS .En la DATOS MRP , seleccione Datos MRP , y realice lo siguiente entradas:Verificación de disponibilidad : por ejemplo, PEPlazo de entrega previsto : para ejemplo, 3Tiempo de procesamiento de entrada de mercancías : para ejemplo, 1Caract.planif.nec. : Por ejemplo, PD MRPPlanificador de necesidades : Por ejemplo, 001 |  |  |
| 7 | Introducir centros - Datos de tamaño de lote | En la vista DATOS MRP, seleccione Tamaño de lote DatosEn la Datos de tamaño de lote vista, introduzca la siguientes:Cálculo del tamaño del lote : para ejemplo, EX |  |  |
| 8 | Introducir centros: Datos de aprovisionamiento | En la Datos MRP > Sección Aprovisionamiento , efectúe la siguiente entrada:● Plazo de entrega previsto : por ejemplo, 3● Tiempo de procesamiento de entrada de mercancías : para ejemplo, 1 |  |  |
| 9 | Seleccionar centros - Datos de previsión | En la Gestión de maestro de productos - CENTROS vista, seleccione PREVISIÓN | El Centro - PREVISIÓN se visualiza. |  |
| 10 | Introducir centros - Datos de previsión | En la PREVISIÓN vista, haga el siguientes entradas:Tipo de período : por ejemplo, M |  |  |
| 11 | Volver a la vista principal | Seleccionar Aplicar para volver a Producto vista. | Volver a Maestro de productos vista. |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación de que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles dependen de su rol asignado, por lo que hay dos opciones proporcionado.

Requisito previo

Debe completar la sección anterior, Crear datos maestros de producto - Datos básicos , antes de continuar con esto sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la sección anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (vista inicial) muestra. |  |
| 2 | Introducir datos básicos de material | En la Crear material (vista inicial) , efectúe las siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : HALB (semielaborado) Producto)Seleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione la ventana vistas siguientes y seleccione Continuar :Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2 | El Niveles de organización ver se visualiza. |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización vista, en la Nivel de organización sección, haga lo siguiente entradas:Centro : <Centro número>Almacén : <Almacén número> | Se abre una ventana nueva que muestra la Crear material (Producto semielaborado) vista.Aparece el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 5 | Introducir datos de almacén | En la Crear material (producto semielaborado) vista, en la Dat.ce./almacén 1 pestaña, en el Datos generales , realice la siguiente entrada y confirme con Intro :Número de vales de entrada de mercancías : por ejemplo, 1 | El Dat.ce./alm.2 se visualiza. |  |
| 6 | Confirmar entradas | El Dat.ce./Almacén 2 en la pestaña Parámetros generales de centro , realice las siguientes entradas:Centro de beneficio : por ejemplo, YB110 o YB111SerialNoProfileSeleccione un perfil de número de serie válido que se haya asignado con el tipo de equipo adecuado para su negocio. | Una ventana nueva Última vista de datos alcanzada se visualiza con el siguiente mensaje Está a punto de salir. ¿Desea grabar los datos para este material? primero? . |  |
| 7 | Guardar los datos | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Gestionar datos maestros de producto Se abre la aplicación y varios campos de búsqueda se visualizan. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Seleccionar Editar . | Producto se visualiza en modo de edición (campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | En la Gestionar maestro de productos , seleccione CENTROSNota Si aún no lo ha hecho ha añadido un registro de datos de centro, siga los pasos anteriores procedimiento, Crear datos maestros de producto - Datos de planificación MRP / Datos de centro . | El CENTROS se visualiza. |  |
| 4 | Seleccionar detalles de centro | En la CENTROS ver, utilice la flecha hacia la derecha icono para seleccionar el Datos de centro que ha creado en el Procedimiento anterior. | El Centro de maestro de productos se visualiza. |  |
| 5 | Navegar a Centro: Almacén | En la CENTROS ver, navegar a CENTROS > UBICACIÓN DE ALMACENAMIENTO | El CENTROS la vista se abre en Editar Modo . |  |
| 6 | Seleccione Crear. | Desde el CENTROS > UBICACIONES DE ALMACENAMIENTO > Almacenes , seleccione Crear . | ElAlmacén la vista se abre en Modo de edición . |  |
| 7 | Introducir centro: Datos de almacén | En la Almacén , efectúe las siguientes entradas:Almacén : <Número de almacén | El Nuevo registro - Almacén se visualiza. |  |
| 8 | Volver a la vista principal | Seleccione la flecha Atrás, dos veces, para volver Maestro de productos . | Volver a Maestro de productos vista. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El sistema muestra una notificación que indica que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles dependen de su rol asignado, por lo que hay dos opciones proporcionado.

Requisito previo

Debe completar la sección anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (vista inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | En la Crear material (vista inicial) , efectúe las siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : HALB (semielaborado) Producto)Haga clic en Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione la ventana vistas siguientes y seleccione Continuar :Contabilidad 1Contabilidad 2 | El Niveles de organización ver se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización vista, en el Nivel de organización sección, hacer las siguientes entradas:Centro | Se muestra una nueva ventana que muestra la Crear material (Producto semielaborado) vista.Se muestra el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliará | . |
| 5 | Introducir datos de contabilidad | En la Crear material (semielaborado) Producto) vista, en la Contabilidad 1 en la pestaña Valoración general Datos , realice la siguiente entrada:Categoría de valoración : por ejemplo, 7900 |  |  |
| 6 | Introducir datos de contabilidad | En la Precios y valores la sección, haga siguientes entradas:Precio estándarPrecio por unidad : por ejemplo, 20Ctrl.precio : por ejemplo, SPara confirmar sus entradas, pulse Intro dos veces. | El Contabilidad 2 se visualiza. |  |
| 7 | Confirmar entradas | En la Contabilidad 2 no tiene para realizar cualquier entrada. | Una ventana nueva Última vista de datos alcanzada se visualiza con el mensaje Está a punto de salir. ¿Eres tú? ¿Desea grabar primero sus datos para este material? . |  |
| 8 | Guardar los datos | En la ventana Última vista de datos alcanzada , seleccionar Sí . | El Datos maestros - Producto se visualiza la ventana.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Gestionar datos maestros de producto Se abre la aplicación y varios campos de búsqueda se visualizan. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Haga clic en Editar . | Producto se visualiza en modo de edición (campos están listos para su entrada). |  |
| 3 | Seleccionar datos de área de valoración | Desde el Maestro de productos , seleccione VALORACIÓN ÁREA . | El ÁREA DE VALORACIÓN muestra el área de visualización. |  |
| 4 | Seleccione Crear. | En la Nuevo maestro de productos - ÁREA DE VALORACIÓN sección de vista, seleccione Crear . | El Maestro de productos: Valoración Se abre la vista en modo de edición. |  |
| 5 | Introducir datos de área de valoración | En la vista Nuevo maestro de productos: Valoración, realice lo siguiente: entradas:Área de valoración : <número>Determinación de control de precio : para ejemplo, 2Nota Solo para Brasil: Determinación de precio para Brasil debe ser 3 , para Brasil Principios de contabilidad de costes.Categoría de valoración : <número> , por ejemplo, 3100 |  |  |
| 6 | Introducir datos de área de valoración actual | En la ÁREAS DE VALORACIÓN > VALORACIÓN , seleccione Actual Período... y realice las siguientes entradas:Precio medio variable : por ejemplo, 20Indicador de control de precio : por ejemplo, S |  |  |
| 7 | Volver a la vista principal | Seleccionar Aplicar para volver a Producto vista. | Volver al principal Maestro de productos vista. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | El sistema emite una notificación que indica que el objeto se ha grabado. |  |

### Crear datos maestros de producto – Producto configurable y variantes

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar un procedimiento anterior, Crear datos maestros de producto – Básico Datos , antes de continuar con este procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una ventana nueva que muestra la Crear material (Acceso) . |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : HALB (producto semielaborado)Seleccionar Seleccionar vista(s) . | Se abre una ventana nueva que muestra la Seleccionar Vista(s) vista. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione la ventana vistas siguientes y seleccione Continuar :Datos básicos 1Datos básicos 2Clasificación |  |  |
| 4 | Introducir datos básicos | En la Material (producto terminado) vista, en la Datos básicos 1 introduzca la etiqueta Descripción de material (texto breve) y Unidad base de Medida .Pulsar Intro . | El Datos básicos 2 se visualiza. |  |
| 5 | Introducir datos básicos | En la Datos básicos 2 , verifique el El material es configurable casilla de selección.Pulsar Intro . | Clasificación visualizaciones de fichas y Categoría de clase Se abre la ventana emergente. |  |
| 6 | Seleccionar categoría de clase | En la Categoría de clase seleccione la categoría de clase 300 (Variante) y Continuar . | El Clasificación se visualiza. |  |
| 7 | Asignar clase | En la Asignación sección, asigne una clase y pulse Intro . | Las características correspondientes se muestran debajo del Asignación sección. |  |
| 8 | Seleccionar valores de característica | Seleccione los valores necesarios de las características. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Se crea el material configurable. Ahora debe crear la variante. |  |
| 10 | Crear variante | Para crear Variante , de nuevo abierto Crear material y siga lo anterior Pasos para crear un nuevo material con Datos básicos 1 y Datos básicos 2 . |  |  |
| 11 | Crear variante | En Datos básicos 2 , vaya a Específico de mandante configuración e introduzca los datos creados anteriormente Material configurable en Válido para todos los centros CM . Seleccione Configurar variante y, a continuación, seleccione las características necesarias valor para configurar variantes. | Se ha creado la variante. |  |

Procedimiento: Opción 2 – Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Gestionar datos maestros de producto se abre la aplicación y varios campos de búsqueda visualizado. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Producto Número en el Producto campo de búsqueda.Seleccione el Producto de la lista que le llevará a la Producto vista.Seleccionar Editar . | Producto se visualiza en modo de edición (campos están listos para su entrada). |  |
| 3 | Hacer que el producto sea configurable | En la Producto ver, vaya a Configuración y verifique el El producto es configurable casilla de selección. |  |  |
| 4 | Asignar clase de variante | En la Producto vista, vaya a Clasificación pestaña y seleccionar Haga clic aquí para asignar una clase . A continuación, seleccionar una clase de tipo 300 (Variante). | Se visualizan las características de la clase asignada. |  |
| 5 | Seleccionar características | Seleccione los valores de característica necesarios para cada característica. |  |  |
| 6 | Vaya a la pestaña Variantes | En la Producto ver, vaya a Variantes y seleccione Seleccionar Variantes de producto | Se visualiza un árbol/tabla con las diferentes características. |  |
| 7 | Seleccionar características y crear variantes | Seleccione la combinación de valores de característica y seleccione Aplicar . | Se crean variantes. |  |
| 8 | Grabar | Seleccionar Grabar . | El sistema emite una notificación de que el objeto grabado. |  |

### Crear datos maestros de producto – Grabar anexos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar un procedimiento anterior, Crear datos maestros de producto – Básico Datos , antes de continuar con este procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una ventana nueva que muestra la Crear material (Acceso) . |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , en Más seleccionar menú Material > Cambiar > Inmediatamente , y realice las siguientes entradas:Material : Material númeroRamo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena con oscuro.Tipo de material : HALB (producto semielaborado)Seleccionar Seleccionar vista(s) . | Se abre una ventana nueva que muestra la Seleccionar Vista(s) vista. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Datos básicos 1 y Datos básicos 2 y seleccione Continuar . | El Crear material (producto terminado) ver se visualiza. |  |
| 4 | Seleccionar servicios para objeto | En la barra de herramientas de la aplicación, haga clic en Servicios para objeto > Crear anexo . | Importar archivo Se abre la ventana. |  |
| 5 | Seleccione Cargar. | Importar archivo seleccione Cargar botón. | Se abre una ventana de carga de archivos. |  |
| 6 | Cargar anexo | Marque el fichero y seleccione Abra. | Se ha cargado el archivo. |  |
| 7 | Grabar | Seleccionar Seleccionar y Grabar . | El sistema emite una notificación de que el objeto grabado. |  |

Procedimiento: Opción 2 – Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Gestionar datos maestros de producto se abre la aplicación y varios campos de búsqueda son visualizado. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto introduciendo Producto Número en el Producto campo de búsqueda.Seleccione el Producto de la lista que navegue hasta Producto vista.Haga clic en Editar . | Producto se visualiza en modo de edición (campos están listos para su entrada). |  |
| 3 | Seleccionar anexos | En la Producto ver, vaya a Anexos pestaña. | Se muestra la vista Anexos. |  |
| 4 | Seleccione Crear. | En el Sistema de gestión de documentos sección, seleccione Crear . | Se abre una ventana de carga de archivos. |  |
| 5 | Cargar anexo | Marque el archivo y seleccione Abierto . | Se ha cargado el archivo. |  |
| 6 | Grabar | Seleccionar Grabar . | El sistema emite una notificación de que el objeto grabado. |  |

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
| 2 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Material número>Ramo : MNota Si el Ramo introduzco el campo está oculto, no se requiere ninguna entrada. Cuando el No se ofrece el ramo para la entrada, el campo se rellena con en la oscuridad.Tipo de material : HALBSeleccionar Seleccionar vista(s) . | Seleccionar vista(s) Se abre la pantalla. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) de selección de ventana Datos básicos y Ventas: Datos generales/de centro y seleccione continuar . | Niveles de organización aparece |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización pantalla, en el Nivel de organización sección, hacer siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (mercaderías) pantalla se abre. |  |
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
| 5 | Introducir centros - Datos generales | En la Datos generales sección, hacer siguientes entradas:Centro : Centro número por ejemplo, 1710 |  |  |
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

El siguiente procedimiento proporciona instrucciones para crear un maestro de materiales (productos) datos. Las aplicaciones disponibles dependen de su rol asignado, por lo que hay dos opciones Se proporcionan .

Requisito previo

Debe completar el procedimiento anterior, Creación de material (producto) Datos maestros - Datos básicos , antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de datos básicos, como se describe en la Procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | Crear material (pantalla inicial) se abre. |  |
| 2 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Material número>Ramo : MNota Si el Ramo introduzco el campo está oculto, no se requiere ninguna entrada. Cuando el No se ofrece el ramo para la entrada, el campo se rellena con en la oscuridad.Tipo de material : HALBSeleccionar Seleccionar vista(s) . | Seleccionar vista(s) Se abre la pantalla. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) selección de ventana Datos básicos 1 , Planif.necesidades 1 y MRP 4 y seleccione continuar . | Niveles de organización aparece |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización pantalla, en el Nivel de organización sección, hacer siguientes entradas:Centro : <Centro número>Almacén : <Almacén número> | El Crear material... (mercaderías) pantalla se abre. |  |
| 5 | Introducir datos en Datos básicos 1 | En la vista Datos básicos 1, efectúe las siguientes entradas y seleccione Intro :Descripción : Actualizar descripción para productoUnidad base : Actualizar unidad base "EA" por ejemplo 1 |  |  |
| 6 | Introducir datos en MRP 1 | En la Método de planificación de necesidades realice la siguiente entrada:Caract.planif.nec. : Actualizar característica de planificación de necesidades "ND", por ejemplo |  |  |
| 7 | Introducir datos en MRP 4 | En la Fabricación repetitiva/montaje/despliegue estrategia realice la siguiente entrada:Fabricación repetitiva : Seleccione el casilla de selecciónPerfil fabricación repetitiva : elegir cualquiera valor de la ayuda para entradas |  |  |
| 8 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Gestionar datos maestros de producto (F1602) | El Gestionar datos maestros de producto (F1602) aplicación se abre y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Buscar el creado anteriormente Producto por introduciendo Número de producto en el Producto campo de búsqueda.Seleccione el Producto de la lista que le dirigirá a Producto vista.Seleccionar Editar . | El producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | En la Producto , seleccione Centros | El Centros se visualiza. |  |
| 4 | Seleccione Crear. | En la Centros , seleccione Crear . |  |  |
| 5 | Introducir centros - Datos generales | En la Datos generales sección, hacer siguientes entradas:Centro : Centro número por ejemplo, 1710 |  |  |
| 6 | Introducir datos de planificación de necesidades | En la Sección MRP , haga lo siguiente entradas:Caract.planif.nec. : ejemplo ND |  |  |
| 7 | Introducir datos de fabricación repetitiva | En la Fabricación repetitiva sección efectúe las siguientes entradas:Fabricación repetitiva activada : marque la casilla de selección para activar la fabricación repetitiva Campo de perfilPerfil de fabricación repetitiva : seleccionar cualquier valor del valor ayuda | Al verificar Fabricación repetitiva habilitada la casilla de selección, el Repetitivo Perfil de fabricación El campo debe ser editable.Al desmarcar Fabricación repetitiva Activado la casilla de selección Repetitivo El campo Perfil de fabricación solo debe visualizarse. |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar para volver a Producto vista. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema indica que el objeto es grabado . |  |

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
> Flagged while digesting this document, not verified: Machine-translated Spanish text with some garbled phrases (e.g. 'En la oscuridad' for 'dark/blank'); sections 4.6/4.7 mention 'producto terminado' despite semi-finished scope; sample valuation class differs between options (7900 vs 3100).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-669]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-sap-s-4hana-cloud-public-edition-2608-japanese-667]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 62,720 chars in the whole document
