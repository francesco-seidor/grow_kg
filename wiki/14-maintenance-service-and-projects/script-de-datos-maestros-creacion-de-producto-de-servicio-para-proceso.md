---
id: 14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso
title: "Script de datos maestros: Creación de producto de servicio para procesos de servicio - MDS (3KV) (3KV_S4CLD2608_Master_Data_ES_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated): creating service products SRV_* and EXP_FSM_*, their prices and overtime/calculation-criterion conditions."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-products-for-service-processes]
aliases: [3KV_S4CLD2608_Master_Data_ES_XX]
keywords: [Service Products and Service Prices, service product master data, service product types, service contract products, service expenses, spare parts, service bundles, stock spare part material, service product pricing, overtime pricing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-348
topic: 14-maintenance-service-and-projects/service-products-for-service-processes
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Creación de producto de servicio para procesos de servicio - MDS (3KV) (3KV_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Service Products and Service Prices** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de producto de servicio para procesos de servicio - MDS (3KV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233894646)

[2 Requisitos previos 4](#_Toc233894647)

[2.1 Acceso al sistema 4](#_Toc233894648)

[2.2 Roles 4](#_Toc233894649)

[2.3 Unidades organizativas necesarias 4](#_Toc233894650)

[3 Tabla de resumen 6](#_Toc233894651)

[4 Procedimientos 7](#_Toc233894652)

[4.1 Crear productos de servicio 7](#_Toc233894653)

[4.1.1 SRV_01 7](#_Toc233894654)

[4.1.2 SRV_CONTRACT 9](#_Toc233894655)

[4.1.3 SRV_CTR_RENEWAL 11](#_Toc233894656)

[4.1.4 SRV_02 13](#_Toc233894657)

[4.1.5 FSM – Posición de gastos 14](#_Toc233894658)

[4.1.6 SRV_03 16](#_Toc233894659)

[4.1.7 SRV_04 18](#_Toc233894660)

[4.1.8 SRV_BUNDLE_01 20](#_Toc233894661)

[4.1.9 SRV_BUNDLE_02 22](#_Toc233894662)

[4.1.10 SRV_05 24](#_Toc233894663)

[4.1.10.1 Crear datos básicos 24](#_Toc233894664)

[4.1.10.2 Crear datos de ventas 25](#_Toc233894665)

[4.1.10.3 Crear datos de compras 27](#_Toc233894666)

[4.1.10.4 Crear datos MRP/planificación 28](#_Toc233894667)

[4.1.10.5 Crear datos de almacén 30](#_Toc233894668)

[4.1.10.6 Crear datos de contabilidad 31](#_Toc233894669)

[4.2 Fijar precios para materiales 33](#_Toc233894670)

[4.2.1 Precio para SRV_01 33](#_Toc233894671)

[4.2.2 Precio para SRV_CONTRACT 34](#_Toc233894672)

[4.2.3 Precio para SRV_CTR_RENEWAL 35](#_Toc233894673)

[4.2.4 Precio para SRV_02 36](#_Toc233894674)

[4.2.5 Precio para SRV_04 37](#_Toc233894675)

[4.2.6 Precio para SRV_BUNDLE_01 38](#_Toc233894676)

[4.2.7 Precio para SRV_05 39](#_Toc233894677)

[4.2.8 Precio para FSM - Gastos EXP_FSM_MILEAGE 41](#_Toc233894678)

[4.3 Fijar precios para horas extras 42](#_Toc233894679)

[4.4 Creación de registro de condición para criterio para cálculo 43](#_Toc233894680)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear registros de datos maestros de productos de servicio, incluidos los precios. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance no se describen en este documento, aunque pueden aparecer en la IU.

Un registro maestro de productos de servicio que se crea como se describe aquí se puede utilizar para la orden de servicio y procesamiento de confirmación de servicio.

| ID de producto de servicio | Descripción | Utilización |
| --- | --- | --- |
| SRV_01 | Servicio | representa el propio servicio, por ejemplo, una instalación, una reparación, un mantenimiento |
| SRV_CONTRACT | Producto de contrato | representa el propio servicio dentro del contrato |
| SRV_CTR_RENEWAL | Producto de renovación de contrato de servicio | representa el producto de contrato de servicio dentro del contrato con Valores prefijados para renovación automática |
| SRV_02 | Gastos de servicio | refleja el gasto que podría ocurrir debido al servicio, por ejemplo, los gastos de viaje, Combustible |
| SRV_03 | Pieza de recambio (no definida) | refleja un material necesario para el servicio y permite texto libre descripcióneste material no de almacén solo se puede aprovisionar |
| SRV_04 | Pieza de recambio (definida) | refleja el material como no de almacén con logística mínima/sin logística integracióneste material no de almacén solo se puede aprovisionar |
| SRV_05 | Pieza de recambio de stock | refleja un material que se tomará del stock (picking de stock) escenario) |
| SRV_06 | Pieza de recambio de stock con perfil de número de serie | refleja un material con un perfil de número de serie asignado que Tomar de stock (Efectuar picking de escenario de stock) |
| SRV_BUNDLE_01 | Paquete de servicios 01 | representa un servicio complejo como un paquete con subposiciones |
| SRV_BUNDLE_02 | Paquete de servicios 02 | representa un servicio complejo como un paquete con subposiciones (posición de servicio y posiciones de precio fijo) |
| EXP_FSM_TRAVELEXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_MILEAGE | Gastos de servicio | refleja el gasto, por ejemplo, el coste del viaje o las comidas, en caso de integración con SAP Field Service Management. |

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |
| Especialista en determinación de precios | SAP_BR_PRICING_SPECIALIST | Gestión de precios | SAP_BR_PRICING_SPECIALIST |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Unidad organizativa que se utilizará para EE. UU. | Unidad organizativa a utilizar para DE |
| --- | --- | --- | --- |
| Crear material | Centro | 1710 (Centro 1 US) | 1010 (Centro 1 DE) |
| Crear material | Organización de ventas | 1710 (Org.ventas nac.US) | 1010 (Org.ventas nac.DE) |
| Crear material | Canal de distribución | 10 (Ventas directas) | 10 (Ventas directas) |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear productos de servicio | SAP_BR_PRODMASTER_SPECIALIST | Crear material (MM01) | Se crean productos de servicio. |
| Fijar precios para materiales (Crear registros de condición) | SAP_BR_PRICING_SPECIALIST | Fijar precios de material - Ventas (VK12) | Se definen los precios de los productos de servicio. |
| Fijar precios para horas extras (crear registros de condición) | SAP_BR_PRICING_SPECIALIST | Fijar precios de material - Ventas (VK12) | Se ha definido el precio de las horas extras. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear productos de servicio

#### SRV_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material se visualiza. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) Servicio) | El Crear material (pantalla inicial) hacer las siguientes entradas: ventana de diálogo, seleccione elMaterial: SRV_01Ramo MSi el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena en la oscuridad. Actualmente solo existe una entrada para el sector (M = Mecánico) ingeniería).Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.El Seleccionar vista(s) la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroComprasContabilidad1A continuación, seleccione Continuar (Intro) . | El Nivel de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:Centro: 1710 (Centro 1 US)Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_01 (servicios) la vista es visualizado. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 vista, actualice la valores siguientes:Descr.: ServicioUnidad de medida base: HR (horas)Grupo de materiales: P001 (Servicios)Gr.pos.gen.: SRVP (producto de servicio)A continuación, seleccione Continuar (Intro) . | Los datos básicos se actualizan y Ventas: org.ventas 1 la etiqueta es visualizado.Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generalesDescuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Grupo de tipos de posición: SRVP (producto de servicio)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |
| 9 | Actualizar datos generales de ventas | El Ventas: General/Centro vista, actualice la valores siguientes:Unidad de medida base: HR (horas)Duración del trabajo: 1 RR. HH.Perfil de servicio: 5x10 (Mo-Fr: 7-17h)Perfil de respuesta: FIRST (tiempo de respuesta de primer nivel)A continuación, seleccione Intro . | Se actualizan los datos generales de ventas. |  |
| 10 | Actualizar datos de compras | El Compras vista, en los Datos generales sección, realice las siguientes entradas:Unidad de medida base : por ejemplo, RR.HH.Grupo de materiales : por ejemplo, P001Grupo de compras : por ejemplo, 001Ind.impto.p.material : para ejemplo, 1A continuación, seleccione Continuar (Intro) . | Se actualizan los datos de compras. |  |
| 11 | Actualizar datos de contabilidad | El Contabilidad 1 vista, en el Datos de valoración actuales la sección, haga entrada siguiente:Unidad de medida base : por ejemplo, RR.HH.Categoría de valoración : por ejemplo, 3200A continuación, seleccione Grabar . | Se actualizan los datos de contabilidad.Se graba el producto de servicio. El sistema muestra el Crear material (inicial) Pantalla) vista. |  |

#### SRV_CONTRACT

Objetivo

Este material es relevante para la edición en la nube y local.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) Servicio) | El Crear material (pantalla inicial) hacer las siguientes entradas:● Material : SRV_CONTRACT● Ramo MSi el Ramo el campo de entrada está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para entrada, el campo se rellena en la oscuridad. Actualmente solo hay una entrada existe para la industria (M = Ingeniería mecánica).● Tipo de material : Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.El Seleccionar vista(s) la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione lo siguiente vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:• Centro : 1710 (Centro 1) US)• Org.ventas .: 1710 (Org.ventas nac. US)• Canal distrib. : 10 (directo) Ventas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_CONTRACT (servicio Producto) Se muestra la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 vista, actualice la valores siguientes:• Descr. .: Contrato de servicio Producto• Unidad de medida base : AU Unidad de actividad• Grupo de materiales : P001 (Servicios)• Gr.pos.gen. : SCNP Contrato serv. Prod.A continuación, seleccione Continuar (Intro) . | Se actualizan los datos básicos y Ventas: org.ventas 1 la pestaña es visualizado. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generales• Descuento por pronto pago : X <seleccionado>Datos fiscales• Clasificación fiscal : 1 (impuesto completo)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: org.ventas 2 se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Grupo de tipos de posición : SNCP - Contrato serv. Prod.A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |
| 9 | Actualizar datos generales de ventas | El Ventas: General/Centro vista, actualice la valores siguientes:• Unidad de medida base : AU Unidad de actividad• Duración del trabajo : 1 día (días)• Perfil de servicio : 5x10 (Mo-Fr: 7-17h)• Perfil de respuesta .: FIRST (primero) Tiempo de respuesta de nivel)A continuación, seleccione Grabar . | Se actualizan los datos generales de ventas. |  |

#### SRV_CTR_RENEWAL

Objetivo

Este material es relevante para la edición en la nube y local.

Este material tiene valores predeterminados de renovación automática.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) Servicio) | El Crear material (inicial) Pantalla) efectúe las siguientes entradas:● Material : SRV_CTR_RENEWAL● Ramo MSi el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena en la oscuridad. Actualmente solo existe una entrada para el sector (M = Mecánico) ingeniería).● Tipo de material : Servicio ProductoA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.Ha actualizado la información básica para el nuevo servicio producto. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Ventas Datos org.1Ventas : Ventas Datos org.2Ventas : Datos centro/gral.A continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice los siguientes valores:• Centro : 1710 (Centro 1) US)• Org.ventas .: 1710 (Dom. Org.ventas EE. UU.)• Canal distrib. : 10 Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_CTR_RENEWAL (servicio Producto) Se muestra la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 , actualice los siguientes valores:• Descr. .: Servicio Producto de renovación de contrato• Unidad de medida base : AU (unidad de actividad)• Grupo de materiales : P001 (Servicios)• Gr.pos.gen. : SCNP Prod.contrato serv.• Indicador de renovación automática de contrato : 1A continuación, seleccione Continuar (Intro) . | Se actualizan los datos básicos y Ventas: org.ventas 1 la pestaña es visualizado. |  |
| 7 | Actualizar datos de organización de ventas 1) | El Ventas: org.ventas 1 vista, actualice los siguientes valores:Datos generales• Descuento por pronto pago : X <seleccionado>Datos fiscales• Clasificación fiscal : 1 (impuesto completo)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: Org.ventas 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas 2) | El Ventas: org.ventas 2 vista, actualice la siguiente entrada:Términos de agrupación• Grupo de tipos de posición : SRVP (Producto de servicio)Período de prórroga de renovación automática• Período de prórroga por defecto : 1• Unidad para ampliación : Año A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro la etiqueta es visualizado. |  |
| 9 | Actualizar datos generales de ventas | El Ventas: General/Centro vista, actualice los siguientes valores:• Unidad de medida base : AU Unidad de actividad• Duración del trabajo : 1 día (días)• Perfil de servicio : 5x10 (Mo-Fr: 7-17h)• Perfil de respuesta .: PRIMERO (Tiempo de respuesta de primer nivel)A continuación, seleccione Grabar . | Se actualizan los datos generales de ventas.Se graba el producto de servicio. El sistema muestra el Crear material (pantalla inicial) vista. |  |

#### SRV_02

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para servicio de producto de servicio) Gastos) | El Crear material (pantalla inicial) hacer las siguientes entradas:Material: SRV_02Ramo MSi el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena en la oscuridad. Actualmente solo existe una entrada para el sector (M = Mecánico) ingeniería).Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.El Seleccionar vista(s) la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosComercio internacional : ExportarA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:Centro: 1710 (Centro 1 US)Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_02 (gastos de servicio) se visualiza la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 vista, actualice la valores siguientes:Descr.: Gastos de servicioUnidad de medida base: EA (cada uno)Grupo de materiales: P002 (Gastos)Gr.pos.gen.: SRVE (posición de gastos)A continuación, seleccione Continuar (Intro) . | Los datos básicos se han actualizado y Ventas: org.ventas 1 la pestaña es visualizado.Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generalesDescuento por pronto pago: <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Grupo de tipos de posición: SRVE (posición de gastos)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El producto de servicio es grabado. |  |

#### FSM – Posición de gastos

Objetivo

Este material solo es relevante para la edición en la nube.

Aplicar posiciones de servicio para FSM (procesamiento de órdenes de servicio con SAP Field Service Management) como SRV_02, por ejemplo, "Posición de gastos para alojamiento".

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para servicio de producto de servicio) Gastos) | El Crear material (pantalla inicial) hacer las siguientes entradas:Material: EXP_FSM_ACCOMRamo MSi el Ramo campo de entrada está oculto, no se requiere ninguna entrada. Cuando la industria No se ofrece el sector para la entrada, el campo se rellena en la oscuridad. Actualmente solo existe una entrada para industria (M = Ingeniería mecánica).Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.También puede crear como material de gastos, por ejemplo:EXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_TRAVELEXP_FSM_MILEAGEEl Seleccionar vista(s) la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosContabilidad 1 (solo para EXP_FSM_MILEAGE)A continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:Centro: 1710 (Centro 1 US)Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_02 (gastos de servicio) se visualiza la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 vista, actualice la valores siguientes:Descripción: Gastos de servicioPara todos los gastos excepto EXP_FSM_MILEAGEUnidad base de Medida: EA (cada uno)Para gasto EXP_FSM_MILEAGEUnidad base de Medida: KM (kilómetro)Grupo de materiales: P002 (Gastos)Gr.pos.gen.: SRVE (posición de gastos)A continuación, seleccione Grabar . | Los datos básicos se han actualizado y Ventas: org.ventas 1 la pestaña es visualizado. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generalesDescuento por pronto pago: <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Grabar . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Grupo de tipos de posición: SRVE (posición de gastos)A continuación, seleccione Grabar .Para Polonia o EXP_FSM_MILEAGE: seleccione Intro en lugar de Grabar . | Se actualizan los datos organizativos de ventas. Se graba el producto de gastos. |  |
| 9 | Actualizar contabilidad 1(solo para EXP_FSM_MILEAGE) | En la vista Contabilidad 1, actualice los siguientes valores:Valoración actual- Clase de valor: por ejemplo, 3300- Precio estándar: por ejemplo, 1.50A continuación, seleccione Grabar . | Se actualizan los datos de Contabilidad 1. Se graba el producto de gastos. |  |

#### SRV_03

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para reserva de producto de servicio) Parte) | El Crear material (pantalla inicial) hacer las siguientes entradas:Material: SRV_03Ramo MSi el Ramo el campo de entrada es oculto, no se requiere ninguna entrada. Cuando el ramo está no se ofrece para la entrada, el campo se rellena en la oscuridad. Actualmente solo existe una entrada para el sector (M = Mecánico) ingeniería).Tipo de material: Material no de almacénA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.El Seleccionar vista(s) la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosComprasContabilidad 1A continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:Centro: 1710 (Centro 1 US)Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_03 (pieza de recambio) ver se visualiza. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 vista, actualice la valores siguientes:Descr.: Pieza de recambioUnidad de medida base: EA (cada uno)Grupo de materiales: YBMM00 (material no de almacén sin ID)Gr.pos.gen.: SRVM (material de servicio)A continuación, seleccione Continuar (Intro) . | Los datos básicos se actualizan y Ventas: org.ventas 1 la pestaña es visualizado.Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generalesDescuento por pronto pago: <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Grupo de tipos de posición: SRVM (material de servicio) | Se actualizan los datos organizativos de ventas. |  |
| 9 | Actualizar datos de compras | en la Compras vista, en el Datos generales sección, haga lo siguiente entradas:Unidad de medida base : por ejemplo, UNGrupo de materiales : por ejemplo, YBM00Grupo de compras : por ejemplo, 001Ind.impto.p.material : por ejemplo, 1A continuación, seleccione Continuar (Intro) . | Se actualizan los datos de compras. |  |
| 10 | Actualizar datos de contabilidad | en la Contabilidad 1 vista, en el Datos de valoración actuales la sección, haga entrada siguiente:Categoría de valoración : para ejemplo, YB01Control de precio : para ejemplo, SPrecio estándar : para ejemplo, 1Unidad de precio : por ejemplo, 1A continuación, seleccione Grabar . | Se actualizan los datos de contabilidad.Se graba el producto de servicio. El sistema muestra Crear Material (imagen inicial) vista. |  |

#### SRV_04

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio gestionado) Pieza de recambio) | El Crear material (pantalla inicial) hacer las siguientes entradas:● Material : SRV_04● Ramo MSi el campo de entrada Ramo está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo es poblado en la oscuridad. Actualmente solo existe una entrada para el sector (M = Ingeniería mecánica).● Tipo de material : No gestionado en stock MaterialA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.La(s) vista(s) de selección la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosComercio internacional : ExportarComprasContabilidad 1A continuación, seleccione Continuar (Intro) . | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:● Centro : 1710 (Centro 1) US)● Org.ventas : 1710 (Org.ventas nac. US)● Canal distrib. : 10 (directo) Ventas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_04 (pieza de recambio gestionada) (No gestionado en stock)) Se muestra la vista. |  |
| 6 | Actualizar datos básicos | En la vista Datos básicos 1, actualice los siguientes valores:● Descr. : Pieza de recambio gestionada (no de almacén)● Unidad de medida base : UN (cada uno)● Grupo de materiales : YBMM01 (no gestionado en stock) Material con ID)● Gr.pos.gen. : SRVM (servicio) Material)A continuación, seleccione Continuar (Intro) . | Los datos básicos se actualizan y Ventas: org.ventas 1 la pestaña es visualizado.Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generales• Descuento por pronto pago : <seleccionado>Datos fiscales• Clasificación fiscal : 1 (completo) impuesto)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | En la pantalla Sales: sales org. 2 vista, actualice la entrada siguiente:Grupo de tipos de posición : SRVM (servicio) Material)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. |  |
| 9 | Datos de compras de actualización de pieza de recambio | El Compras vista, en el Datos generales sección, haga lo siguiente entradas:• Unidad de medida base : por ejemplo, UN• Grupo de materiales : por ejemplo, YBMM01• Grupo de compras : por ejemplo, 001Ind.impto.p.material : por ejemplo, 1A continuación, seleccione Continuar (Intro) . | Se actualizan los datos de compras. |  |
| 10 | Actualizar datos de contabilidad | El Contabilidad 1 vista, en el Datos de valoración actuales la sección, haga entrada siguiente:• Categoría de valoración : por ejemplo, YB01• Control de precio : por ejemplo, S• Precio estándar : por ejemplo, 1• Unidad de precio : por ejemplo, 1A continuación, seleccione Grabar . | Se actualizan los datos de contabilidad.Se graba el producto de servicio.El sistema muestra el Crear material (inicial) Pantalla) vista. |  |

#### SRV_BUNDLE_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) es visualizado. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) Servicio) | El Crear material (pantalla inicial) hacer las siguientes entradas:● Material : SRV_BUNDLE_01● Ramo MSi el campo de entrada Ramo está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo es poblado en la oscuridad. Actualmente solo existe una entrada para el sector (M = Ingeniería mecánica).● Tipo de material : Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo servicio producto.La(s) vista(s) de selección la ventana de diálogo es visualizado. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione las siguientes vistas:Datos básicos 1Ventas : Datos org.ventas 1Ventas : Datos org.ventas 2Ventas : General/Centro DatosComercio internacional : ExportarA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualizar los siguientes valores:● Centro : 1710 (Centro 1) US)● Org.ventas : 1710 (Org.ventas nac. US)● Canal distrib. : 10 (directo) Ventas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_BUNDLE_01 (servicios) se visualiza la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 , actualice los siguientes valores:● Descr. : Precio fijo de paquete de servicios● Unidad de medida base : UN (cada uno)● Grupo de materiales : p001 (Servicios)● Gr.pos.gen. : SVBL (paquete de servicios FP)A continuación, seleccione Continuar (Intro) . | Los datos básicos se actualizan y Ventas: org.ventas 1 la pestaña es visualizado.Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:Datos generales• Descuento por pronto pago : X <seleccionado>Datos fiscales• Clasificación fiscal : 1 (completo) impuesto)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | En la pantalla Sales: sales org. 2 vista, actualice la entrada siguiente:Grupo de tipos de posición : SVBL (paquete de servicios) FP)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |
| 9 | Actualizar datos generales de ventas | El Ventas: General/Centro , actualice el siguientes entradas:• Unidad de medida base : UN (Cada)• Duración del trabajo : por ejemplo, 2 RR. HH. (horas)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos generales de ventas. |  |

#### SRV_BUNDLE_02

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Actualizar datos básicos de material (para servicio de producto de servicio) | El Crear material (pantalla inicial) , haga el siguientes entradas:Material : SRV_BUNDLE_02Ramo MSi el campo de entrada Ramo está oculto, no se requiere ninguna entrada. Cuando el ramo no se ofrece para la entrada, el campo es Poblado en la oscuridad. Actualmente solo existe una entrada para el sector (M = Ingeniería mecánica).Tipo de material : Servicio ProductoA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.La(s) vista(s) de selección se visualiza la ventana de diálogo. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione el vistas siguientes:Datos básicos 1Ventas : Org.ventas Datos 1Ventas : Org.ventas Datos 2Ventas : General/Centro DatosA continuación, seleccione Continúe (Intro). | El Niveles de organización se visualiza. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice la valores siguientes:Centro : 1710 (Centro 1) EE. UU.)Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 (directo) Ventas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_BUNDLE_02 (servicios) la vista es visualizados. |  |
| 6 | Actualizar datos básicos | En la vista Datos básicos 1, actualice los siguientes valores:Descr. : Servicio PaqueteUnidad de medida base : UN (cada uno)Grupo de materiales : p001 (Servicios)Gr.pos.gen. : SVBV (servicio) Agrupar T&M)A continuación, seleccione Continuar (Intro) . | Los datos básicos se actualizan y Ventas: org.ventas 1 pestaña se visualiza.Nota Para cada idioma diferente utilizado en su empresa, el descripción para el producto debe actualizarse por código de idioma. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 , actualice los siguientes valores:Datos generalesDescuento por pronto pago : X <seleccionado>Datos fiscalesClasificación fiscal : 1 (completo) impuesto)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: org.ventas 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | En la pantalla Sales: sales org. 2 , actualice la siguiente entrada:Grupo de tipos de posición : SVBV (servicio) Paquete)A continuación, seleccione Continuar (Intro) . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |
| 9 | Actualizar datos generales de ventas | El Ventas: General/Centro , actualice lo siguiente entradas:Unidad de medida base : UN (Cada uno)Duración del trabajo : por ejemplo, 2 RR. HH. (horas)A continuación, seleccione Grabar . | Se actualizan los datos generales de ventas. |  |

#### SRV_05

##### Crear datos básicos

Objetivo

Este material solo es relevante para la edición en la nube.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | El Crear material (pantalla inicial) aparece. |  |
| 3 | Introducir datos básicos de material | En la Crear material (pantalla inicial)Material : SRV_05Ramo : MNota Si el Ramo introduzco el campo está oculto, no se requiere ninguna entrada. Cuando la industria No se ofrece el sector para la entrada, el campo se rellena con en la oscuridad.Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | Aparece una ventana nueva, Seleccionar vista(s) . |  |
| 4 | Seleccionar vistas | En Seleccionar vista(s) , seleccione Datos básicos 1 y realice las siguientes entradas: | Crear material SRV_05 (mercaderías) se abre. |  |
| 5 | Introducir datos básicos | Introduzca:Descripción : Pieza de recambio de stockEn la Datos generales introduzca lo siguiente:Unidad base : UNGrupo de productos : L001Sector : 00Gr.tp.pos.gen. : SVST o NORMEn la Dimensiones/EAN introduzca lo siguiente:Peso bruto : 2Unidad de peso : KGPeso neto : 1 | Nota Para cada idioma diferente utilizado en su empresa, Se debe actualizar la descripción correspondiente para el producto por código de idioma |  |
| 6 | Completar datos básicos | No se requieren entradas para Datos básicos 2 no tiene que realizar ninguna entrada. |  |  |
| 7 | Guardar los datos | En la parte inferior derecha de la pantalla, seleccione Grabar para guardar los datos. | El Crear material (pantalla inicial) aparece.Los datos básicos se crean y se graban. |  |

##### Crear datos de ventas

Objetivo

Este material solo es relevante para la edición en la nube.

Requisito previo

Debe completar la sección anterior, Crear datos básicos, antes de continuar con esta sección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | Crear material (vista inicial) es visualizado. |  |
| 2 | Introducir datos básicos de material | En la Crear material , efectúe las siguientes entradas:Material : SRV_05Tipo de material : Comercio MercancíasSeleccionar Seleccionar vista(s) . | Después de completar las entradas, se abre una ventana nueva, Seleccionar Vista(s) . |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) de selección de ventana Ventas: Datos org.ventas 1 , Ventas: Datos org.ventas 2 y Ventas: Datos generales/de centro y seleccione Continuar . | Una ventana con Niveles de organización es visualizado. |  |
| 4 | Introducir datos de niveles de organización | En Niveles de organización , en el Nivel de organización sección, introduzca Descripciones para lo siguiente:Centro : 1710Org.ventas : 1710Canal distrib. : 10Seleccionar Continuar .Nota La información aparece en la parte inferior de la vista: El El material ya existe y se ampliado . | Crear material SRV_05 (mercaderías) se visualiza la vista. |  |
| 5 | Introducir datos de ventas | En Material SRV_05 (mercaderías) , de el Ventas: org.ventas 1 pestaña, en el Datos generales la sección, haga entrada siguiente:Centro suministrador : 1710 |  |  |
| 6 | Introducir datos de ventas | En Material SRV_05 (mercaderías) , de el Ventas: org.ventas 1 pestaña, en el Datos fiscales sección, haga lo siguiente entradasClasificación fiscal : 1Seleccione la pestaña Ventas: org.ventas 2 . | La siguiente pestaña Ventas: org.ventas 2 es visualizado. |  |
| 7 | Introducir datos de ventas | El Ventas: org.ventas 2 pestaña, en el Conceptos de agrupación la sección, haga siguientes entradas:Mat.gr.imputación : 01Grupo de tipos de posición : SVST o NORMSeleccione la pestaña Ventas: General/Centro . | La siguiente pestaña Ventas: General/Centro es visualizado. |  |
| 8 | Introducir datos de ventas | El Ventas: General/Centro pestaña, en el Datos generales , introduzca lo siguiente datos:Verificación de disponibilidad : PE |  |  |
| 9 | Introducir datos de ventas | El Ventas: General/Centro pestaña, en el Datos de expedición (tiempos en días) sección, introduzca los siguientes datos:Gpo.transp. : 0001Gr.carga : 0001 |  |  |
| 10 | Introducir datos de ventas | En la Parámetros generales de centro sección, indique los datos siguientesCentro de beneficio : <YB700> |  |  |
| Solo para Polonia | Introducir datos de ventas | En la Comercio internacional: Exportación sección, introduzca los siguientes datos:Código de control. : por ejemplo, 41.00.30.0 | Se actualiza el código PKWiU para Polonia. |  |
| 11 | Grabe los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

##### Crear datos de compras

Objetivo

Este material solo es relevante para la edición en la nube.

Requisito previo

Debe completar los procedimientos anteriores antes de continuar con esta sección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material mosaico de aplicación. | Crear material (pantalla inicial) aparece. |  |
| 2 | Introducir datos básicos de material | En la Crear material , efectúe las siguientes entradas:Material : SRV_05Tipo de material :Mercaderías (HAWA)Seleccionar Seleccionar vista(s) . | Seleccionar vista(s) Se abre la pantalla. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) selección de ventana Compras y seleccione Continuar . | Niveles de organización es visualizado. |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización en la pantalla Nivel de organización , realice la siguiente entrada:Centro : 1710Seleccionar Continuar .Nota Aparece un mensaje en la parte inferior de la pantalla: El El material ya existe y se ampliado . | Crear material SRV_05 (mercaderías) se abre. |  |
| 5 | Introducir datos de compras | En la Material SRV_05 (mercaderías) pantalla, en la pantalla Compras en la pestaña Datos generales , realice las siguientes entradas:Grupo de compras : 001Grupo de materiales : L001 |  |  |
| 6 | Introducir datos de compras | En la Otros datos/datos del fabricante , realice la siguiente entrada:Tmpo.tratam.EM : por ejemplo, 1 |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

