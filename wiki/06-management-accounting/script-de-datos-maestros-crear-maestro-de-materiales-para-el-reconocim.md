---
id: 06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim
title: Script de datos maestros - Crear maestro de materiales para el reconocimiento universal de ingresos (7R8) (7R8_S4CLD2608_Master_Data_ES_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated): create URR test materials and condition prices for SFS, fixed-price project and service contract scenarios."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [7R8_S4CLD2608_Master_Data_ES_XX]
keywords: [Event-Based Revenue Recognition for Sell from Stock, material master data, universal revenue recognition, sales from stock, service products, fixed-price customer project, service contract, material pricing, business roles, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-534
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear maestro de materiales para el reconocimiento universal de ingresos (7R8) (7R8_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear maestro de materiales para el reconocimiento universal de ingresos (7R8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894874)

[2 Requisitos previos 3](#_Toc233894875)

[2.1 Acceso al sistema 3](#_Toc233894876)

[2.2 Roles 3](#_Toc233894877)

[2.3 Unidades organizativas necesarias 3](#_Toc233894878)

[3 Tabla de resumen 5](#_Toc233894879)

[4 Crear datos maestros de material para escenario de integración de venta contra almacén (SFS) 6](#_Toc233894880)

[4.1 Mercaderías: URR_MAT1_NORM 6](#_Toc233894881)

[4.2 Producto de servicio para servicio único: URR_MAT1_SERV 9](#_Toc233894882)

[5 Crear datos maestros de material para escenario de integración de proyecto de cliente de precio fijo 11](#_Toc233894883)

[5.1 URR_FPPRJ_1 11](#_Toc233894884)

[6 Crear datos maestros de material para escenario de integración de contrato de servicio 14](#_Toc233894885)

[6.1 URR_SRVCONT1 14](#_Toc233894886)

[7 Fijar precios para materiales 16](#_Toc233894887)

[7.1 Precio para mercaderías para SFS: URR_MAT1_NORM 16](#_Toc233894888)

[7.2 Precio para producto de servicio para servicio único: URR_MAT1_SERV 18](#_Toc233894889)

[7.3 Precio para material de contrato de servicio: URR_SRVCONT1 20](#_Toc233894890)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este documento proporciona una guía sobre cómo crear registros de datos maestros de material, incluidos los precios para diferentes escenarios de integración de reconocimiento universal de ingresos (URR): URR integrado con venta contra almacén, URR integrado con proyectos de servicio al cliente y URR integrado con contrato de servicio.

La guía incluye la descripción de segmentos de datos que son relevantes para que los datos maestros trabajen en un proceso URR y campos que deben rellenarse con valores de entrada en los segmentos de datos. Los segmentos de datos y los campos que no son relevantes para el alcance no se describen en este documento, aunque pueden aparecer en la IU.

Los datos maestros de material que se crean como se describe aquí se pueden utilizar para procesos URR:

| ID de maestro de materiales | Descripción | Utilización |
| --- | --- | --- |
| URR_MAT1_NORM | Material de prueba URR 1 NORM | Este material se utiliza en el escenario de integración Venta contra almacén URR |
| URR_MAT2_NORM | Material de prueba URR 2 NORM | Este material se utiliza en el escenario de integración Venta contra almacén URR |
| URR_MAT1_SERV | Material de test URR 1 TAD | Este material se utiliza en el escenario de integración Venta contra almacén URR |
| URR_FPPRJ_1 | URR Proy. cliente de precio fijo de material de prueba | Este material se utiliza en el escenario de integración de proyecto de cliente URR |
| URR_SRVCONT1 | Contrato de servicio de material de prueba URR | Este material se utiliza en el escenario de integración Contrato de servicio URR |

## Requisitos previos

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
| Especialista en determinación de precios | SAP_BR_PRICING_SPECIALIST | Gestión de precios | SAP_BR_PRICING_SPECIALIST |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Unidad organizativa a utilizar para DE | Unidad organizativa que se utilizará para EE. UU. |
| --- | --- | --- | --- |
| Crear material | Centro | 1010 (Centro 1 DE) | 1710 (Centro 1 US) |
| Crear material | Organización de ventas | 1010 (Org.ventas nac.DE) | 1710 (Org.ventas nac.US) |
| Crear material | Canal de distribución | 10 (Ventas directas) | 10 (Ventas directas) |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

Tabla 1: Crear datos maestros de material para escenario de integración de venta contra almacén (SFS)

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Mercaderías: URR_MAT1_NORM](#unique_6) [página ] 6 | Especialista en datos maestros - Datos de producto | Crear material |  |
| [Producto de servicio para servicio único: URR_MAT1_SERV](#unique_7) [página ] 9 | Especialista en datos maestros - Datos de producto | Crear material |  |

Tabla 2: Crear datos maestros de material para integración de proyecto de cliente de precio fijo Escenario

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [URR_FPPRJ_1](#unique_8) [página ] 11 | Especialista en datos maestros - Datos de producto | Crear material |  |

Tabla 3: Crear datos maestros de material para el escenario de integración de contrato de servicio

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [URR_SRVCONT1](#unique_9) [página ] 14 | Especialista en datos maestros - Datos de producto | Crear material |  |

Tabla 4: Crear datos maestros de material para escenario de integración de contrato de servicio

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Precio para mercaderías para SFS: URR_MAT1_NORM](#unique_10) [página ] 16 | Especialista en determinación de precios | Fijar precios de material |  |
| [Precio para producto de servicio para servicio único: URR_MAT1_SERV](#unique_11) [página ] 18 | Especialista en determinación de precios | Fijar precios de material |  |
| [Precio para material de contrato de servicio: URR_SRVCONT1](#unique_12) [página ] 20 | Especialista en determinación de precios | Fijar precios de material |  |

## Crear datos maestros de material para escenario de integración de venta contra almacén (SFS)

### Mercaderías: URR_MAT1_NORM

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar APP Crear material l (si la aplicación no está disponible en la pantalla puede intentar buscar la aplicación Crear material). | Se visualiza Crear material (pantalla inicial). |  |
| 3 | Introducir número de material y tipo de material | En la pantalla Create Material (Initial Screen), efectúe las entradas siguientes:Número de producto : URR_MAT1_NORMTipo de material : MercaderíasA continuación, seleccione Continuar (Intro). | Ha introducido el número de material y el tipo de material para los nuevos datos maestros de material.Se muestra la ventana de diálogo Seleccionar vista(s). |  |
| 4 | Seleccionar vistas | En la ventana de diálogo Seleccionar vista(s), seleccione las siguientes vistas:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroContabilidad1A continuación, seleccione Continuar (Intro). | Se muestra la ventana de diálogo Niveles de organización. |  |
| 5 | Seleccionar niveles de organización | En la ventana Niveles de organización, actualice los siguientes valores:Centro: 1010 (centro 1 DE)Org.ventas: 1010 (Org.ventas nac.DE)Canal distrib.: 10 (venta directa)A continuación, seleccione Continuar (Intro). | Se han seleccionado datos organizativos.Se muestra la vista Datos básicos 1. |  |
| 6 | Actualizar vista: Datos básicos 1 | En la vista Datos básicos 1, actualice los siguientes valores:Descr.: Material de test URR 1 NORMUnidad de medida base: UN (unidad)Grupo de materiales: L001 (materiales de venta)GenItemGroup: NORM (posición estándar)Peso bruto: 1Peso neto: 1Unidad de peso: KGVolumen: 1Unidad de volumen: M3A continuación, pulse Intro. | Se actualizan los datos básicos.Después de pulsar Intro, se visualiza la vista Ventas: organización de ventas 1. |  |
| 7 | Actualizar vista: Ventas: Org.ventas 1 | En la vista Ventas: organización de ventas 1, actualice los siguientes valores:Datos generalesDescuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 0A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 1. Se visualiza la vista Ventas: organización de ventas 2. |  |
| 8 | Actualizar vista: Ventas: Org.ventas 2 | En la vista Sales: sales org. 2, actualice la siguiente entrada:Tp.pos.genér. Grupo: NORM (posición estándar)Grupo de tipos de posición: NORM (posición estándar)A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 2. Se visualiza la vista Ventas: General/Centro. |  |
| 9 | Actualizar vista: Ventas: General/Centro | En la vista Ventas: General/Centro, actualice los siguientes valores:Unidad de medida base: UN (unidad)Peso bruto: 1 kgPeso neto: 1Verificación de disponibilidad: NCGpo.trans.: 0001Grupo de carga: 0001Centro de beneficio: Y1041A continuación, seleccione Intro. | Se actualizan los datos generales de ventas. Se muestra la vista Contabilidad 1. |  |
| 10 | Actualizar vista: Contabilidad 1 | En la vista Contabilidad 1, en la sección Período actual, realice la siguiente entrada:Unidad de medida base: UNClase de valoración: 3100Precio estándar: 16Precio por unidad: 16Unidad de precio: 1Control de precio: VPrecio futuro: vacíoA continuación, seleccione Grabar. | Se actualizan los datos de contabilidad.Se graban los datos maestros de material. |  |
| 11 | Crear más datos maestros de material para realizar pruebas si es necesario | Crear más maestro de materiales siguiendo la convención para fijar nombres URR_MAT*_NORM (por ejemplo: URR_MAT2_NORM, URR_MAT3_NORM, etc.) con diferente precio estándar. | Se crean más datos maestros de material de prueba. | Para CE 2502, URR_MAT1_NORM y URR_MAT2_NORM se suministran como datos de demostración, por lo que el usuario no necesita crearlos manualmente.Si se requieren más datos maestros de material para la prueba del escenario de integración de venta contra almacén, siga los pasos de esta sección para crear más materiales. |

### Producto de servicio para servicio único: URR_MAT1_SERV

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione APP Crear material (si la aplicación no está disponible en la pantalla, puede intentar buscar la aplicación Crear material). | Se visualiza Crear material (pantalla inicial). |  |
| 3 | Introducir número de material y tipo de material | En la pantalla Create Material (Initial Screen), efectúe las entradas siguientes:Número de producto: URR_MAT1_SERVTipo de material: Producto de servicioA continuación, seleccione Continuar (Intro). | Ha introducido el número de material y el tipo de material para los nuevos datos maestros de material.Se muestra la ventana de diálogo Seleccionar vista(s). |  |
| 4 | Seleccionar vistas | En la ventana de diálogo Seleccionar vista(s), seleccione las siguientes vistas:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroContabilidad1A continuación, seleccione Continuar (Intro). | Se muestra la ventana de diálogo Niveles de organización. |  |
| 5 | Seleccionar niveles de organización | En la ventana Niveles de organización, actualice los siguientes valores:Centro: 1010 (centro 1 DE)Org.ventas: 1010 (Org.ventas nac.DE)Canal distrib.: 10 (venta directa)A continuación, seleccione Continuar (Intro). | Se han seleccionado datos organizativos.Se muestra la vista Datos básicos 1. |  |
| 6 | Actualizar vista: Datos básicos 1 | En la vista Datos básicos 1, actualice los siguientes valores:Descr.: URR Test Material1 SERVUnidad de medida base: H (horas)Grupo de materiales: YBMM01 (materiales no de almacén con ID)Gr.pos.gen.: SERV (servicio)A continuación, pulse Intro. | Se actualizan los datos básicos.Después de pulsar Intro, se visualiza la vista Ventas: organización de ventas 1. |  |
| 7 | Actualizar vista: Ventas: Org.ventas 1 | En la vista Ventas: organización de ventas 1, actualice los siguientes valores:Datos generalesCentro suministrador: 1010Descuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 0A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 1. Se visualiza la vista Ventas: organización de ventas 2. |  |
| 8 | Actualizar vista: Ventas: Org.ventas 2 | En la vista Sales: sales org. 2, actualice la siguiente entrada:Gr.tp.pos.gral.: SERV(servicio)Grupo de tipos de posición: SERV(Servicio)A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 2. Se visualiza la vista Ventas: General/Centro. |  |
| 9 | Actualizar vista: Ventas: General/Centro | En la vista Ventas: General/Centro, actualice los siguientes valores:Centro de beneficio: YB600A continuación, seleccione Intro. | Se actualizan los datos generales de ventas. Se muestra la vista Contabilidad 1. |  |
| 10 | Actualizar vista: Contabilidad 1 | En la vista Contabilidad 1, en la sección Período actual, realice la siguiente entrada:Clase de valoración: 3300Precio estándar: 20Unidad de precio: 1A continuación, seleccione Grabar. | Se actualizan los datos de contabilidad.Se graban los datos maestros de material. |  |

## Crear datos maestros de material para escenario de integración de proyecto de cliente de precio fijo

### URR_FPPRJ_1

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione APP Crear material (si la aplicación no está disponible en la pantalla, puede intentar buscar la aplicación Crear material). | Se visualiza Crear material (pantalla inicial). |  |
| 3 | Introducir número de material y tipo de material | En la pantalla Create Material (Initial Screen), efectúe las entradas siguientes:Número de producto: URR_FPPRJ_1Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro). | Ha introducido el número de material y el tipo de material para los nuevos datos maestros de material.Se muestra la ventana de diálogo Seleccionar vista(s). |  |
| 4 | Seleccionar vistas | En la ventana de diálogo Seleccionar vista(s), seleccione las siguientes vistas:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroContabilidad1A continuación, seleccione Continuar (Intro). | Se muestra la ventana de diálogo Niveles de organización. |  |
| 5 | Seleccionar niveles de organización | En la ventana Niveles de organización, actualice los siguientes valores:Centro: 1010 (centro 1 DE)Org.ventas: 1010 (Org.ventas nac.DE)Canal distrib.: 10 (venta directa)A continuación, seleccione Continuar (Intro). | Se han seleccionado datos organizativos.Se muestra la vista Datos básicos 1. |  |
| 6 | Actualizar vista: Datos básicos 1 | En la vista Datos básicos 1, actualice los siguientes valores:Descr.: URR Test Material1 SERVUnidad de medida base: AU (unidad de actividad)Grupo de materiales: P000 (clase de pedido abierto)Gr.pos.gen.: PSFP (pos.precio fijo)A continuación, pulse Intro. | Se actualizan los datos básicos.Después de pulsar Intro, se visualiza la vista Ventas: organización de ventas 1. |  |
| 7 | Actualizar vista: Ventas: Org.ventas 1 | En la vista Ventas: organización de ventas 1, actualice los siguientes valores:Datos generalesCentro suministrador: 1010Descuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 0A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 1. Se visualiza la vista Ventas: organización de ventas 2. |  |
| 8 | Actualizar vista: Ventas: Org.ventas 2 | En la vista Sales: sales org. 2, actualice la siguiente entrada:Tp.pos.genér. Grupo: PSFP (posición de precio fijo)Mat.grupo imputación: Y1 (precio fijo)Grupo de tipos de posición: PSFP (posición de precio fijo)A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 2. Se visualiza la vista Ventas: General/Centro. |  |
| 9 | Actualizar vista: Ventas: General/Centro | En la vista Ventas: General/Centro, actualice los siguientes valores:Centro de beneficio: YB101A continuación, seleccione Intro. | Se actualizan los datos generales de ventas. Se muestra la vista Contabilidad 1. |  |
| 10 | Actualizar vista: Contabilidad 1 | En la vista Contabilidad 1, en la sección Período actual, realice la siguiente entrada:Clase de valoración: 3300Precio estándar: 30Unidad de precio: 1A continuación, seleccione Grabar. | Se actualizan los datos de contabilidad.Se graban los datos maestros de material. |  |
| 11 | Crear más datos maestros de material para realizar pruebas si es necesario | Crear más maestro de materiales con convención para fijar nombres URR_FPPRJ* (por ejemplo: URR_FPPRJ3, URR_FPPRJ4, etc.) con un precio estándar diferente si es necesario. | Se crean más datos maestros de material de prueba. |  |

## Crear datos maestros de material para escenario de integración de contrato de servicio

### URR_SRVCONT1

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione APP Crear material (si la aplicación no está disponible en la pantalla, puede intentar buscar la aplicación Crear material). | Se visualiza Crear material (pantalla inicial). |  |
| 3 | Introducir número de material y tipo de material | En la pantalla Create Material (Initial Screen), efectúe las entradas siguientes:Número de producto: URR_SRVCON1Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro). | Ha introducido el número de material y el tipo de material para los nuevos datos maestros de material.Se muestra la ventana de diálogo Seleccionar vista(s). |  |
| 4 | Seleccionar vistas | En la ventana de diálogo Seleccionar vista(s), seleccione las siguientes vistas:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2Ventas: Datos generales/de centroComprasA continuación, seleccione Continuar (Intro). | Se muestra la ventana de diálogo Niveles de organización. |  |
| 5 | Seleccionar niveles de organización | En la ventana Niveles de organización, actualice los siguientes valores:Centro: 1010 (centro 1 DE)Org.ventas: 1010 (Org.ventas nac.DE)Canal distrib.: 10 (venta directa)A continuación, seleccione Continuar (Intro). | Se han seleccionado datos organizativos.Se muestra la vista Datos básicos 1. |  |
| 6 | Actualizar vista: Datos básicos 1 | En la vista Datos básicos 1, actualice los siguientes valores:Descr.: Material de test URR 1 contrato de servicioUnidad de medida base: AU (unidad de actividad)Grupo de materiales: P001 (servicios)Gr.pos.gen.: SCNP (serv. Prod.contrato)A continuación, pulse Intro. | Se actualizan los datos básicos.Después de pulsar Intro, se visualiza la vista Ventas: organización de ventas 1. |  |
| 7 | Actualizar vista: Ventas: Org.ventas 1 | En la vista Ventas: organización de ventas 1, actualice los siguientes valores:Datos generalesUnidad de medida base: AU (unidad de actividad)Grupo de materiales: P001 (servicios)A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 1. Se visualiza la vista Ventas: organización de ventas 2. |  |
| 8 | Actualizar vista: Ventas: Org.ventas 2 | En la vista Sales: sales org. 2, actualice la siguiente entrada:Tp.pos.genér. SCNP grupo (serv. Prod.contrato)A continuación, seleccione Intro. | Se actualizan los datos organizativos de ventas 2. Se visualiza la vista Ventas: General/Centro. |  |
| 9 | Actualizar vista: Ventas: General/Centro | En la vista Ventas: General/Centro, actualice los siguientes valores:Unidad de medida base: AU (unidad de actividad)A continuación, seleccione Intro. | Se actualizan los datos generales de ventas. Se muestra la vista Contabilidad 1. |  |
| 10 | Actualizar vista: Compras | En la vista Compras, realice la siguiente entrada:Unidad de medida base: AU (unidad de actividad)Grupo de materiales: P001 (servicios)A continuación, seleccione Grabar. | Se actualizan los datos de contabilidad.Se graban los datos maestros de material. |  |

## Fijar precios para materiales

### Precio para mercaderías para SFS: URR_MAT1_NORM

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas (VK12) . | Se visualiza la vista Modificar registros de condición. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición introduzca la siguiente información:Clase de condición : PPR0A continuación, haga clic en Intro . | Se visualiza la vista Combinación de claves. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione la vista Material con status de liberación opción.A continuación, haga clic en Seleccionar . | Se visualiza la vista Modificar precio (PPR0): Selección. |  |
| 5 | Selección | En la Modificar precio (PPR0): Selección , actualice la siguiente información:Organización de ventas: 1010 (nac. Org.ventas DE)Canal de distribución: 10 (Ventas directas)Material: URR_MAT1_NORMVálido el: <Fecha>, por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Se visualiza la vista Modificar condición de precio (PPR0): Resumen. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen , actualice los siguientes datos para el material:Material: URR_MAT1_NORMImporte: por ejemplo, 25,00Unidad: EURInicio de validez: <Fecha>, por ejemplo, la fecha de hoyHaga clic en Intro . | Se han actualizado las condiciones de precio. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios. |  |
| 8 | Volver y acceder a la aplicación de nuevo | En la Modificar registros de condición introduzca la siguiente información:Clase de condición : PSAMA continuación, seleccione Intro . | Se visualiza la vista Combinación de claves. |  |
| 9 | Combinación de claves | En la Combinación de claves seleccione la opción Material con estado de liberación.A continuación, seleccione Intro . | Se visualiza la vista Modificar precio (PSAM): Selección. |  |
| 10 | Selección | En la vista Modificar precio (PSAM): Selección, actualice la siguiente información:Organización de ventas: 1010 (nac. Org.ventas DE)Canal de distribución: 10 (Ventas directas)Material: URR_MAT1_NORMVálido el: <Fecha>, por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Se visualiza la vista Modificar condición de precio (PSAM): Resumen. |  |
| 11 | Modificar condición de precio | En la Modificar condición de precio (PSAM): Resumen , actualice los siguientes datos para el material:Material: URR_MAT1_NORMImporte: por ejemplo, 35,00Unidad: EURInicio de validez: <Fecha>, por ejemplo, la fecha de hoySeleccionar Intro . | Se han actualizado las condiciones de precio. |  |
| 12 | Grabar | Seleccionar Grabar . | Se ha definido el precio. |  |

### Precio para producto de servicio para servicio único: URR_MAT1_SERV

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas (VK12) . | Se visualiza la vista Modificar registros de condición. |  |
| 3 | Tipo de condición de determinación de precios | En la vista Modificar registros de condición, introduzca la siguiente información:Clase de condición: PPR0A continuación, seleccione Intro . | Se visualiza la vista Combinación de claves. |  |
| 4 | Combinación de claves | En la vista Combinación de claves, seleccione la opción Material con estado de liberación.A continuación, seleccione Seleccionar (Intro). | Se visualiza la vista Modificar precio (PPR0): Selección. |  |
| 5 | Selección | En la vista Modificar precio (PPR0): Selección, actualice la siguiente información:Organización de ventas: 1010 (nac. Org.ventas DE)Canal de distribución: 10 (Ventas directas)Material: URR_MAT1_SERVVálido el: <Fecha>, por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Se visualiza la vista Modificar condición de precio (PPR0): Resumen. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PPR0): Resumen , actualice los siguientes datos para el material:Material: URR_MAT1_SERVImporte: por ejemplo, 25,00Unidad: EURInicio de validez: <Fecha>, por ejemplo, la fecha de hoySeleccionar Intro . | Se han actualizado las condiciones de precio para los productos de servicio SRV_01. |  |
| 7 | Grabar | Seleccionar Grabar . | Se han definido los precios de los productos de servicio. |  |
| 8 | Volver y acceder a la aplicación de nuevo | En la Modificar registros de condición introduzca la siguiente información:Clase de condición: PSAMA continuación, seleccione Intro . |  |  |
| 9 | Combinación de claves | En la Combinación de claves seleccione la opción Material con estado de liberación.A continuación, seleccione Intro . | Se visualiza la vista Modificar precio (PSAM): Selección. |  |
| 10 | Selección | En la vista Modificar precio (PSAM): Selección, actualice la siguiente información:Organización de ventas: 1010 (nac. Org.ventas DE)Canal de distribución: 10 (Ventas directas)Material: URR_MAT1_SERVVálido el: <Fecha>, por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Se visualiza la vista Modificar condición de precio (PSAM): Resumen. |  |
| 11 | Modificar condición de precio | En la Modificar condición de precio (PSAM): Resumen , actualice los siguientes datos para el material:Material: URR_MAT1_SERVImporte: por ejemplo, 35,00Unidad: EURInicio de validez: <Fecha>, por ejemplo, la fecha de hoySeleccionar Intro . | Se han actualizado las condiciones de precio para los productos de servicio SRV_01. |  |
| 12 | Grabar | Seleccionar Grabar . | Se ha definido el precio. |  |

### Precio para material de contrato de servicio: URR_SRVCONT1

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en determinación de precios . | Se abre la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Fijar precios de material - Ventas (VK12) . | Se visualiza la vista Modificar registros de condición. |  |
| 3 | Tipo de condición de determinación de precios | En la Modificar registros de condición introduzca la siguiente información:Clase de condición : PSI1A continuación, seleccione Intro . | Se visualiza la vista Combinación de claves. |  |
| 4 | Combinación de claves | En la Combinación de claves , seleccione Material.A continuación, seleccione Intro . | Se visualiza la vista Modificar precio (PSI1): Selección. |  |
| 5 | Selección | En la Modificar precio (PSI1): Selección , actualice la siguiente información:Organización de ventas: 1010 (Org.ventas nac.DE)Canal de distribución: 10 (Ventas directas)Material: URR_SRVCONT1Válido el: <Fecha>, por ejemplo, la fecha de hoyA continuación, seleccione Ejecutar . | Se visualiza la vista Modificar condición de precio (PSI1): Resumen. |  |
| 6 | Modificar condición de precio | En la Modificar condición de precio (PSI1): Resumen , actualice los siguientes datos:Material : URR_SRVCONT1Cantidad : por ejemplo, 90,00Unidad : por ejemplo, EURInicio de validez : <Fecha>, por ejemplo, la fecha de hoySeleccionar Intro . | Se actualizan las condiciones de precio. |  |
| 7 | Grabar | Seleccionar Grabar . | Se ha definido el precio. |  |

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
> Flagged while digesting this document, not verified: Document mentions CE 2502 demo data although it is the 2608 release; step 3 of service contract uses product number URR_SRVCON1 while the rest uses URR_SRVCONT1

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]
- related-to :: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 36,351 chars in the whole document
