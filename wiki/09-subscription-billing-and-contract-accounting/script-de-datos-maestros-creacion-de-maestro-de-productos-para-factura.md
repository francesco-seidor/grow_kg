---
id: 09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura
title: Script de datos maestros - Creación de maestro de productos para facturación basada en consumo (3JA) (3JA_S4CLD2608_Master_Data_ES_XX)
description: "Spanish SAP S/4HANA Cloud 2608 master data script (3JA): create configurable material with variant pricing for consumption-based billing, step by step."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_ES_XX]
keywords: [Variant-Configured Products in Provider Contracts, master data script, configurable material, characteristics, classes, configuration profile, variant pricing, material classification, sales data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-324
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de productos para facturación basada en consumo (3JA) (3JA_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de productos para facturación basada en consumo - MDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894600)

[2 Requisitos previos 3](#_Toc233894601)

[2.1 Acceso al sistema 3](#_Toc233894602)

[2.2 Roles 3](#_Toc233894603)

[2.3 Unidades organizativas necesarias 3](#_Toc233894604)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894605)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894606)

[2.5.1 Agrupaciones y rangos de números 4](#_Toc233894607)

[2.5.2 Ramo 5](#_Toc233894608)

[3 Tabla de resumen 6](#_Toc233894609)

[4 Procedimientos de prueba 7](#_Toc233894610)

[4.1 Crear maestro de materiales configurable - Datos básicos 7](#_Toc233894611)

[4.2 Crear característica 8](#_Toc233894612)

[4.3 Crear clase 11](#_Toc233894613)

[4.4 Crear perfil de configuración 12](#_Toc233894614)

[4.5 Crear maestro de materiales - Clasificación 13](#_Toc233894615)

[4.6 Crear determinación de precios de variante 14](#_Toc233894616)

[4.7 Crear datos maestros de producto - Datos de ventas/Datos de impuestos sobre ventas 16](#_Toc233894617)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un registro de datos maestros de material para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance del SAP S/4HANA Cloud Public Edición El contenido de no se describe en este documento, aunque puede que aparezca en la IU.

Un registro maestro de productos con determinación de precios de variante que se crea como se describe aquí se puede utilizar para la facturación basada en el consumo.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Modelador de configuración de producto | SAP_BR_PRODUCT_CONFIG_MODELER | Configuración de variantes | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de unidades organizativas | Descripción de material (texto breve), Número de material, Grupo de materiales, Unidad de medida base, etc. | Los datos básicos solo existen una vez para un registro de datos maestros de material. | n/d |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales, Grupo de tipos de posición, etc. | Pueden existir datos de centro para cada ID de centro de su estructura empresarial para la que se utiliza el registro maestro de materiales. | Centro: ____________ Organización de ventas: __________ Canal de distribución: __________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un maestro registro de datos.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear un registro de datos maestros de material:

#### Agrupaciones y rangos de números

Con la ayuda de los tipos de material, el sistema determina qué segmentos de datos (vistas) se pueden actualizados o qué campos son obligatorios u opcionales. En función de los tipos de material, el el sistema también determina los rangos de números para materiales. En el contenido estándar de SAP, todos Los tipos de material utilizan la misma definición de rango de números

#### Ramo

El contenido estándar solo proporciona un ramo M. Actualmente, esto es visible en SAP Solo GUI

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear maestro de materiales configurable - Datos básicos](#unique_11) [página ] 7 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Datos maestros de material – Se crean datos básicos. |
| [Crear característica](#unique_12) [página ] 8 | Modelador de configuración de producto | Gestionar características (CT04) | Se ha creado la característica. |
| [Crear clase](#unique_13) [página ] 11 | Modelador de configuración de producto | Gestionar clases (CL02) | Se ha creado la clase. |
| [Crear perfil de configuración](#unique_14) [página ] 12 | Modelador de configuración de producto | Entorno de modelado VC (PMEVC) | Se ha creado el perfil de configuración. |
| [Crear maestro de materiales - Clasificación](#unique_15) [página ] 13 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los Datos maestros de material – Clasificación. |
| [Crear determinación de precios de variante](#unique_16) [página ] 14 | Modelador de configuración de producto | Entorno de modelado VC (PMEVC) | La condición de variante se asigna a un valor de característica. |
| [Crear datos maestros de producto - Datos de ventas/Datos de impuestos sobre ventas](#unique_17) [página ] 16 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Se crean los Datos maestros de material – Datos de ventas (Datos de IVA). |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear maestro de materiales configurable - Datos básicos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso del proceso se crea la vista de datos básicos para el maestro de materiales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) pantalla, efectúe las siguientes entradas:Material : <CBPTS001>Sector sector : MNota Si el campo de entrada Ramo está oculto, no se obligatorio. Cuando el ramo no se ofrece para la entrada, el El campo se rellena en la oscuridad.Tipo de material : KMAT - Materiales configurables | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Datos básicos 1 y Datos básicos 2 y seleccione Continuar . | El Crear material (materiales configurables) se visualiza. |  |
| 5 | Introducir datos básicos | El Crear material CBPTS001 (materiales configurables) pantalla, en la pantalla Datos básicos 1 introduzca la descripción del material (texto breve).Por ejemplo, introduzca <Herramientas eléctricas basadas en el consumo> . |  |  |
| 6 | Introducir datos básicos | El Datos básicos 1 en la pestaña General Datos , realice las siguientes entradas:Unidad base de Medida : <UN>Gr.tp.pos.gen. : <0003> |  |  |
| 7 | Introducir datos básicos | En la Dimensiones/EAN , realice la siguiente entrada:Unidad de peso : KGSeleccione el Datos básicos 2 pestaña. |  |  |
| 8 | Introducir datos básicos | El Datos básicos 2 no es necesario realizar ninguna entrada.Pulsar Intro . | El Última vista de datos alcanzada con el mensaje: Está a punto de salir. ¿Eres tú? ¿Desea grabar primero los datos para este material? . |  |
| 9 | Guardar los datos | El Última vista de datos alcanzada , seleccione Sí . | El Crear material (pantalla inicial) se visualiza.Los datos básicos se crean y se graban. |  |

### Crear característica

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad IMG se crea una característica.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Abrir Gestionar datos maestros de cliente | Abierto Gestionar características (CT04) . | Se abre la aplicación. | Pantalla común para el modo de creación, modificación y visualización. |
| 3 | Introduzca el nombre de característica | Realice la siguiente entrada y seleccione Crear :Característica : <CATEGORÍA> | El Crear característica se visualiza. | El valor en el Inicio de validez El campo es rellenado automáticamente.Si la característica <CATEGORY> ya existe, cree la característica <CATEGORY>_Vnn, donde nn es la ejecución número. |
| 4 | Introducir datos básicos | El Datos básicos , efectúe las siguientes entradas:El Datos básicos sección:Descripción : <Categoría>Estado : Liberado (por defecto)El Formato sección:Tipo de datos : Formato carácterCtd.caract. : <15>Distingue entre mayúsculas y minúsculas : <no seleccionado>El Valoración sección:Seleccione el Valor individual botón de selección.Anule la selección de Restringible casilla de selección. |  |  |
| 5 | Introducir valores | El Valores en la pestaña Valores permitidos , realice las siguientes entradas.Valor caract. :<ESTÁNDAR><HIGH_END>Descripción :<Herramientas eléctricas estándar><Herramientas eléctricas de alta gama>Seleccione el Valor por defecto para la casilla de selección <ESTÁNDAR> valor. |  |  |
| 6 | Grabar la característica | Seleccionar Grabar . | Se crea la característica. |  |
| 7 | Crear otra característica | Realice la siguiente entrada y seleccione Crear :Característica : <CATEGORÍA_VARCOND> |  |  |
| 8 | Introducir datos básicos | El Datos básicos , efectúe las siguientes entradas:El Datos básicos sección:Descripción : <Clave de condición de variante>Estado : Liberado (predeterminado)El Formato sección:Tipo de datos : Formato carácterCtd.caract. : <26>Distingue entre mayúsculas y minúsculas : <seleccionado>El Valoración sección:Seleccione el Valores múltiples botón de selección.Anule la selección de Restringible casilla de selección. |  |  |
| 9 | Introducir datos adicionales | El Dat.adic. , efectúe las siguientes entradas:El Referencia a campo de tabla sección:Nombre de tabla : SDCOMNombre de campo : VKONDEl Comportamiento para valoración sección:No listo para la entrada : <no seleccionado> |  |  |
| 10 | Grabar la característica | Seleccionar Grabar . |  |  |

### Crear clase

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso del proceso se crea una clase con la categoría de clase 300.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar clases (CL02) . | Se abre la aplicación. | Pantalla común para el modo de creación, modificación y visualización. |
| 3 | Introducir nombre de clase | Realice las siguientes entradas y seleccione Crear :Clase : <CATEGORÍA>Categoría de clase : 300 | El Crear clase se visualiza. | El valor en el Inicio de validez El campo se rellena automáticamente.Si la clase <CATEGORY> ya existe, cree la clase <CATEGORÍA>_Vnn, donde nn es el número actual. |
| 4 | Introducir datos básicos | El Datos básicos , efectúe las siguientes entradas:En la Datos básicos sección:Descripción : <Potencia Categoría de herramientas>Estado : Liberado (por defecto)En la Misma clasificación sección:Seleccione el No verificar radio botón (predeterminado). |  | Si utiliza la misma clasificación, puede seleccionar la forma de verificación (advertencia mensaje, error, ninguno). |
| 5 | Introducir caract. | El Caract. , efectúe las siguientes entradas:Caract. : <CATEGORÍA>Caract. : <CATEGORÍA_VARCOND> |  |  |
| 6 | Grabar la clase | Seleccionar Grabar . | Se crea la clase. |  |

### Crear perfil de configuración

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso del proceso se crea un perfil de configuración.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Entorno de modelado VC (PMEVC) . | Se abre la aplicación. |  |
| 3 | Introducir datos de modelo de configuración | En la pantalla inicial, efectúe las siguientes entradas y seleccione Introducir modelo :Material : <CBPTS001>Categoría de clase : 300 (por defecto) | Aparece la pantalla de configuración. |  |
| 4 | Crear perfil de configuración | En la Objeto sección, haga clic con el botón derecho <CBPTS001> y seleccione Crear Perfil de configuración .En la Crear perfil de configuración , realice la siguiente entrada:Perfil de configuración : <CBPT_CP_V01>Seleccionar Continuar . | El Perfil de configuración se muestra en el panel de la derecha y el Datos básicos Se ha seleccionado la pestaña. |  |
| 5 | Grabar el perfil de configuración | Seleccionar Grabar . | Se crea el perfil de configuración. |  |

### Crear maestro de materiales - Clasificación

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso del proceso se crea una vista de clasificación para el maestro de materiales.

Requisito previo

Debe completar los pasos de la sección anterior, [Crear maestro de materiales configurable - Datos básicos](#unique_11) [página ] 7, antes de continuar con esto sección. Inicie el procedimiento después de haber grabado las entradas de Datos básicos, como se describe en el procedimiento anterior.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <CBPTS001>Ramo : MNota Si el campo de entrada Ramo está oculto, no se requiere ninguna entrada. Cuando el ramo no está ofrecido para la entrada, el campo se rellena dentro de la oscuridad.Tipo de material : KMAT – Materiales configurables | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Clasificación y seleccionar Continuar . | El Categoría de clase (1) se visualiza. |  |
| 5 | Introducir categoría de clase | En la Nivel de restricciones , realice las siguientes entradas y seleccione Continuar :Descripción de categoría de clase : VariantesTipo : 300 | El Clasificación se visualiza. |  |
| 6 | Introducir datos de clasificación | El Clasificación en la pantalla, debajo de la Asignaciones introduzca los siguientes datos en el Clase y seleccione Grabar :<CATEGORÍA>En el Valores para la clase CATEGORY - Objeto <CBPTS001> introduzca los siguientes datos en la pestaña Valor y seleccione Grabar :<ESTÁNDAR><HIGH_END> | Se han guardado los datos. |  |

### Crear determinación de precios de variante

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

La condición de variante se asigna a un valor de característica.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Entorno de modelado VC (PMEVC) . | Se abre la aplicación. |  |
| 3 | Introducir datos de modelo de configuración | En la pantalla inicial, efectúe las siguientes entradas y seleccione Introducir actualización de modelo :Material : <CBPTS001>Categoría de clase : 300 (por defecto) | Aparece la pantalla de configuración. |  |
| 4 | Crear determinación de precios de variante | En la Objeto sección, haga doble clic en <CBPTS001> y seleccione la Variante Determinación de precios en el panel de la derecha.Seleccionar Modif. y realice las siguientes entradas:Característica : <CATEGORÍA>Valor caract. : <HIGH_END>Cond.var. : <HIGH_END> |  |  |
| 5 | Guardar la configuración | Seleccionar Grabar . | Se crea la determinación de precios de variante. |  |

### Crear datos maestros de producto - Datos de ventas/Datos de impuestos sobre ventas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso del proceso se crea la vista de datos de ventas para el maestro de materiales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos básicos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <CBPTS001>Ramo : MNota Si el campo de entrada Ramo está oculto, no se obligatorio. Cuando el ramo no se ofrece para la entrada, el campo se rellena en la oscuridad.Tipo de material : KMAT - Materiales configurables | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) pantalla, seleccione Ventas: Datos org.ventas 1 , Ventas: Org.ventas Datos 2 , y Ventas: Datos generales/de centro y, a continuación, seleccione Continuar . | El Niveles de organización se visualiza. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización sección, hacer lo siguiente entradas y seleccione Continuar :Centro : Por ejemplo, <1010> .Org.ventas : Por ejemplo, <1010 para el centro 1010> .Canal distrib. : Por ejemplo, <10> . | El Crear material (materiales configurables) se visualiza.Obtendrá el siguiente mensaje del sistema en la parte inferior de la pantalla: El material ya existe y se ampliará . |  |
| 6 | Introducir datos de ventas | El Crear material CBPTS001 (materiales configurables) en la pantalla, debajo de la Ventas: Org.ventas 1 introduzca un valor adecuado para Clasificación fiscal .Normalmente, se trata de un valor 1 para imponible en su totalidad.Pulsar Intro . | El Ventas: org.ventas 2 se visualiza.El valor introducido indica que el material está (normalmente) completo imponible. |  |
| 7 | Introducir datos de ventas | El Ventas: org.ventas 2 en la pestaña Conceptos de agrupación , realice la siguiente entrada y pulse Intro :Grupo de tipos de posición : <0003> | El Ventas: General/Centro se visualiza. |  |
| 8 | Introducir datos de ventas | El Ventas: General/Centro en la pestaña Datos generales , realice la siguiente entrada y pulse Intro :Verificación de disponibilidad : Por ejemplo, <NC> . | El Última vista de datos alcanzada con el mensaje: Está a punto de salir. ¿Desea grabar su datos primero para este material? . |  |
| 9 | Guardar los datos | Seleccionar Sí en la Última vista de datos alcanzada pantalla. | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 28,157 chars in the whole document