##### Crear datos MRP/planificación

Objetivo

Este material solo es relevante para la edición en la nube.

Requisito previo

Debe completar los procedimientos anteriores antes de continuar con esta sección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | Crear material (pantalla inicial) se abre. |  |
| 2 | Introducir datos básicos de material | En la Crear material , realice lo siguiente entradas:Material : SRV_05Tipo de material : Comercio MercancíasSeleccionar Seleccionar vista(s) . | Seleccionar vista(s) Se abre la pantalla. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) de selección de ventana MRP1 , MRP2 , MRP3 , y MRP4 y seleccione Continuar . | Niveles de organización aparece. |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización en la pantalla Nivel de organización , realice las siguientes entradas:Centro : 1710Almacén : 171ANota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliado . | El Crear material SRV_05 (mercaderías) Se abre la pantalla. |  |
| 5 | Introducir datos de planificación/MRP | En la Material SRV_05 (mercaderías) pantalla, en la pantalla MRP1 en la pestaña Datos generales , realice las siguientes entradas:Caract.planif.nec. : NDPlanificador de necesidades : <001> |  |  |
| 6 | Introducir datos de planificación/MRP | En la Datos de tamaño de lote realice la siguiente entrada:Cálculo del tamaño del lote : <EX>Seleccione la siguiente pestaña Planif.necesidades 2 | La siguiente pestaña, Planif.necesidades 2 se abre. |  |
| 7 | Introducir datos de planificación/MRP | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Planif.necesidades 2 en la pestaña Aprovisionamiento sección, haga lo siguiente entradas:Clase de aprovisionamiento : XEn la Programación sección, haga lo siguiente entradas:Plazo de entrega previsto : por ejemplo, 3Tmpo.tratam.EM : por ejemplo, 1Clave de horizonte : por ejemplo, 000Seleccione la siguiente pestaña Planif.necesidades 3 . | La siguiente pestaña, Planif.necesidades 3 se abre. |  |
| 8 | Introducir datos de planificación/MRP | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Planif.necesidades 3 en la pestaña Planificación , realice las siguientes entradas:Grupo de estrategias : por ejemplo, 40 |  |  |
| 9 | Introducir datos de planificación/MRP | En la Verificación de disponibilidad , realice las siguientes entradas:Verificación de disponibilidad : NCPlazo reaprov.total : por ejemplo, 3Seleccione la siguiente pestaña Planif.necesidades 4 | La siguiente pestaña, Planif.necesidades 4 se abre. |  |
| 10 | Introducir datos de planificación/MRP | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Planif.necesidades 4 en la pestaña Explosión de la lista de materiales/necesidades secundarias realice las siguientes entradas:Individual/Colectivo : <vacío> |  |  |
| 11 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Se han guardado los datos. |  |

