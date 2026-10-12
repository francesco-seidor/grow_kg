---
id: 08-sales-order-management/script-de-datos-maestros-crear-script-de-datos-maestros-de-jerarquia-d
title: Script de datos maestros - Crear script de datos maestros de jerarquía de clientes (6N3) (6N3_S4CLD2608_Master_Data_ES_XX)
description: "Spanish test script (6N3) for SAP S/4HANA Cloud Public Edition 2608: creating customer master data (general, company code, sales area) and customer hierarchies."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-hierarchies]
aliases: [6N3_S4CLD2608_Master_Data_ES_XX]
keywords: [Customer Hierarchies, customer master data, company code data, sales area data, business partner roles, partner functions, tax identification numbers, organizational units, country-specific requirements, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-516
topic: 08-sales-order-management/customer-hierarchies
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear script de datos maestros de jerarquía de clientes (6N3) (6N3_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Customer Hierarchies** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear script de datos maestros de jerarquía de clientes (6N3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894850)

[2 Requisitos previos 3](#_Toc233894851)

[2.1 Acceso al sistema 3](#_Toc233894852)

[2.2 Roles 3](#_Toc233894853)

[2.3 Unidades organizativas necesarias 3](#_Toc233894854)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894855)

[3 Tabla de resumen 5](#_Toc233894856)

[4 Procedimientos de prueba 6](#_Toc233894857)

[4.1 Creación de datos maestros de cliente - Datos generales 6](#_Toc233894858)

[4.2 Creación de datos maestros de cliente - Datos de sociedad 13](#_Toc233894859)

[4.3 Creación de datos maestros de cliente - Datos de área de ventas 18](#_Toc233894860)

[4.4 Creación de jerarquías de clientes 24](#_Toc233894861)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

El Gestionar jerarquías de clientes le ayuda a crear, copiar, editar y borrar jerarquías de clientes y asignar varias niveles de nodos de jerarquía. También puede gestionar los períodos de validez de las jerarquías y se tendrá en cuenta una jerarquía para procesa solo durante este período de tiempo especificado.

Jerarquía de clientes - Análisis : este tipo de jerarquía se utiliza en el análisis de ventas para proyectar datos transaccionales y obtener información esclarecedora.

Jerarquía de clientes - Ventas : este tipo de jerarquía se utiliza para el precio determinación en documentos de ventas y documentos de facturación. Esta jerarquía contiene cliente información que pertenece a la misma área de ventas. El sistema le permite añadir nodos de texto, que puede denotar cualquier tipo de información, como estado, distrito, etc., que ayude organizar mejor la jerarquía. Además, estos nodos de texto se pueden actualizar como relevante para la determinación de precios. La jerarquía también contiene nodos de socio comercial que deben tener un área de ventas de cliente asociada.

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
| Especialista en datos maestros - Datos de socio comercial | SAP_BR_BUPA_MASTER_SPECIALIST | Datos maestros - Socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Unidades organizativas necesarias

Las unidades organizativas necesarias se enumeran a continuación:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos | Independiente de las unidades organizativas | Descripción de interlocutor comercial, Número de cliente, Relevante para la determinación de precios, etc. | Los datos básicos solo existen una vez para un registro de datos maestros de interlocutor comercial. | N/D |
| Datos de ventas | Organización de ventas, canal de distribución y sector | Datos fiscales, Relevante para la determinación de precios, etc. | Los datos de ventas pueden existir para cada organización de ventas de la estructura de su empresa para la que el registro de datos maestros del interlocutor comercial es utilizado. | Organización de ventasCanal de distribuciónSector |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de interlocutor comercial pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los datos maestros obligatorios y opcionales objetos de datos que se utilizarán en un registro de datos maestros de interlocutor comercial.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Área de ventas |  | Obligatorio | La asignación de un área de ventas a los datos maestros del interlocutor comercial es obligatoria para la jerarquía de clientes. |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de cliente (F0850A) | Se ha creado el Maestro de clientes - Datos generales. |
| [Creación de datos maestros de cliente - Datos de sociedad](#unique_9) [página ] 13 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de cliente (F0850A) | Maestro de clientes - Se han creado los datos de sociedad. |
| [Creación de datos maestros de cliente - Datos de área de ventas](#unique_10) [página ] 18 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de cliente (F0850A) | Maestro de clientes: se crean los datos del área de ventas. |
| [Creación de jerarquías de clientes](#unique_11) [página ] 24 | Especialista en datos maestros - Datos de socio comercial | Gestionar jerarquías de clientes (F5794) | Se crean jerarquías de clientes. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de datos maestros de cliente - Datos generales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de cliente. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

La siguiente nota es solo para Arabia Saudí.

|  |
| --- |
| Nota Para cumplir con las normativas de la factura electrónica ZATCA, asegúrese de que todos los campos obligatorios, como Calle 2 , Calle 3 , Distrito , etc., se han introducido correctamente en los formularios de interlocutor comercial antes de generar documentos electrónicos. Esto es necesario para validar correctamente las facturas electrónicas antes de enviarlas al portal de la autoridad fiscal.Esta información se utiliza para rellenar las etiquetas XML adecuadas según lo requiera ZATCA, según el tipo de documento electrónico. Para obtener más información sobre las directrices de ZATCA, consulte Directrices estándar de implementación XML de factura electrónica. |

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Crear una organización de socio comercial | Seleccionar Organización . | El Crear organización se visualiza. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Interlocutor comercial : <Introduzca un ID de socio comercial que empiece por una letra>Agrupación : seleccione, por ejemplo, Numeración alfanumérica externa .El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) Rol de . Mantenga esta opción.Pulsar Intro .Nota Para obtener más información sobre los detalles de Datos generales, consulte la [Requisitos previos](#unique_2) [página ] 3 sección. |  |  |
| 5 | Introducir datos de dirección | El Dirección en la pestaña Nombre introduzca los siguientes datos:Título : <Seleccione un título>Nombre : <Nombre> |  |  |
| 6 | Introducir datos de dirección | En la Dirección estándar introduzca la dirección. |  |  |
| 7 | Introducir huso horario y huso horario de transporte | En la Dirección sección, seleccione Más campos . Indique los siguientes datos:Huso horario : <Huso horario>Zona de transporte : <Zona de transporte> |  |  |
| Solo para Tailandia | Introducir datos de dirección adicionales (solo para Tailandia) | En la Dirección sección, seleccione Más e introduzca los siguientes datos:Código de edificio : <Edificio>Sala : <Número de sala>Planta : <Nº planta>Calle 2 : <Moo>Calle 3 : <Soi/Lane>Calle : <Carretera>Número : <no>Otra ciudad : <Subdistrito>Distrito : <Distrito/Sección>Población : <Provincia>Código postal : <Código postal>Teléfono : <Número de teléfono> |  |  |
| 8 | Introducir términos de búsqueda | El Dirección en la pestaña Conceptos de búsqueda introduzca uno o dos conceptos de búsqueda para el interlocutor comercial. |  |  |
| 9 | Introducir datos de comunicación | En la Comunicación sección, en la Idioma introduzca el idioma preferido del interlocutor comercial. |  |  |
| Solo para Japón | Introducir datos de sector (solo para Japón) | El Identificación en la pestaña Sectores sección, seleccione Todos los sistemas sectoriales . Introduzca los siguientes datos:Sistema de ramos : Seleccionar Banco de Japón .Sector : <Seleccione un número de sector>Sector estándar : <No seleccionado> |  |  |
| 10 | Introducir números de identificación fiscal | El Identificación en la pestaña Números de identificación fiscal introduzca los siguientes datos:Categoría : <Categoría>Número de identificación fiscal : <Número de identificación fiscal>Nota Seleccione la categoría correcta aplicable al país/región del socio comercial. Por ejemplo, para un socio comercial alemán, actualice un valor para la categoría DE1, que representa el número de identificación fiscal de IVA utilizado comúnmente (Umsatzsteuer-Identifikationsnummer). |  |  |
| 11 | Introducir cuentas bancarias | El Transacciones de pago en la pestaña Datos bancarios introduzca los siguientes datos:Clave de banco : <Clave de banco>Cta.banc. : <Cuenta bancaria>Atención Las claves de banco deben definirse previamente. Utilice la ayuda para entradas para obtener más información sobre las entradas permitidas en este campo. |  |  |
| 12 | Guardar los datos | Guarde las entradas. | Se han guardado los datos. |  |

Procedimiento: Opción 2 - Gestionar datos maestros de cliente

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de cliente (F0850A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de cliente (F0850A) . | Se abre la aplicación. |  |
| 3 | Crear nueva organización | El Maestro de clientes , seleccione Crear > Organización . | El Crear organización se visualiza en modo de edición. |  |
| 4 | Introducir datos básicos | El Crear organización , efectúe las siguientes entradas:Información generalInterlocutor comercial : Por ejemplo, Z … (es decir, cualquier ID alfanumérico externo, ya que debe empezar por una letra).Agrupación : Por ejemplo, BPAB .Debe asignar cada interlocutor comercial a una agrupación al crear el registro de interlocutor comercial. La agrupación determina el rango de números. No puede modificar la asignación posteriormente.Rol de interlocutor comercial : seleccione un rol, por ejemplo, FLCU01 - Cliente .Nota Se debe crear un cliente con el rol de interlocutor comercial FLCU00 - Cliente (Gestión financiera) o con el rol de interlocutor comercial FLCU01 - Cliente , o con ambos roles. El rol de interlocutor comercial FLCU00 - Cliente (Gestión financiera) se utiliza en la contabilidad financiera y el rol de interlocutor comercial FLCU01 - Cliente se utiliza en Ventas.Título de organización : Por ejemplo, Sociedad GL (0003) .Nombre 1 : <Introduzca un nombre>Dirección estándarPaís/Región : Por ejemplo, EE. UU. .Idioma : Por ejemplo, ES . |  |  |
| 5 | Cerrar la pantalla Crear organización | El Crear organización , seleccione OK . | El Crear organización la pantalla está cerrada. El Cliente nuevo se visualiza. |  |
| 6 | Elegir roles | El Cliente nuevo , seleccione Roles . | Ha navegado a Roles sección. |  |
| 7 | Seleccione Crear. | En la Roles sección, seleccione Crear . |  |  |
| 8 | Introducir datos de roles adicionales | En la Roles sección, seleccione Crear y realice la siguiente entrada:Rol de interlocutor comercial : seleccione el rol adicional, por ejemplo, FLCU00 - Cliente (Gestión financiera)Nota Se debe crear un cliente con el rol de interlocutor comercial FLCU00 - Cliente (Gestión financiera) o con el rol de interlocutor comercial FLCU01 - Cliente , o con ambos roles. El rol de interlocutor comercial FLCU00 - Cliente (Gestión financiera) se utiliza en la contabilidad financiera y el rol de interlocutor comercial FLCU01 - Cliente se utiliza en Ventas. | Después de completar la actualización de todos los roles de interlocutor comercial, se visualizan en la Roles en la sección Cliente nuevo pantalla. |  |
| 9 | Seleccionar datos básicos | El Cliente nuevo , seleccione Datos básicos y vaya a la Información del cliente sección. | Ha navegado a Información del cliente sección. |  |
| 10 | Introducir información del cliente | En la Información del cliente , realice las siguientes entradas:Clasificación de clientes : Por ejemplo, A - Cliente .Grupo de cuentas de cliente : <Grupo de cuentas de deudor>Nota Cuando la agrupación de interlocutores comerciales permite una asignación flexible de grupos de cuentas, puede seleccionar el grupo de cuentas que se va a utilizar y desviarse del valor propuesto. Para obtener más detalles sobre la agrupación de socios comerciales y cómo se relaciona con la numeración de ID, consulte la Agrupación de interlocutores comerciales y rangos de números en este documento. |  |  |
| 11 | Seleccionar información adicional | El Cliente nuevo , seleccione Datos básicos y vaya a la Información adicional sección. | Ha navegado a Información adicional sección. |  |
| 12 | Introducir información adicional | En la Información adicional , realice las siguientes entradas:Estación exprés : <Nombre de estación exprés>Centro : <Seleccionar un centro>Código de sector 1 : <Seleccione un código de sector>Grupo de condiciones 1 : <Seleccione un grupo de condiciones> |  |  |
| 13 | Seleccionar dirección | El Cliente nuevo , seleccione Dirección y vaya a la Dirección estándar sección. | Ha navegado a Dirección estándar sección. |  |
| 14 | Introducir datos de dirección | En la Dirección estándar , realice las siguientes entradas:Calle : Por ejemplo, Augusta Ave SE .Seleccione el país/región si no lo ha hecho en el paso 4.Número : Por ejemplo, 200 .Código postal : Por ejemplo, 30315-1402 .Población : Por ejemplo, Atlanta .Región : Por ejemplo, GA .Nota Cuando crea un interlocutor comercial ubicado en los Estados Unidos, el código de domicilio fiscal se determina automáticamente. Sin embargo, debe introducir la dirección correcta y completa, ya que la jurisdicción se deriva en función de las entradas de Región y Código postal.Comunicación estándarSeleccione el idioma si no lo ha hecho en el paso 4.Teléfono móvil : <Teléfono móvil>Correo electrónico : Añada una dirección de correo electrónico, por ejemplo, contact@Z.com . |  |  |
| 15 | Seleccionar cuentas bancarias | El Cliente nuevo , seleccione Cuentas bancarias . | Ha navegado a Cuentas bancarias sección. |  |
| 16 | Seleccione Crear. | En la Cuentas bancarias sección, seleccione Crear . | Se visualiza una entrada para la cuenta bancaria en modo de edición. |  |
| 17 | Introducir datos bancarios | El Nueva cuenta bancaria , efectúe las siguientes entradas y seleccione Aplicar :ID : Por ejemplo, BNK1País del banco : Por ejemplo, EE. UU. .Clave de banco : Por ejemplo, 011000390 - Banco 1 BANCO DE MUESTRA .Número de cuenta : Por ejemplo, 102030 .Realice entradas para todos los demás campos para Datos bancarios en función de sus necesidades. | Se le redirigirá a la Cliente nuevo pantalla. |  |
| 18 | Seleccionar números de identificación | El Cliente nuevo , seleccione Números de identificación y vaya a la Números de identificación fiscal sección. | Ha navegado a Números de identificación fiscal sección. |  |
| 19 | Seleccione Crear. | En la Números de identificación fiscal sección, seleccione Crear . |  |  |
| 20 | Introducir datos de número de identificación fiscal | En la Números de identificación fiscal , realice las siguientes entradas:Categoría fiscal : <Seleccione una categoría fiscal>Número de identificación fiscal : <Número de identificación fiscal>Los números de identificación fiscal que se introducen dependen de los requisitos específicos del país/región.Nota Seleccione la categoría correcta que se aplica al país/región del cliente. Por ejemplo, para un socio comercial alemán, actualice un valor para la categoría DE1, que representa el número de identificación fiscal de IVA utilizado comúnmente (Umsatzsteuer-Identifikationsnummer).Realice solo entradas para los campos que necesite; de lo contrario, seleccione Borrar para eliminar el conjunto de datos (vacío). |  |  |
| 21 | Seleccionar categorías fiscales | El Cliente nuevo , seleccione Categorías fiscales . | Ha navegado a Categorías fiscales sección. |  |
| 22 | Seleccione Crear. | En la Categorías fiscales sección, seleccione Crear . |  |  |
| 23 | Introducir datos de categorías fiscales (opcional) | En la Categorías fiscales , realice las siguientes entradas:Indicador de impuestos : Por ejemplo, COC Cámara de comercio .Número de certificado de exención : <Número de certificado de exención>Tasa de certificado de exención : Por ejemplo, 800 .Fecha de inicio de exención : <Fecha de inicio de exención> .Fecha de fin de exención : <Fecha de fin de exención> |  |  |
| 24 | Seleccionar textos | El Cliente nuevo , seleccione Textos . | Ha navegado a Textos sección. |  |
| 25 | Crear textos | En la Textos sección, seleccione Crear y realice las siguientes entradas:Idioma : Por ejemplo, ES .ID : Por ejemplo, 01 .Texto explicativo : <Introduzca un texto explicativo> |  |  |
| 26 | Seleccionar datos básicos | Seleccionar Datos básicos > Clientes adicionales . | Ha navegado a Clientes adicionales sección. |  |
| 27 | Añadir datos de cliente adicionales | En la Clientes adicionales sección, seleccione Crear .Añada los datos necesarios como se describe en los pasos anteriores.Nota Este escenario es para varias asignaciones de clientes a los mismos interlocutores comerciales y, por lo tanto, se aplican los mismos datos maestros que se describen en los pasos anteriores.Si se requieren datos adicionales, como datos de ventas y datos de sociedad, consulte las secciones anteriores que describen, por ejemplo, cómo añadir datos de ventas y datos de sociedad. |  |  |
| 28 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que el objeto se ha guardado . |  |

### Creación de datos maestros de cliente - Datos de sociedad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de cliente. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6, antes de continuar con este capítulo.

Siga el procedimiento después de haber grabado las entradas de Datos generales, como se describe en el capítulo anterior.

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/ Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Buscar y abrir | Busque y abra el interlocutor comercial (cliente) que ha creado en el capítulo anterior: [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6. | El interlocutor comercial se visualiza en la lista de búsqueda. |  |
| 4 | Cambiar a modo de modificación | Seleccionar Cambiar entre visualizar y modificar (F6) para cambiar al modo de modificación. |  |  |
| 5 | Modificar rol de interlocutor comercial | En la Modificación en rol IC seleccione el siguiente valor:Deudor (contabilidad financiera)Nota La clave técnica de este rol de interlocutor comercial es FLCU00. |  |  |
| 6 | Abrir datos de sociedad | Seleccionar Sociedad . | El Sociedad se visualiza. |  |
| 7 | Introducir sociedad | Introduzca el Sociedad . |  |  |
| 8 | Introducir datos de contabilidad de cliente | El Cliente: Gestión de cuentas en la pestaña Gestión de cuentas , realice las siguientes entradas:Cuenta asociada : 140000 (Clientes - Créditos nacionales)Clave de clasificación : <Clave de clasificación> |  |  |
| 9 | Introducir datos de pago de cliente | El Deudor: Operaciones de pago en la pestaña Datos de pago , realice una entrada para el siguiente campo:Condiciones de pago : <Condiciones de pago> |  |  |
| 10 | Introducir datos de pago de cliente | El Deudor: Operaciones de pago en la pestaña Transacciones de pago automático , realice entradas para los siguientes campos:Vías de pago : <Vías de pago>Banco propio : <Banco propio>Nota Pulsar F4 para abrir la selección en el campo Vías de pago. |  |  |
| 11 | Introducir datos de correspondencia de cliente | El Deudor: Correspondencia en la pestaña Correspondencia , realice las siguientes entradas:Responsable : <Responsable>Cuenta en cliente : <Cuenta en el cliente> |  |  |
| Solo para Tailandia | Código de sucursal (solo para Tailandia) | Abrir datos generales, en la Ampl.esp.país ficha, actualice los datos de Código de sucursal junto con la dirección y el Código de sucursal por defecto para este interlocutor comercial.Para la dirección del código de sucursal, seleccione Dirección e introduzca los siguientes datos:Nombre (Primeras dos líneas): <Nombre del contribuyente>País : JUCódigo de edificio : <Nombre del edificio/Población>Sala : <Número de sala>Planta : <Planta>Calle 2 : <Moo>Calle 3 : <Trok/Soi>Calle : <Carretera>Número : <no>Otra ciudad : <Tumbol/Subsección>Distrito : <Distrito/Sección>Población : <Provincia>Código postal : <Código postal>Teléfono : <Número de teléfono>Nota Cuando hay más de un código de sucursal para un interlocutor comercial, debe actualizar cada código de sucursal junto con la dirección de cada código de sucursal. También debe fijar un Código de sucursal que el Interlocutor comercial suele utilizar por defecto. |  |  |
| Solo para Japón | Resumen de facturas (solo para Japón) | El Ampl.esp.país Si este cliente es relevante para el resumen de facturas, realice las siguientes entradas según sus necesidades:En la Japón: Resumen de facturas - Rol sección:Rol IS : <Rol IS>En caso de que Rol IS es P: Pagador de resumen de facturas , en la Japón: Resumen de facturas - Factura sección:Rango de números: MI : <Rango de números: MI>Impuesto de cálculo en MI : <Impuesto de cálculo en MI>Mover fecha de vencimiento : <Mover fecha de vencimiento>Condición de pago de regla : <Condición de pago de regla>Inicio de validez : <Inicio de validez>Condición de pago : <Condición de pago>En la Japón: Resumen de facturas - Pago sección:Rango de números: PI : <Rango de números: PI>Receptor del pago de gastos bancarios : <Receptor del pago de gastos bancarios>ID de patrón de gastos bancarios : <ID de patrón de gastos bancarios>Relevante para casos especiales : <NO seleccionar>País del banco : <País del banco>Clave de banco : <Clave de banco>Número de cuenta virtual : <Número de cuenta virtual>Número actual : <Número secuencial>Nombre de receptor alternativo del pago : <Nombre de receptor alternativo del pago>Nombre de banco de contador : <Nombre de banco contador>Nombre de sucursal bancaria de contador : <Nombre de sucursal del banco contador>En caso de que Rol IS es M: Destinatarios de factura mensuales en el Japón: Resumen de facturas - Rol sección:Pagador de resumen de facturas : <Pagador de resumen de facturas>En la Japón: Resumen de facturas - Factura sección:Rango de números: MI : <Rango de números: MI>Impuesto de cálculo en MI : <Impuesto de cálculo en MI>En caso de que Rol IS es C: (Resumen de facturas) Cliente en el Japón: Resumen de facturas - Rol sección:Destinatario de resumen de factura : <Destinatario de resumen de facturas> |  |  |
| 12 | Guardar los datos | Guarde las entradas. | La entrada en la Modificación en rol IC modificaciones de campo de Deudor FI (nuevo) hasta Deudor FI (definido) . |  |

Procedimiento: Opción 2 - Gestionar datos maestros de cliente

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de cliente (F0850A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de cliente (F0850A) . | Se abre la aplicación. |  |
| 3 | Buscar y abrir | Busque y abra el interlocutor comercial (cliente) que ha creado en el capítulo anterior: [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6. |  |  |
| 4 | Seleccione Editar. | Seleccionar Editar . | El Maestro de clientes se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 5 | Seleccionar sociedad | El Maestro de clientes seleccione el pulsador Sociedades pestaña. | Ha navegado a Sociedades sección. |  |
| 6 | Seleccione Crear. | En la Sociedades sección, seleccione Crear . | El Nueva sociedad se visualiza en modo de edición. |  |
| 7 | Introducir datos de sociedad | El Nueva sociedad , efectúe las siguientes entradas:Sociedad : introduzca la sociedad, por ejemplo, 1710 .El Correspondencia pestaña:Responsable : Por ejemplo: 01 Sra. Smith .El Finanzas pestaña:Finanzas - ContabilidadCuenta asociada : Por ejemplo, 12100000: Créditos internacionales .Clave de clasificación : Por ejemplo, 009 Número de documento externo .Finanzas: Datos de pagoCondiciones de pago : Por ejemplo, 0001 .Finanzas - Transacciones de pago automáticoVías de pago : Por ejemplo, C (Verifique, por ejemplo, para EE. UU.)El Datos de reclamación pestaña:Área de reclamación : Unidad organizativa que utiliza para procesar el programa de reclamación, por ejemplo, por sector u organización de ventas.Procedimiento de reclamación, Bloqueo de reclamación, Destinatario de reclamación, Responsable de reclamación : Seleccione de la ayuda para entradas.Nivel de reclamación : Por ejemplo, 0 .Última reclamación : Por ejemplo, 10.02.2020 .Procedimiento de reclamación legal de : Por ejemplo, 11.02.2020 .El Textos pestaña:En la Textos sección, seleccione Crear y realice las siguientes entradas:.Idioma : Por ejemplo, ES .ID : Por ejemplo, 01 .Texto explicativo : <Introduzca un texto explicativo> |  |  |
| 8 | Volver a la pantalla principal | Seleccionar Aplicar . |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que el objeto se ha grabado . |  |

### Creación de datos maestros de cliente - Datos de área de ventas

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de cliente. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6, antes de continuar con este capítulo.

Siga el procedimiento después de haber guardado las entradas de Datos generales, como se describe en el capítulo anterior, en la Visualizar organización: Nombre de cliente pantalla.

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Cambiar a modo de modificación | Seleccionar Cambiar entre visualizar y modificar (F6) para cambiar al modo de modificación. |  |  |
| 4 | Modificar rol de interlocutor comercial | En la Modificación en rol IC seleccione el siguiente valor:ClienteNota La clave técnica de este rol de interlocutor comercial es FLCU01. |  |  |
| 5 | Abrir área de ventas | Seleccionar Comercial en la pantalla. | El Área de ventas se visualiza. |  |
| 6 | Introducir datos de área de ventas | Realice las siguientes entradas:Org.ventas : <Organización de ventas>Canal distrib. : <Canal de distribución>Sector : <Sector>Nota Estas tres entradas (Organización de ventas, Canal de distribución y Sector) forman el área de ventas. En muchos casos, el área de ventas fija el objetivo para el procesamiento de ventas, por ejemplo, dentro del pedido de cliente o la determinación de precios. |  |  |
| 7 | Introducir datos de pedidos de cliente | El Pedidos en la pestaña Orden , realice la siguiente entrada:Moneda : <Moneda> |  |  |
| 8 | Introducir datos de expedición | El Expedición en la pestaña Expedición , realice las siguientes entradas:Prioridad de entrega : <Prioridad de entrega>Centro suministrador : <Centro suministrador>Condiciones de expedición : <Condiciones de expedición> |  |  |
| 9 | Introducir datos de facturación | El Facturación en la pestaña Condiciones de entrega y pago , realice las siguientes entradas:Incoterms : EXW (puesto en fábrica)Puede actualizar el valor de incoterm y proporcionar su descripción.Nota Los campos para incoterms son interdependientes. Por ejemplo, si actualiza el valor para el Incoterms debe proporcionar información para el ID ubic.incoterm 1 y Ubicación de incoterm 1 campos.Condiciones de pago : <Seleccione las condiciones de pago>Nota Las condiciones de pago definidas aquí se copian en un pedido de cliente y se utilizan en lugar de las condiciones de pago definidas en el nivel de sociedad. |  |  |
| 10 | Introducir datos de contabilidad | En la Contabilidad , realice la siguiente entrada:Gr.imputación clte. : <Seleccione el grupo de imputación para el cliente>Por ejemplo, los clientes nacionales se pueden asignar al grupo de imputación 01 y los clientes extranjeros se pueden asignar al grupo de imputación 02 . Vaya a la ayuda para entradas para ver más opciones. |  |  |
| 11 | Introducir datos fiscales | En la IVA repercutido seleccione el siguiente valor para la entrada existente en la tabla:Clasif.fiscal : <1>Por ejemplo, valor <1> significa que este cliente está totalmente sujeto a impuestos. |  |  |
| 12 | Modificar datos de funciones de interlocutor | El Funciones de interlocutor , las siguientes 4 funciones de interlocutor estándar están disponibles para el cliente. Puede crear las 4 funciones de interlocutor:SP - SolicitanteIC - Destinatario de facturaPY - PagadorSH - Destinatario de mercancíasNota Las 4 funciones de interlocutor mencionadas anteriormente son el conjunto mínimo de funciones de interlocutor que deben asignarse a un registro de datos maestros de cliente para trabajar en un proceso de venta y distribución estándar. |  |  |
| 13 | Introducir texto explicativo | En la Texto de cliente introduzca los detalles de los datos de ventas. Tenga en cuenta que se trata de un campo de solo lectura. Utilice la Editar texto para modificar el texto explicativo. |  |  |
| 14 | Abrir datos generales | Seleccionar Datos generales en la pantalla. |  |  |
| 15 | Introducir datos de organización | El Deudor: Datos generales en la pestaña Marketing , realice la siguiente entrada:Clasif.clientes : <Seleccione una clasificación de cliente> |  |  |
| 16 | Guardar los datos | Guarde las entradas. |  |  |

Procedimiento: Opción 2 - Gestionar datos maestros de cliente

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de cliente (F0850A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de cliente (F0850A) . | Se abre la aplicación. |  |
| 3 | Buscar y abrir | Busque y abra el interlocutor comercial (cliente) que ha creado en el capítulo anterior: [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6. |  |  |
| 4 | Seleccione Editar. | Seleccionar Editar . | El Maestro de clientes se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 5 | Seleccionar área de ventas | El Maestro de clientes , seleccione Áreas de ventas .Nota La pestaña Áreas de ventas solo está disponible si el interlocutor comercial tiene el rol FLCU01 (Cliente). | El Áreas de ventas Se muestra la sección. |  |
| 6 | Seleccione Crear. | En la Áreas de ventas sección, seleccione Crear . | El Nueva área de ventas se visualiza en modo de edición. |  |
| 7 | Introducir datos de área de ventas | El Nueva área de ventas , efectúe las siguientes entradas:Datos generalesOrganización de ventas : Por ejemplo, 1710 .Nota Si selecciona la organización de ventas de la ayuda para entradas, los siguientes campos ( Canal de distribución y Sector ) se introducen automáticamente.Canal de distribución : Por ejemplo, 10 .Sector : Por ejemplo, 00 .Detalles de área de ventasDetalles de área de ventas - Pedidos de cliente :Cuenta en cliente : <Introduzca su cuenta en el cliente>Moneda : Por ejemplo, USD .Detalles de área de ventas - Facturación :Incoterms : Por ejemplo, EXW .Ubicación de incoterms 1 : Por ejemplo, Palo Alto .Condiciones de pago : Por ejemplo, 0001 .Detalles de área de ventas - Expedición :Prioridad de entrega : Por ejemplo, Normal .Centro de entrega : Por ejemplo, 1710 .Condiciones de expedición : Por ejemplo, Inmediatamente .Detalles de área de ventas - Contabilidad :Grupo de imputación : Por ejemplo, Ingresos nacionales .Detalles de área de ventas: Determinación de precios y estadísticas :Esquema de cliente : Por ejemplo, Procedimiento 01 . |  |  |
| 8 | Seleccionar textos | El Nueva área de ventas , seleccione Textos . |  |  |
| 9 | Seleccione Crear. | En la Textos sección, seleccione Crear y realice las siguientes entradas:Idioma : Por ejemplo, ES .ID : seleccione un número de ID o introduzca un número de ID manualmente, por ejemplo, 01 .Texto explicativo : <introduzca un texto explicativo> |  |  |
| 10 | Seleccionar impuestos | El Nueva área de ventas , seleccione Impuestos . | El Impuestos Se muestra la sección. |  |
| 11 | Seleccionar país/región y categoría fiscal | En la Impuestos seleccione la entrada para un país/región, por ejemplo, EE. UU. (EE. UU.) .Nota El Categoría fiscal la entrada depende de la ubicación del Cliente. Por ejemplo, UTXJ es la categoría fiscal para crear un cliente de EE. UU. y TTXJ es la categoría fiscal para crear un cliente DE. | El Impuestos de área de ventas se visualiza en modo de edición. |  |
| 12 | Introducir clasificación fiscal | El Impuesto , realice la siguiente entrada:Clasificación fiscal : seleccione, por ejemplo, Sujeto a impuestos (1) . |  |  |
| 13 | Seleccione Aplicar. | Seleccionar Aplicar . | Volverá a la vista principal. |  |
| 14 | Seleccionar funciones de interlocutor | El Nueva área de ventas , seleccione Funciones de socio . | El Funciones de socio Se muestra la sección. |  |
| 15 | Seleccione Crear. | En la Funciones de interlocutor sección, seleccione Crear . | El Funciones de interlocutor se muestra en modo de edición. |  |
| 16 | Introducir datos de función de interlocutor | Seleccione una función de interlocutor, por ejemplo, Solicitante (SP) .Seleccione la entrada para la función de interlocutor y en la Datos generales seleccione un número de interlocutor e introduzca una descripción de interlocutor. |  |  |
| 17 | Volver a la vista principal | Seleccionar Aplicar . | La función de interlocutor añadida se visualiza en la vista principal. |  |
| 18 | Introducir datos de función de interlocutor | Repita los pasos 15 a 17 (para añadir una función de interlocutor) para incluir datos de función de interlocutor adicionales. Añada los siguientes roles de interlocutor:Nota Las claves de función de interlocutor de dos caracteres dependen del idioma. Las claves documentadas aquí son válidas para el idioma de trabajo inglés.En otros idiomas, estas claves pueden ser diferentes. Por ejemplo, las claves de función de interlocutor de dos caracteres en alemán son:AG para solicitante (Auftraggeber)EM para destinatario de mercancías (Warenempfänger)RE para Destinatario de factura (Rechnungsempfänger)GR para pagador (Regulierer)Rol de interlocutor: Destinatario de mercancías :Función de interlocutor : SH Destinatario de mercancíasFunción de interlocutor: Destinatario de factura :Función de interlocutor : IC Destinatario de facturaFunción de interlocutor: Pagador PY :Función de interlocutor : Pagador PY |  |  |
| 19 | Volver a la vista principal | Seleccionar Aplicar .Nota Asegúrese de que el mensaje del sistema Borrador actualizado se muestra en la parte inferior de la vista antes de volver a la vista principal. |  |  |
| 20 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que el objeto se ha grabado . |  |

### Creación de jerarquías de clientes

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para la jerarquía de clientes del tipo ventas y análisis mediante Gestionar jerarquías de clientes (F5794) aplicación.

Requisito previo

Debe completar el capítulo anterior, [Creación de datos maestros de cliente - Datos generales](#unique_8) [página ] 6, antes de continuar con esto capítulo.

Siga el procedimiento después de haber grabado las entradas de Datos generales, como se describe en el capítulo anterior.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar jerarquías de clientes (F5794) . | Se abre la aplicación. |  |
| 3 | Crear nueva jerarquía | El Gestionar jerarquías de clientes , seleccione Crear . |  |  |
| 4 | Seleccionar tipo de jerarquía | Seleccione el tipo de jerarquía de las siguientes opciones:Jerarquía de clientes - VentasJerarquía de clientes - Análisis |  |  |
| 5 | Introducir datos relacionados con la jerarquía | En la Crear nuevas jerarquías indique el ID de jerarquía e introduzca otros datos necesarios. |  |  |
| 6 | Editar subnodo | Una vez creado el nodo superior con el ID de jerarquía proporcionado en el paso anterior, añada subnodos a este nodo superior. Podrá realice las siguientes acciones:Modifique el nombre de la jerarquía.Modificar valideces y otros detalles como ventas, distribución, sector, etc.Simular opción como on/off.Borre los subnodos asignados a la jerarquía. |  |  |
| 7 | Opciones de subnodo | Seleccione el nodo superior definido en el paso anterior.Seleccione la opción para definir el subnodo. A continuación se muestran los tres tipos de subnodos que se pueden añadir:Subnodo : es un nodo de texto que se puede personalizar en función de sus necesidades empresariales. Puede contener varios subnodos.Subnodo - Socio comercial : este es un nodo de socio comercial, que puede contener varios subnodos. El sistema verifica automáticamente que el interlocutor comercial añadido a la jerarquía pertenece a la misma área de ventas.Interlocutor comercial : Este es un nodo de socio comercial, sin embargo, es un nodo final y no puede contener más nodos. El sistema verifica automáticamente que el socio comercial añadido a la jerarquía pertenezca a las mismas ventas área. | El Datos maestros - Producto se visualiza.Se han guardado los datos. |  |
| 8 | Crear subnodo | Seleccione el nodo superior.Seleccionar Editar . Seleccione + para añadir un subnodo.Seleccione los registros maestros de cliente relevantes que ya existen en el sistema.Si el tipo de jerarquía es Ventas, seleccione si el subode es relevante para la determinación de precios.Nota Los subnodos también se pueden crear en modo de entrada rápida, lo que ayuda a crear varios subnodos de una sola vez. | Asegúrese de que el subnodo se crea y se visualiza debajo del nodo raíz.Nota Si los valores de área de ventas/sector/distribución no coinciden con el cliente relevante añadido anteriormente, el El subnodo no se puede añadir y un mensaje de error el cliente no tiene Ventas/Sector/Distribución muestra. |  |
| 9 | Activar jerarquía | Seleccionar Activar . | La jerarquía de clientes está activada. |  |
| 10 | Borrar jerarquía | Seleccionar Borrar si desea borrar una jerarquía. |  |  |
| 11 | Exportación/Importación | Seleccionar Exportación/Importación si desea exportar o importar una jerarquía. | Puede exportar o importar una estructura jerárquica. |  |

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
- related-to :: [[08-sales-order-management/6n3-517]]
- related-to :: [[08-sales-order-management/6n3-519]]
- related-to :: [[08-sales-order-management/create-customer-hierarchy-master-data-script-6n3-515]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-script-de-dados-mestre-de-hierarquia-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 48,515 chars in the whole document
