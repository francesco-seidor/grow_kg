---
id: 09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc
title: Script de datos maestros - Creación de facturación convergente de productos de suscripción (5LP) (5LP_S4CLD2608_Master_Data_ES_XX)
description: "Spanish master data script (5LP, S/4HANA Cloud Public Edition 2608): create business partner, contract account, subscription products, price tables and extend SBPD/SBRE products."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_ES_XX]
keywords: [Subscription Products and Rate Plans, subscription products, business partner, contract accounts, rate elements, rate plan templates, price calculation, lookup tables, product master extension, subscription billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-450
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de facturación convergente de productos de suscripción (5LP) (5LP_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de facturación convergente de productos de suscripción - MDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894747)

[2 Requisitos previos 3](#_Toc233894748)

[2.1 Acceso al sistema 3](#_Toc233894749)

[2.2 Roles 3](#_Toc233894750)

[2.3 Unidades organizativas necesarias (SAP S/4HANA) 3](#_Toc233894751)

[3 Tabla de resumen 5](#_Toc233894752)

[4 Procedimientos 6](#_Toc233894753)

[4.1 Crear interlocutor comercial 6](#_Toc233894754)

[4.1.1 Crear datos maestros de cliente 7](#_Toc233894755)

[4.1.2 Crear una cuenta de contrato 9](#_Toc233894756)

[4.2 Crear producto de suscripción (SAP Subscription Billing) 11](#_Toc233894757)

[4.2.1 Crear elementos de tarifa 11](#_Toc233894758)

[4.2.2 Crear plantilla para planes de tarifa 12](#_Toc233894759)

[4.2.3 Crear producto (SAP Subscription Billing) 14](#_Toc233894760)

[4.2.4 Crear un producto para servicios de cálculo de precios 16](#_Toc233894761)

[4.2.5 Carga de tablas de búsqueda para la determinación de precios 19](#_Toc233894762)

[4.3 Enriquecer productos de facturación de suscripciones 23](#_Toc233894763)

[4.3.1 Ampliar producto de suscripción del tipo SBPD 23](#_Toc233894764)

[4.3.2 Ampliar productos de suscripción del tipo SBRE 26](#_Toc233894765)

[5 Apéndice 31](#_Toc233894766)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, encontrará una descripción de cómo crear un maestro de productos de suscripción datos. La descripción incluye los segmentos de datos que son relevantes para los datos maestros para trabajar en un entorno de sistema "habitual". Aquí, el lector aprende principalmente sobre los datos segmentos y campos que deben rellenarse con valores de entrada. Campos que no son relevantes para el alcance no se describen en este documento, aunque pueden aparecer en la IU.

Un registro maestro de suscripción que se crea según este documento se puede utilizar para facturación de suscripciones.

| ID de producto de suscripción | Descripción | Utilización |
| --- | --- | --- |
| P-CLOUD_COMM | Producto de suscripción | Representa el producto de suscripción |
| P-CLOUD_SUPPORT | Producto de suscripción | Representa el producto de suscripción |

## Requisitos previos

### Acceso al sistema

La siguiente tabla trata los requisitos de acceso al sistema.

| Sistema | Detalles |
| --- | --- |
| Sistema SAP S/4HANA | Accesible a través de la rampa de lanzamiento SAP Fiori.El administrador del sistema le proporciona la URL para acceder a varias aplicaciones asignadas a su rol. |
| SAP Subscription Billing | Accesible mediante URL.El administrador del sistema le proporciona la URL para acceder a aplicación. |

### Roles

Puede crear roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de test individuales.

SAP S/4HANA

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Datos maestros Especialista - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST |  |
| Contable de acreedores y deudores (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contable de acreedores y deudores (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

Debe ponerse en contacto con el administrador del sistema para configurar el autorizaciones.

### Unidades organizativas necesarias (SAP S/4HANA)

Mientras que algunos segmentos de datos maestros dependen de las unidades organizativas de empresa, los datos generales (centrales) no dependen de una unidad organizativa o la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Unidad organizativa a utilizar | Comentarios |
| --- | --- | --- | --- |
| Crear registro de datos maestros | Organización de ventas | 1710 (Org.ventas nac.US) | Para Alemania, utilice 1010 (Org. Org.ventas DE) |
| Crear registro de datos maestros | Canal de distribución | 10 (Ventas directas) |  |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear producto de suscripción (suscripción de SAP) Facturación) | N/D | N/D | Se han creado los productos de suscripción. |
| Enriquecer productos de suscripción (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Gestionar datos maestros de producto | Se han creado los productos de suscripción. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear interlocutor comercial

Contexto

En esta actividad se crea un interlocutor comercial para un nuevo cliente FI-CA en S/4HANA Cloud.

Procedimiento

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como contable de acreedores y deudores (FI-CA). | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial Se muestra la vista. |  |
| 3 | Crear un interlocutor comercial | Seleccionar Persona o seleccionar Más > Interlocutor comercial > Crear > Persona . | El Crear persona Se muestra la vista. |  |
| 4 | Seleccionar el rol IC | Realice la siguiente entrada:Crear en rol IC : Parte contratante | El Cambiar a otro rol IC la vista se visualiza en Crear modo. |  |
| 5 | Crear | Seleccionar Crear | Seleccionar Rol de parte contratante en la Crear Persona ventana de diálogo.Parte contratante (nueva) está seleccionado para Crear en rol IC . |  |
| 6 | Introducir datos básicos | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID específico> , por ejemplo, BP_US_97Agrupación : Numeración alfanumérica externa |  |  |
| 7 | Introducir datos de dirección | Realice la siguiente entrada en Dirección pestaña:Nombre/Apellido : John/MillerCalle/Número : Hillview Ave/3410Código postal/Población : 94304/PALO ALTOPaís : EE. UU.Región : CCDomicilio fiscal : CA00000000Consejo Si Domicilio fiscal no es visible, haga clic en + para expandir la opciones. |  |  |
| 8 | Actualizar datos de pago | Añada los datos bancarios mediante la Gestionar socio comercial aplicación y Registrar tarjeta de pago mediante Gestionar Datos maestros de interlocutor comercial aplicación.Realice la siguiente entrada en el campo Pago Transacciones pestaña:En Datos bancarios introduzca:ID : 01País : EE. UU.Clave de banco : 011000390Cta.banc. : <Banco Cuenta>Código SWIFT (SWIFT/BIC) : CIUDAD 33XXXSeleccionar Enviar . | El Verificación de clave de reconciliación Aparece la vista. |  |
| 9 | Grabar | Seleccionar Grabar . | Se crea un nuevo interlocutor comercial. |  |

#### Crear datos maestros de cliente

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

En esta actividad se amplía un interlocutor comercial FI-CA con el rol IC. FLCU01 y MKK con datos maestros de área de ventas.

Procedimientos

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Fiori Launchpad con sus credenciales de usuario como SAP_BR_APR_ACCOUNTANT_FICA | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Seleccionar interlocutor comercial | Introduzca el Interlocutor comercial número |  |  |
| 4 | Abrir interlocutor comercial | Seleccionar Intro |  |  |
| 5 | Cambiar a modo de modificación | Seleccionar Cambiar entre visualizar y modificar |  |  |
| 6 | Modificación en rol IC | En la Modificación en rol IC seleccione el campo valor siguiente: ClienteLa clave técnica de este rol de socio comercial es FLCU01 . |  |  |
| 7 | Información de entrada para dirección | Idioma de correspondencia: <EN> |  |  |
| 8 | Abrir área de ventas | Seleccionar Comercial en la parte superior de la vista. | El Área de ventas Se muestra la vista. |  |
| 9 | Introducir datos de área de ventas | Indique los siguientes datos:Org.ventas : 1710Canal distrib. : 10Sector : 00Seleccionar Intro y luego Grabar .Nota Las tres entradas anteriores forman el área de ventas. En muchos casos, las ventas fija el Objetivo para el procesamiento de ventas, por ejemplo, dentro de la pedido de cliente o determinación de precios. | Las modificaciones se guardan para el socio comercial. |  |
| 10 | Introducir datos de expedición | El Expedición ficha en el Expedición introduzca lo siguiente datos:Centro suministrador : 1710 |  |  |
| 11 | Introducir datos fiscales | El Facturación en la pestaña Salida Impuesto introduzca los siguientes datos:Clasificación fiscal : <1>Por ejemplo, el valor <1> significa que este cliente está totalmente sujeto a impuestos. |  |  |
| 12 | Guardar los datos | Guarde las entradas. |  |  |
| 13 | Modificación en rol IC | En la Modificación en rol IC seleccione el campo valor siguiente: Parte contratanteLa clave técnica de este rol de socio comercial es MKK . |  |  |
| 14 | Información de entrada para dirección | Idioma de correspondencia: <EN> |  |  |
| 15 | Introducir datos de expedición | El Expedición en la etiqueta Expedición introduzca los siguientes datos:Centro suministrador : 1710 |  |  |
| 16 | Introducir datos fiscales | El Facturación en la etiqueta Salida Impuesto introduzca los siguientes datos:Clasificación fiscal : <1>Por ejemplo, el valor <1> significa que este cliente está totalmente sujeto a impuestos. |  |  |
| 17 | Guardar los datos | Guarde las entradas. |  |  |

#### Crear una cuenta de contrato

Contexto

En esta actividad se crean datos maestros de cuenta contrato para un cliente FI-CA en SAP S/4HANA Cloud Public Edición .

Procedimiento

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario con el rol empresarial Contable de acreedores y deudores (FI-CA). | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar cuenta de contrato (CAA3) . | El Visualización de cuenta contrato: Acceso se visualiza. |  |
| 3 | Crear una cuenta de contrato | Seleccionar Crear o seleccionar Más > Cuenta de contrato > Crear . | El Crear cuenta contrato: Acceso se visualiza. |  |
| 4 | Introducir datos básicos | Realice la siguiente entrada:Cuenta contrato : <Introduzca un ID específico> , por ejemplo, CA_US_97Interlocutor comercial : <Seleccione el número de interlocutor comercial creado en el paso Create a Business Partner>Tp.cta.contr. : Y1Inicio de validez : <Fecha actual> |  |  |
| 5 | Actualizar detalles de cuenta de contrato | Seleccionar Continuar . | El Crear cuenta contrato: Datos generales se visualiza. |  |
| 6 | Introducir datos generales | Realice la siguiente entrada en el campo General pestaña:Nom.cta.contr. : <Nombre de cuenta de contrato>Relación de cuentas : Titular de la cuentaGrupo de tolerancia : Tolerancia Y001 no permitidaGrupo de planificación : Clientes nacionalesCond.pago : YN01ID determ.activ. : Y1 |  |  |
| 7 | Introducir datos de pagos/impuestos | Realice la siguiente entrada en el campo Pagos/Impuestos pestaña:Grupo de sociedades : 1710Sociedad estándar : 1710 |  |  |
| 8 | Introducir reclamación/correspondencia | Realice la siguiente entrada en Reclamación/Correspondencia pestaña:Variante corresp. : <solo impresión, inmediatamente> |  |  |
| 9 | Grabar | Seleccionar Grabar . | Se crea una nueva cuenta de contrato. |  |

### Crear producto de suscripción (SAP Subscription Billing)

#### Crear elementos de tarifa

Objetivo

En esta actividad se crean elementos de tarifa en SAP Subscription Billing. Los ID de tarifa debe corresponderse con los productos S/4HANA relevantes del tipo SBRE :

| ID de tarifa | Tipo de cambio | Descripción |
| --- | --- | --- |
| R-ONETIME | Único | Tasa de activación única |
| R-SEATS | Periódico | Tarifa mensual basada en asientos |
| R-TICKETS | Basado en uso | Tarifa de uso basada en boleto |

Procedimiento

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Elementos de tarifa | Por debajo de Datos maestros y configuración , seleccionar Configuración empresarial > Elementos de tarifa . | El Elementos de tarifa Se muestra la vista. |  |
| 3 | Crear elemento de tarifa: Único | Seleccionar Crear , a continuación, actualice lo siguiente datos:Tipo: ÚnicoID: R-ONETIMEUnidad : Cada EA)Etiqueta : Activación única TasaFuente de datos : NingunoTipo único : Inicial TasaClase de factura : CargoDescripción : Actualice una descripción, para ejemplo , tasa de activación únicaActivo : SeleccionadoSeleccionar Grabar . | Se crea el elemento de tarifa R-Único. |  |
| 4 | Crear elemento de tarifa: R-SEATS | Seleccionar Crear , a continuación, actualice lo siguiente datos:Tipo: PeriódicoID: R-SEATSUnidad : Cada EA)Etiqueta : Basado en asientos mensual TasaFuente de datos : SuscripciónClase de factura : CargoDescripción : Actualice una descripción, para ejemplo , tarifa mensual basada en asientosActivo : SeleccionadoSeleccionar Grabar . | Se creó el elemento de tarifa R-SEATS. |  |
| 5 | Crear elemento de tarifa: R-TICKETS | Seleccionar Crear , a continuación, actualice lo siguiente datos:Tipo: Basado en usoID: R-TICKETSUnidad : Gigabyte (GB)/Cada uno (EA)Etiqueta : Uso basado en ticket TasaFuente de datos : UtilizaciónClase de factura : CargoVariante de determinación de tarifas de uso : AgregadoTipo de ID de recurso técnico: ID de espacio de almacenamiento en la nubeDescripción : Actualice una descripción, para ejemplo , Cargar/Descargar tráfico en GBActivo : SeleccionadoSeleccionar Grabar . | Se creó el elemento de tarifa R-TICKETS. |  |

#### Crear plantilla para planes de tarifa

Objetivo

En esta actividad se crea una plantilla para planes de tarifa en SAP Subscription Billing.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a las plantillas del plan de tarifas | Por debajo de Determinación de precios , abra el Plantillas del plan de tarifas apl. | Se visualizan las plantillas para planes de tarifa disponibles. |  |
| 3 | Crear plantilla para planes de tarifa: ASIENTOS | Seleccionar Crear > Sin esquema de determinación de precios , y actualice los siguientes datos en Información general :Descripción: Plantilla de planificación basada en asientosCiclo de facturación : Valor - Mensual el primer día del mesMoneda: Valor – USD (para versión de país US)Seleccionar Añadir | Se definen los datos básicos para la plantilla. |  |
| 4 | Actualizar gastos/abonos para SEATS | Cree un cargo único en Cargos/abonos sección por seleccionando Añadir > Único . Actualice los siguientes datos:Elemento de tarifa : R-ONETIMEPrecio : Valor - 9,99 USD (para versión de país US)Crear un cargo recurrente en Cargos/abonos sección por seleccionando Añadir > Recurrente > Determinación de precios por porcentaje . Actualice los siguientes datos:Elemento de tarifa : R-SEATSAplicar modificaciones con el siguiente ciclo : SeleccionadoAnticipo de facturación : seleccionadoProrratear primer ciclo : SeleccionadoPrecio por unidad : 1 USDRatio : 100Cree un cargo basado en el uso en Cargos/abonos sección por seleccionando Añadir > Basado en uso > Determinación de precios por bloques . Actualice los siguientes datos:Tasa Elemento : R-TICKETSAplicar modificaciones con el siguiente ciclo : No seleccionadoCantidad incluida : Valor – 1Tamaño de bloque : Valor – 1Precio por bloque : Valor – 1 USD (para país versión US)Seleccionar Grabar y Publicar . | Se crean los cargos/abonos. |  |

#### Crear producto (SAP Subscription Billing)

Objetivo

En esta actividad se crean los productos P-CLOUD_COMM y P-CLOUD_SUPPORT en SAP. Facturación de suscripciones. El ID del producto en SAP Subscription Billing debe corresponden al ID de producto relevante en SAP S/4HANA

Procedimiento

Producto: P-CLOUD_COMM

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Productos | En el Datos maestros y Configuración catálogo, seleccione Configuración empresarial > Productos . | Se visualizan los productos disponibles. |  |
| 3 | Actualizar información general de producto | Seleccionar Crear , a continuación, actualice la los siguientes datos en el Información general Área:Nombre de producto: Comunicación CloudID de producto: P-CLOUD_COMMTipo de suscripción : ComercialCrear suscripciones como pendientes: DesmarcadoVendido electrónicamente: Seleccionado | Se ha actualizado la información general. |  |
| 4 | Actualizar plan de tarifas para producto | En la Planes de tarifas área , seleccionar Crear plan de tarifas desde Modelo.El Crear plan de tarifas vista, actualizar los siguientes datos:Mercado : este de EE. UU. (para versión de país US)Plantilla del plan de tarifas : Plantilla de planificación basada en asientosDescripción : Periódico Plan de tarifas (basado en asientos) | Se actualizó el plan de tarifas del producto. |  |
| 5 | Actualizar condiciones de suscripción | Actualice los siguientes detalles de parámetros de suscripción:Período de vigencia previsto : para ejemplo,12Período de vigencia mínimo : 12Período de renovación : 12Período de revocación : 14 | Se actualizan los términos de la suscripción. |  |
| 6 | Crear producto | El Crear plan de tarifas , seleccione Crear .El Producto , seleccione Grabar .A continuación, seleccione Publicar . | Se crea el producto P-CLOUD_COMM. |  |

Producto: P-CLOUD_SUPPORT

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Productos | En el área de navegación de la izquierda, seleccione Productos . | Se visualizan los productos disponibles. |  |
| 3 | Actualizar información general de producto | Seleccionar Crear , a continuación, actualice la los siguientes datos en el Información general Área:Nombre de producto: Asistencia en la nubeID de producto: P-CLOUD_SUPPORTTipo de suscripción : ComercialCrear suscripciones como pendientes: DesmarcadoVendido electrónicamente: Seleccionado | Se ha actualizado la información general. |  |
| 4 | Actualizar plan de tarifas para producto | En la Planes de tarifas área , seleccionar Crear plan de tarifas desde Modelo.El Crear plan de tarifas vista, actualizar los siguientes datos:Mercado : este de EE. UU. (para versión de país US)Plantilla del plan de tarifas : Plantilla de planificación basada en asientosDescripción : Periódico Plan de tarifas (basado en asientos) | Se actualizó el plan de tarifas del producto. |  |
| 5 | Actualizar condiciones de suscripción | Actualizar detalles de parámetros de suscripción:Período de vigencia previsto : para ejemplo, 12Período de vigencia mínimo : 12Período de renovación : 12Período de revocación : 14 | Se actualizan los términos de la suscripción. |  |
| 6 | Crear producto | El Crear plan de tarifas , seleccione Crear .El Producto , seleccione Grabar .A continuación, seleccione Publicar . | Se crea el producto P-CLOUD_SUPPORT. |  |

#### Crear un producto para servicios de cálculo de precios

Al revisar un caso de uso de muestra, puede utilizar los valores de muestra para crear datos desde cero, o puede utilizar la configuración predefinida que se entrega con cada nuevo arrendatario. Debe ejecutar los siguientes pasos en el cálculo de precios antes de crear un para PCS.

Procedimiento

1. Gestionar catálogo de campos

Si utiliza los datos de muestra, se utiliza un catálogo de campos predefinido en el Gestionar catálogo de campos aplicación. Por lo tanto, no necesita hacer ninguna opciones adicionales aquí. El Gestionar catálogo de campos aplicación le permite crear campos que se utilizarán posteriormente para definir las tablas de búsqueda y propiedades de entrada para especificaciones de elemento de precio.

2. Crear tablas de búsqueda

En la Gestionar tablas de búsqueda aplicación, puede crear una búsqueda tablas asignando un conjunto de campos de entrada a un conjunto de campos de salida. Esta búsqueda las tablas se utilizan en un paso posterior para crear especificaciones de elementos de precio. El el objetivo de este paso es crear las siguientes tablas de búsqueda para una sola vez, tarifas recurrentes y de uso:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Descuento1

Estas tablas forman parte del contenido predefinido. Por lo tanto, no necesita hacer ninguna parametrizaciones adicionales en este paso.

3. Especificaciones del elemento de precio

En la Gestionar especificaciones de elemento de precio defina su configuración de determinación de precios creando especificaciones del elemento de precio. Esto incluye configuración de la lógica de determinación de precios y campos sustituibles:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Descuento1

Estas especificaciones del elemento de precio forman parte del contenido predefinido. Por lo tanto, no es necesario realizar ninguna parametrización adicional en este paso.

4. Esquema de determinación de precios

En la Gestionar esquema de determinación de precios la aplicación, puede crear y actualizar esquemas de precios. Un esquema de determinación de precios es un procedimiento que define el uso y relación de las especificaciones del elemento de precio para un documento con precios calculables determinado. También determina la secuencia para ejecutar estas especificaciones para generar un importe total en un documento con precio fijado.

El esquema de determinación de precios "Inicial" forma parte del contenido predefinido. Por lo tanto, necesita no realice ninguna parametrización adicional en este paso.

5. Crear plantilla para planes de tarifa

| Paso de test # | Nombre de paso de test | Instrucciones | Resultados previstos | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegue a la Plan de tarifas Modelos aplicación | Ir a Determinación de precios > Plantillas del plan de tarifas | Se visualizan las plantillas para planes de tarifa. |  |
| 3 | Seleccionar Crear | Seleccionar Crear - Con determinación de precios Esquema y actualizar los siguientes datos en Información general :Descripción : RPT para Cálculo de precioEtiquetas : PCS (Opcional)Esquema de determinación de precios : InicialCiclo de facturación : Mensualmente el primer día del mesMoneda : USD | Se ha actualizado la información general. |  |
| 4 | Actualizar Cargos/abonos para tarifa elementos | Para una sola vez, seleccione Cargos/Abonos > Añadir > Único e introduzca Tasa Elemento = R-ONETIME .Para recurrente, seleccione Cargos/Abonos > Añadir > Periódico e introduzca Tasa Elemento = R-SEATS .Para el uso, seleccione Cargos/Abonos > Añadir > Uso: Determinación de precios por bloques e introduzca Tasa Elemento = R-TRAFFIC .Seleccionar Grabar y luego Publicar . |  |  |

6. Crear producto

Crea un producto P-CLOUD_STORAGE_PC en SAP Subscription Billing. El ID del producto en SAP Subscription Billing debe corresponderse con el ID de producto relevante en SAP S/4HANA. Puede utilizar la Procedimiento siguiente:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Productos | Por debajo de Datos maestros y Configuración , abra el Productos aplicación. | Se visualizan los productos disponibles. |  |
| 3 | Actualizar información general del producto | Seleccionar Crear y actualizar la los siguientes datos en el General Info área:Nombre de producto : Nube Cálculo de precio de almacenamientoID de producto : P-CLOUD_STORAGE_PCTipo de suscripción : ComercialCrear suscripciones como pendientes : Desmarcado | Se ha actualizado la información general. |  |
| 4 | Actualizar plan de tarifas para producto | El Planes de tarifas , seleccione Crear - Con determinación de precios Esquema .Nota Para obtener más información sobre los productos de cálculo de precios, consulte. [SAP Subscription Billing con Esquemas de precios](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)Navegar a Crear plan de tarifas desde Modelo > Crear plan de tarifas con determinación de precios Esquema y actualice los siguientes datos:Mercado : EE. UU. Este (para versión de país US)Plantilla del plan de tarifas : RPT para determinación de precioDescripción : RPT para Cálculo de precioCiclo de facturación : Mensualmente el primer día del mesSeleccionar Crear . | El plan de tarifas se actualizó para el producto. |  |
| 5 | Actualizar Términos de la suscripción | Actualice los siguientes datos en el Términos de la suscripción área:Período de vigencia previsto : por ejemplo, 12Período de vigencia mínimo : 12Período de renovación : 12Período de revocación : 14 | Se actualizan los términos de la suscripción. |  |
| 6 | Crear producto | El Crear plan de tarifas vista, seleccionar Crear .El Producto , seleccione Grabar .Seleccionar Publicar . | El P-CLOUD_STORAGE_PC se crea el producto. |  |

7. Cargar tablas de búsqueda para determinación de precio

Para obtener más información sobre la carga de tablas de búsqueda, consulte Cargando Tablas de búsqueda para determinación de precio.

Para obtener más información sobre los productos de cálculo de precios, consulte. [SAP Subscription Billing con esquemas de precios](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)

#### Carga de tablas de búsqueda para la determinación de precios

Puede cargar sus tablas de búsqueda para tarifas únicas, recurrentes y basadas en el uso y para el descuento, utilizando el siguiente procedimiento. Los datos de la siguiente tabla se utilizan para buscar los precios relevantes durante la determinación de precios como parte del proceso de valoración.

Tabla 1: Cargar tabla única

| Paso de test # | Nombre de paso de test | Instrucciones | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Iniciar sesión en SAP Price Calculation | El Inicio Aparece la página. |  |
| 2 | Navegar a Plantillas del plan de tarifas | Por debajo de Gestión de datos maestros , abra el Gestionar datos de tabla de búsqueda aplicación. | Se visualizan las tablas de búsqueda. |  |
| 3 | Seleccionar OneTimePrice | Seleccione la tabla de búsqueda OneTimePrice .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:productCode : P-CLOUD_STORAGE_PCID de mercado : A1rateElement : R-ONETIMEprecio : Individualprice (tipo de precio) : Fijoprice (Valor) : 5000price (moneda de valor) : USD |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda OneTimePrice y ir a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar . | La tabla de búsqueda OneTimePrice se ha actualizado. |  |

Tabla 2: Cargar tabla periódica

| Paso de test # | Nombre de paso de test | Instrucciones | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Iniciar sesión en SAP Price Calculation | El Inicio Aparece la página. |  |
| 2 | Navegar a Plantillas del plan de tarifas | Por debajo de Gestión de datos maestros , abra el Gestionar datos de tabla de búsqueda aplicación. | Se visualizan las tablas de búsqueda. |  |
| 3 | Seleccione RecurringPrice | Seleccione la tabla de búsqueda RecurringPrice .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:productCode : P-CLOUD_STORAGE_PCID de mercado : A1rateElement : R-SEATSprecio : Individualprice (tipo de precio) : Linealprice (Valor) : 50price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : UN |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda RecurringPrice y ir a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar . | La tabla de búsqueda RecurringPrice se ha actualizado. |  |

Tabla 3: Cargar tabla de utilización

| Paso de test # | Nombre de paso de test | Instrucciones | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Iniciar sesión en SAP Price Calculation | El Inicio Aparece la página. |  |
| 2 | Navegar a Plantillas del plan de tarifas | Por debajo de Gestión de datos maestros , abra el Gestionar datos de tabla de búsqueda aplicación. | Se visualizan las tablas de búsqueda. |  |
| 3 | Seleccionar UsagePrice | Seleccione la tabla de búsqueda OneTimePrice .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:productCode : P-CLOUD_STORAGE_PCID de mercado : A1rateElement : R-TRAFFICprecio : Volumenprice (tipo de precio) : LinealLos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa alta:rateSubElement : Altaprice (Rango) : 500price (unidad de intervalo) : EAprice (Valor) : 30price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel:rateSubElement : Altaprice (Rango) : 1000price (unidad de intervalo) : EAprice (Valor) : 25price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel:rateSubElement : Altaprice (Rango) :price (unidad de intervalo) : EAprice (Valor) : 20price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) : 500price (unidad de intervalo) : EAprice (Valor) : 15price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) : 1000price (unidad de intervalo) : EAprice (Valor) : 10price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) :price (unidad de intervalo) : EAprice (Valor) : 5price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EA |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda OneTimePrice y vaya a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar .. | La tabla de búsqueda OneTimePrice se ha actualizado. |  |

Tabla 4: Cargar tabla de descuentos

| Paso de test # | Nombre de paso de test | Instrucciones | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Iniciar sesión en SAP Price Calculation | El Inicio Aparece la página. |  |
| 2 | Navegar a Plantillas del plan de tarifas | Por debajo de Gestión de datos maestros , abra el Gestionar datos de tabla de búsqueda aplicación. | Se visualizan las tablas de búsqueda. |  |
| 3 | Seleccionar Descuento1 | Seleccione la tabla de búsqueda Descuento1 .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:ID de mercado : A1descuento : Individualdescuento (tipo de precio) : Porcentajedescuento (valor) : 0,1 |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda Descuento1 y vaya a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar .. | La tabla de búsqueda Descuento1 se ha actualizado. |  |

### Enriquecer productos de facturación de suscripciones

#### Ampliar producto de suscripción del tipo SBPD

Objetivo

En esta actividad, amplía los productos de suscripción P-CLOUD_COMM y P-CLOUD_SUPPORT en SAP S/4HANA. Estos productos se crean en la suscripción de SAP Facturación y replicada en SAP S/4HANA.

Procedimiento

Producto: P-CLOUD_COMM

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto aplicación aparece. |  |
| 3 | Buscar producto P-CLOUD_COMM | En el área de búsqueda de la parte superior,introduzca el Producto: P-CLOUD_COMM .Pulse el botón Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: Información general | Seleccione el Producto de la lista de informes,Número de producto: P-CLOUD_COMMUnidad base: UNTipo de producto: SBPD (subproducto de facturación)A continuación, seleccione OK .Nota En Descripción proporcionar el Idioma y Producto detalles específicos región, por ejemplo, Idioma : Inglés y Producto : Suscripción Producto de facturación . | El producto debe ser abierto y la información general es actualizado. |  |
| 5 | Actualizar cadenas de distribución: General Información | El Producto vista, en el Área de cadenas de distribución, c seleccione Crear y actualizar lo siguiente datos:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 Ventas directas)Nota La cadena de distribución no es necesaria para el producto SBPD escriba si está utilizando MDI. Solo es necesario si mediante Cloud Integration. | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (impuesto completo):Clasificación fiscal: 6 (impuesto completo (servicios))Las otras entradas son las mismas para ambos países. |
| 6 | Actualizar cadenas de distribución: Agrupación Condiciones | Navegue a la Términos de agrupación área y actualice los siguientes datos:Grupo de tipos de posición : SBPD (Subproducto de facturación)Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto total)A continuación, seleccione Aplicar y, a continuación, crear .Nota El grupo de tipos de posición solo es necesario si está utilizando Integración en la nube y no integración de datos maestros para replicación |  |  |
| 7 | Actualizar centros | Navegue a la Área de centros , seleccione Cree y actualice los siguientes datos:Centro : 1710 (Centro US)A continuación, seleccione Aplicar y luego Grabar | Se actualizan los datos del centro. |  |

Producto: P-CLOUD_SUPPORT

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto aplicación aparece. |  |
| 3 | Buscar producto P-CLOUD_SUPPORT | En el área de búsqueda de la parte superior,introduzca el Producto: P-CLOUD_SUPPORTPulse el botón Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: Información general | Seleccione el Producto de la lista de informes,Número de producto: P-CLOUD_COMMUnidad base: UNTipo de producto: SBPD (subproducto de facturación)A continuación, seleccione OK .Nota En Descripción proporcionar el Idioma y Producto detalles específicos región, por ejemplo, Idioma : Inglés y Producto : Suscripción Producto de facturación . | El producto debe ser abierto y la información general es actualizado. |  |
| 5 | Actualizar cadenas de distribución: General Información | El Producto vista, en el Área de cadenas de distribución, c seleccione Crear y actualizar lo siguiente datos:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 Ventas directas)Nota La cadena de distribución no es necesaria para el producto SBPD escriba si está utilizando la integración de datos maestros. Solo necesario si está utilizando Cloud Integration. | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (impuesto completo):Clasificación fiscal: 6 (impuesto completo (servicios))Las otras entradas son las mismas para ambos países. |
| 6 | Actualizar cadenas de distribución: Agrupación Condiciones | Navegue a la Términos de agrupación área y actualice los siguientes datos:Grupo de tipos de posición : SBPD (Subproducto de facturación)Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto total)A continuación, seleccione Aplicar y, a continuación, crear .Nota La cadena de distribución no es necesaria para el producto SBPD escriba si está utilizando la integración de datos maestros y Solo es necesario si está utilizando Cloud Integración. |  |  |
| 7 | Actualizar centros | Navegue a la Área de centros , seleccione Cree y actualice los siguientes datos:Centro : 1710 (Centro US)A continuación, seleccione Aplicar y luego Grabar | Se actualizan los datos del centro. |  |

#### Ampliar productos de suscripción del tipo SBRE

Objetivo

En esta actividad, amplía los siguientes productos de suscripción en SAP S/4HANA. Estos productos se crean en SAP Subscription Billing y se replican en SAP S/4HANA.

| ID de producto | Tipo de producto | Descripción |
| --- | --- | --- |
| R-ONETIME | SBRE | Tasa de activación única |
| R-SEATS | SBRE | Tasa mensual basada en asientos |
| R-TICKETS | SBRE | Tarifa de uso basada en boleto |

Procedimiento

Producto: R_ONETIME

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto aplicación aparece. |  |
| 3 | Buscar producto R_ONETIME | En el área de búsqueda, introduzca el Producto: R-ONETIMEHaga clic en Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: Información general | El Producto vista, en el Área de cadenas de distribución, c seleccione Crear y actualizar lo siguiente datos:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 Ventas directas)Descuento por pronto pago : SíNota En Descripción proporcionar el Idioma y Producto detalles específicos región, por ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe ser abierto y la información general es actualizado. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (Org.ventas nac.DE)Las otras entradas son las mismas para ambos países. |
| 5 | Actualizar cadenas de distribución: Agrupación Condiciones | Navegue a la Términos de agrupación área y actualice los siguientes datos:Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto total)A continuación, seleccione Aplicar . | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (impuesto completo):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambos países. |
| 6 | Actualizar centros | Navegue a la Centros seleccione Crear y actualizar lo siguiente datos:Centro: 1710 (Centro US)A continuación, seleccione Aplicar y luego Crear . | Se actualizan los datos del centro. |  |

Producto: R_SEATS

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto aplicación aparece. |  |
| 3 | Buscar producto R_SEATS | En el área de búsqueda, introduzca el Producto: R-SEATSHaga clic en Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: Información general | Seleccione el producto de la lista de informes.El Producto ver, haga clic en el Editar .En la Cadenas de distribución área, seleccionar Crear y actualizar la datos siguientes:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 Ventas directas)Nota En Descripción proporcionar el Idioma y Producto detalles específicos región, por ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe ser abierto y la información general es actualizado. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (Org.ventas nac.DE)Las otras entradas son las mismas para ambos países. |
| 5 | Actualizar cadenas de distribución: Agrupación Condiciones | Navegue a la Términos de agrupación área y actualice los siguientes datos:Grupo de tipos de posición : SBRE Sub. Elemento de tarifa de facturación)Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto total)A continuación, seleccione Aplicar. | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (impuesto completo):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambos países. |
| 6 | Actualizar centros | Navegue a la Centros seleccione Crear y actualizar lo siguiente datos:Centro: 1710 (Centro US)A continuación, seleccione Aplicar y Grabar . | Se actualizan los datos del centro. |  |

Producto: R_TICKETS

| Número de paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto aplicación aparece. |  |
| 3 | Buscar producto R_TICKETS | En el área de búsqueda, introduzca el Producto: R-TICKETSHaga clic en Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: Información general | Seleccione el producto de la lista de informes.El Producto ver, haga clic en el Editar .En la Cadenas de distribución área, seleccionar Crear y actualizar la datos siguientes:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 Ventas directas)Nota En Descripción proporcionar el Idioma y Producto detalles específicos región, por ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe ser abierto y la información general es actualizado. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (Org.ventas nac.DE)Las otras entradas son las mismas para ambos países. |
| 5 | Actualizar cadenas de distribución: Agrupación Condiciones | Navegue a la Términos de agrupación área y actualice los siguientes datos:Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto total)A continuación, seleccione Aplicar. | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (impuesto completo):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambos países. |
| 6 | Actualizar centros | Navegue a la Centros seleccione Crear y actualizar lo siguiente datos:Centro: 1710 (Centro US)A continuación, seleccione Aplicar y Grabar . | Se actualizan los datos del centro. |  |

## Apéndice

Tabla 5: Convenciones tipográficas

| Estilo de tipo | Descripción |
| --- | --- |
| Ejemplo | Palabras o caracteres citados desde la pantalla.Estos incluyen nombres de campo, títulos de pantalla, etiquetas de pulsadores, menú nombres, accesos vía menús y opciones de menú.Referencias cruzadas textuales a otros documentos. |
| Ejemplo | Palabras o expresiones destacadas. |
| Ejemplo | Nombres técnicos de objetos de sistema.Estos incluyen nombres de informe, nombres de programa, códigos de transacción, tabla nombres y conceptos clave de un lenguaje de programación cuando son rodeado por texto del cuerpo, por ejemplo, SELECT e INCLUDE. |
| Ejemplo | Salida en la pantalla.Esto incluye nombres de archivos y directorios y sus rutas, mensajes, nombres de variables y parámetros, texto fuente y nombres desactivados herramientas de instalación, actualización y base de datos. |
| Ejemplo | Entrada de usuario exacta.Se trata de palabras o caracteres que se introducen en el sistema exactamente como aparecen en la documentación. |
| <Ejemplo> | Entrada variable de usuario.Los paréntesis angulares indican que reemplaza estas palabras y caracteres con las entradas adecuadas para realizar entradas en el sistema. |
| Ejemplo | Teclas del teclado, por ejemplo, F2 o Intro . |

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
> Flagged while digesting this document, not verified: Inconsistent IDs: rate element R-TICKETS is created but the price calculation plan template and usage lookup use R-TRAFFIC; headings use R_ONETIME/R_SEATS/R_TICKETS vs R-ONETIME.

> [!warning] Conflict
> Flagged while digesting this document, not verified: P-CLOUD_SUPPORT SBPD step 4 enters product number P-CLOUD_COMM (likely copy error).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Usage lookup table steps select OneTimePrice instead of UsagePrice in step 3 and import.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Machine-translated text, tax classification note says 1 is full tax and 6 for Germany.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 51,428 chars in the whole document