##### Crear datos de almacén

Objetivo

Este material solo es relevante para la edición en la nube.

Requisito previo

Debe completar los procedimientos anteriores antes de continuar con esta sección.

|  |
| --- |
| Nota Primero, cree una vista para el almacén 171A y, a continuación, cree igual para el almacén 171B. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material mosaico de aplicación. | Crear material (pantalla inicial) se abre. |  |
| 2 | Introducir datos básicos de material | En la Crear material , efectúe las siguientes entradas:Material : SRV_05Tipo de material : MercaderíasSeleccionar Seleccionar vista(s) . | Seleccionar vista(s) se abre. |  |
| 3 | Seleccionar vistas | En la Seleccionar vista(s) seleccione las siguientes vistas:Datos de centro generales/Almacenamiento 1Datos de centro generales/Almacenamiento 2Seleccionar Continuar . | Niveles de organización se visualiza. |  |
| 4 | Introducir datos de niveles de organización | En Niveles de organización , en la Nivel de organización , realice las siguientes entradas:Centro : 1710Almacén : 171ANota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliado . | Crear material SRV_05 (mercaderías) se abre. |  |
| 5 | Introducir datos de almacén | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Dat.ce./almacén 1 en la pestaña Datos generales , realice la siguiente entrada:Número de vales de entrada de mercancías : por ejemplo, 1 | La siguiente pestaña, Dat.ce./alm.2 se abre. |  |
| 6 | Introducir datos de almacén | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Dat.ce./Almacén 2 en la pestaña Datos generales , realice la siguiente entrada:Centro de beneficio : YB700 |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | Datos maestros: Producto aparece.Se han guardado los datos. |  |

