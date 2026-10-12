---
id: 11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de
title: Script de datos maestros - Creación de maestro de transportistas - MDS (4DE) (4DE_S4CLD2608_Master_Data_ES_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (Spanish, machine-translated): step-by-step creation of carrier business partners by transport mode for invoice verification and ERS."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/carrier-master-data]
aliases: [4DE_S4CLD2608_Master_Data_ES_XX]
keywords: [Carrier Business Partners, carrier master data, business partner creation, invoice verification, evaluated receipt settlement, road carrier, rail carrier, ocean carrier, freight forwarder, air carrier]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-408
topic: 11-inventory-warehouse-and-transportation/carrier-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de transportistas - MDS (4DE) (4DE_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Carrier Business Partners** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de transportistas - MDS (4DE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894716)

[2 Requisitos previos 3](#_Toc233894717)

[2.1 Acceso al sistema 3](#_Toc233894718)

[2.2 Roles 3](#_Toc233894719)

[2.3 Unidades organizativas necesarias 3](#_Toc233894720)

[2.4 Parámetros principales para la creación de datos 4](#_Toc233894721)

[2.4.1 Agrupaciones 4](#_Toc233894722)

[3 Tabla de resumen 5](#_Toc233894723)

[4 Procedimientos 6](#_Toc233894724)

[4.1 Crear interlocutor comercial Transportista (carretera) para el proceso de verificación de facturas 6](#_Toc233894725)

[4.2 Crear socio comercial Transportista (carretera) para proceso de autofacturación (ERS) 10](#_Toc233894726)

[4.3 Crear transportista de socio comercial (tren) para proceso de verificación de facturas 14](#_Toc233894727)

[4.4 Crear socio comercial Transportista (ferrocarril) para proceso de autofacturación (ERS) 18](#_Toc233894728)

[4.5 Crear interlocutor comercial Transportista (marítimo) para proceso de verificación de facturas 21](#_Toc233894729)

[4.6 Crear socio comercial Transportista (marítimo) para proceso de autofacturación (ERS) 25](#_Toc233894730)

[4.7 Crear transportista de interlocutor comercial (agente de flete) para proceso de verificación de facturas 29](#_Toc233894731)

[4.8 Crear socio comercial Transportista (agente de flete) para autofacturación (ERS) Proceso 32](#_Toc233894732)

[4.9 Crear socio comercial transportista (aéreo) para proceso de verificación de facturas 36](#_Toc233894733)

[4.10 Crear socio comercial Transportista (aéreo) para proceso de autofacturación (ERS) 40](#_Toc233894734)

[5 Apéndice 44](#_Toc233894735)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este documento proporciona una descripción para crear un interlocutor comercial: Transportista para su Sistema SAP S/4HANA. La descripción incluye los segmentos de datos que son relevantes para la aplicación SAP S/4HANA, como los roles de interlocutor comercial y otros campos relevantes. Campos que no son relevantes para el alcance del contenido de SAP S/4HANA suministrado por SAP Best Practices no se describe en este documento.

Un transportista es un interlocutor comercial responsable del transporte de mercancías. Un transportista puede ofrecer servicios a expedidores o transportistas.

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
| Especialista en datos maestros - Datos de socio comercial | SAP_BR_BUPA_MASTER_SPECIALIST | Datos maestros - Socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de un unidad organizativa o sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos de compras (Gestión de materiales) | Organización de compras |  |  |  |
| Sociedad | Sociedad |  |  |  |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear una empresa registro de datos maestros de interlocutor transportista.

#### Agrupaciones

Se definen las siguientes agrupaciones para Transportista de interlocutor comercial:

| Agrupación | Rango / IDs | Comentarios |
| --- | --- | --- |
| Numeración numérica externa (rango superior) | BP03 |  |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear interlocutor comercial Transportista (carretera) para el proceso de verificación de facturas](#unique_8) [página ] 6 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se crea el transportista del socio comercial. |

## Procedimientos

En esta sección se describen los procedimientos para cada segmento o paso de proceso que se utiliza para diferentes procesos empresariales: Proceso de verificación de facturas y proceso de autofacturación.

### Crear interlocutor comercial Transportista (carretera) para el proceso de verificación de facturas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (orden de flete). Este transportista se utiliza principalmente en el proceso de verificación de facturas, donde los importes de la factura del transportista se comparan con los costes de transporte previstos calculados en la orden de flete.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Actualizar interlocutor comercial (IC) | Se abre una ventana nueva en la que se muestra Actualizar interlocutor comercial (IC) pantalla. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) rol. Mantenga esta opción. El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Nota Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Interlocutor comercial : <17386001>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <TM transportista por carretera US 1>Concepto de búsqueda : <TMROADCARRUS> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior: Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Seleccionar Cambiar entre visualizar y modificar para asegurarse de que se encuentra en el modo de modificación. Asignar un nuevo rol de socio comercial Transportista (CRM010) seleccionando el rol mediante la lista desplegable Modificación en rol IC .El Dirección para el rol de SC, introduzca un transportista con la siguiente información:Calle : <Nombre de calle>Código postal de la población : <Código postal de ciudad>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Languagename>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Nota Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Calle : <WindgapAve>Código postal de la población : <95206>Población : <Pittsburgh>País : <EE. UU.>Región (estado, provincia, condado) : <AP>Huso horario : <EST>Idioma : <EN>Teléfono (prefijo + número) : <412-264-5632>Correo electrónico : <info@17386001.com> |  |  |
| 7 | Introducir datos de operaciones de pago para el rol Transportista | El Transacciones de pago para el rol IC Transportista, introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Nota Valores de ejemplo con localizaciones de EE. UU. para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <790133> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (FLVN01) seleccionándolo en la lista desplegable Modificación en rol IC . A continuación, realice los siguientes pasos:Seleccionar Compras .Introduzca el siguiente valor en el campo Compras Organización campo: <Organización de compras>Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <Valor de grupo de compras>Gr.esq.prov. : <valor>Guarde las entradas.Nota Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (contab.fin.) (FLVN00) seleccionándolo en la lista desplegable.Modificación en rol ICSeleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en la pestaña correspondiente:Acreedor: Gestión de cuentas .Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Nota Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Correnspondencia de proveedor pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Nota Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR1> |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial Transportista (carretera) para proceso de autofacturación (ERS)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (orden de flete). Este transportista se utiliza principalmente para el escenario Autofacturación (ERS), donde se realiza la liquidación automática de facturas, sin esperar a una factura de transportista.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial (IC) se visualiza. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en IC el sistema rellena el campo de rol con el Rol de interlocutor comercial (Gen.) . Mantenga esta opción.El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Nota Consulte la sección Datos maestros, datos organizativos y otros datos en el escenario 3EP: Consolidación de transporte basada en orden para seleccionar los valores correctos.Valores de ejemplo para los campos anteriores:Interlocutor comercial : <17386002>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : TM autofacturación transportista por carretera USConcepto de búsqueda : <TMROADCARRSBUS> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior:Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Utilice el conmutador entre Visualizar y Modif. para asegurarse de que se encuentra en el modo de modificación. Asignar el nuevo rol IC Transportista (CRM010) seleccionando el rol mediante la lista desplegable Change in BP Role.El Dirección introduzca la siguiente información:Calle : <Nombre de la calle>Código postal de la población : <Código postal de la población>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Nombre de idioma>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Nota Valores de ejemplo para los campos anteriores:Calle : <E Sweet Ave>Código postal de la población : <58504>Población : <Bismarck>País : <EE. UU.>Región (estado, provincia, condado) : <ND>Huso horario : <MST>Idioma : <EN>Teléfono (prefijo + número) : <999 254 3623>Correo electrónico : <info@17386002.com> | Se añade el rol Socios comerciales Transportista. |  |
| 7 | Introducir datos de operaciones de pago para el rol de transportista | El Transacciones de pago introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Nota Valores de ejemplo para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <102610> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol IC Proveedor (FLVN01) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Compras .Introduzca el valor en el campo Organización de compras : <Organización de compras> campo.Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <valor>Gr.esq.prov. : <valor>Autofact.entr.entr. : <seleccionar>Guarde las entradas.Nota Valores de ejemplo para los campos anteriores:Compras Organización : <1710>Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03>Autofact.entr.entr. : <seleccionar> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de interlocutor comercial | Asignar el nuevo rol IC Proveedor (contab.fin.) (FLVN00) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en el campo Acreedor: Gestión de cuentas pestaña:Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Nota Valores de ejemplo para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Acreedor: Correspondencia pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Nota Valores de ejemplo para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR2> . |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear transportista de socio comercial (tren) para proceso de verificación de facturas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (orden de flete). Este transportista se utiliza principalmente en el proceso de verificación de facturas, donde los importes de la factura del transportista se comparan con los costes de transporte previstos calculados en la orden de flete.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Actualizar interlocutor comercial (IC) | Se abre una ventana nueva en la que se muestra Actualizar interlocutor comercial (IC) pantalla. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) función. Mantenga esta configuración. En la Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Empresarial Interlocutor : <17386201>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <TM compañía ferroviaria EE. UU. 1>Búsqueda Término : <TMRAILCARRUS1> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior: Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Seleccionar Cambiar entre visualizar y modificar para asegurarse de que se encuentra en el modo de modificación. Asignar un nuevo rol de socio comercial Transportista (CRM010) seleccionando el rol mediante la lista desplegable Modificación en rol IC .El Dirección para el rol de SC, introduzca un transportista con la siguiente información:Calle : <Nombre de calle>Código postal de la población : <Código postal de ciudad>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Languagename>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Calle : <WindgapAve>Código postal de la población : <95206>Población : <Pittsburgh>País : <EE. UU.>Región (estado, provincia, condado) : <AP>Huso horario : <EST>Idioma : <EN>Teléfono (prefijo + número) : <412-264-5632>Correo electrónico : <info@17386201.com> |  |  |
| 7 | Introducir datos de operaciones de pago para el rol Transportista | El Transacciones de pago para el rol IC Transportista, introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo con localizaciones de EE. UU. para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <790133> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (FLVN01) seleccionándolo en la lista desplegable Modificación en rol IC . A continuación, realice los siguientes pasos:Seleccionar Compras .Introduzca el siguiente valor en el campo Organización de compras campo: <Organización de compras>Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <Valor de grupo de compras>Gr.esq.prov. : <valor>Guarde las entradas.Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (contab.fin.) (FLVN00) seleccionándolo en la lista desplegable.Modificación en rol ICSeleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en la pestaña correspondiente:Acreedor: Gestión de cuentas .Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Correnspondencia de proveedor pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR201> |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial Transportista (ferrocarril) para proceso de autofacturación (ERS)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (orden de flete). Este transportista se utiliza principalmente para el escenario Autofacturación (ERS), donde se realiza la liquidación automática de facturas, sin esperar a una factura de transportista.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Socio comercial Datos . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial (IC) se visualiza. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en IC el sistema rellena el campo de rol con el Rol de interlocutor comercial (Gen.) . Mantenga esta configuración.El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Consulte la sección Datos maestros, datos organizativos y otros datos en el escenario 3EP: Consolidación de transporte basada en orden para seleccionar los valores correctos.Valores de ejemplo para los campos anteriores:Empresarial Interlocutor : <17386202>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <Autofacturación de compañía ferroviaria TM EE. UU.>Concepto de búsqueda : <TMRAILCARRSBUS> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior:Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Utilice el conmutador entre Visualizar y Modif. para asegurarse de que se encuentra en el modo de modificación. Asignar el nuevo rol IC Transportista (CRM010) seleccionando el rol mediante la lista desplegable Change in BP Role.El Dirección introduzca la siguiente información:Calle : <Nombre de la calle>Código postal de la población : <Código postal de la población>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Nombre de idioma>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo para los campos anteriores:Calle : <E Sweet Ave>Código postal de la población : <58504>Población : <Bismarck>País : <EE. UU.>Región (estado, provincia, condado) : <ND>Huso horario : <MST>Idioma : <EN>Teléfono (prefijo + número) : <999 254 3623>Correo electrónico : <info@17386202.com> | Se añade el rol Socios comerciales Transportista. |  |
| 7 | Introducir datos de operaciones de pago para el rol de transportista | El Transacciones de pago introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <102610> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol IC Proveedor (FLVN01) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Compras .Introduzca el valor en el campo Organización de compras : <Organización de compras> campo.Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <valor>Gr.esq.prov. : <valor>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar>Guarde las entradas.Valores de ejemplo para los campos anteriores:Organización de compras : <1710>Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de interlocutor comercial | Asignar el nuevo rol IC Proveedor (contab.fin.) (FLVN00) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en el campo Acreedor: Gestión de cuentas pestaña:Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Acreedor: Correspondencia pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR202> . |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear interlocutor comercial Transportista (marítimo) para proceso de verificación de facturas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista es asignado a una orden de transporte (reserva de flete) como transportista ejecutante/emisor de factura el nivel de etapa. Este transportista se utiliza principalmente en el proceso de verificación de facturas, donde los importes de la factura del transportista se comparan con los costes de transporte previstos calculado en la reserva de flete.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Actualizar interlocutor comercial (IC) | Se abre una ventana nueva en la que se muestra Actualizar interlocutor comercial (IC) pantalla. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) función. Mantenga esta configuración. En la Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Empresarial Interlocutor : <17386301>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <TM transportista marítimo US 1>Búsqueda Término : <TMOCEANCARRUS1> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior: Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Seleccionar Cambiar entre visualizar y modificar para asegurarse de que se encuentra en el modo de modificación. Asignar un nuevo rol de socio comercial Transportista (CRM010) seleccionando el rol mediante la lista desplegable Modificación en rol IC .El Dirección para el rol de SC, introduzca un transportista con la siguiente información:Calle : <Nombre de calle>Código postal de la población : <Código postal de ciudad>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Languagename>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Calle : <5301 Waterford en Blue Laguna>Código postal de la población código : <33126>Población : <Miami>País : <EE. UU.>Región (estado, provincia, Condado) : <FL>Hora Zona : <EST>Idioma : <EN>Teléfono (prefijo + número) : <412-264-5632>Correo electrónico : <info@17386301.com> |  |  |
| 7 | Introducir datos de operaciones de pago para el rol Transportista | El Transacciones de pago para el rol IC Transportista, introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo con localizaciones de EE. UU. para lo anterior campos:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <790133> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (FLVN01) seleccionándolo en la lista desplegable Modificación en rol IC . A continuación, realice los siguientes pasos:Seleccionar Compras .Introduzca el siguiente valor en el campo Organización de compras campo: <Organización de compras>Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <Valor de grupo de compras>Gr.esq.prov. : <valor>Guarde las entradas.Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (contab.fin.) (FLVN00) seleccionándolo en la lista desplegable.Modificación en rol ICSeleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en la pestaña correspondiente:Acreedor: Gestión de cuentas .Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Correnspondencia de proveedor pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR301> |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial Transportista (marítimo) para proceso de autofacturación (ERS)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista es asignado a una orden de transporte (reserva de flete) como transportista ejecutante/emisor de factura el nivel de etapa. Este transportista se utiliza principalmente para la autofacturación (ERS) escenario en el que se realiza la liquidación automática de facturas, sin esperar a un transportista factura.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Socio comercial Datos . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial (IC) se visualiza. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en IC el sistema rellena el campo de rol con el Rol de interlocutor comercial (Gen.) . Mantenga esta configuración.El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Consulte la sección Datos maestros, datos organizativos y otros datos en el escenario 3EP: Consolidación de transporte basada en orden para seleccionar los valores correctos.Valores de ejemplo para los campos anteriores:Empresarial Interlocutor : <17386302>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <TM Autofacturación transportista marítimo EE. UU. 2>Concepto de búsqueda : <TMOCEANCARRSBUS2> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior:Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Utilice el conmutador entre Visualizar y Modif. para asegurarse de que se encuentra en el modo de modificación. Asignar el nuevo rol IC Transportista (CRM010) seleccionando el rol mediante la lista desplegable Change in BP Role.El Dirección introduzca la siguiente información:Calle : <Nombre de la calle>Código postal de la población : <Código postal de la población>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Nombre de idioma>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo para los campos anteriores:Calle : <888 Brannan Calle>Código postal de la población código : <94103>Población : <San Francisco>País : <EE. UU.>Región (estado, provincia, Condado) : <CA>Huso horario : <PST>Idioma : <EN>Teléfono (prefijo + número) : <999 254 3623>Correo electrónico : <info@17386302.com> | Se añade el rol Socios comerciales Transportista. |  |
| 7 | Introducir datos de operaciones de pago para el rol de transportista | El Transacciones de pago introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <102610> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol IC Proveedor (FLVN01) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Compras .Introduzca el valor en el campo Organización de compras : <Organización de compras> campo.Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <valor>Gr.esq.prov. : <valor>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar>Guarde las entradas.Valores de ejemplo para los campos anteriores:Organización de compras : <1710>Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de interlocutor comercial | Asignar el nuevo rol IC Proveedor (contab.fin.) (FLVN00) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en el campo Acreedor: Gestión de cuentas pestaña:Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Acreedor: Correspondencia pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR302> . |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear transportista de interlocutor comercial (agente de flete) para proceso de verificación de facturas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de socio comercial para permitir la organización de la ejecución del transporte. El El agente de flete está asignado a una orden de transporte (reserva de flete). Este porte transportista se utiliza principalmente para el proceso de subcontratación y la organización de ejecución de transporte. El agente de flete se paga por su servicio para organizar el transporte.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Actualizar interlocutor comercial (IC) | Se abre una ventana nueva en la que se muestra Actualizar interlocutor comercial (IC) pantalla. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) función. Mantenga esta configuración. En la Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Empresarial Interlocutor : <17386401>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <Agente de flete TM US>Búsqueda Término : <TMOCEANFORWUS1> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior: Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Seleccionar Cambiar entre visualizar y modificar para asegurarse de que se encuentra en el modo de modificación. Asignar un nuevo rol de socio comercial Transportista (CRM010) seleccionando el rol mediante la lista desplegable Modificación en rol IC .El Dirección para el rol de SC, introduzca un transportista con la siguiente información:Calle : <Nombre de calle>Código postal de la población : <Código postal de ciudad>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Languagename>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Calle : <131 Aberdeen Dr.>Código postal de la población código : <92007>Población : <CARDIFF POR SEA>País : <EE. UU.>Región (estado, provincia, Condado) : <CA>Hora Zona : <PST>Idioma : <EN>Teléfono (prefijo + número) : <412-264-5632>Correo electrónico : <info@17386401.com> |  |  |
| 7 | Introducir datos de operaciones de pago para el rol Transportista | El Transacciones de pago para el rol IC Transportista, introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo con localizaciones de EE. UU. para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <790133> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (FLVN01) seleccionándolo en la lista desplegable Modificación en rol IC . A continuación, realice los siguientes pasos:Seleccionar Compras .Introduzca el siguiente valor en el campo Organización de compras campo: <Organización de compras>Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <Valor de grupo de compras>Gr.esq.prov. : <valor>Guarde las entradas.Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (contab.fin.) (FLVN00) seleccionándolo en la lista desplegable.Modificación en rol ICSeleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en la pestaña correspondiente:Acreedor: Gestión de cuentas .Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Correnspondencia de proveedor pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR401> |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial Transportista (agente de flete) para autofacturación (ERS) Proceso

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de socio comercial para permitir la organización de la ejecución del transporte. El El agente de flete está asignado a una orden de transporte (reserva de flete). Este porte transportista se utiliza principalmente para el proceso de subcontratación y la organización de ejecución de transporte. El agente de flete se paga por su servicio para organizar el transporte. Este transportista se utiliza principalmente para la autofacturación. escenario (ERS), en el que se realiza la liquidación automática de facturas, sin esperar un factura de transportista.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Socio comercial Datos . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial (IC) se visualiza. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en IC el sistema rellena el campo de rol con el Rol de interlocutor comercial (Gen.) . Mantenga esta configuración.El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Consulte la sección Datos maestros, datos organizativos y otros datos en el escenario 3EP: Consolidación de transporte basada en orden para seleccionar los valores correctos.Valores de ejemplo para los campos anteriores:Empresarial Interlocutor : <17386402>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <Autofacturación de agente de flete TM US>Concepto de búsqueda : <TMOCEANFORWSBUS1> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior:Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Utilice el conmutador entre Visualizar y Modif. para asegurarse de que se encuentra en el modo de modificación. Asignar el nuevo rol IC Transportista (CRM010) seleccionando el rol mediante la lista desplegable Change in BP Role.El Dirección introduzca la siguiente información:Calle : <Nombre de la calle>Código postal de la población : <Código postal de la población>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Nombre de idioma>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo para los campos anteriores:Calle : <2601 Westheimer Carretera>Código postal de la población código : <77098>Población : <Houston>País : <EE. UU.>Región (estado, provincia, Condado) : <TX>Huso horario : <CST>Idioma : <EN>Teléfono (prefijo + número) : <999 254 3623>Correo electrónico : <info@17386402.com> | Se añade el rol Socios comerciales Transportista. |  |
| 7 | Introducir datos de operaciones de pago para el rol de transportista | El Transacciones de pago introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <102610> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol IC Proveedor (FLVN01) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Compras .Introduzca el valor en el campo Organización de compras : <Organización de compras> campo.Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <valor>Gr.esq.prov. : <valor>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar>Guarde las entradas.Valores de ejemplo para los campos anteriores:Organización de compras : <1710>Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03>Autoeval.liq.EM entrg.a eval. Recibo Liquidación : <seleccionar> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de interlocutor comercial | Asignar el nuevo rol IC Proveedor (contab.fin.) (FLVN00) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en el campo Acreedor: Gestión de cuentas pestaña:Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Acreedor: Correspondencia pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR402> . |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial transportista (aéreo) para proceso de verificación de facturas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (reserva de flete) como transportista ejecutante/emisor de factura a nivel de etapa. Este transportista se utiliza principalmente en el proceso de verificación de facturas, donde los importes de la factura del transportista se comparan con los costes de transporte previstos calculados en la reserva de flete.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Aparece la página Inicio. |  |
| 2 | Acceder a la aplicación SAP Fiori | Actualizar interlocutor comercial (IC) | Se abre una ventana nueva en la que se muestra Actualizar interlocutor comercial (IC) pantalla. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) función. Mantenga esta configuración. En la Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Interlocutor comercial : <17386501>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <TM Airline US 1>Concepto de búsqueda : <TMAIRLINEUS1> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior: Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Seleccionar Cambiar entre visualizar y modificar para asegurarse de que se encuentra en el modo de modificación. Asignar un nuevo rol de socio comercial Transportista (CRM010) seleccionando el rol mediante la lista desplegable Modificación en rol IC .El Dirección para el rol de SC, introduzca un transportista con la siguiente información:Calle : <Nombre de calle>Código postal de la población : <Código postal de ciudad>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Languagename>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Calle : < 5301 Waterford en Blue Lagoon>Código postal de la población : < 33126>Población : <Miami>País : <EE. UU.>Región (estado, provincia, condado) : <FL>Huso horario : <EST>Idioma : <EN>Teléfono (prefijo + número) : <412-264-5632>Correo electrónico : <info@17386501.com> |  |  |
| 7 | Introducir datos de operaciones de pago para el rol Transportista | El Transacciones de pago para el rol IC Transportista, introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo con localizaciones de EE. UU. para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <790133> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (FLVN01) seleccionándolo en la lista desplegable Modificación en rol IC . A continuación, realice los siguientes pasos:Seleccionar Compras .Introduzca el siguiente valor en el campo Organización de compras campo: <Organización de compras>Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <Valor de grupo de compras>Gr.esq.prov. : <valor>Guarde las entradas.Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de socio comercial | Asignar el nuevo rol de socio comercial Proveedor (contab.fin.) (FLVN00) seleccionándolo en la lista desplegable.Modificación en rol ICSeleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en la pestaña correspondiente:Acreedor: Gestión de cuentas .Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Correnspondencia de proveedor pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo con la localización de EE. UU. para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR501> |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

### Crear socio comercial Transportista (aéreo) para proceso de autofacturación (ERS)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Cree un transportista de interlocutor comercial para habilitar la ejecución del transporte. El transportista está asignado a una orden de transporte (reserva de flete) como transportista ejecutante/emisor de factura a nivel de etapa. Este transportista se utiliza principalmente para el escenario Autofacturación (ERS), donde se realiza la liquidación automática de facturas, sin esperar a una factura de transportista.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como especialista en datos maestros - Datos de interlocutor comercial. | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial (IC) se visualiza. |  |
| 3 | Crear una organización de IC | Seleccionar Organización . | El Crear organización Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece con un carácter>Agrupación : <Numeración alfanumérica externa>El Crear en IC el sistema rellena el campo de rol con el Rol de interlocutor comercial (Gen.) . Mantenga esta configuración.El Dirección introduzca la siguiente información:Nombre : <Nombre de la organización>Concepto de búsqueda : <Concepto de búsqueda para interlocutor comercial>Consulte la sección Datos maestros, datos organizativos y otros datos en el escenario 3EP: Consolidación de transporte basada en orden para seleccionar los valores correctos.Valores de ejemplo para los campos anteriores:Interlocutor comercial : <17386502>Agrupación : <Numeración numérica externa (rango superior) (BP03)>Nombre : <Autofacturación de aerolínea TM US 2>Concepto de búsqueda : <TMAIRLINESBUS2> |  |  |
| 5 | Introducir datos de identificación | El Identificación pestaña para el Interlocutor comercial rol, introduzca la siguiente información:Forma jurídica : <Forma jurídica de la organización>Valores de ejemplo para el campo anterior:Forma jurídica : <01 (Corporación)>Guarde las entradas. |  |  |
| 6 | Asignar nuevo rol de transportista e introducir datos de dirección | Utilice el conmutador entre Visualizar y Modif. para asegurarse de que se encuentra en el modo de modificación. Asignar el nuevo rol IC Transportista (CRM010) seleccionando el rol mediante la lista desplegable Change in BP Role.El Dirección introduzca la siguiente información:Calle : <Nombre de la calle>Código postal de la población : <Código postal de la población>Población : <Nombre de ciudad>País : <Nombre de país>Región (estado, provincia, condado) : <Nombre de región>Huso horario : <Huso horario>Idioma : <Nombre de idioma>Teléfono (prefijo + número) : <Número de teléfono con prefijo>Correo electrónico : <Dirección de correo electrónico>Valores de ejemplo para los campos anteriores:Calle : <888 Brannan Street>Código postal de la población : <94103>Población : <San Francisco>País : <EE. UU.>Región (estado, provincia, condado) : <CA>Huso horario : <PST>Idioma : <EN>Teléfono (prefijo + número) : <999 254 3623>Correo electrónico : <info@17386502.com> | Se añade el rol Socios comerciales Transportista. |  |
| 7 | Introducir datos de operaciones de pago para el rol de transportista | El Transacciones de pago introduzca la siguiente información:País : <Clave de banco>Clave de banco : <Clave de banco>Cuenta bancaria : <Número de cuenta bancaria>Guarde las entradas.Valores de ejemplo para los campos anteriores:País : <EE. UU.>Clave de banco : <150350300>Cuenta bancaria : <102610> |  |  |
| 8 | Asignar nuevo rol de proveedor e introducir datos de socio comercial | Asignar el nuevo rol IC Proveedor (FLVN01) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Compras .Introduzca el valor en el campo Organización de compras : <Organización de compras> campo.Seleccionar Intro .Introduzca la siguiente información en el campo Datos de compras pestaña:Moneda de pedido : <Nombre de moneda>Condiciones de pago : <Condiciones de pago>Condiciones de expedición : <Nombre de condición de expedición>Grupo de compras : <valor>Gr.esq.prov. : <valor>Liquidación de entrada de evaluación : <seleccionar>Guarde las entradas.Valores de ejemplo para los campos anteriores:Organización de compras : <1710>Moneda de pedido : <USD>Condiciones de pago : <0004>Condiciones de expedición : <01>Grupo de compras : <005>Gr.esq.prov. : <03>Liquidación de entrada de evaluación : <seleccionar> |  |  |
| 9 | Asignar nuevo rol de proveedor FI e introducir datos de interlocutor comercial | Asignar el nuevo rol IC Proveedor (contab.fin.) (FLVN00) seleccionando el rol mediante la lista desplegable Change in BP Role.Seleccionar Sociedad .Introduzca el Sociedad : <Sociedad>Seleccionar Intro .Introduzca la siguiente información en el campo Acreedor: Gestión de cuentas pestaña:Cuenta asociada : <Número de cuenta>Clave de clasificación : <Valor>Valores de ejemplo para los campos anteriores:Sociedad : <1710>Cuenta asociada : <21100000>Clave de clasificación : <009> |  |  |
| 10 | Introducir datos de correspondencia de proveedor | Introduzca la siguiente información en el campo Acreedor: Correspondencia pestaña:Abrev.responsable : <Valor>Cuenta con proveedor : <Valor>Valores de ejemplo para los campos anteriores:Abrev.responsable : <01>Cuenta con proveedor : <1710-CARR502> . |  |  |
| 11 | Guardar los datos | Seleccionar Grabar . | El sistema muestra un mensaje que indica que el objeto se ha grabado. |  |

## Apéndice

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
> Flagged while digesting this document, not verified: Machine-translated text has inconsistencies (e.g., 'Interlocutor comercial' vs 'socio comercial', untranslated 'Change in BP Role'); step 4 says alphanumeric external numbering while examples use numeric BP03.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Org-unit table in prerequisites is empty and summary table lists only the first procedure.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-411]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 70,671 chars in the whole document
