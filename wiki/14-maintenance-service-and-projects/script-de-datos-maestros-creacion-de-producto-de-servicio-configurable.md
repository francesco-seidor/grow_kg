---
id: 14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable
title: Script de datos maestros - Creación de producto de servicio configurable - MDS (5BE) (5BE_S4CLD2608_Master_Data_ES_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (5BE, Spanish, machine-translated): create configurable service products, classes, configuration profiles, prices and variants."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [5BE_S4CLD2608_Master_Data_ES_XX]
keywords: [Configurable Service Products and Advanced Variant…, configurable service product, service contracts, service orders, characteristics and classes, configuration profile, variant pricing, material variant, master data scripts, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-432
topic: 14-maintenance-service-and-projects/configurable-service-products
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de producto de servicio configurable - MDS (5BE) (5BE_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de producto de servicio configurable - MDS (5BE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233894719)

[2 Requisitos previos 4](#_Toc233894720)

[2.1 Acceso al sistema 4](#_Toc233894721)

[2.2 Roles 4](#_Toc233894722)

[2.3 Unidades organizativas necesarias 4](#_Toc233894723)

[2.4 Datos maestros obligatorios y operativos 5](#_Toc233894724)

[2.5 Pasos preliminares (obligatorios) 5](#_Toc233894725)

[3 Tabla de resumen 7](#_Toc233894726)

[4 Procedimientos 8](#_Toc233894727)

[4.1 Crear producto de servicio configurable para contratos de servicio 8](#_Toc233894728)

[4.1.1 Crear características 8](#_Toc233894729)

[4.1.2 Crear clase 10](#_Toc233894730)

[4.1.3 Crear producto de servicio configurable para contratos 11](#_Toc233894731)

[4.1.4 Crear perfil de configuración 14](#_Toc233894732)

[4.1.5 Fijar precios 15](#_Toc233894733)

[4.2 Crear producto de servicio configurable para órdenes de servicio 17](#_Toc233894734)

[4.2.1 Crear características 17](#_Toc233894735)

[4.2.2 Crear clase 21](#_Toc233894736)

[4.2.3 Crear producto de servicio configurable para orden de servicio 22](#_Toc233894737)

[4.2.4 Crear perfil de configuración 24](#_Toc233894738)

[4.2.5 Fijar precios 26](#_Toc233894739)

[4.3 Crear variante de material para un producto de servicio 28](#_Toc233894740)

[4.3.1 Fijar precios para variante de material 31](#_Toc233894741)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear productos de servicio configurables para contratos de servicio y órdenes de servicio, así como los precios relacionados. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance de la entrega de contenido de S/4 HANA por parte de SAP Best Practices no se describen en este documento, aunque pueden aparecer en la IU.

Los productos de servicio configurables que se crean como se describe aquí se pueden utilizar para el servicio procesamiento de contratos y procesamiento de órdenes de servicio. Para hacer uso de la configuración producto de servicio, consulte la Gestión de servicios con configuración de variantes avanzada (6GS) posición de alcance o el Gestión de contratos de servicio con configuración de variantes avanzada (6GU).

La funcionalidad de la configuración del producto que se puede utilizar en los contratos de servicio y las órdenes de servicio es la misma que se describe en el elemento de alcance 22T - Configurar modelo configurable mediante la configuración de variantes.

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Crear roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asignar a sus usuarios de prueba individuales.

| Nombre | ID |
| --- | --- |
| Modelador de configuración de producto | SAP_BR_PRODUCT_CONFIG_MODELER |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST |
| Especialista en determinación de precios | SAP_BR_PRICING_SPECIALIST |

Además, el siguiente rol es relevante para el usuario de configuración que se encarga de la obligatorio Pasos preliminares descrito a continuación:

| Nombre | ID |
| --- | --- |
| Experto en configuración - Configuración del proceso empresarial | SAP_BR_BPC_EXPERT |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa, General Los datos (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Unidad organizativa a utilizar | Comentarios |
| --- | --- | --- | --- |
| Crear material | Centro | 1710 (Centro 1 US) | Para Alemania, utilice 1010 (centro 1 DE) |
| Crear material | Organización de ventas | 1710 (Org.ventas nac.US) | Para Alemania, utilice 1010 (Org. Org.ventas DE) |
| Crear material | Canal de distribución | 10 (Ventas directas) | Para Alemania, utilice 10 (Ventas directas) |

### Datos maestros obligatorios y operativos

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de material.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

### Pasos preliminares (obligatorios)

Uso

Antes de crear el producto de servicio configurable como se describe en el siguiente procedimiento, primero debe habilitar el tipo de material existente SERV (servicios) para utilizar datos de clasificación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abra la Gestionar su solución aplicación. | El Gestionar su solución se visualiza la aplicación. |  |
| 3 | Configurar su solución | El Gestionar su solución , seleccione Configurar Su solución . | El Configurar su solución: fase Realizar la pantalla es visualizado. |  |
| 4 | Abrir la posición de producto para la configuración | En los filtros de búsqueda, realice las siguientes entradas:Área de aplicación : <Base de datos y datos GestiónÁrea de subaplicación : ProductoSeleccione el Producto registro en la búsqueda resultados. | El Configurar su solución: Producto la pantalla es visualizado. |  |
| 5 | Configure su solución: Producto | En la Pasos de configuración sección, para Definir Atributos de tipos de material , seleccione Configurar . | El Definir atributos de tipos de material: Modificar la pantalla es visualizado. |  |
| 6 | Abrir atributos del tipo de material SERV | Haga doble clic en SERV – Producto de servicio entrada. | El Definir atributos de tipos de material: Modificar: Detalles pantalla se visualiza. |  |
| 7 | Activar clasificación | En la Departamentos de usuario seleccione Clasificación .Atención Antes de guardar las modificaciones en la configuración, asegúrese de que las selecciones preexistentes en el Usuario/a Departamentos lista también están seleccionado. |  |  |
| 8 | Guardar los datos | Seleccionar Grabar . |  |  |

Resultado

Al crear productos del tipo SERV – Producto de servicio, el Clasificación está activada.

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear características](#unique_8) [página ] 8 | SAP_BR_PRODUCT_CONFIG_MODELER | Gestionar características | Se crean características para la clase de contrato de servicio. |
| [Crear clase](#unique_9) [página ] 10 | SAP_BR_PRODUCT_CONFIG_MODELER | Gestionar clases | Se crea una clase. |
| [Crear producto de servicio configurable para contratos](#unique_10) [página ] 11 | SAP_BR_PRODMASTER_SPECIALIST | Crear material | Se crea el producto de servicio para contratos de servicio. |
| [Crear perfil de configuración](#unique_11) [página ] 14 | SAP_BR_PRODUCT_CONFIG_MODELER | Entorno de modelado VC | Se ha creado el perfil de configuración. |
| [Fijar precios](#unique_12) [página ] 15 | SAP_BR_PRICING_SPECIALIST | Fijar precios de material | Se definen los precios. |
| [Crear características](#unique_13) [página ] 17 | SAP_BR_PRODUCT_CONFIG_MODELER | Gestionar características | Se crean características para la clase de contrato de servicio. |
| [Crear clase](#unique_14) [página ] 21 | SAP_BR_PRODUCT_CONFIG_MODELER | Gestionar clases | Se crea una clase. |
| [Crear producto de servicio configurable para orden de servicio](#unique_15) [página ] 22 | SAP_BR_PRODMASTER_SPECIALIST | Crear material | Se ha creado el producto de servicio para la orden de servicio. |
| [Crear perfil de configuración](#unique_16) [página ] 24 | SAP_BR_PRODUCT_CONFIG_MODELER | Entorno de modelado VC | Se ha creado el perfil de configuración. |
| [Fijar precios](#unique_17) [página ] 26 | SAP_BR_PRICING_SPECIALIST | Fijar precios de material | Se definen los precios de los productos de servicio. |
| [Crear variante de material para un producto de servicio](#unique_18) [página ] 28 | SAP_BR_PRODMASTER_SPECIALIST | Crear material | Se crea una variante de material para un producto de servicio configurable. |
| [Fijar precios para variante de material](#unique_19) [página ] 31 | SAP_BR_PRICING_SPECIALIST | Fijar precios de material | Se ha definido el precio para una variante de material. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear producto de servicio configurable para contratos de servicio

#### Crear características

Objetivo

En esta actividad se crean características que deben estar disponibles para la selección en el producto de servicio configurable y para las que puede actualizar precios de variante individuales.

Procedimiento

Característica VARKOND (clave de condición de variante)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, actualizar Característica : VARKONDA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos actualice los siguientes datos:Descripción : Clave de condición de varianteEstado : LiberadoTipo de datos : Formato carácterCtd.caract. : 26Distingue entre mayúsculas y minúsculas : SeleccionadoValores múltiples : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, actualice idiomas adicionales en Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir datos adicionales | Navegue a la Dat.adic. y actualice los siguientes datos:Nombre de tabla : SDCOMNombre de campo : VKONDNo listo para la entrada : SeleccionadoSin visualización : Seleccionado |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

Característica SERVICE_CHANNEL (canal de servicio)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, actualizar Característica : CANAL DE SERVICIOA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos actualice los siguientes datos:Descripción : Canal de servicioEstado : LiberadoTipo de datos : Formato carácterCtd.caract. : 20Valores múltiples : SeleccionadoEntrada obligatoria : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, actualice idiomas adicionales en Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir valores | Navegue a la Valores y actualice los siguientes datos:Valor caract./Descripción : CORREO ELECTRÓNICO / Soporte por correo electrónicoValor caract./Descripción : TELÉFONO / Soporte telefónico |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

Característica PREVENTIVE_MAINTENANCE (Mantenimiento preventivo)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, actualizar Característica : PREVENTIVE_MAINTENANCEA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos actualice los siguientes datos:Descripción : Mantenimiento preventivoEstado : LiberadoTipo de datos : Formato carácterCtd.caract. : 20Valores múltiples : SeleccionadoEntrada obligatoria : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, actualice idiomas adicionales en Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir valores | Navegue a la Valores y actualice los siguientes datos:Valor caract./Descripción : AÑO / AnualValor caract./Descripción : HALFYEARLY / SemestralValor caract./Descripción : TRIMESTRAL / Trimestral |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

#### Crear clase

Objetivo

En esta actividad se crea una clase a la que se asignan las características del capítulo anterior.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar clases .El Clase actualice los siguientes datos:Clase : SERVICE_CONTRACT_CCategoría de clase : 300 (Variantes)A continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos actualice los siguientes datos:Descripción : Clase de contrato de servicioEstado : LiberadoNo verificar : Seleccionado |  |  |
| 4 | Introducir características | Navegue a la Caract. y actualice los siguientes datos:VARKONDCANAL DE SERVICIOPREVENTIVE_MAINTENANCE | Las características relevantes se asignan a la clase. |  |
| 5 | Grabar clase | Seleccionar Grabar . | Se crea la nueva clase. |  |

#### Crear producto de servicio configurable para contratos

Objetivo

En esta actividad se actualiza un producto de servicio configurable que se puede utilizar en contratos de servicio.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado. Verificar creación Datos maestros para Brasil (JD0_BR) en el capítulo Definir campos específicos de BR para datos maestros para datos maestros de material. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Seleccionar Crear material enlace debajo de la Gestionar datos maestros de producto mosaico. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Introducir ID y tipo de material | El Crear material (pantalla inicial) actualizar las siguientes entradas:Material : SRV_CONTR_CONFIGRamo : MSi el Ramo el campo de entrada está oculto, no se requiere ninguna entrada.Tipo de material : Producto de servicioA continuación, seleccione Continuar (Intro) . |  |  |
| 4 | Seleccionar vista de datos básicos | El Seleccionar vista(s) ventana de diálogo, seleccione el Datos básicos 1 y, a continuación, seleccione Continuar (Intro) .El Niveles de organización introduzca la ventana de diálogo siguiente:Planta: 1710Organización de ventas: 1710Canal de distribución: 10Nota Para DE, introduzca Centro/Organización de ventas/ Canal de distribución como 1010/1010/10 | El Crear material SRV_CONTR _CONFIG la vista es visualizados. |  |
| 5 | Introducir datos básicos | El Datos básicos 1 , actualice los siguientes valores:Descr. : Servicio configurable ContratoUnidad de medida base : AU (unidad de actividad)Grupo de materiales : P001 (Servicios)Gr.pos.gen. : SCNP (Prod.contrato serv.)El material es configurable: SeleccionadoNavegar a Datos adicionales y actualice los siguientes datos:Idioma : DEDescripción de material : Konfigurierbarer ServicevertragA continuación, seleccione Grabar . | Se crea el producto y se Crear material (pantalla inicial) Se muestra la vista. |  |
| 6 | Seleccionar vistas de ventas | El Crear material (pantalla inicial) vista, actualizar material SRV_CONTR_CONFIG , luego seleccione Continuar (Intro) .El Seleccionar vista(s) ventana de diálogo, seleccione la siguiente vista:Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza la ventana de diálogo. |  |
| 7 | Seleccionar niveles de organización | El Niveles de organización ventana de diálogo, actualice los siguientes valores:Centro : 1710 (Centro 1 US)Org.ventas .: 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Nota Nota: Para DE, actualice 1010/1010/10 respectivamente.A continuación, seleccione Continuar (Intro) . | El Ventas: org.ventas 1 Se muestra la vista. |  |
| 8 | Introducir datos de organización de ventas (1) | El Ventas: org.ventas 1 , actualice los siguientes valores:Datos generales• Descuento por pronto pago : X <seleccionado>Datos fiscales• Clasificación fiscal : 1 (impuesto completo)A continuación, seleccione Intro . | El Ventas: org.ventas 2 Se muestra la vista. |  |
| 9 | Introducir datos de organización de ventas (2) | El Ventas: org.ventas 2 , actualice la siguiente entrada:Grupo de tipos de posición : SCNP (Prod.contrato serv.)A continuación, seleccione Intro . | El Ventas: General/Centro Se muestra la vista. |  |
| 10 | Introducir datos generales de ventas | El Ventas: General/Centro , actualice los siguientes valores:Unidad de medida base : AU (unidad de actividad)Duración del trabajo : 1 RR. HH.A continuación, seleccione Grabar .Solo para Polonia: seleccione Intro en lugar de Grabar . | El Crear material (pantalla inicial) Se muestra la vista. |  |
| Solo para Polonia | Introducir datos de ventas | En la Comercio internacional: Exportación introduzca los siguientes datos:Código de control. : por ejemplo, 41.00.30.0A continuación, seleccione Grabar . | El Crear material (pantalla inicial) Se muestra la vista. |  |
| 11 | Seleccionar vista de clasificación | El Crear material (pantalla inicial) vista, actualizar material SRV_CONTR_CONFIG , luego seleccione Continuar (Intro) .El Seleccionar vista(s) ventana de diálogo, seleccione la siguiente vista:ClasificaciónA continuación, seleccione Continúe (Intro). | El Clasificación Se muestra la vista. |  |
| 12 | Introducir clasificación | El Categoría de clase ventana de diálogo, seleccione el Variantes (300) entrada y, a continuación, seleccione Copiar .El Clasificación , actualice los siguientes datos:Clase : SERVICE_CONTRACT_CSeleccionar Intro para visualizar las características asignado a la clase.En la Valores para la clase SERVICE_CONTRACT_C , para cada característica, abra la ayuda para entradas y seleccione todos los valores disponibles.A continuación, seleccione Grabar . | El Crear material (pantalla inicial) Se muestra la vista. |  |

#### Crear perfil de configuración

Objetivo

En esta actividad se crea un perfil de configuración en el modelador de la configuración de variantes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Entorno de modelado VC .El Pantalla inicial de entorno de modelado de configuración de variantes actualice los siguientes datos:Material : SRV_CONTR_CONFIGCategoría de clase : 300 (variantes)A continuación, seleccione Introducir modelo . | El Configuración para SRV_CONTR_CONFIG se visualiza. |  |
| 3 | Crear perfil de configuración | En la Objeto columna, haga clic con el botón derecho en el SRV_CONTR_CONFIG y seleccione Crear perfil de configuración .El Crear perfil de configuración ventana de diálogo, actualice los siguientes datos:Perfil de configuración : SRV_CONTR_CONFSin número de modificación .: SeleccionadoA continuación, seleccione Continúe (Intro).En la Objeto , haga doble clic en el SRV_CONTR_CONFIG material.Abra la Determinación de precios de variante etiqueta, seleccione Modif. y, a continuación, seleccione Desplegar lista .Actualice todas las características asignadas a su configuración producto excepto la característica VARKOND. Además, asegúrese de actualizar una condición de variante y una descripción para todas ellas. El La condición de variante se utiliza en la condición de precio actualización.Por ejemplo, para Característica / Caract. Valor / Cond.variantes / Cond.variantes Descripción , actualizar:SERVICE_CHANNEL / EMAIL / EMAIL /E-mail SoporteSERVICE_CHANNEL / TELETELÉFONO / TELÉFONO / Teléfono SoportePREVENTIVE_MAINTENANCE / YEARLY / YEARLY / AnualPREVENTIVE_MAINTENANCE / HALFYEARLY / HALFYEARLY / SemestralPREVENTIVE_MAINTENANCE / QUARTERLY / QUARTERLY / TrimestralA continuación, seleccione Grabar . | El Configuración para SRV_CONTR_CONFIG se visualiza. |  |

#### Fijar precios

Objetivo

En esta actividad se actualiza un registro de condición de precio estándar para el producto de servicio configurable, así como registros de precio de variante para las variantes configurables.

Procedimiento

Clase de condición: PSI1 (precio para posición de contrato de servicio)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición ver, actualizar Clase de condición : PSI1 (Precio p.cont.serv.), y, a continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Seleccionar combinación de claves | En la Combinación de claves , seleccione MaterialA continuación, seleccione Intro . | El Modificar precio (PSI1): Selección Se muestra la vista. |  |
| 5 | Selección | El Modificar precio (PSI1): Selección , actualice la siguiente información:Org.ventas : 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Material :SRV_CONTRACT (producto de contrato de servicio)Válido el : <Fecha> , por ejemplo, Fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPSI): Resumen Se muestra la vista. |  |
| 6 | Introducir condición de precio | El Modificar condición de precio (PSI1): Resumen , actualice los siguientes datos:Material : SRV_CONTR_CONFIG (Contrato de servicio configurable)Cantidad : por ejemplo, 200,00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, la fecha de hoySeleccionar Intro .A continuación, seleccione Grabar . | Se ha fijado un precio estándar para el producto de servicio SRV_CONTR_CONFIG actualizado. |  |

Clase de condición: VASE (precio de variante)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición ver, actualizar Clase de condición : VASE Precio de variante), y, a continuación, seleccione Intro . | El Modificar precio de variante Se muestra la vista. |  |
| 4 | Introducir datos de ventas | El Modificar precio de variante (VASE): Selección , actualice la siguiente información:Org.ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 (Ventas directas)Material : SRV_CONTR_CONFIG (Contrato de servicio configurable)Válido el : <Fecha> por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio de variante (VASE): Resumen Se muestra la vista. |  |
| 5 | Introducir condiciones de variante | El Modificar condición de precio de variante (VASE): Resumen vista, actualice los precios para todas las condiciones de variante que ha actualizado en el capítulo anterior, por ejemplo:Variante / Importe / Unidad :CORREO ELECTRÓNICO / 30 USDTELÉFONO / 50 USDAÑO / 250 USDHALFYEARLY / 135 USDTRIMESTRAL / 90 USDSeleccionar Intro y verifique sus entradas.A continuación, seleccione Grabar . | Se han actualizado las condiciones de precio de variante. |  |

### Crear producto de servicio configurable para órdenes de servicio

#### Crear características

Objetivo

En esta actividad se crean características que deben estar disponibles para la selección en el producto de servicio configurable y para las que puede actualizar precios de variante individuales.

Procedimiento

Característica VARKOND (clave de condición de variante)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, en el campo Característica : introduzca VARKONDA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos introduzca los siguientes datos:Descripción : Clave de condición de varianteEstado : LiberadoTipo de fecha : Formato carácterCtd.caract. : 26Distingue entre mayúsculas y minúsculas : SeleccionadoValores múltiples : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, puede introducir idiomas adicionales en el Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir datos adicionales | Navegue a la Dat.adic. e introduzca los siguientes datos:Nombre de tabla : SDCOMNombre de campo : VKONDNo listo para la entrada : SeleccionadoSin visualización : Seleccionado |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva clave de condición de variante. |  |

Característica CAR_WASH_TYPE (tipo de lavado de coche)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, en el campo Característica: introduzco CAR_WASH_TYPEA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos introduzca los siguientes datos:Descripción : Tipo de lavado de automóvilEstado : LiberadoTipo de fecha : Formato carácterCtd.caract. : 20Valores individuales : SeleccionadoEntrada obligatoria : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, puede introducir idiomas adicionales en el Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir valores | Navegue a la Valores e introduzca los siguientes datos:Valor caract./Descripción : BÁSICO / Lavado básicoValor caract./Descripción : ESTÁNDAR / Lavado estándarValor caract./Descripción : PREMIUM / Lavado premium |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

Característica CAR_SIZE (tamaño del coche)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, en el campo Característica: introduzco CAR_SIZEA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos introduzca los siguientes datos:Descripción : Tamaño del automóvilEstado : LiberadoTipo de fecha : Formato carácterCtd.caract. : 20Valores individuales : SeleccionadoEntrada obligatoria : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, puede introducir idiomas adicionales en el Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir valores | Navegue a la Valores e introduzca los siguientes datos:Valor caract./Descripción : S / PequeñoValor caract./Descripción : M / MedioValor caract./Descripción : L / Grande |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

Característica EXTRA_POLISH (polaco extra)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar características .El Características pantalla, en el campo Característica: introduzco EXTRA_POLISHA continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introducir datos básicos | En la Datos básicos introduzca los siguientes datos:Descripción : Polaco extraEstado : LiberadoTipo de fecha : Formato carácterCtd.caract. : 10Valor individual : SeleccionadoEntrada obligatoria : Seleccionado |  |  |
| 4 | Introducir descripciones | Opcionalmente, puede introducir idiomas adicionales en el Actualizar descripciones etiqueta. |  |  |
| 5 | Introducir valores | Navegue a la Valores e introduzca los siguientes datos:Valor caract./Descripción : SÍ / SíValor caract./Descripción : NO / No |  |  |
| 6 | Grabar característica | Seleccionar Grabar . | Se crea la nueva característica. |  |

#### Crear clase

Objetivo

En esta actividad se crea una clase a la que se asignan las características del capítulo anterior.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar clases .El Clase introduzca los siguientes datos:Clase : CAR_WASHCategoría de clase : 300 (variantes)A continuación, seleccione Crear . | Aparecen ámbitos de imagen adicionales. |  |
| 3 | Introduzca el nombre de clase | El Pantalla de clases , introduzca los siguientes datos:Clase : CAR_WASHCategoría de clase : 300 (variantes)A continuación, seleccione Crear |  |  |
| 4 | Introducir datos básicos | En la Datos básicos introduzca los siguientes datos:Descripción : Coche LavadoEstado : LiberadoNo verificar : Seleccionado |  |  |
| 5 | Introducir características | Navegue a la Caract. y actualice los siguientes datos:VARKONDCAR_WASH_TYPECAR_SIZEEXTRA_POLISH | Las características relevantes se asignan a la clase. |  |
| 6 | Grabar clase | Seleccionar Grabar . | Se crea la nueva clase. |  |

#### Crear producto de servicio configurable para orden de servicio

Objetivo

En esta actividad se actualiza un producto de servicio configurable que se puede utilizar en el servicio pedidos.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Introducir ID y tipo de material | El Crear material (pantalla inicial) , introduzca el Datos siguientes:Material : CAR-WASH_CONFSi el Ramo el campo de entrada está oculto, no se requiere ninguna entrada.Tipo de material : SERV Producto de servicioA continuación, seleccione Continuar (Intro) . |  |  |
| 4 | Seleccionar vista de datos básicos | El Niveles de organización indique los siguientes datos:Centro : 1710 (Centro 1 US)Org.ventas .: 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Nota: Para DE, introduzca 1010/1010/10 respectivamente.A continuación, seleccione Continuar (Intro) . | El Crear material CAR-WASH _CONF la vista es visualizados. |  |
| 5 | Introducir datos básicos | El Datos básicos 1 introduzca los siguientes datos:Descr. .: Lavado de coche configurableUnidad de medida base : AU (unidad de actividad)Grupo de materiales : P001 (Servicios)Gr.tp.pos.gen. : SRVP (servicio) Producto)El material es configurable: SeleccionadoNavegar a Datos adicionales y actualice los siguientes datos:Idioma : DEDescripción de material : Konfigurierbare AutowäscheA continuación, seleccione Grabar . | Se crea el producto y se Crear material (pantalla inicial) Se muestra la vista. |  |
| 6 | Seleccionar vistas de ventas | El Crear material (pantalla inicial) ver, en el campo Material, introduzco CAR-WASH_CONF , luego seleccione Continuar (Intro) .El Seleccionar vista(s) seleccione las siguientes vistas:Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza la ventana de diálogo. |  |
| 7 | Seleccionar niveles de organización | El Niveles de organización indique los siguientes datos:Centro : 1710 (Centro 1 US)Org.ventas .: 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Nota: Para DE, introduzca 1010/1010/10 respectivamente.A continuación, seleccione Continuar (Intro) . | El Ventas: org.ventas 1 Se muestra la vista. |  |
| 8 | Introducir datos de organización de ventas (1) | El Ventas: org.ventas 1 introduzca los siguientes datos:Datos generales• Descuento por pronto pago : X <seleccionado>Datos fiscales• Clasificación fiscal : 1 (impuesto completo)A continuación, seleccione Intro . | El Ventas: org.ventas 2 Se muestra la vista. |  |
| 9 | Introducir datos de organización de ventas (2) | El Ventas: org.ventas 2 introduzca los siguientes datos:Grupo de tipos de posición : SRVP (producto de servicio)A continuación, seleccione Intro . | El Ventas: General/Centro Se muestra la vista. |  |
| 10 | Introducir datos generales de ventas | El Ventas: General/Centro introduzca los siguientes datos:Unidad de medida base : AU (unidad de actividad)Duración del trabajo : 1 RR. HH.A continuación, seleccione Grabar .Solo para Polonia: seleccione Intro en lugar de Grabar . | El Crear material (pantalla inicial) Se muestra la vista. |  |
| Solo para Polonia | Introducir datos de ventas | El Comercio internacional: Exportación en el área Fecha de comercio exterior , introduzca los siguientes datos:Código de control. : por ejemplo, 41.00.30.0A continuación, seleccione Grabar . |  |  |
| 11 | Seleccionar vista de clasificación | El Crear material (pantalla inicial) ver, en el campo Material introduzco CAR-WASH_CONF , luego seleccione Continuar (Intro) .El Seleccionar vista(s) seleccione la siguiente vista:ClasificaciónA continuación, seleccione Continúe (Intro). | El Clasificación Se muestra la vista. |  |
| 12 | Introducir clasificación | El Categoría de clase seleccione la ventana de diálogo Variantes (300) entrada y, a continuación, seleccione Copiar .El Clasificación introduzca los siguientes datos:Clase : CAR_WASHSeleccionar Intro para visualizar las características asignadas a la clase.En la Valores para la clase CAR_WASH , para cada característica, abra la ayuda para entradas y seleccione todos los valores disponibles.A continuación, seleccione Grabar . | Las características se asignan al material. |  |

#### Crear perfil de configuración

Objetivo

En esta actividad se crea un perfil de configuración en el modelador de la configuración de variantes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Entorno de modelado VC .El Pantalla inicial de entorno de modelado de configuración de variantes introduzca los siguientes datos:Material : CAR-WASH_CONFCategoría de clase : 300 (variantes)A continuación, seleccione Introducir modelo . | El Configuración para CAR_WASH_CONF se visualiza. |  |
| 3 | Crear perfil de configuración | En la Objeto columna, haga clic con el botón derecho en el CAR-WASH_CONF y seleccione Crear perfil de configuración .El Crear perfil de configuración indique los siguientes datos:Perfil de configuración : CAR-WASH_CONFSin número de modificación .: SeleccionadoA continuación, seleccione Continúe (Intro).En la Objeto columna, haga doble clic en el CAR-WASH_CONF entrada. Abra el Determinación de precios de variante y seleccione Modif. . A continuación, seleccione Desplegar Lista .Introduzca todas las características asignadas a su producto configurable excepto la característica VARKOND. Además, asegúrese de introducir un Cond.variantes y Descripción a todos ellos. La condición de variante se utiliza en la actualización de condiciones de precio.Por ejemplo, para Característica / Caract. Valor / Condición de variante / Condición de variante Descripción , introduzca:CAR_WASH_TYPE / BASIC / C_W_T_B / BásicoCAR_WASH_TYPE / STANDARD / C_W_T_S / EstándarCAR_WASH_TYPE / PREMIUM / C_W_T_P / PrimaCAR_SIZE / S / C_S_S / PequeñoCAR_SIZE / M / C_S_M / MedioCAR_SIZE / L / C_S_L / GrandeEXTRA_POLISH / YES / E_P_Y / SíEXTRA_POLISH / NO / E_P_N / NoA continuación, seleccione Grabar . | Las condiciones de variante se crean para todas las características. |  |

#### Fijar precios

Objetivo

En esta actividad se actualiza un registro de condición de precio estándar para el producto de servicio configurable, así como registros de precio de variante para las variantes configurables.

Procedimiento

Clase de condición: PPR0 (precio)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición vista, en el campo Clase de condición : introduzca PPR0 (precio), a continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Seleccionar combinación de claves | En la Combinación de claves , seleccione MaterialA continuación, seleccione Intro . | El Modificar precio (PPR0): Selección Se muestra la vista. |  |
| 5 | Selección | El Modificar precio (PPR0): Selección introduzca los siguientes datos:Org.ventas : 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Material : CAR-WASH_CONF (lavado de vehículos) Configurable)Válido el : <Fecha> , por ejemplo, Fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen Se muestra la vista. |  |
| 6 | Introducir condición de precio | El Modificar condición de precio (PPR0): Resumen introduzca los siguientes datos:Material : CAR-WASH_CONF (lavado de vehículos) Configurable)Cantidad : por ejemplo, 10,00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, la fecha de hoySeleccionar Intro .A continuación, seleccione Grabar . | Se crea un precio estándar para el producto de servicio. |  |

Clase de condición: PVA0 (precio de variante)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición vista, actualizar Clase de condición : PVA0 (precio de variante), a continuación, seleccione Intro . | El Modificar precio de variante Se muestra la vista. |  |
| 4 | Introducir datos de ventas | El Modificar precio de variante (PVA0): Selección , actualice la siguiente información:Org.ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 (Ventas directas)Material : CAR-WASH_CONF (Contrato de servicio configurable)Válido el : <Fecha> por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio de variante ( PVA0 ): Resumen Se muestra la vista. |  |
| 5 | Introducir condiciones de variante | El Crear condición de precio de variante ( PVA0): Resumen , introduzca precios para todas las condiciones de variante que ha creado en el capítulo anterior, por ejemplo:Variante / Importe / Unidad :C_W_T_B / 5 USDC_W_T_S / 8 USDC_W_T_P / 12 USDC_S_S / 2 USDC_S_M / 4 USDC_S_L / 10 USDSeleccionar Intro y verifique sus entradas.A continuación, seleccione Grabar . | Se han creado condiciones de precio de variante. |  |

PVA1 (% de precio de variante)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición vista, en el campo Clase de condición : introduzca PVA1 Precio de variante (%), a continuación, seleccione Intro . | El Modificar precio de variante (% PVA1) Se muestra la vista. |  |
| 4 | Introducir datos de ventas | El Modificar precio de variante (% (PVA1): Selección introduzca los siguientes datos:Org.ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 (Ventas directas)Material : CAR-WASH_CONFVálido el : <Fecha> por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio de variante (%) (PVA1) : Resumen Se muestra la vista. |  |
| 5 | Introducir condiciones de variante | El Crear condición de precio de variante (%) (PVA1): Resumen introduzca registros de condición para todas las condiciones de variante relevantes, por ejemplo:Variante / Importe / Unidad :E_P_Y / 20%E_P_N / -10%Seleccionar Intro y verifique sus entradas.A continuación, seleccione Grabar . | Se han creado condiciones de precio de variante. |  |

### Crear variante de material para un producto de servicio

Objetivo

En esta actividad se crea una variante de material con una configuración predefinida que puede utilizarse en una orden de servicio. El registro maestro de la variante está vinculado a un el producto utiliza sus características.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Seleccione el enlace Crear material debajo del Gestionar datos maestros de producto mosaico. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Introducir ID y tipo de material | El Crear material (pantalla inicial) introduzca el Datos siguientes:Material : CAR-WASH-VARRamo : Ingeniería mecánicaSi el Ramo el campo de entrada está oculto, no se requiere ninguna entrada.Tipo de material : SERV Producto de servicioA continuación, seleccione Continuar (Intro) .El Seleccionar vista(s) seleccione Datos básicos 1Seleccionar Niv.org. |  |  |
| 4 | Seleccionar niveles de organización | El Niveles de organización indique los siguientes datos:Centro : 1710 (Centro 1 US)Organización de ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Nota Para DE, introduzca 1010/1010/10 respectivamente.A continuación, seleccione Continuar (Intro) . | El Crear material CAR-WASH-VAR Se muestra la vista. |  |
| 5 | Introducir datos básicos | El Datos básicos 1 introduzca los siguientes datos:Descr. : Lavado de automóviles VarianteUnidad de medida base : AU (unidad de actividad)Grupo de materiales : P001 (Servicios)Gr.pos.gen. : SRVP (producto de servicio)El material es configurable: no seleccionadoCM válido para todos los centros: CAR-WASH_CONFSeleccionar Configurar varianteEn la vista Configuración de variantesSeleccione las siguientes características:Tamaño del automóvil: PequeñoPolaco extra: SíTipo de lavado de coche: Lavado estándarseleccionar HechoA continuación, seleccione Grabar . | Se crea el producto y se Crear material (pantalla inicial) Se muestra la vista. |  |
| 6 | Seleccionar vistas de ventas | El Crear material (pantalla inicial) vista, en el campo Material, introduzco CAR-WASH-VAR , luego seleccione Continuar (Intro) .El Seleccionar vista(s) seleccione las siguientes vistas:Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza la ventana de diálogo. |  |
| 7 | Seleccionar niveles de organización | El Niveles de organización indique los siguientes datos:Centro : 1710 (Centro 1 US)Org.ventas .: 1710 (Org.ventas nac.US)Canal distrib. : 10 Ventas directas)Nota Para DE, introduzca 1010/1010/10 respectivamente.A continuación, seleccione Continuar (Intro) . | El Ventas: org.ventas 1 Se muestra la vista. |  |
| 8 | Introducir datos de organización de ventas (1) | El Ventas: org.ventas 1 introduzca los siguientes datos:Datos generales• Descuento por pronto pago : X <seleccionado>• Datos fiscales• Clasificación fiscal : 1 (impuesto completo)A continuación, seleccione Intro . | El Ventas: org.ventas 2 Se muestra la vista. |  |
| 9 | Introducir datos de organización de ventas (2) | El Ventas: org.ventas 2 introduzca los siguientes datos:Grupo de tipos de posición : SRVP (producto de servicio)A continuación, seleccione Intro . | El Ventas: General/Centro Se muestra la vista. |  |
| 10 | Introducir datos generales de ventas | El Ventas: General/Centro introduzca los siguientes datos:Unidad de medida base : AU (unidad de actividad)Duración del trabajo : 1 RR. HH.A continuación, seleccione Grabar . | El Crear material (pantalla inicial) Se muestra la vista. |  |

#### Fijar precios para variante de material

Objetivo

En esta actividad se actualiza un registro de condición de precio estándar para la variante.

Procedimiento

Clase de condición: PPR0 (precio)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación | Abierto Fijar precios de material . | El Modificar registros de condición Se muestra la vista. |  |
| 3 | Introducir tipo de condición | El Modificar registros de condición vista, en el campo Clase de condición : introduzca PPR0 (Precio), y, a continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Seleccionar combinación de claves | En la Combinación de claves , seleccione Material con status de liberaciónA continuación, seleccione Intro . | El Modificar precio (PPR0): Selección Se muestra la vista. |  |
| 5 | Selección | El Modificar precio (PPR0): Selección introduzca los siguientes datos:Org.ventas : 1710 (Org.ventas nac.US)Canal distrib. : 10 (Ventas directas)Material : CAR-WASH-VAR (variante de lavado de coche)Válido el : <Fecha> , por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen Se muestra la vista. |  |
| 6 | Introducir condición de precio | El Modificar condición de precio (PPR0): Resumen introduzca los siguientes datos:Material : CAR-WASH-VAR (Car Wash VAR)Cantidad : por ejemplo, 20.00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, la fecha de hoySeleccionar Intro .A continuación, seleccione Grabar . | Se crea un precio estándar para la variante. |  |

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
> Flagged while digesting this document, not verified: Document is machine-translated and unreviewed; some values inconsistent: condition TELETELÉFONO, 'TRIMESTRAL' vs QUARTERLY, 'AÑO' vs YEARLY, contract price material SRV_CONTRACT vs SRV_CONTR_CONFIG, CAR-WASH_CONF vs CAR_WASH_CONF.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Contract-order characteristics use 'Valores múltiples' while service-order ones use single values; the service-order class section says the characteristics belong to the 'service contract class' in the summary table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]
- related-to :: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 52,960 chars in the whole document