##### Crear datos de contabilidad

Objetivo

Este material solo es relevante para la edición en la nube.

Requisito previo

Debe completar los procedimientos anteriores antes de continuar con esta sección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Acceder a la aplicación SAP Fiori | Seleccionar Crear material aplicación. | Se abre una ventana nueva que muestra la Crear material (pantalla inicial) . |  |
| 2 | Introducir datos básicos de material | En la Crear material (pantalla inicial) efectúe las siguientes entradas:Material : SRV_05Tipo de material : Mercaderías HAWASeleccionar Seleccionar vista(s) . | Seleccionar vista(s) se abre. |  |
| 3 | Seleccionar vistas | En Seleccionar vista(s) , seleccione las siguientes vistas:Contabilidad 1Seleccionar Continuar . | Niveles de organización se abre. |  |
| 4 | Introducir datos de niveles de organización | En la Niveles de organización en la pantalla Nivel de organización , realice las siguientes entradas:Centro : 1710Nota La información aparece en la parte inferior de la pantalla: El material ya existe y se ampliado . | Crear material SRV_05 (mercaderías) se abre. |  |
| 5 | Introducir datos de contabilidad | En la Crear material SRV_05 (mercaderías) pantalla, en la pantalla Contabilidad 1 en la pestaña Datos de valoración generales , realice la siguiente entrada:Categoría de valoración : 3100Determ.precio : 2 (basado en transacción) |  |  |
| 6 | Introducir datos de contabilidad | En la Precios y valores , realice las siguientes entradas:Precio estándar : por ejemplo, 13.50Control de precio : S |  |  |
| 7 | Guardar los datos | En la parte inferior de la pantalla, seleccione Grabar . | El Datos maestros: Producto Aparece la ventana.Se han guardado los datos. |  |

