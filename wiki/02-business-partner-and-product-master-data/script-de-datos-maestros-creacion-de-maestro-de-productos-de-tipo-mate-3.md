---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3
title: "Script de datos maestros: Creación de maestro de productos de tipo \"Material configurable\" - MDS (2T7) (2T7_S4CLD2608_Master_Data_ES_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating KMAT configurable material masters via MM01 or F1602, scope item 2T7."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2T7_S4CLD2608_Master_Data_ES_XX]
keywords: [Configurable Materials and Characteristic Display, configurable material master, product master data, basic data, sales data, mrp planning data, purchasing data, classification, work scheduling, warehouse data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-282
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Creación de maestro de productos de tipo "Material configurable" - MDS (2T7) (2T7_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos de tipo "Material configurable" - MDS (2T7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894564)

[2 Requisitos previos 3](#_Toc233894565)

[2.1 Acceso al sistema 3](#_Toc233894566)

[2.2 Roles 3](#_Toc233894567)

[2.3 Condiciones empresariales 3](#_Toc233894568)

[2.4 Unidades organizativas necesarias 4](#_Toc233894569)

[2.5 Datos maestros obligatorios y opcionales 5](#_Toc233894570)

[2.6 Parámetros principales para la creación de datos 5](#_Toc233894571)

[2.6.1 Tipo de material y rangos de números 6](#_Toc233894572)

[2.6.2 Ramo 6](#_Toc233894573)

[3 Tabla de resumen 7](#_Toc233894574)

[4 Procedimientos de prueba 8](#_Toc233894575)

[4.1 Crear datos maestros de producto - Datos básicos 8](#_Toc233894576)

[4.2 Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas 11](#_Toc233894577)

[4.3 Crear datos maestros de producto - Datos de compras 14](#_Toc233894578)

[4.4 Crear datos maestros de producto - Clasificación 16](#_Toc233894579)

[4.5 Crear datos maestros de producto - Datos de planificación MRP / Datos de centro 18](#_Toc233894580)

[4.6 Crear datos maestros de producto: Preparación de trabajo 21](#_Toc233894581)

[4.7 Crear datos maestros de producto - Datos de almacén 23](#_Toc233894582)

[4.8 Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración 26](#_Toc233894583)

[4.9 Crear datos maestros de producto – Cálculo del coste 29](#_Toc233894584)

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

### Condiciones empresariales

Antes de que se pueda probar este script de datos maestros, se debe cumplir la siguiente condición empresarial.

|  |
| --- |
| Nota Elemento de alcance 22T - Configurar el modelo configurable mediante la configuración de variantes es un requisito previo para este script de datos maestros. |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de material dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de unidades organizativas | Descripción de material (texto breve), número de material, grupo de materiales, unidad base de Medida, etc. | Los datos básicos solo existen una vez para los datos maestros de material registro. | n/d |
| Clasificación | Independiente de unidades organizativas | Valores de categoría de clase, clase y clase | Existen datos de clasificación para la categoría de clase para la que se utilizan datos de clasificación. | n/d |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales, Grupo de tipos de posición, Tipo de Grupo, grupo de carga, tiempo de preparación, etc. on. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales. | Centro:____________Organización de ventas:__________Canal de distribución:__________ |
| Datos de compras | Centro | Unidad de medida base, grupo de artículos | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para los que se utiliza el registro maestro de materiales. | Centro:____________ |
| Datos de planificación/MRP (datos de centro) | Centro, almacén | Característica de planificación de necesidades, Planificador de necesidades, Tamaño de lote, Plazo de entrega previsto, etc. | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función del necesita realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Preparación de trabajo | Centro | Supervisor de producción y programación de producción Perfil | Los datos de centro pueden existir para cada estructura empresarial para la que se utiliza el registro maestro de materiales. | Centro:_____________ |
| Datos de almacén | Centro, almacén | Cantidad de vales de entrada de mercancías, máx. Período de almacenamiento, mín. Rest. Estante, etc. |  | Centro:____________Almacén:__________ |
| Datos de contabilidad (datos de valoración) | Área de valoración (=centro), clase de valoración | Clase de valoración, Precio por unidad, Control de precio, etc. | Pueden existir datos de área de valoración para cada ID de centro de su estructura de la empresa para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, diferente precio de valoración de un material en centros diferentes) | Centro:____________Clase de valoración:__________ |
| Cálculo de costes | Centro | Unidad de medida base, centro de beneficio, tamaño de lote para cálculo del coste, clase de valoración, precio control y unidad de precio. | Los datos del área de cálculo del coste pueden existir para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales. | Centro:____________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un material registro de datos maestros.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

Esta sección describe algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear un registro de datos maestros de material:

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizados o qué campos son obligatorios u opcionales. En función de los tipos de material, el el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos Los tipos de material utilizan la misma definición de rango de números

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe ser más de 8 dígitos. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un Número numérico de un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M . Actualmente, esto solo es visible en SAP GUI.

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de producto - Datos básicos](#unique_12) [página ] 8 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean datos básicos. |
| [Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas](#unique_13) [página ] 11 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Datos maestros de material – Datos de ventas (datos de IVA) es creado. |
| [Crear datos maestros de producto - Datos de compras](#unique_14) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean los datos de compras. |
| [Crear datos maestros de producto - Clasificación](#unique_15) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los Datos maestros de material – Clasificación. |
| [Crear datos maestros de producto - Datos de planificación MRP / Datos de centro](#unique_16) [página ] 18 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material – Datos de planificación/MRP (datos de centro). |
| [Crear datos maestros de producto: Preparación de trabajo](#unique_17) [página ] 21 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de material – Preparación de trabajo. |
| [Crear datos maestros de producto - Datos de almacén](#unique_18) [página ] 23 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Datos maestros de material – Los datos de almacén son creado. |
| [Crear datos maestros de producto - Datos de contabilidad / Datos de área de valoración](#unique_19) [página ] 26 | Especialista en datos maestros - Datos de producto | Crear material (MM01) o bien Gestionar datos maestros de producto (F1602) | Datos maestros de material – Se crean los datos de contabilidad (datos de valoración). |
| [Crear datos maestros de producto – Cálculo del coste](#unique_20) [página ] 29 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los datos maestros de material – Cálculo de costes. |

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

El siguiente procedimiento proporciona instrucciones para crear datos maestros de producto. Aplicaciones disponibles dependen de su rol asignado, por lo que hay dos opciones proporcionado.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria No se ofrece el sector para la entrada, el campo es rellenado con En la oscuridad .Tipo de material : KMAT - Materiales configurables | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Datos básicos 1 y Básico datos 2 y seleccione Continuar . | El Crear material (materiales configurables) se visualiza. |  |
| 5 | Introducir datos básicos | El Crear material CM-FL-V01 (configurable) materiales) vista, en la Datos básicos 1 introduzca la descripción del material (breve texto).Por ejemplo: Carretilla elevadora |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 pestaña, en el Datos generales la sección, haga siguientes entradas:Unidad base de Medida : UNGrupo de materiales : L004Gr.tp.pos.gen. : 0002 |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN la sección, haga siguientes entradas:Peso bruto : 3Unidad de peso : KGPeso neto : 2 | La pestaña Datos básicos 2 muestra. |  |
| 8 | Introducir datos básicos | El Datos básicos 2 no tiene para realizar cualquier entrada. | Una ventana nueva Última vista de datos alcanzada se abre con el mensaje Está a punto de salir. ¿Desea grabar los datos? para este material? |  |
| 9 | Guardar los datos | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Crear material (pantalla inicial) se visualiza.El Datos básicos se ha creado y guardado. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear nuevo maestro de productos. | En la Gestionar datos maestros de producto , seleccione Crear | Crear registro de datos maestros se visualiza. |  |
| 4 | Introducir datos para campos obligatorios | En la Crear registro de datos maestros , efectúe las siguientes entradas:Número de producto : por ejemplo, CM-FL-V01 …cualquier ID alfanumérico externo … (al menos este debe empezar por un carácter) o cuando no hay ninguna entrada El sistema asigna automáticamente un ID numéricoPara obtener más información sobre Número de producto , consulte el Tipo de material y rangos de números sección en Parámetros principales para la creación de datosTipo de producto : KMATGrupo de productos : por ejemplo, L004Unidad base : por ejemplo, UNDescripción : Carretilla elevadora |  |  |
| 5 | Seleccione OK. | En la Crear registro de datos maestros , seleccione OK . | Vista de producto muestra. |  |
| 6 | Introducir datos básicos | En la Producto > Información general > Datos básicos , efectúe las siguientes entradas:Sector : por ejemplo, 00 |  |  |
| 7 | Seleccionar descripciones | Ir a Producto > Información general > Descripciones . | El Descripciones se visualiza. |  |
| 8 | Seleccione Añadir (+) | En la Descripciones , seleccione + Añadir . | Algunos campos ya están rellenados. |  |
| 9 | Introducir datos de descripciones | En la Descripciones realice las siguientes entradas:Idioma : por ejemplo, InglésDescripción de producto : <su descripción> |  |  |
| 10 | Seleccionar unidad de medida base | Ir a Producto > Información general > Unidad de medida base . |  |  |
| 11 | Introducir datos de unidad de medida base | En la Peso ver, hacer lo siguiente entradas:Unidad de peso : por ejemplo, KGPeso bruto : por ejemplo, 2Peso neto : por ejemplo, 1Nota Si el Peso bruto , Unidad de peso o Peso neto campos no visualizar como campos de entrada, seleccione Consulte Más en la esquina derecha. |  |  |
| 12 | Guardar los datos | Seleccionar Grabar . | El sistema emite una notificación de que el objeto se ha guardado. |  |

### Crear datos maestros de producto - Datos de ventas / Datos de impuestos sobre ventas

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

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en la Procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear Material aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , realice lo siguiente entradas:Material : : CM-FL-V01Ramo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : : KMAT - Configurable materiales | Una nueva ventana muestra el Seleccionar vista(s) vista. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Ventas: Datos org.ventas 1 , Ventas: Datos org.ventas 2 y Ventas: Datos generales/de centro y seleccione Continuar . | Una nueva ventana muestra el Niveles de organización . |  |
| 5 | Introducir datos de niveles de organización | En la Niveles de organización vista, en el Nivel de organización sección, hacer las siguientes entradas y seleccione Continuar :Centro : por ejemplo, 1710Org.ventas : por ejemplo, 1710Canal distrib. : por ejemplo, 10 | Una nueva ventana muestra el Crear material (materiales configurables) vista.Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de ventas | En la Crear material CM-FL-V01 (configurable) materiales) vista, en la vista Ventas: Org.ventas 1 introduzca un valor adecuado para el <Clasificación fiscal>Normalmente se trata del valor 1 para totalmente sujeto a impuestos. | El Ventas: org.ventas 2 se visualiza.El valor introducido indica que el material está (normalmente) completo imponible. |  |
| 7 | Introducir datos de ventas | El Ventas: org.ventas 2 pestaña, en el Conceptos de agrupación haga que la sección entrada siguiente:Grupo de tipos de posición : 0002Gr.estadíst.material : 1 | Ha navegado a la siguiente pestaña, Ventas: General/Centro . |  |
| 8 | Introducir datos de ventas | El Ventas: General/Centro pestaña, en el Datos generales introduzca la sección datos siguientes:Verificación de disponibilidad : para ejemplo, PE |  |  |
| 9 | Introducir datos de ventas | En la Datos de expedición (tiempos en días) sección, introduzca los siguientes datos:Gpo.transp. :por ejemplo, 0001Gr.carga : por ejemplo, 0001 |  |  |
| 10 | Introducir datos de ventas | En la Parámetros generales de centro sección, indique los siguientes datos:Centro de beneficio : por ejemplo, YB110 o YB111 | Aparece una ventana nueva: Última vista de datos alcanzado con el mensaje Está a punto de salir. ¿Desea grabar los datos para este material? primero? . |  |
| 11 | Guardar los datos | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto se visualiza la ventana.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Editar. | Seleccionar Editar .Nota Este paso asume que continúa desde el paso anterior y ya están en el Gestionar Datos maestros de producto mosaico. Después de ha grabado sus datos de la sección anterior, el sistema está en Modo de visualización . Para continuar, debe estar en Editar Modo . | Modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar cadenas de distribución | En la Producto , seleccione Distribución Cadenas . | El Cadenas de distribución se visualiza. |  |
| 5 | Seleccione Añadir (+) | En la Cadenas de distribución > Cadenas de distribución , seleccione + (Añadir) | El Maestro de productos - Cadenas de distribución la vista se abre en Editar Modo . |  |
| 6 | Introducir datos de cadenas de distribución | En la Maestro de productos - Cadenas de distribución Ver marcas siguiendo entradas:DATOS GENERALES - Información generalOrganización de ventas : <Ventas Número org.> por ejemplo, 1710Canal de distribución : por ejemplo, 10Centro de entrega : <Centro número> por ejemplo, 1710TÉRMINOS DE AGRUPACIÓNGrupo de tipos de posición : por ejemplo, 0002Grupo de imputación : para ejemplo, 03 Finalizado ProductosIMPUESTO SOBRE VENTASPaís : <código de país> para ejemplo, DECategoría fiscal : TTX1Clasificación fiscal : Cualquiera 1 para material o 2 serviciosImpuesto Clasificación : por ejemplo 1 Impuesto completo al utilizar UTXJ Condición para determinación de impuestos para EE.UU.Clasificación fiscal depende de los requisitos específicos del país/región. Clasificación fiscal en el maestro de materiales y Tablas maestras de clientes determinan porcentaje de impuesto entradas.Solo para Brasil en el Clasificación fiscal sección, realice las siguientes entradas:País : BRImpuesto Categoría : IBRXClasificación fiscal : O 1 para material o 2 para servicios |  |  |
| 7 | Guardar los datos | Seleccionar Grabar . | El sistema emite una notificación que indica que el objeto es grabado. |  |

### Crear datos maestros de producto - Datos de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

|  |
| --- |
| Nota Si desea ejecutar el material KMAT con un proceso de terceros, amplíe la vista. |

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) Crear material (MM01).

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : : CM-FL-V01Ramo : MTipo de material : : KMAT - Materiales configurables | Una nueva ventana muestra el Seleccionar vista(s) vista. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Compras y seleccione Continuar . | Una nueva ventana muestra el Organizativo Niveles . |  |
| 5 | Introducir datos de niveles de organización | En la Niveles de organización vista, en el Nivel de organización sección, hacer las siguientes entradas y seleccione Continuar :Centro : por ejemplo, 1010 | Una nueva ventana muestra el Crear material (configurable) Materiales) vista.Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de compras | Asegúrese de que las siguientes entradas estén disponibles.Unidad de medida base : UNGrupo de materiales : L004 | El Compras muestra la pestaña |  |
| 7 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 – Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Editar. | Seleccionar Editar | Modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccione la vista Compras | En la Maestro de productos , seleccione Compras . | El Compras se visualiza. |  |
| 5 | Introducir datos de compras | En la Compras vista, realice lo siguiente entrada y seleccione Grabar .Unidad de medida de pedido : UN | El sistema emite una notificación que indica que el objeto es grabado. |  |

### Crear datos maestros de producto - Clasificación

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

Debe completar la sección anterior, Crear datos maestros de producto – Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial) , realice lo siguiente entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena con En la oscuridad .Tipo de material : KMAT – Materiales configurables | Una nueva ventana muestra el Seleccionar vista(s) vista. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Clasificación y seleccione Continuar . | Una nueva ventana muestra el Categoría de clase (1) vista |  |
| 5 | Introducir datos de niveles de organización | En la Nivel de restricciones sección, seleccione las siguientes entradas y seleccione Continuar :Descripción de categoría de clase : VariantesTipo : 300 | Una nueva ventana muestra la vista Clasificación. |  |
| 6 | Introducir datos de ventas | En la Clasificación vista, en el Asignaciones introduzca lo siguiente valores bajo el Clase y seleccione Grabar .AVC_CL_ELECADD_V01AVC_CL_REFCSTC_V01AVC_CL_COMMON_V01 | El Clasificación ventana de vista se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

|  |
| --- |
| Nota Los campos obligatorios no están disponibles actualmente para esta aplicación. Use la Opción 1 (arriba) |

### Crear datos maestros de producto - Datos de planificación MRP / Datos de centro

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

Debe completar un procedimiento anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con en el oscuro .Tipo de material : KMAT - Materiales configurables | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione MRP1 , MRP2 , MRP3 y MRP4 y seleccione Continuar . | El Niveles de organización ver se visualiza. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en el Nivel de organización sección, hacer las siguientes entradas:Centro : <Centro código> por ejemplo 1710Almacén : por ejemplo 171A | El Crear material (configurable) Materiales) se visualiza.Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de planificación/MRP | El Material (materiales configurables) vista, en el Planif.necesidades 1 pestaña, en el Datos generales la sección, haga entrada siguiente:Unidad de medida base : UN |  |  |
| 7 | Introducir datos de planificación/MRP | En la Método de planificación de necesidades la sección, haga siguientes entradas:Caract.planif.nec. : por ejemplo, PDPlanificador de necesidades : por ejemplo, 001 |  |  |
| 8 | Introducir datos de planificación/MRP | En la Cálculo del tamaño del lote sección, hacer la siguiente entrada:Cálculo del tamaño del lote : EX | La siguiente pestaña Planif.necesidades 2 muestra. |  |
| 9 | Introducir datos de planificación/MRP | En la Crear material CM-FL-V01 (configurable) Material) vista, en la MRP 2 , realice entradas en función de sus necesidades o en rellene como mínimo los campos obligatorios con valores, por ejemplo, Tiempo de fabricación propia en días. | La siguiente pestaña Planif.necesidades 3 muestra. |  |
| 10 | Introducir datos de planificación/MRP | En la Crear material (configurable) Materiales) vista, en la MRP 3 en la pestaña Planificación sección, realice las siguientes entradas:Grupo de estrategias : por ejemplo, 25Modo de consumo : por ejemplo, 2 |  |  |
| 11 | Introducir datos de planificación/MRP | En la Verificación de disponibilidad sección, hacer las siguientes entradas:Verificación de disponibilidad : por ejemplo, PEPlazo reaprov.total : por ejemplo, 3 | La siguiente pestaña Planif.necesidades 4 muestra. |  |
| 12 | Introducir datos de planificación/MRP | En la Crear material CM-FL-V01 (configurable) Material) vista, en la MRP 4 no es necesario realizar ninguna entrada. | Una ventana nueva Última vista de datos alcanzada abre con el mensaje Está a punto de salir. ¿Desea ¿Desea grabar primero los datos para este material? . |  |
| 13 | Grabar | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto ver se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Editar. | Seleccionar EditarNota Este paso supone que usted está continuando desde el paso anterior y ya están en el Gestionar datos maestros de producto mosaico. Después de guardar los datos de la sección anterior, el sistema está en Modo de visualización . Para continuar, debe estar en Modo de edición . | Modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar datos de centros | En la Maestro de productos , seleccione Centros | El Centros se visualiza. |  |
| 5 | Seleccione Añadir (+) | En la Centros sección de vista, seleccione + (Añadir) | El Centro la vista se abre en Editar Modo . |  |
| 6 | Introducir centros: Datos de información general | En la Centro > Datos generales , efectúe las siguientes entradas:Centro : <Centro número> por ejemplo, 1710Centro de beneficio : por ejemplo, YB110 o YB111Gr.carga : por ejemplo, 0001 - Carretilla elevadora |  |  |
| 7 | Seleccionar centros – Datos de planificación de necesidades | En la Centro , seleccione MRP Datos | El Datos MRP se visualiza. |  |
| 8 | Introducir centros – Datos de planificación de necesidades | En la Datos MRP , seleccione Datos MRP y hacer el seguimiento entradas:Verificación de disponibilidad : por ejemplo, PEPlazo de entrega previsto : por ejemplo, 3Tiempo de procesamiento de entrada de mercancías : para ejemplo, 1Caract.planif.nec. : Por ejemplo, PDPlanificador de necesidades : Por ejemplo, 001 |  |  |
| 9 | Seleccionar centros – Datos de tamaño de lote | En la Datos MRP , seleccione Datos de tamaño de lote . | El Datos de tamaño de lote sección de vista se visualiza. |  |
| 10 | Introducir centros – Datos de tamaño de lote | En la Datos de tamaño de lote vista, haga el entrada siguiente:Cálculo del tamaño del lote : para ejemplo EX |  |  |
| 11 | Seleccionar centros – Datos de previsión | En la Producto > CENTROS , seleccione PREVISIÓN . | PREVISIÓN muestra |  |
| 12 | Introducir centros - Datos de previsión | En la PREVISIÓN vista, haga el entrada siguiente:Tipo de período : por ejemplo, F |  |  |
| 13 | Volver a la vista principal | Seleccione la flecha hacia atrás para volver a Producto Maestro . | El Maestro de productos se visualiza. |  |
| 14 | Guardar los datos | Seleccionar Grabar . | El sistema emite una notificación de que el objeto se ha guardado. |  |

### Crear datos maestros de producto: Preparación de trabajo

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

Debe completar la sección anterior, Crear datos maestros de producto – Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) se visualiza. |  |
| 3 | Introducir datos básicos de material | En la Crear material (vista inicial) , hacer las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo no está ofrecido para entrada, el campo se rellena con en el oscuro .Tipo de material : KMAT - Materiales configurables | El Seleccionar vista(s) ver se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Preparación de trabajo , y seleccione Continuar . | El Niveles de organización ver se visualiza. |  |
| 5 | Introducir datos de niveles de organización | En la Niveles de organización crear la vista después de la entrada y seleccione Continuar .Centro : 1710 | Una ventana nueva Modificar material CM-FL-V01 (configurable) materiales) muestra. |  |
| 6 | Introducir datos de preparación de trabajo | En la Modificar material CM-FL-V01 (configurable) materiales) ventana, debajo General Datos introduzca las siguientes entradas y seleccione Grabar .Unidad de medida base : UNSupervisor de producción : YB3Perfil de programación de producción : YB0003 | Aparece una ventana nueva: Última vista de datos alcanzado con el mensaje Está a punto de salir. ¿Desea grabar los datos para este material? primero? |  |
| 7 | Guardar los datos | En la Última vista de datos alcanzada seleccione Sí . | El Datos maestros – Producto ventana se visualiza.Se han guardado los datos. |  |

Procedimiento: Opción 2 – Gestionar datos maestros de producto

|  |
| --- |
| Nota Los campos obligatorios no están disponibles actualmente para esta aplicación. Uso Opción 1 (arriba) y grabe sus entradas. |

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

Debe completar un procedimiento anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo El campo de entrada está oculto, no se requiere ninguna entrada. Cuándo el ramo no se ofrece para la entrada, el el campo se rellena con En la oscuridad .Tipo de material : KMAT - Configurable materiales | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione la ventana vistas siguientes y seleccione Continuar :Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2 | El Niveles de organización ver se visualiza. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización vista, en el Nivel de organización sección, hacer siguientes entradas:Centro : por ejemplo, 1710Almacén : por ejemplo, 171A | Se abre una ventana nueva que muestra la Crear material (configurable) materiales) vista.Obtendrá el siguiente mensaje del sistema en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de almacén | En la Crear material (materiales configurables) vista, en el Dat.ce./almacén 1 pestaña, en el Datos generales la sección, haga entrada siguiente:Número de vales de entrada de mercancías : por ejemplo, 1 | Se muestra la siguiente pestaña: Centro datos/alm.2 . |  |
| 7 | Confirmar entradas | El Dat.ce./Almacén 2 pestaña, no debe realizar cualquier entrada. | Una ventana nueva Última vista de datos alcanzada abre con el mensaje Está a punto de salir. ¿Desea ¿Desea grabar primero los datos para este material? . |  |
| 8 | Grabar | En la Última vista de datos alcanzada ventana, seleccionar Sí . | El Datos maestros - Producto se visualiza la ventana.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Editar. | Seleccionar EditarNota Este paso asume que continúa desde el paso anterior y ya están en el Gestionar producto Datos maestros mosaico. Después de grabar los datos de la sección anterior, el sistema está en Modo de visualización . Para continuar, debe estar en Modo de edición . | Modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar datos de centros | En la Producto , seleccione CENTROS .Nota Si no hay ningún registro de datos de centro, siga los pasos en el sección anterior, Crear datos maestros de producto - MRP Datos de planificación / Datos de centro | El CENTROS se visualiza. |  |
| 5 | Seleccionar detalles de centro | En la CENTROS vista, utilice el icono de flecha para seleccione los datos de centro que ha creado en el paso anterior. | El Centro de maestro de productos ver se visualiza. |  |
| 6 | Navegar a Centro: Almacén | En la Maestro de productos: Centro ver navegar a CENTROS > UBICACIONES DE ALMACENAMIENTO . | El Maestro de productos: CENTROS la vista se abre en Modo de edición . |  |
| 7 | Seleccione Añadir (+) | En la UBICACIONES DE ALMACENAMIENTO > Almacenes y seleccione + (Añadir) . | El Centro – Almacén la vista se abre en Modo de edición . |  |
| 8 | Introducir centro: Datos de almacén | En la Almacenes marca de visualización siguientes entradas:Almacén: <Número de almacén> por ejemplo, 171A |  |  |
| 9 | Volver a la vista principal | Seleccione la flecha hacia atrás, dos veces, para volver a Maestro de productos . | Volver a Maestro de productos vista. |  |
| 10 | Grabar | Seleccionar Grabar . | El sistema emite una notificación de que el objeto se ha guardado. |  |

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

Debe completar un procedimiento anterior, Crear datos maestros de producto - Básico Datos , antes de continuar con este procedimiento.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | El Crear material (vista inicial) , efectúe las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria No se ofrece el sector para la entrada, el campo es rellenado con En la oscuridad .Tipo de material : KMAT - Configurable materiales | El Seleccionar vista(s) muestra. |  |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione la ventana vistas siguientes y seleccione Continuar :Contabilidad 1Contabilidad 2 | El Niveles de organización se visualiza. |  |
| 5 | Introducir datos de niveles de organización | En la Niveles de organización vista, en la Sección Nivel de organización, realice las siguientes entradas:Centro : 1710 | El Crear material (materiales configurables) se visualiza.Obtendrá la información en la parte inferior de la vista: El material ya existe y se ampliado . |  |
| 6 | Introducir datos de contabilidad | En la Crear material (materiales configurables) vista, en el Contabilidad 1 pestaña, en el Datos de valoración generales sección, hacer la siguiente entrada:Categoría de valoración : 7920 |  |  |
| 7 | Introducir datos de contabilidad | En la Precios y valores la sección, haga siguientes entradas:Precio estándar : 1Precio por unidad : 1Ctrl.precio : S | Ha navegado a la siguiente pestaña, Contabilidad 2 . |  |
| 8 | Confirmar entradas | En la Contabilidad 2 no tiene para realizar cualquier entrada. | Una ventana nueva Última vista de datos alcanzada se visualiza con el mensaje Está a punto de salir. ¿Desea grabar los datos? para este material? . |  |
| 9 | Guardar los datos | En la ventana Última vista de datos alcanzada seleccionar Sí . | El Datos maestros - Producto se visualiza la ventana.Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . |  |  |
| 3 | Seleccione Editar. | Seleccionar EditarNota Este paso asume que continúa desde el paso anterior y ya están en el Gestionar Datos maestros de producto mosaico. Después de ha grabado sus datos de la sección anterior, el sistema está en Modo de visualización . Para continuar, debe estar en Editar Modo . | Modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar datos de área de valoración | En la Producto , seleccione VALORACIÓN ÁREAS | El ÁREAS DE VALORACIÓN se visualiza. |  |
| 5 | Seleccione Añadir (+) | En la ÁREAS DE VALORACIÓN , seleccione + (Añadir) | El ÁREAS DE VALORACIÓN la vista se abre en Editar Modo . |  |
| 6 | Introducir datos de área de valoración | En la ÁREAS DE VALORACIÓN > Área de valoración realice las siguientes entradas:Área de valoración : <número> , por ejemplo, 1710Control de precio Determinación: 2Categoría de valoración: por ejemplo, 7920 |  |  |
| 7 | Introducir datos de área de valoración actual | En la Valoración , seleccione Período actual vista, haga el siguientes entradas:Precio medio variable : por ejemplo, 20Control de precio : para ejemplo, S |  |  |
| 8 | Volver a la vista principal | Seleccione la flecha hacia atrás para volver a Producto Maestro | Volver a Maestro de productos vista. |  |
| 9 | Grabar | Seleccionar Grabar . | El sistema emite una notificación de que el objeto se ha guardado. |  |

### Crear datos maestros de producto – Cálculo del coste

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

Debe completar la sección anterior, Crear datos maestros de producto – Básico Datos , antes de continuar con esta sección.

Inicie el procedimiento después de grabar el Datos básicos entradas, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 – Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (MM01) muestra. |  |
| 3 | Introducir datos básicos de material | En Crear material (vista inicial) , efectúe las siguientes entradas:Material : CM-FL-V01Ramo : MNota Si el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo no está ofrecido para entrada, el campo se rellena con en el oscuro .Tipo de material : KMAT – Configurable materiales | El Seleccionar vista(s) se visualiza. | El campo no está disponible. |
| 4 | Seleccionar vistas | En la Seleccionar vista(s) seleccione Cálculo del coste 1 y Cálculo de costes 2 y seleccione Continuar . | El Categoría de clase (1) se visualiza. |  |
| 5 | Introducir datos de niveles de organización | En la Nivel de organización sección, seleccione las siguientes entradas y Continuar :Centro : 1710 | El Cálculo del coste 1 se visualiza. |  |
| 6 | Introducir datos de cálculo del coste 1 | En la Cálculo del coste 1 , seleccione la vista las siguientes entradas y seleccione la Cálculo de costes 2 pestaña.Unidad de medida base : UNCentro de beneficio : YB110Tamaño de lote para cálculo del coste : 100 | El Cálculo del coste 2 se visualiza.Se han guardado los datos. |  |
| 7 | Introducir datos de cálculo del coste 2 | En la Cálculo del coste 2 , seleccione la vista las siguientes entradas y seleccione Continuar a grabar :Categoría de valoración : 7920Control de precio : SUnidad de precio : 1 | Se han guardado los datos. |  |

Procedimiento: Opción 2 – Gestionar datos maestros de producto

|  |
| --- |
| Nota Los campos obligatorios no están disponibles actualmente para esta aplicación. Use la Opción 1 (arriba) y grabe sus entradas. |

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
> Flagged while digesting this document, not verified: Text is machine-translated and may contain errors (e.g. 'Categoría de valoración' used for valuation class); 'Ramo' vs 'Sector' terminology varies.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Procedure steps assume MM01 exists, while it is described in Fiori; some Brazil tax/field details refer to other scope items.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2t7-285]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-2t7-283]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 59,778 chars in the whole document
