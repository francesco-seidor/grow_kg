---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-embalaje-e
title: "Script de datos maestros: Crear maestro de productos de tipo \"Embalaje en préstamo\" - MDS (65B) (65B_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (65B): test steps to create a returnable packaging (LEIH) product master via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [65B_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", product master data, returnable packaging, material master basic data, sales data, mrp planning data, storage data, accounting data, business roles, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-498
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear maestro de productos de tipo "Embalaje en préstamo" - MDS (65B) (65B_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear maestro de productos de tipo "Embalaje en préstamo" - MDS (65B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894826)

[2 Requisitos previos 3](#_Toc233894827)

[2.1 Acceso al sistema 3](#_Toc233894828)

[2.2 Roles 3](#_Toc233894829)

[2.3 Unidades organizativas necesarias 3](#_Toc233894830)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894831)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233894832)

[2.5.1 Tipo de material y rangos de números 5](#_Toc233894833)

[2.5.2 Ramo 5](#_Toc233894834)

[3 Tabla de resumen 6](#_Toc233894835)

[4 Procedimientos de prueba 7](#_Toc233894836)

[4.1 Crear datos maestros de material (producto) - Datos básicos 7](#_Toc233894837)

[4.2 Crear datos maestros de material (producto) - Datos de ventas (datos de IVA) 10](#_Toc233894838)

[4.3 Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro) 14](#_Toc233894839)

[4.4 Crear datos maestros de material (producto) - Datos de almacén 17](#_Toc233894840)

[4.5 Crear datos maestros de material (producto) - Datos de contabilidad 19](#_Toc233894841)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

El maestro de materiales o productos contiene información sobre todos los materiales físicos que se almacenan y venden.

El maestro de materiales contiene información como el número de material unívoco, el nombre, el tipo de material, la unidad de medida, las descripciones, el peso y dimensiones. Esta información de material se utiliza y almacena en transacciones como pedidos de cliente, entregas y movimientos de mercancías.

Como toda la información de un material se almacena centralmente, la información del maestro de materiales se organiza en diferentes vistas. Por ejemplo, ventas, almacenamiento y contabilidad.

Parte de la información de cada material es específica de determinadas unidades organizativas. Por ejemplo, una descripción de ventas es específica de una unidad (conocida como área de ventas), un planificador de necesidades es específico de un sitio específico (conocido como centro) o alguna información puede ser específica de un almacén.

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

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Descripción de material (texto breve) , Número de material , Material Grupo , Unidad de medida base , etc. | Datos básicos solo existe una vez para un registro de datos maestros de material. | N/D |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales , Grupo de tipos de posición , Gpo.transporte , Cargando Grupo , etc. | Pueden existir datos de ventas para cada organización de ventas de su estructura empresarial para la que se utiliza el registro maestro de materiales. | Centro:____________Organización de ventas:__________Canal de distribución:__________ |
| Datos de planificación/MRP | Centro, almacén | Caract.planif.nec. , Planificador de necesidades , Plazo de entrega previsto , etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función de la necesidad de realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Datos de almacén | Centro, almacén | Centro de beneficio , etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales.Los datos de almacén (contexto de planificación) son opcionales en función de la necesidad de realizar una planificación específica de almacén. | Centro:____________Almacén:__________ |
| Datos de contabilidad | Área de valoración(=Centro) | Precio por unidad , Control de precio , etc. | Los datos del área de valoración pueden existir para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales. Cada centro representa un área de valoración (por ejemplo, precio de valoración diferente de un material en diferentes centros). | Centro:____________Clase de valoración:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de material.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | La asignación de un centro de beneficio a un maestro de materiales (productos) es necesaria para procesos de valoración correctos. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear un registro de datos maestros de materiales.

#### Tipo de material y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizar o qué campos son obligatorios u opcionales. En función de los tipos de material, el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos los tipos de material utilizan el misma definición de rango de números.

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este rango debe comenzar con un carácter. En general, el ID no debe tener más de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este rango se utiliza si el sistema debe asignar automáticamente un número numérico a un material. |

#### Ramo

El contenido estándar solo proporciona un ramo M . Actualmente, este es visible solo en SAP GUI .

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.

Puede encontrar todas las demás aplicaciones no incluidas en la página de inicio utilizando la barra de búsqueda.

Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones .

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos básicos. |
| [Crear datos maestros de material (producto) - Datos de ventas (datos de IVA)](#unique_12) [página ] 10 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean datos de ventas. |
| [Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)](#unique_13) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Se crean los datos maestros de material - Datos de planificación/MRP. |
| [Crear datos maestros de material (producto) - Datos de almacén](#unique_14) [página ] 17 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Se crean los datos de almacén. |
| [Crear datos maestros de material (producto) - Datos de contabilidad](#unique_15) [página ] 19 | Especialista en datos maestros - Datos de producto | Crear material (MM01) / Gestionar datos maestros de producto (F1602) | Datos maestros de material - Datos de contabilidad (datos de área de valoración). |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear datos maestros de material (producto) - Datos básicos

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (pantalla inicial) es visualizados. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) introduzca lo siguiente:Material : <Número de material>Ramo : Ingeniería mecánicaNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo está atenuado.Tipo de material : Embalaje en préstamoSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) seleccione lo siguiente entradas y seleccione Continuar :Datos básicos 1Datos básicos 2 | El Crear material... (Embalaje en préstamo) se visualiza. |  |
| 5 | Introducir datos básicos | El Datos básicos 1 introduzca una descripción de material (texto breve). |  |  |
| 6 | Introducir datos básicos | En el Datos básicos 1 en la pestaña Datos generales introduzca la sección descripciones para lo siguiente:Unidad de medida baseGrupo de materialesGr.tp.pos.gen. : LEIH |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN introduzca lo siguiente:Peso brutoUnidad de pesoPeso netoPulsar Intro . | La siguiente pestaña, Datos básicos 2 se visualiza. |  |
| 8 | Completar datos básicos | No se requieren entradas para Datos básicos 2 . |  |  |
| 9 | Guardar los datos | En la parte inferior derecha de la pantalla, seleccione Grabar para guardar los datos. | El Crear material (pantalla inicial) la pantalla es visualizados.Los datos básicos se crean y se graban. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | El Gestionar datos maestros de producto la pantalla es visualizados. |  |
| 3 | Seleccione Crear nuevo maestro de productos. | El Gestionar datos maestros de producto en la pantalla Productos sección, seleccione Crear . | El Crear registro de datos maestros la pantalla es visualizados. |  |
| 4 | Introducir datos para campos obligatorios | El Crear registro de datos maestros , efectúe las siguientes entradas:Número de producto : por ejemplo, Z …Nota Puede introducir cualquier ID alfanumérico externo y ese ID debe empezar con un carácter alfanumérico o si proporciona ninguna entrada, el sistema asigna automáticamente un ID numérico.Para obtener más información sobre el número de producto, consulte el anterior Tipo de material y rangos de números sección.Tipo de producto : LEIHGrupo de productos : por ejemplo, L006Unidad base : por ejemplo, UNDescripción : <cualquier descripción> |  |  |
| 5 | Seleccione OK. | Seleccionar OK . |  |  |
| 6 | Introducir datos básicos | Ir a Gestionar maestro de productos > Información general > Datos básicos , y realice la siguiente entrada:Sector : por ejemplo, 00 |  |  |
| 7 | Seleccione Añadir (+) | Ir a Gestionar maestro de productos > Información general > Descripciones y seleccione Crear . | La descripción en el idioma predeterminado (por ejemplo, inglés) ya se ha rellenado. |  |
| 8 | Introducir datos de descripciones | En la Descripciones , efectúe las siguientes entradas:Idioma : por ejemplo, AlemánDescripción de producto : <su descripción> |  |  |
| 9 | Introducir datos de fecha de peso | En la Peso (si no aparece, seleccione Mostrar más ), introduzca el siguiente:Peso bruto : por ejemplo, 2Unidad de peso : por ejemplo, KGPeso neto : por ejemplo, 1Nota Si Peso la sección no aparece, seleccione Mostrar más .Cuando los campos Peso bruto , Unidad de peso , o Peso neto No proporcionar un campo de entrada, actualizar o volver a cargar la página web. Después de actualizar o volver a cargar, los campos están disponibles para entrada. |  |  |
| 10 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de material (producto) - Datos de ventas (datos de IVA)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar la sección anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material (MM01) . | El Crear material (pantalla inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : Ingeniería mecánicaNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo está atenuado.Tipo de material : LEIH Embalaje en préstamoSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Ventas: Datos org.ventas 1 , Ventas: Datos org.ventas 2 , y Ventas: Datos generales/de centro y seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización sección, introduzca las descripciones para lo siguiente:CentroOrg.ventasCanal distrib.Seleccionar Continuar .Nota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliará. | El Crear material... (Embalaje en préstamo) se visualiza. |  |
| 5 | Introducir datos de ventas | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Ventas: Org.ventas 1 en la pestaña Datos generales , realice las siguientes entradas:Unidad de medida baseCentro suministrador |  |  |
| 6 | Introducir datos de ventas | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Ventas: Org.ventas 1 en la pestaña Datos fiscales , realice las siguientes entradas:Clasificación fiscal : 1Nota El valor introducido indica que el material está (normalmente) completo sujeto a impuestos.Solo para Brasil: en el Datos fiscales la sección, haga siguientes entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : 1Pulsar Intro . | La siguiente pestaña, Ventas: org.ventas 2 se visualiza. |  |
| 7 | Introducir datos de ventas | En el Ventas: org.ventas 2 en la pestaña Conceptos de agrupación la sección, haga siguientes entradas:Gr.estadíst.materialGrupo de tipos de posición : CB02Gr.tp.pos.gen. : LEIHMat.gr.imputación : Y2Pulsar Intro . | La siguiente pestaña, Ventas: General/Centro se visualiza. |  |
| 8 | Introducir datos de ventas | En el Ventas: General/Centro en la pestaña Datos generales introduzca la sección Datos siguientes:Verificación de disponibilidad : RE |  |  |
| 9 | Introducir datos de ventas | En el Ventas: General/Centro en la pestaña Datos de expedición (tiempos en días) introduzca los siguientes datos:Gpo.trans. : <0001>Gr.carga : <0001> |  |  |
| 10 | Introducir datos de ventas | En el Ventas: General/Centro en la pestaña Parámetros generales de centro sección, introduzca los siguientes datos:Centro de beneficio |  |  |
| 11 | Grabe los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar cadenas de distribución | El Producto seleccione el pulsador Cadenas de distribución pestaña. | El Cadenas de distribución se visualiza. |  |
| 4 | Seleccione Añadir (+) | En el Cadenas de distribución , seleccione Crear . | Cadenas de distribución se visualiza en modo de edición. |  |
| 5 | Introducir datos de cadenas de distribución | El Cadenas de distribución de pantalla, haga siguientes entradas:Ir a Información general > Datos generales :Organización de ventas : <Número de organización de ventas>Nota El valor de la unidad organizativa viene determinado por lo que se ofrece en la ayuda para entradas.Canal de distribución : por ejemplo, 10Centro de entrega : <Número de centro>En la Términos de agrupación sección:Grupo de tipos de posición : por ejemplo, CB02Grupo de imputación : por ejemplo, Y2 Mercancías en préstamoEn la Impuesto sobre ventas sección:País : <código de país>Categoría fiscal : por ejemplo, TTX1Clasificación fiscal : por ejemplo, o 1 para material o 2 para servicios. Clasificación fiscal ejemplo: 1 lleno impuesto al utilizar la condición para determinación de impuestos UTXJ para los EE. UU.Nota La clasificación fiscal depende de los requisitos específicos de la país. Clasificación fiscal en el maestro de materiales y en el maestro de clientes tablas determinan entradas porcentuales.Solo para Brasil : en el Clasificación fiscal sección, haga lo siguiente entradas:País : BRCategoría fiscal : IBRXClasificación fiscal : 1 |  |  |
| 6 | Volver a la vista principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 7 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior,[Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (pantalla inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : Ingeniería mecánicaNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo está atenuado.Tipo de material : Embalaje en préstamoSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Planif.necesidades 1 , Planif.necesidades 2 , Planif.necesidades 3 , y Planif.necesidades 4 y seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización sección, efectúe las siguientes entradas:Centro : <Número de centro>Almacén : <Número de almacén>Seleccionar Continuar .Nota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliará . | El Crear material... (Embalaje en préstamo) se visualiza. |  |
| 5 | Introducir datos de planificación/MRP | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Planif.necesidades 1 en la pestaña Método de planificación de necesidades , realice las siguientes entradas:Caract.planif.nec. : NDPlanificador de necesidades : <001>Pulsar Intro . | La siguiente pestaña, Planif.necesidades 2 se visualiza. |  |
| 6 | Introducir datos de planificación/MRP | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Planif.necesidades 2 en la pestaña Programación , realice la siguiente entrada:Plazo entrega prev. : por ejemplo, 10En la Aprovisionamiento , realice la siguiente entrada:Clase de aprovisionamiento : FPulsar Intro . | La siguiente pestaña, Planif.necesidades 3 se visualiza. |  |
| 7 | Introducir datos de planificación/MRP | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Planif.necesidades 3 en la pestaña Verificación de disponibilidad , realice la siguiente entrada:Verificación de disponibilidad : por ejemplo, REPulsar Intro . | La siguiente pestaña, Planif.necesidades 4 se visualiza. |  |
| 8 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto seleccione el pulsador Centros pestaña. | El Centros se visualiza. |  |
| 4 | Seleccione Añadir (+) | En el Centros , seleccione Crear . | El Centro se visualiza en modo de edición. |  |
| 5 | Introducir centros - Datos generales | Ir a Información general > Datos generales , y realice las siguientes entradas:Centro : Número de centro , por ejemplo, 1010Centro de beneficio : por ejemplo, YB111En la Ventas , realice la siguiente entrada:Grupo de carga : por ejemplo, 0001 |  |  |
| 6 | Introducir centros - Datos de planificación de necesidades | Ir a Datos de planificación de necesidades > Datos MRP , y realice las siguientes entradas:Verificación de disponibilidad : por ejemplo, RECaract.planif.nec. : por ejemplo, NDPlanificador de necesidades : por ejemplo, 001 |  |  |
| 7 | Introducir centros - Datos de aprovisionamiento | Ir a Datos de planificación de necesidades > Aprovisionamiento , y realice la siguiente entrada:Plazo de entrega previsto : por ejemplo, 10 |  |  |
| 8 | Volver a la vista principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de material (producto) - Datos de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (pantalla inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : Ingeniería mecánicaNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo está atenuado.Tipo de material : Embalaje en préstamoSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione lo siguiente:Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización sección, efectúe las siguientes entradas:Centro : por ejemplo, <Número de centro>Almacén : <Número de almacén>Seleccionar Continuar .Nota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliará. | El Crear material... (Embalaje en préstamo) se visualiza. |  |
| 5 | Introducir datos de almacén | Para el Dat.ce./almacén 1 no se requieren entradas. |  |  |
| 6 | Confirmar entradas | Para el Dat.ce./Almacén 2 no se requieren entradas. |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de centros | El Producto seleccione el pulsador Centros pestaña.Nota Si no hay ningún registro de datos de centro, siga los pasos de la sección anterior. [Crear datos maestros de material (producto) - Datos de planificación/MRP (datos de centro)](#unique_13) [página ] 14. | El Centros se visualiza. |  |
| 4 | Seleccionar detalles de centro | En el Centros utilice el icono de flecha para seleccionar los datos de centro que ha creado en el paso. | El Centro se visualiza. |  |
| 5 | Navegar a Centro: Almacén | El Centro pantalla, vaya a Almacenes > Almacenes . |  |  |
| 6 | Seleccione Añadir (+) | En el Almacenes en la pestaña Almacenes sección, seleccione Crear . | El Centro - Almacenes Se muestra la vista. |  |
| 7 | Introducir centro: Datos de almacén | En la Centro - Almacenes , realice la siguiente entrada:Almacén : <Número de almacén> |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar dos veces para volver al Producto pantalla. | El Producto se visualiza. |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

### Crear datos maestros de material (producto) - Datos de contabilidad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de material (producto). Las aplicaciones disponibles dependen de su rol asignado, por lo que se proporcionan dos opciones.

Requisito previo

Debe completar el procedimiento anterior, [Crear datos maestros de material (producto) - Datos básicos](#unique_11) [página ] 7, antes de continuar con esta sección.

Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

Procedimiento: Opción 1 - Crear material

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear material (MM01) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | El Crear material (pantalla inicial) se visualiza. |  |
| 2 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Número de material>Ramo : Ingeniería mecánicaNota Si el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo está atenuado.Tipo de material : Embalaje en préstamoSeleccionar Seleccionar vista(s) . | El Seleccionar vista(s) se visualiza. |  |
| 3 | Seleccionar vistas | El Seleccionar vista(s) seleccione lo siguiente:Contabilidad 1Contabilidad 2Seleccionar Continuar . | El Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización sección, realice la siguiente entrada:Centro : <Número de centro>Seleccionar Continuar .Nota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliará . | El Crear material... (Embalaje en préstamo) se visualiza. |  |
| 5 | Introducir datos de contabilidad | El Crear material... (Embalaje en préstamo) en la pantalla, debajo de la Contabilidad 1 en la pestaña Valoración actual , realice las siguientes entradas:Categoría de valoración : por ejemplo, 3050Precio variable : por ejemplo, 5Control de precio : por ejemplo, VPulsar Intro .Nota La clase de valoración no es obligatoria para el tipo de producto LEIH, puede fijarla como vacía mediante la aplicación Modificar material (MM02) . | La siguiente pestaña, Contabilidad 2 se visualiza. |  |
| 6 | Confirmar entradas | Para el Contabilidad 2 no se requieren entradas. |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de producto

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de producto (F1602) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de producto (F1602) . | Se abre la aplicación y se visualizan varios campos de búsqueda. |  |
| 2 | Buscar y abrir el producto para editarlo | Busque el producto creado anteriormente introduciendo el número de producto en la Producto campo de búsqueda.Seleccione el producto de la lista que le llevará al Producto pantalla.Seleccionar Editar . | El Producto se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 3 | Seleccionar datos de área de valoración | El Producto seleccione el pulsador Áreas de valoración pestaña. | El Áreas de valoración se visualiza. |  |
| 4 | Seleccione Crear. | En el Áreas de valoración en la pestaña Áreas de valoración sección, seleccione Crear . | El Área de valoración se visualiza en modo de edición. |  |
| 5 | Introducir datos de área de valoración actual | En el Información general en la pestaña Datos generales la sección, haga siguientes entradas:Área de valoración : por ejemplo, 1010Categoría de valoración : por ejemplo, 3050En la Período actual , realice las siguientes entradas:Precio de inventario : por ejemplo, 5Control de precio : por ejemplo, Precio medio variable/Precio interno periódico (V) |  |  |
| 6 | Volver a la pantalla principal | Seleccionar Aplicar para volver al Producto pantalla. | El Producto se visualiza. |  |
| 7 | Guardar los datos | Seleccionar Grabar . | El objeto se ha grabado. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-returnable-packaging]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-499]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-501]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-embalagem-reto]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 40,873 chars in the whole document