### Fijar precios para materiales

#### Precio para SRV_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , introduzca la siguiente información:Clase de condición : PPR0A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione el Material con status de liberación opción.A continuación, seleccione Seleccione (Intro). . | El Modificar precio (PPR0): Selección la vista es visualizado. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :SRV_01 (producto de servicio)Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen se visualiza la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen vista, actualice los siguientes datos para el material SRV_01:Material: por ejemplo, SRV_01 (producto de servicio)Cantidad : por ejemplo, 35,00Unidad : USDInicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . | Se han actualizado las condiciones de precio para los productos de servicio SRV_01. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

#### Precio para SRV_CONTRACT

Objetivo

Este material es relevante para la edición en la nube y local.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : PSI1A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material .A continuación, seleccione Intro . | El Modificar precio (PSI1): Selección ver se visualiza. |  |
| 5 | Selección | En la Modificar precio (PSI1): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :SRV_CONTRACT (contrato de servicio) Producto)Válido el : <Fecha> por ejemplo, Fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPSI): Resumen Se muestra la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PSI1): Resumen , actualice los siguientes datos para material SRV_CONTRACT:Material : por ejemplo, SRV_CONTRACT (contrato de servicio) Producto)Cantidad : por ejemplo, 100,00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, Fecha de hoySeleccionar Intro . | Se actualizan las condiciones de precio para el producto de contrato de servicio SRV_CONTRACT. |  |
| 7 | Grabar | Seleccionar Grabar . | Se graba el precio del producto de contrato de servicio. |  |

