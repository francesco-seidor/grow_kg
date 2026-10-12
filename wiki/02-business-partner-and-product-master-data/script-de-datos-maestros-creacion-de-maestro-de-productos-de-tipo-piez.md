---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-piez
title: "Script de datos maestros - Creación de maestro de productos de tipo \"Piezas de recambio\" (MDS 2J7) (2J7_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (2J7): test steps to create a spare parts (ERSA) material master via MM01, with optional document link."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-spare-parts]
aliases: [2J7_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Spare Parts", spare parts material master, material master creation, purchasing data, mrp planning data, storage data, accounting valuation data, document info record, document to material link, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-264
topic: 02-business-partner-and-product-master-data/product-master-spare-parts
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos de tipo "Piezas de recambio" (MDS 2J7) (2J7_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Spare Parts** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Piezas de recambio" - MDS (2J7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894532)

[2 Requisitos previos 3](#_Toc233894533)

[2.1 Roles 3](#_Toc233894534)

[2.2 Unidades organizativas necesarias 3](#_Toc233894535)

[2.3 Datos maestros obligatorios y opcionales 4](#_Toc233894536)

[2.4 Parámetros principales para la creación de datos 5](#_Toc233894537)

[2.4.1 Tipo de material y rangos de números 5](#_Toc233894538)

[2.4.2 Ramo 5](#_Toc233894539)

[3 Tabla de resumen 6](#_Toc233894540)

[4 Procedimientos de prueba 7](#_Toc233894541)

[4.1 Crear datos maestros de material - Datos básicos 7](#_Toc233894542)

[4.2 Crear datos maestros de material - Datos de compras 8](#_Toc233894543)

[4.3 Crear datos maestros de material - Datos de planificación/MRP (datos de centro) 10](#_Toc233894544)

[4.4 Crear datos maestros de material - Datos de almacén 12](#_Toc233894545)

[4.5 Crear datos maestros de material - Datos de contabilidad (datos de área de valoración) 14](#_Toc233894546)

[4.6 Crear documento (opcional) 16](#_Toc233894547)

[4.7 Modificar datos maestros de material - Enlazar documento con datos maestros de material (opcional) 17](#_Toc233894548)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este módulo crea un registro de datos maestros de producto para piezas de recambio.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Ingeniero de diseño | SAP_BR_DESIGN_ENGINEER | Gestión de documentos | SAP_BR_DESIGN_ENGINEER |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de material dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Descripción de material (texto breve), Número de material, Grupo de artículos, unidad de medida base, etc. on. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Datos de compras | Centro | Grupo de compras, grupo de artículos, tiempo de procesamiento de EM, y así sucesivamente. | Pueden existir datos de compras para cada organización de compras para qué material se debe utilizar en compras procesos. | Centro:__________ |
| Datos de planificación/MRP | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Entrega planificada hora, etc. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del es necesario realizar una planificación específica de almacén | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. rest. Estante, etc. |  | Centro:____________Almacén:__________ |
| Datos de contabilidad | Área de valoración (=centro), clase de valoración | Clase de valoración, Precio por unidad, Control de precio, etc. on. | Pueden existir datos de área de valoración para cada ID de centro de su estructura de la empresa para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, diferente precio de valoración de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un maestro de materiales registro de datos.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
|  |  | Opcional |  |
|  |  | Obligatorio |  |

### Parámetros principales para la creación de datos

En los siguientes temas de esta sección, se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y siempre son necesarios para crear un registro de datos maestros de material.

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizados o qué campos son obligatorios u opcionales. En función de los tipos de material, el el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos Los tipos de material utilizan la misma definición de rango de números

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe ser más de 8 dígitos. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un Número numérico de un material. |

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
| [Crear datos maestros de material - Datos básicos](#unique_10) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de material básicos. |
| [Crear datos maestros de material - Datos de compras](#unique_11) [página ] 8 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de compras. |
| [Crear datos maestros de material - Datos de planificación/MRP (datos de centro)](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de planificación MRP |
| [Crear datos maestros de material - Datos de almacén](#unique_13) [página ] 12 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se han creado los datos maestros de almacén |
| [Crear datos maestros de material - Datos de contabilidad (datos de área de valoración)](#unique_14) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de contabilidad |
| [Crear documento (opcional)](#unique_15) [página ] 16 | Ingeniero de diseño | Gestionar documentos (F2733) | Se crea un nuevo registro info de documento y se añaden metadatos. Los anexos se añaden al documento. |
| [Modificar datos maestros de material - Enlazar documento con datos maestros de material (opcional)](#unique_16) [página ] 17 | Especialista en datos maestros - Datos de producto | Modificar material (MM02) | El Documento creado en el paso anterior está vinculado a los Datos maestros de material. |

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

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Se muestra la página.Nota El inicio de sesión con SAP Fiori Launchpad solo es relevante para el uso de Web GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una pantalla nueva, Crear material (pantalla inicial) . |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : por ejemplo, ERSA Piezas de recambio | Se abre una pantalla nueva que muestra la Seleccionar vista(s) . |  |
| 4 | Seleccionar vistas | En la Seleccionar vistas pantalla, seleccione Datos básicos 1 y Datos básicos 2 y seleccione Continuar . | Se abre una pantalla nueva que muestra la Crear material (piezas de recambio) vista. |  |
| 5 | Introducir datos básicos | En la Crear material … (piezas de recambio) vista, en la Datos básicos 1 introduzca la etiqueta Descripción (texto breve). |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida base: por ejemplo, UNGrupo de materiales: por ejemplo, YBPM01 |  |  |
| 7 | Guardar los datos | Seleccionar Grabar | Se ha creado el número de material. |  |

### Crear datos maestros de material - Datos de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material.

Requisito previo

Ha completado y grabado los datos básicos para el material como se describe en la sección anterior, Crear datos maestros de material - Datos básicos.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Se muestra la página.Nota El inicio de sesión con la rampa de lanzamiento SAP Fiori solo es relevante para web Uso GUI. |  |
| 2 | Abrir mosaico Crear material | En la Maestro de productos sección, seleccione Crear material (MM01) . | Se abre una pantalla nueva que muestra la Crear material (inicial) Pantalla) . |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , haga el siguientes entradas:Material : Número de material creado en el paso anterior.Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : por ejemplo, ERSA Piezas de recambio | Se abre una pantalla nueva que muestra la Seleccionar vista(s) pantalla. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) pantalla, seleccione Compras y seleccione Continuar .Nota Solo para Polonia: para introducir el código PKWiU, seleccione también Comercio internacional: Importación . | Se abre una pantalla nueva que muestra la Organizativo Niveles . |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización la sección, haga siguiente entrada:Centro : <Centro código>Seleccionar Continuar . | Se abre una pantalla nueva que muestra la Crear material (reserva) Piezas) pantalla.Nota Aparece el siguiente mensaje del sistema en la parte inferior de la pantalla: El material ya existe y se ampliado. |  |
| 6 | Introducir datos de compras | En la Crear material (piezas de recambio) pantalla, en el Compras en la pestaña General Datos , realice las siguientes entradas:Grupo de compras : Compras Número de grupo |  |  |
| 7 | Introducir datos de compras | En la Otros datos/datos del fabricante sección, hacer la siguiente entrada:Tmpo.tratam.EM : por ejemplo, 1 |  |  |
| Solo para Polonia | Introducir datos de ventas | En la Comercio internacional: Importación sección, introduzca los siguientes datos:Código de control : por ejemplo, 41.00.30.0A continuación, seleccione Grabar . | Se actualiza el código PKWiU para Polonia. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se ha creado el número de material. |  |

### Crear datos maestros de material - Datos de planificación/MRP (datos de centro)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material.

Requisito previo

Ha completado las secciones anteriores, Crear datos maestros de material - Datos básicos y han grabado los datos maestros de compras.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Se muestra la página.Nota El inicio de sesión con la rampa de lanzamiento SAP Fiori solo es relevante para web Uso GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una nueva vista que muestra la Crear material (inicial) Pantalla) . |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , haga el siguientes entradas:Material : Número de material creado en el paso anteriorRamo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : por ejemplo, ERSA Recambio Piezas | Se abre una nueva vista que muestra la Seleccionar vista(s) vista. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) vista, seleccionar MRP1 , MRP2 , MRP3 y MRP4 y seleccione Continuar . | Se abre una nueva vista que muestra la Organizativo Niveles . |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en la Nivel de organización la sección, haga siguientes entradas:Centro : <Centro número>Almacén : <almacenamiento ubicación> | Se abre una nueva vista que muestra la Crear material (reserva) Piezas) vista. |  |
| 6 | Introducir datos de planificación/MRP | El Crear material (piezas de recambio) vista, en la Planif.necesidades 1 en la pestaña MRP procedimiento , realice las siguientes entradas:Caract.planif.nec. : por ejemplo, PDPlanificador de necesidades : por ejemplo, 001 | Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliará. |  |
| 7 | Introducir datos de planificación/MRP | En la Datos de tamaño de lote sección, haga lo siguiente entrada:Cálculo del tamaño del lote : por ejemplo, EX | Ha navegado a la siguiente pestaña Planif.necesidades 2 . |  |
| 8 | Introducir datos de planificación/MRP | El Crear material (piezas de recambio) vista, en la Planif.necesidades 2 en la pestaña Aprovisionamiento sección, haga lo siguiente entradas:Clase de aprovisionamiento : por ejemplo, F Almacén de producción : <Ubicación>Almacén para EP <Ubicación> |  |  |
| 9 | Introducir datos de planificación/MRP | En la Programación sección, haga lo siguiente entradas:Plazo de entrega previsto : Por ejemplo, 3Tmpo.tratam.EM : por ejemplo, 1Clave de horizonte : por ejemplo, 000 | Ha navegado a la siguiente pestaña Planif.necesidades 3 . |  |
| 10 | Introducir datos de planificación/MRP | En la Crear material (piezas de recambio) vista, en la Planif.necesidades 3 en la pestaña Disponibilidad verificación , realice las siguientes entradas:Verificación de disponibilidad : por ejemplo, PEPlazo reaprov.total : por ejemplo, 3 | Ha navegado a la siguiente pestaña Planif.necesidades 4 . |  |
| 11 | Introducir datos de planificación/MRP | En la Crear material (piezas de recambio) vista, en la Planif.necesidades 4 en la pestaña Lista de materiales explosión/necesidades secundarias la sección, haga siguientes entradas:Individual/Colectivo : 2 |  |  |
| 12 | Guardar los datos | Seleccionar Grabar | Se crea el número de material. |  |

### Crear datos maestros de material - Datos de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material.

Requisito previo

Ha rellenado los datos para el material como se describe en el Crear Datos maestros de material - Datos básicos y han completado y guardado el Datos de planificación/MRP.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Se muestra la página.Nota El inicio de sesión con la rampa de lanzamiento SAP Fiori solo es relevante para web Uso GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre una nueva vista que muestra la Crear material (inicial) vista) . |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , haga el siguientes entradas:Material : Número de material creado en el paso anterior.Ramo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando no se ofrece el ramo para la entrada, el campo se rellena con en el oscuro .Tipo de material : por ejemplo, ERSA Piezas de recambio | Se abre una nueva vista que muestra la Seleccionar vista(s) vista. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) , seleccione lo siguiente y seleccione Continuar :Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2 | Se abre una nueva vista que muestra la Organizativo Niveles . |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en la Nivel de organización la sección, haga siguientes entradas:Centro : <Centro código>Almacén : <Almacenamiento Número de ubicación> | Se abre una nueva vista que muestra la Crear material (reserva) Piezas) vista.Nota Aparece un mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de almacén | El Crear material (piezas de recambio) vista, en la Dat.ce./almacén 1 en la pestaña Datos generales sección, haga lo siguiente entradas:Número de vales de entrada de mercancías : por ejemplo, 1 | Ha navegado a la siguiente pestaña, Centro Datos/Almacén 2 . |  |
| 7 | Confirmar entradas | El Dat.ce./Almacén 2 en la pestaña Parámetros generales de centro la sección, haga entrada siguiente:Centro de beneficio . |  |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se ha creado el número de material. |  |

### Crear datos maestros de material - Datos de contabilidad (datos de área de valoración)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material.

Requisito previo

Ha creado los datos para el material descrito en el procedimiento anterior, Crear Datos maestros de material - Datos básicos y han completado y guardado el almacenamiento datos de ubicación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Iniciar Se muestra la página.Nota El inicio de sesión con la rampa de lanzamiento SAP Fiori solo es relevante para web Uso GUI. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Crear material (pantalla inicial) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , haga el siguientes entradas:Material : <El número de material creado en el paso anterior>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : por ejemplo, ERSA Piezas de recambio | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En Seleccionar vista(s) , seleccione lo siguiente y seleccione Continuar :Contabilidad 1Contabilidad 2 | El Niveles de organización se visualiza. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en la Nivel de organización la sección, haga siguientes entradas:Centro | El Crear material (piezas de recambio) ver muestra.Aparece este mensaje del sistema: El material ya existe y se ampliará. |  |
| 6 | Introducir datos de contabilidad | Desde el Crear material (piezas de recambio) ver, en el Contabilidad 1 en la pestaña General Datos de valoración , realice la siguiente entrada:Categoría de valoración : 3040 |  |  |
| 7 | Introducir datos de contabilidad | En la Precios y valores la sección, haga siguientes entradas:Precio estándar por ejemplo, 100Unidad de precio : 1Ctrl.precio : manténgalo como estándar | La siguiente pestaña, Contabilidad 2 se abre. |  |
| 8 | Confirmar entradas | El Contabilidad 2 pestaña, no realiza ninguna entradas. |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Se ha creado el número de material. |  |

### Crear documento (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un documento.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario Ingeniero de diseño . | El Iniciar Se muestra la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar documentos (F2733) . | El Gestionar documentos (F2733) se visualiza. |  |
| 3 | Crear documento nuevo | El Gestionar documento , seleccione Crear para crear un documento nuevo. | El Documento Aparece la vista. |  |
| 4 | Introducir metadatos | El Información general pestaña de la Documento , efectúe las siguientes entradas:Clase de documento : por ejemplo, YBOParte de documento : por ejemplo, 000El Datos de documento pestaña de la Documento , efectúe las siguientes entradas:Descripción : por ejemplo, <SparePartsDoc001> | Los metadatos se actualizan en el Documento con valores predeterminados. |  |
| 5 | Cargar anexos en el documento | El Documento vista, vaya a la Originales y seleccione Cargar para examinar y cargar el documentos:Nombre de archivo : por ejemplo, <test001.jpg> | Los anexos del documento aparecen con el check in efectuado. |  |
| 6 | Grabar el documento | Seleccionar Crear para guardar el documento. | Se crea y graba un nuevo documento del tipo YBO.Anote Número de documento . |  |
| 7 | Modificar estado | El Documento , seleccione Editar y del Datos de documento sección, fijar Estado del documento hasta Re (Liberado) |  |  |
| 8 | Grabar el documento | Seleccionar Grabar para guardar el documento. |  |  |

### Modificar datos maestros de material - Enlazar documento con datos maestros de material (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para enlazar un documento con los datos maestros de material.

Requisito previo

Ha creado los datos para el material descrito en el procedimiento anterior, Crear datos maestros de material - Datos básicos y completaron el proceso opcional Crear documento procedimiento.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Modificar material (MM02) . | Se abre una ventana nueva que muestra la Modificar material (pantalla inicial) . |  |
| 3 | Introducir datos básicos de material | El Modificar material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material creado en anterior paso>Ramo : MNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo se rellena con En la oscuridad . |  |  |
| 4 | Seleccionar vistas | El Modificar material (pantalla inicial) , seleccione Seleccionar vista(s) en la barra superior. | Se abre una nueva vista que muestra la Seleccionar vista(s) vista. |  |
| 5 | Seleccionar vistas | En la Seleccionar vista(s) seleccione las siguientes vistas y seleccione Continuar :Datos básicos 1 | Se abre una ventana nueva que muestra la Modificar material … (piezas de recambio) pantalla. |  |
| 6 | Abrir datos adicionales | El Modificar material … (piezas de recambio) , seleccione Datos adicionales en la barra superior. |  |  |
| 7 | Introducir datos de documento | Seleccione el Datos de documento pestaña y de Documentos enlazados , seleccione Todas las versiones . Seleccione el signo más (+) para insertar una fila nueva. Busque el documento que ha creado en el procedimiento anterior. |  |  |
| 8 | Copiar datos de documento | Seleccione el documento creado en el paso anterior y, a continuación, seleccione Copiar para insertar el documento en la fila. |  |  |
| 9 | Grabe los datos | Seleccionar Grabar . | Se ha modificado el número de material. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-spare-parts-mds-2j7-2]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-265]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-267]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-pecas-de-repos]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 33,016 chars in the whole document
