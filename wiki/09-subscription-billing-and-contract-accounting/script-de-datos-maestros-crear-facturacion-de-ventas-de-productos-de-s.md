---
id: 09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s
title: "Script de datos maestros: Crear facturación de ventas de productos de suscripción - MDS (5BD) (5BD_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (5BD): create subscription products, rate elements, rate plan templates and pricing lookup tables."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_ES_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, rate plan templates, pricing schemes, pricing lookup tables, product master extension, subscription billing, master data scripts, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-426
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear facturación de ventas de productos de suscripción - MDS (5BD) (5BD_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear facturación de ventas de productos de suscripción - MDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894743)

[2 Requisitos previos 3](#_Toc233894744)

[2.1 Acceso al sistema 3](#_Toc233894745)

[2.2 Roles 3](#_Toc233894746)

[2.3 Unidades organizativas necesarias (SAP S/4HANA) 3](#_Toc233894747)

[3 Tabla de resumen 4](#_Toc233894748)

[4 Procedimientos 5](#_Toc233894749)

[4.1 Crear producto de suscripción (SAP Subscription Billing) 5](#_Toc233894750)

[4.1.1 Crear elementos de tarifa 5](#_Toc233894751)

[4.1.2 Crear plantilla para planes de tarifa 7](#_Toc233894752)

[4.1.3 Crear un producto 8](#_Toc233894753)

[4.1.4 Crear un producto con un esquema de determinación de precios 10](#_Toc233894754)

[4.1.5 Carga de tablas de búsqueda para la determinación de precios 12](#_Toc233894755)

[4.2 Enriquecer productos de suscripción (SAP S/4HANA) 17](#_Toc233894756)

[4.2.1 Ampliar productos de facturación de suscripciones del tipo SBPD 17](#_Toc233894757)

[4.2.2 Ampliar productos de facturación de suscripciones del tipo SBRE 19](#_Toc233894758)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, encontrará una descripción de cómo crear un maestro de productos de suscripción datos. La descripción incluye los segmentos de datos que son relevantes para los datos maestros para trabajar en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos Los campos y normalmente deben rellenarse con valores de entrada. Campos que no son relevantes para el alcance no se describe en este documento, aunque pueden aparecer en la IU.

Un registro maestro de suscripción que se crea como se describe aquí se puede utilizar para facturación de suscripciones.

| ID de producto de suscripción | Descripción | Utilización |
| --- | --- | --- |
| P-CLOUD_STORAGE | Producto de suscripción | Representa el producto de facturación de suscripciones |
| P-CLD_STORAGE_PCS | Producto de servicios de cálculo de precios | Representa el producto de cálculo de precios |

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema SAP S/4HANA | Accesible a través de la rampa de lanzamiento SAP Fiori. Su administrador del sistema proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |
| SAP Subscription Billing | Accesible mediante URL. El administrador del sistema le proporciona la URL para acceder a la aplicación. |
| Servicio de cálculo de precios | Accesible a través de la rampa de lanzamiento SAP Fiori. Su administrador del sistema proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Crear roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asignar a sus usuarios de prueba individuales.

SAP S/4HANA

| Nombre | ID |
| --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

Póngase en contacto con el administrador del sistema para configurar la autorización.

### Unidades organizativas necesarias (SAP S/4HANA)

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa, General Los datos (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Unidad organizativa a utilizar | Unidad organizativa a utilizar |
| --- | --- | --- | --- |
| Crear registro de datos maestros | Organización de ventas | 1710 (Org.ventas nac.US) | Para Alemania, utilice 1010 (Org. Org.ventas DE) |
| Crear registro de datos maestros | Canal de distribución | 10 (Ventas directas) | 10 (Ventas directas) |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear producto de suscripción (SAP Subscription Billing) | N/D | N/D | Se han creado los productos de suscripción. |
| Crear productos de suscripción (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Gestionar datos maestros de producto | Se han creado los productos de suscripción. |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este maestro registro.

### Crear producto de suscripción (SAP Subscription Billing)

#### Crear elementos de tarifa

Objetivo

En esta actividad se crean elementos de tarifa en SAP Subscription Billing. Los ID de tarifa deben corresponderse con los productos S/4HANA relevantes del tipo SBRE:

| ID de tarifa | Tipo de cambio | Descripción |
| --- | --- | --- |
| R-ONETIME | Único | Tasa de activación única |
| R-SEATS | Periódico | Tarifa mensual basada en asientos |
| R-TRAFFIC | Basado en uso | Tasa de uso basada en tráfico |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Elementos de tarifa | Por debajo de Datos maestros y configuración , seleccione Gestionar configuración empresarial > Elementos de tarifa . | El Elementos de tarifa Se muestra la vista. |  |
| 3 | Crear elemento de tarifa: R-ONETIME | Seleccionar Crear > Único y, a continuación, actualice los siguientes datos:ID: R-ONETIMEUnidad : Cada uno (EA)Etiqueta : Tasa de activación únicaFuente de datos : NingunoTipo único : Inicial TasaClase de factura : CargoDescripción : Actualice una descripción, por ejemplo , tasa de activación únicaActivo : SeleccionadoSeleccionar Grabar . | Se crea el elemento de tarifa R-ONETIME. |  |
| 4 | Crear elemento de tarifa: R-SEATS | Seleccionar Crear , actualice los siguientes datos:Tipo: PeriódicoID: R-SEATSUnidad : Cada uno (EA)Etiqueta : Tarifa mensual basada en asientosFuente de datos : SuscripciónClase de factura : CargoDescripción : Actualice una descripción, por ejemplo , tarifa mensual basada en asientosActivo : SeleccionadoSeleccionar Grabar . | Se creó el elemento de tarifa R-SEATS. |  |
| 5 | Crear elemento de tarifa: R-TRAFFIC | Seleccionar Crear , actualice los siguientes datos:Tipo: Basado en usoID: R-TRAFFICUnidad : CADA EA)Etiqueta : Tasa de uso basada en tráficoFuente de datos : UtilizaciónClase de factura : CargoUtilizar subelementos de tarifa : Seleccionado (solo para productos PCS)Variante de determinación de tarifas de uso : AgregadoTipo de ID de recurso técnico: ID de espacio de almacenamiento en la nubeDescripción : Actualice una descripción, para ejemplo , tráfico de carga/descargaActivo : SeleccionadoSeleccionar Grabar . | Se creó el elemento de tarifa R-TRAFFIC. |  |

|  |
| --- |
| Nota Los recursos técnicos identifican al suscriptor y al servicio suscrito en un sistema técnico. Son necesarios cuando factura a sus clientes en función de la uso de su servicio. Por ejemplo, medir el consumo de electricidad, aquí, el Tipo de ID de recurso técnico: se puede definir como el "ID de contador de electricidad", que es el ID unívoco (por ejemplo, EM392734-A) en la que se contabiliza la utilización. En un escenario en el que el kilometraje medida, el Tipo de ID de recurso técnico: podría ser definido como el "Número de licencia de vehículo".Este es un campo de entrada de usuario y se define según el servicio/escenario. |

#### Crear plantilla para planes de tarifa

Objetivo

En esta actividad se crea una plantilla para planes de tarifa en SAP Subscription Billing.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a las plantillas del plan de tarifas | Por debajo de Determinación de precios , seleccione Gestionar plan de tarifas Modelos aplicación. | Se visualizan las plantillas para planes de tarifa disponibles. |  |
| 3 | Crear plantilla para planes de tarifa: | Seleccionar Crear > Sin esquema de determinación de precios y actualice los siguientes datos en Información general :Descripción: Plantilla de planificación basada en asientosCiclo de facturación : Mensualmente el primer día del mesMoneda: Valor – USD (para versión de país US) | El Plantilla del plan de tarifas se visualiza. |  |
| 4 | Actualizar cargos/abonos para elementos de tarifa | En la sección Cargos/Abonos, seleccione Cargos / Abonos, seleccionar Añadir y seleccione Único .A continuación, actualice el datos siguientes:Elemento de tarifa : R-ONETIMEPrecio Valor : 100 USDPara Cargos/abonos , seleccione Crear y seleccione Periódico y, a continuación, seleccione, Cargo de determinación de precio de porcentaje .Entonces actualice los siguientes datos:Tasa Elemento : R-SEATSAplicar Modificaciones con el siguiente ciclo : SeleccionadoAnticipo de facturación : SeleccionadoProrratear primer ciclo : SeleccionadoPrecio por unidad : 10 USDRatio : 100Para Cargos / Créditos , seleccione Añadir y a continuación, seleccione Utilización Bloquear Determinación de precios .A continuación, actualice lo siguiente: datos:Elemento de tarifa : R-TRAFFICTasa Subelemento : Actualizar Tasa Subelementosi el Tarifa de uso Subelementos está activada en [Crear elementos de tarifa](#unique_7) [página ] 5 paso.Nota Subelemento de tarifa es un campo obligatorio si el Utilizar subelementos de tarifa la opción es activado.Aplicar modificaciones con el siguiente ciclo : No SeleccionadoCantidad incluida : Valor – 1Bloquear Tamaño : Valor – 1Precio por bloque : Valor: 1 USD (para la versión de país) US)Seleccione Crear .A continuación, seleccione Publicar . | Se crean los cargos/abonos. |  |

#### Crear un producto

Objetivo

En esta actividad se crea un producto P-CLOUD_STORAGE en SAP Subscription Billing. El ID de el producto en SAP Subscription Billing debe corresponderse con el ID de producto relevante en SAP S/4HANA.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Productos | Por debajo de Datos maestros y configuración , abra el Gestionar Productos aplicación. | Se visualizan los productos disponibles. |  |
| 3 | Actualizar información general de producto | Seleccionar Crear y actualice los siguientes datos en Información general área:Nombre de producto: Almacenamiento en la nubeID de producto: P-CLOUD_STORAGETipo de suscripción : ComercialCrear suscripciones como pendientes: DesmarcadoPerfil de suscripción : S/4 Integración | Se ha actualizado la información general. |  |
| 4 | Actualizar plan de tarifas para producto | Por debajo de Planes de tarifas , seleccione Crear > Sin esquema de determinación de precios y actualice los siguientes datos:.Nota Si utiliza productos que requieren un esquema de precios, debe seleccionar Con determinación de precios Esquema . Para obtener un resumen de la determinación de precios con y sin esquemas de precios, consulte [Determinación de precios](https://help.sap.com/docs/subscription-billing/feature-overview/pricing) en la documentación de SAP Subscription Billing.Mercado : Este de EE. UU. (para versión de país US)Plantilla del plan de tarifas : Plantilla de planificación basada en asientosDescripción : Plan de tarifas recurrentes (basado en asientos)Ciclo de facturación : Mensualmente el primer día de mesSeleccionar Crear . | El plan de tarifas se actualizó para el producto. |  |
| 5 | Actualizar condiciones de suscripción | Por debajo de Términos de la suscripción , actualice lo siguiente:Período de vigencia previsto : por ejemplo, 12Período de vigencia mínimo : 12Período de renovación : 12Período de revocación : 14 | Se actualizan los términos de la suscripción. |  |
| 6 | Crear producto | Para todo el producto, seleccione Crear .A continuación, seleccione Publicar . | Se crea el producto P-CLOUD_STORAGE. |  |

#### Crear un producto con un esquema de determinación de precios

Al revisar un caso de uso de muestra, puede utilizar los valores de muestra para crear datos a partir de o puede utilizar la configuración predefinida que se suministra con cada nuevo arrendatario. Debe ejecutar los siguientes pasos en el servicio Cálculo de precios antes de crear un producto con un esquema de precios.

Puede encontrar una descripción detallada de cómo configurar la determinación de precios con esquemas de precios (utilizando un ejemplo) en [Guía de configuración de Determinación de precios con esquemas de precios](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide).

Procedimiento

1. Gestionar catálogo de campos

Si utiliza los datos de muestra, se utiliza un catálogo de campos predefinido en el Gestionar catálogo de campos aplicación. Por lo tanto, no necesita hacer ninguna opciones adicionales aquí. El Gestionar catálogo de campos aplicación le permite crear campos que se utilizarán posteriormente para definir las tablas de búsqueda y propiedades de entrada para especificaciones de elemento de precio.

2. Crear tablas de búsqueda

En la Gestionar tablas de búsqueda aplicación, puede crear una búsqueda tablas asignando un conjunto de campos de entrada a un conjunto de campos de salida. Esta búsqueda las tablas se utilizan en un paso posterior para crear especificaciones de elementos de precio. El el objetivo de este paso es crear las siguientes tablas de búsqueda para una sola vez, tarifas recurrentes y de uso:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Descuento1

Estas tablas forman parte del contenido predefinido. Por lo tanto, no necesita hacer ningún adicional opciones en este paso.

3. Especificaciones del elemento de precio

En la Gestionar especificaciones de elemento de precio defina su configuración de determinación de precios creando especificaciones del elemento de precio. Esto incluye configuración de la lógica de determinación de precios y campos sustituibles:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Descuento1

|  |
| --- |
| Nota Si las especificaciones del elemento de precio para los elementos anteriores no actualizados, debe actualizarlos en el Gestionar precio Especificaciones de elemento mediante la selección de la persona elementos Campos sustituibles > Añadir/Crear > Precio/Descuento > Grabar . |

4. Esquema de determinación de precios

En la Gestionar esquemas de precios la aplicación, puede crear y actualizar la determinación de precios esquemas. Un esquema de determinación de precios es un procedimiento que define el uso y la relación de las especificaciones del elemento de precio para un determinado documento con precios calculables. También determina la secuencia para ejecutar estas especificaciones para generar una importe total en un documento con precio fijado.

El esquema de determinación de precios "Inicial" forma parte del contenido predefinido. Por lo tanto, necesita no realice ninguna parametrización adicional en este paso.

5. Crear plantilla para planes de tarifa

| Paso de test # | Nombre de paso de test | Instrucciones | Resultados previstos | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegue a la Plan de tarifas Modelos aplicación | Ir a Determinación de precios > Gestionar plantillas para planes de tarifa | Se visualizan las plantillas para planes de tarifa. |  |
| 3 | Seleccionar Crear | Seleccionar Crear > Con determinación de precios Esquema y actualizar los siguientes datos en Información general :Descripción : RPT para Cálculo de precioEtiquetas : PCS (Opcional)Esquema de determinación de precios : InicialCiclo de facturación : Mensualmente el primer día del mesPerfil de facturación : Opciones inicialesMoneda : USD | Se ha actualizado la información general. |  |
| 4 | Actualizar Cargos/abonos para tarifa elementos | Para una sola vez, seleccione Cargos/Abonos > Crear > Único e introduzca Tasa Elemento = R-ONETIME .Seleccionar Detalles de campos sustituibles > Crear > Descuento 1 e introduzca Único Precio = Seleccionar . Seleccionar Aplicar .Para recurrente, seleccione Cargos/Abonos > Crear > Periódico e introduzca Tasa Elemento = R-SEATS .Seleccionar Detalles de campos sustituibles > Crear > Descuento 1 e introduzca Periódico Precio = Seleccionar . Seleccionar Aplicar .Para el uso, seleccione Cargos/Abonos > Crear > Uso: Determinación de precios por bloques e introduzca Tasa Elemento = R-TRAFFIC y Tasa Subelemento .Nota Subelemento de tarifa es un campo obligatorio si el Tarifa de uso Subelementos está activada en el [Crear elementos de tarifa](#unique_7) [página ] 5 paso.Seleccionar Detalles de campos sustituibles > Crear > Descuento 1 e introduzca Basado en uso Precio = Seleccionar . Seleccionar Aplicar .Seleccionar Crear y luego Publicar . |  |  |

6. Crear producto

Crea un producto P-CLOUD_STORAGE_PC en SAP Subscription Billing. El ID del producto en SAP Subscription Billing debe corresponderse con el ID de producto relevante en SAP S/4HANA. Puede utilizar la Procedimiento siguiente:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en SAP Subscription Billing. | El Inicio Aparece la página. |  |
| 2 | Navegar a Productos | Por debajo de Datos maestros y configuración , abra el Gestionar Productos aplicación. | Se visualizan los productos disponibles. |  |
| 3 | Actualizar información general del producto | Seleccionar Crear y actualizar la los siguientes datos en el General Info área:Nombre de producto : Nube Cálculo de precio de almacenamientoID de producto : P-CLOUD_STORAGE_PCTipo de suscripción : ComercialCrear suscripciones como pendientes : Desmarcado | Se ha actualizado la información general. |  |
| 4 | Actualizar plan de tarifas para producto | El Planes de tarifas , seleccione Crear - > Con esquema de determinación de precios Navegar a Crear plantilla y actualice los siguientes datos:Mercado : EE. UU. Este (para versión de país US)Plantilla del plan de tarifas : RPT para determinación de precioDescripción : RPT para Cálculo de precioCiclo de facturación : Mensualmente el primer día del mesSeleccionar Crear . | El plan de tarifas se actualizó para el producto. |  |
| 5 | Actualizar Términos de la suscripción | Por debajo de Parámetros de suscripción , actualice los siguientes datos en el Términos de la suscripción área:Período de vigencia previsto : por ejemplo, 12Período de vigencia mínimo : 12Período de renovación : 12Período de revocación : 14 | Se actualizan los términos de la suscripción. |  |
| 6 | Crear producto | El Producto , seleccione Crear .Seleccionar Publicar . | El P-CLOUD_STORAGE_PC se crea el producto. |  |

7. Cargar tablas de búsqueda para determinación de precio

Para obtener más información sobre la carga de tablas de búsqueda, consulte [Carga de tablas de búsqueda para la determinación de precios](#unique_11) [página ] 12.

#### Carga de tablas de búsqueda para la determinación de precios

Puede cargar sus tablas de búsqueda para tarifas únicas, recurrentes y basadas en el uso y para descuento, siguiendo el procedimiento siguiente. Los datos de la tabla resultante se utilizan para buscar los precios relevantes durante la determinación de precios como parte del proceso de valoración.

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
| 3 | Seleccionar UsagePrice | Seleccione la tabla de búsqueda UsagePrice .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:productCode : P-CLOUD_STORAGE_PCID de mercado : A1rateElement : R-TRAFFICprecio : Volumenprice (tipo de precio) : LinealLos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa alta:rateSubElement : Altaprice (Rango) : 500price (unidad de intervalo) : EAprice (Valor) : 30price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel:rateSubElement : Altaprice (Rango) : 1000price (unidad de intervalo) : EAprice (Valor) : 25price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel:rateSubElement : Altaprice (Rango) :price (unidad de intervalo) : EAprice (Valor) : 20price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) : 500price (unidad de intervalo) : EAprice (Valor) : 15price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) : 1000price (unidad de intervalo) : EAprice (Valor) : 10price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EALos siguientes valores específicos están disponibles para cada nivel para un subelemento de tarifa baja:rateSubElement : Bajaprice (Rango) :price (unidad de intervalo) : EAprice (Valor) : 5price (moneda de valor) : USDprice (valor de cantidad) : 1price (Unidad de cantidad) : EA |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda UsagePrice e ir a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar . | La tabla de búsqueda UsagePrice se ha actualizado. |  |

Tabla 4: Cargar tabla de descuentos

| Paso de test # | Nombre de paso de test | Instrucciones | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Iniciar sesión en SAP Price Calculation | El Inicio Aparece la página. |  |
| 2 | Navegar a Plantillas del plan de tarifas | Por debajo de Gestión de datos maestros , abra el Gestionar datos de tabla de búsqueda aplicación. | Se visualizan las tablas de búsqueda. |  |
| 3 | Seleccionar Descuento1 | Seleccione la tabla de búsqueda Descuento1 .Descargue la tabla vacía y almacénela localmente como un archivo CSV.Consejo Si el formato del archivo descargado no es una columna separado, debe cambiar el formato de la hoja de cálculo a un formato US. |  |  |
| 4 | Actualizar el archivo descargado | Introduzca los siguientes valores y guarde el archivo:ID de mercado : A1descuento : Individualdescuento (tipo de precio) : Porcentajedescuento (valor) : 0,1 |  |  |
| 5 | Cargar el archivo CSV | Seleccione la tabla de búsqueda Descuento1 e ir a Importar > Explorar para cargar el archivo guardado del paso anterior.Nota Existen dos tipos de importaciones. Seleccione Fusionar para mantener datos intactos.Haga clic en Importar . | La tabla de búsqueda Descuento1 se ha actualizado. |  |

### Enriquecer productos de suscripción (SAP S/4HANA)

#### Ampliar productos de facturación de suscripciones del tipo SBPD

Objetivo

En esta actividad, amplía el producto de facturación de suscripciones P-CLOUD_STORAGE en SAP S/4HANA. Este producto se crea en Facturación de suscripciones, se replica en SAP S/4HANA y se disponible una vez configurada la replicación de productos como parte del elemento de alcance 57Z. Para obtener más información sobre la replicación de productos, consulte [Configurar paquete IFlow para replicación de productos y tarifa Elementos](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html).

|  |
| --- |
| Nota Los campos específicos de Brasil requieren un cálculo de impuestos adecuado. Para obtener más información sobre esto, consulte Datos maestros de material > Definir campos específicos de BR para datos maestros > Crear datos maestros para Brasil (JD0_BR) . |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto Aparece la aplicación. |  |
| 3 | Buscar el producto | En el área de búsqueda de la parte superior, introduzca el Producto : P-CLOUD_ ALMACENAMIENTO y P-CLOUD_ STORAGE_PC .Seleccionar Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: General Información | Seleccione el producto de la lista de informes,Número de producto: P-CLOUD_STORAGEUnidad base: UNTipo de producto: SBPD (subproducto de facturación)Descripción: Almacenamiento en la nubeA continuación, seleccione OK .Nota En Descripción proporcionar el Idioma y Producto detalles para una región específica, por ejemplo, Idioma : Inglés y Producto : Suscripción Producto de facturación . | El producto debe estar abierto y se actualiza la información general. |  |
| 5 | Actualizar cadenas de distribución: Información general | El Producto vista, en la Distribución Cadenas seleccione Crear y actualizar lo siguiente datos:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 (Ventas directas)Nota La cadena de distribución no es necesaria para el SBPD producto escriba si está utilizando MDI. Solo son necesarios si mediante Cloud Integration. |  | Para la versión de país Alemania, actualice el siguiente valor en su lugar de 1710:Organización de ventas : 1010 (nac. Org.ventas DE)Las otras entradas son las mismas para ambos países |
| 6 | Actualizar cadenas de distribución: Conceptos de agrupación | Navegue a la Términos de agrupación y actualice los siguientes datos:Grupo de tipos de posición : SBPD (subproducto de facturación)Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto completo)A continuación, seleccione Aplicar > Crear .Nota El grupo de tipos de posición no es necesario para el SBPD producto escriba si está utilizando MDI. Esto solo es necesario si mediante Cloud Integration. | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en su lugar de 1 (impuesto total):Clasificación fiscal : 6 (Impuesto completo) (Servicios))Las otras entradas son las mismas para ambos países. |
| 7 | Actualizar centros | Navegar a Centros > Crear y actualice los siguientes datos:Centro : 1710 (Centro US)Seleccionar Aplicar > Grabar . | Se actualizan los datos del centro. |  |

#### Ampliar productos de facturación de suscripciones del tipo SBRE

Objetivo

En esta actividad, amplía los siguientes productos de suscripción en SAP S/4HANA que se corresponden con elementos de tarifa en SAP Subscription Billing: los productos se crean en Facturación de suscripciones y replicada en SAP S/4HANA. Los elementos de tarifa estarán disponibles una vez configurada la replicación de productos como se menciona en la guía de configuración del elemento de alcance 57Z o consulte [Replicación de producto y elemento de tarifa](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest).

|  |
| --- |
| Nota Los campos específicos de Brasil requieren un cálculo de impuestos adecuado. Para obtener más información sobre esto, consulte Datos maestros de material > Definir campos específicos de BR para datos maestros > Verificar Crear datos maestros para Brasil (JD0_BR) . |

| ID de producto | Tipo de producto | Descripción |
| --- | --- | --- |
| R-ONETIME | SBRE | Tarifa de activación única |
| R-SEATS | SBRE | Tasa mensual basada en asientos |
| R-TRAFFIC | SBRE | Tarifa de uso basada en tráfico |

Procedimiento

Producto: R-ONETIME

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto Aparece la aplicación. |  |
| 3 | Buscar producto | En el área de búsqueda de la parte superior, introduzca el Producto : R-ONETIME .Seleccionar Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: General Información | El Producto vista, en la Cadenas de distribución , seleccione Crear y actualice los siguientes datos:Organización de ventas : 1710 (Org.ventas nac.US)Canal de distribución : 10 (directo) Ventas)Nota En Descripción proporcionar la Idioma y Producto detalles para una región específica, para ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe estar abierto y se actualiza la información general. | Para la versión de país de Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (Org.ventas nac.DE)Las otras entradas son las mismas para ambos países. |
| 5 | Actualizar cadenas de distribución: Conceptos de agrupación | Navegue a la Términos de agrupación y actualice los siguientes datos:Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto completo)A continuación, seleccione Aplicar y luego Crear .Nota El grupo de tipos de posición no es necesario para la clase de producto SBRE si está utilizando MDI | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1 (Impuesto total):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambas versiones. |
| 6 | Actualizar centros | Navegue a la Centros , seleccione Crear y actualice los siguientes datos:Centro : 1710 (Centro US)Seleccionar Aplicar y Grabar . | Se actualizan los datos del centro. | Para la versión de país de Alemania, actualice el siguiente valor:Centro : Centro 10101 (centro DE) |

Producto: R-SEATS

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto Aparece la aplicación. |  |
| 3 | Buscar producto | En el área de búsqueda de la parte superior,introduzca el Producto : R-SEATSPulse el botón Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: General Información | El Producto vista, en la Cadenas de distribución , seleccione Crear y actualice los siguientes datos:Organización de ventas : 1710 (Dom. Ventas org. EE. UU.)Canal de distribución : 10 (directo) Ventas)Nota En Descripción proporcionar la Idioma y Producto detalles para una región específica, para ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe estar abierto y se actualiza la información general. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (nac. Org.ventas DE)Las otras entradas son las mismas para ambos países |
| 5 | Actualizar cadenas de distribución: Conceptos de agrupación | Navegue a la Términos de agrupación y actualice los siguientes datos:Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto completo)A continuación, seleccione Aplicar . | Los términos de agrupación se actualizan y el producto se guarda. | Para la versión de país de Alemania, actualice el siguiente valor en lugar de 1 (Impuesto total):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambas versiones. |
| 6 | Actualizar centros | Navegue a la Centros , seleccione Crear y actualice los siguientes datos:Centro : 1710 (Centro US)Seleccionar Aplicar y Grabar . | Se actualizan los datos del centro. | Para la versión de país de Alemania, actualice el siguiente valor:Centro : PLant 1010 (centro) DE) |

Producto: R-TRAFFIC

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Gestionar datos maestros de producto mosaico. | El Gestionar datos maestros de producto Aparece la aplicación. |  |
| 3 | Buscar producto | En el área de búsqueda de la parte superior,introduzca el Producto : Tráfico RPulse el botón Ir . | Su producto se visualiza en la lista de informes. |  |
| 4 | Abrir producto y actualizar cadenas de distribución: General Información | El Producto vista, en la Cadenas de distribución , seleccione Crear y actualice los siguientes datos:Organización de ventas : 1710 (Dom. Ventas org. EE. UU.)Canal de distribución : 10 (directo) Ventas)Nota En Descripción proporcionar la Idioma y Producto detalles para una región específica, para ejemplo, Idioma : Inglés y Producto : Facturación de suscripciones Producto . | El producto debe estar abierto y se actualiza la información general. | Para la versión de país Alemania, actualice el siguiente valor en lugar de 1710:Organización de ventas : 1010 (nac. Org.ventas DE)Las otras entradas son las mismas para ambos países |
| 5 | Actualizar cadenas de distribución: Conceptos de agrupación | Navegue a la Términos de agrupación y actualice los siguientes datos:Grupo de tipos de posición : SBRE (elemento de tarifa de facturación secundario)Grupo de imputación : X9 (Prestación de servicios periódica)Clasificación fiscal : 1 (Impuesto completo)Seleccionar Aplicar y luego Grabar .Nota El grupo de tipos de posición no es necesario para el producto SBRE si está utilizando MDI. | El producto se ha grabado. | Para la versión local Alemania, actualice el siguiente valor en lugar de 1 (Impuesto total):Clasificación fiscal : 6 (Impuesto total (servicios))Las otras entradas son las mismas para ambas versiones. |
| 6 | Actualizar centros | Navegue a la Centros , seleccione Crear y actualice los siguientes datos:Centro : 1710 (Centro US)Seleccionar Aplicar y luego Grabar . | Se actualizan los datos del centro. | Para la versión de país Alemania, actualice lo siguiente valor: Centro : Centro 10101 (centro DE) |

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
> Flagged while digesting this document, not verified: Germany plant for R-SEATS is given as 1010 whereas R-ONETIME and R-TRAFFIC use 10101

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 41,534 chars in the whole document