#### Precio para SRV_CTR_RENEWAL

Objetivo

Este material es relevante para la edición en la nube y local.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , introduzca la siguiente información:Clase de condición : PSI1A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material .A continuación, seleccione Intro . | El Modificar precio (PSI1): Selección la vista es visualizado. |  |
| 5 | Selección | En la Modificar precio (PSI1): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 (directo) Ventas)Material :SRV_CTR_RENEWAL (Renovación de contrato de servicio) Producto)Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPSI): Resumen se visualiza la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PSI1): Resumen vista, actualice los siguientes datos para el material SRV_CTR_RENEWAL:Material : por ejemplo, SRV_CTR_RENEWAL (Renovación de contrato de servicio) Producto)Cantidad : por ejemplo, 90,00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . | Se actualizan las condiciones de precio para los productos de contrato de servicio SRV_CTR_RENEWAL. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos del contrato de servicio. |  |

#### Precio para SRV_02

Objetivo

Este material es relevante para la edición en la nube y local.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : PPR0A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material con status de liberación .A continuación, seleccione Intro . | El Modificar precio (PPR0): Selección ver se visualiza. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :SRV_02 (Gastos de servicio)Válido el : <Fecha> por ejemplo, Fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen Se muestra la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen , actualice los siguientes datos para material SRV_02:Material : por ejemplo, SRV_02 (Servicios)Cantidad : por ejemplo, 15.00Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, Fecha de hoySeleccionar Intro . | Se actualizan las condiciones de precio para los productos de servicio SRV_02. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

#### Precio para SRV_04

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , introduzca la siguiente información:Clase de condición : PPR0A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material con status de liberación .A continuación, seleccione Intro . | El Modificar precio (PPR0): Selección la vista es visualizado. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :SRV_04 (pieza de recambio gestionada (no de almacén))Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen se visualiza la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen vista, actualice los siguientes datos para el material SRV_04:Material : SRV_04 (pieza de recambio gestionada (no de almacén))Cantidad : por ejemplo, 15.00Unidad : USDInicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . | Se actualizan las condiciones de precio para los productos de servicio SRV_04. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

#### Precio para SRV_BUNDLE_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición , introduzca la siguiente información:Clase de condición : PPR0A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material con status de liberación .A continuación, seleccione Intro . | El Modificar precio (PPR0): Selección la vista es visualizado. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :SRV_BUNDLE_01 (agrupación de servicios 01)Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen se visualiza la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen vista, actualice los siguientes datos para el material SRV_01:Material : SRV_BUNDLE_01 (paquete de servicios 01)Cantidad : por ejemplo, 200,00Unidad : USDInicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . | Las condiciones de precio para productos de servicio SRV_BUNDLE_01 son actualizado. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

#### Precio para SRV_05

Objetivo

Este precio de material solo es relevante para la edición en la nube.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : PPR0A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione el Material con status de liberación opción.A continuación, seleccione Seleccione (Intro). . | El Modificar precio (PPR0): Selección la vista es visualizado. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección vista, actualice la siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material : SRV_05 (pieza de recambio de stock)Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar condición de precio (PPR0): Resumen Se muestra la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen , actualice los siguientes datos para material SRV_01:Material : SRV_05 (stock Pieza de recambio)Cantidad : por ejemplo, 14.50Unidad : USDInicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . | La condición PriceCorrection para el producto de servicio SRV_01 se ha actualizado. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

#### Precio para FSM - Gastos EXP_FSM_MILEAGE

Objetivo

Este material es relevante para la edición en la nube y local.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar precios de material - Ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : PCO4A continuación, seleccione Intro . | El Combinación de claves Se muestra la vista. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material con status de liberación .A continuación, seleccione Intro . | El Modificar precio (PCO4): Selección Se muestra la vista. |  |
| 5 | Selección | En la Modificar precio (PCO4): Selección vista, actualice lo siguiente información:Org.ventas : 1710 (Dom. Org.ventas EE. UU.)Canal distrib. : 10 Ventas directas)Material :EXP_FSM_MILEAGEVálido el : <Fecha> por ejemplo, Fecha de hoyA continuación, seleccione Ejecutar . | El Modificar condición de precio (PCO4): Resumen Se muestra la vista. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PCO4): Resumen vista, actualice la datos siguientes para material EXP_FSM_MILEAGE:Material : por ejemplo, EXP_FSM_MILEAGECantidad : por ejemplo, 1,50 (Precio por unidad)Unidad : por ejemplo, USDInicio de validez : <Fecha> por ejemplo, Fecha de hoySeleccionar Intro . | Se actualizan las condiciones de precio para el producto de servicio EXP_FSM_MILEAGE. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |

### Fijar precios para horas extras

Objetivo

Este procedimiento describe cómo fijar precios para las horas extras. Este capítulo solo es relevante para 3D2 (edición en la nube).

|  |
| --- |
| Nota Antes de actualizar los precios de las horas extras, debe crear las "Horas extras" Categorías" primero.Encontrará la descripción en el script de test 3D2, capítulo "2.5.6 Actualizar Categoría de horas extras’! |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material para ventas . | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : SOV1 o SOV2A continuación, seleccione Intro . | La pantalla Modificar horas extras (SOV1): Selección o bien Modificar horas extras (SOV 2 ): Selección se abre.Información:¿Se ha seleccionado SOV1 como registro de condiciones, podrá actualizar un valor absoluto como precio.¿Se ha seleccionado SOV2 como registro de condiciones, podrá actualizar un valor porcentual para el cálculo del precio. |  |
| 4 | Selección | En la Modificar horas extras (SOV1): Selección o Modificar horas extras (SOV 2 ): Selección vista, actualice la siguiente información:Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)Válido el : <Fecha> por ejemplo, la fechaA continuación, seleccione Ejecutar . | El Modificar horas extras (SOV1): Resumen o Modificar horas extras (SOV 2 ): Resumen se visualiza la vista. |  |
| 5 | Modificar condición de precio | En la Modificar horas extras (SOV1): Selección o Modificar horas extras (SOV 2 ): Selección vista, actualice una o más condiciones de precio para horas extras:Horas extras : por ejemplo, OV01, OV02, OV03Cantidad : por ejemplo, 30 o 50Unidad : por ejemplo, USD o %UM : por ejemplo, RR.HH.Inicio de validez : <Fecha> por ejemplo, la fechaSeleccionar Intro . |  |  |
| 6 | Grabar | Seleccionar Guarde. | Se han creado condiciones de precio para el cálculo de horas extras |  |

### Creación de registro de condición para criterio para cálculo

Objetivo

En esta actividad IMG se definen los registros de condición para los criterios para cálculo. Esta condición se puede utilizar en órdenes de servicio para diferenciar entre posiciones facturables, no facturables y parcialmente facturables con fines de determinación de precios y controlling. No facturable y parcialmente facturable los servicios son, por ejemplo, los que se prestan bajo garantía o en fondo de comercio. El registro de condición para el criterio para cálculo es opcional y solo para edición en la nube.

Procedimiento (mediante Fiori Launchpad)

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios. | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas | El Modificar registros de condición la vista es visualizado. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición vista, introduzca la siguiente información:Clase de condición : DAI2A continuación, seleccione Intro . | El Modif.ind.contab. (DAI2): Selección la vista es visualizado. |  |
| 4 | Selección | En la Modif.ind.contab. (DAI2): Selección vista, actualice lo siguiente información:Organización de ventas: por ejemplo, 1710 (Org.ventas nac.US)Canal de distribución: por ejemplo, 10 (Ventas directas)Válido el : <Fecha> por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Aparece la pantalla Modificar indicador de contabilidad (%) Condición (DAI2): Resumen la vista es visualizado. |  |
| 5 | Crear registro de condición | En la Modificar ind.contab.(%) condición (DAI2): Resumen cree la siguiente condición para SRV_01:Organización de ventas: por ejemplo, 1710 (Org.ventas nac.US)Canal distrib. : para ejemplo, <10> (Directo Ventas)Material : por ejemplo, <SRV_01>Ind.cta. : S1Cantidad : por ejemplo, <-100>Cl.cálculo : AInicio de validez: <Fecha> por ejemplo, la fechaFin de validez: <Fecha> por ejemplo, la fecha.Seleccionar Intro . | Se ha actualizado la condición de precio. |  |
| 6 | Grabar | Seleccionar Grabar . | Se crean registros de condición para el criterio para cálculo para el producto de servicio. |  |

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
> Flagged while digesting this document, not verified: Machine-translated and unreviewed; some inconsistencies inside: SRV_BUNDLE_01 and SRV_05 price steps refer to 'material SRV_01'; SRV_06 listed in the ID table but has no procedure

> [!warning] Conflict
> Flagged while digesting this document, not verified: Some products flagged cloud-only, others cloud and on-premise; may differ from other scope item scripts

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-3kv-351]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 77,827 chars in the whole document
