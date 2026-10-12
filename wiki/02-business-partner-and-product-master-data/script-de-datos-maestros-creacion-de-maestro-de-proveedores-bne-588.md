---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-proveedores-bne-588
title: Script de datos maestros - Creación de maestro de proveedores (BNE) (BNE_S4CLD2608_Master_Data_ES_XX)
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: test steps to create a supplier master (general, company code, purchasing org data)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/supplier-master]
aliases: [BNE_S4CLD2608_Master_Data_ES_XX]
keywords: [Supplier Master Data, business partner creation, company code data, purchasing organization data, business partner groupings, number ranges, business partner roles, account groups, business roles, withholding tax]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-588
topic: 02-business-partner-and-product-master-data/supplier-master
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de maestro de proveedores (BNE) (BNE_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Supplier Master Data** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de maestro de proveedores - MDS (BNE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894937)

[2 Requisitos previos 3](#_Toc233894938)

[2.1 Acceso al sistema 3](#_Toc233894939)

[2.2 Roles 3](#_Toc233894940)

[2.3 Pasos preliminares 3](#_Toc233894941)

[2.4 Unidades organizativas necesarias 4](#_Toc233894942)

[2.5 Datos maestros obligatorios y opcionales 5](#_Toc233894943)

[2.6 Parámetros principales para la creación de datos 5](#_Toc233894944)

[2.6.1 Agrupación de interlocutores comerciales y rangos de números 5](#_Toc233894945)

[2.6.2 ID de socio comercial 6](#_Toc233894946)

[2.6.3 Función de interlocutor comercial 7](#_Toc233894947)

[2.6.4 Grupo de cuentas 7](#_Toc233894948)

[3 Tabla de resumen 8](#_Toc233894949)

[4 Procedimientos de prueba 9](#_Toc233894950)

[4.1 Creación de datos maestros de proveedor - Datos generales 9](#_Toc233894951)

[4.2 Creación de datos maestros de proveedor - Datos de sociedad 16](#_Toc233894952)

[4.3 Creación de datos maestros de proveedor - Datos de organización de compras 23](#_Toc233894953)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Contexto empresarial

Un proveedor es un interlocutor comercial que entrega y vende mercancías y servicios a su organización. Un interlocutor comercial puede ser un proveedor y un cliente al mismo tiempo si, por ejemplo, su proveedor también le compra mercancías.

Un maestro de proveedores contiene información sobre el proveedor, como su nombre, dirección, datos bancarios, datos fiscales y preferencias de facturación. Se utiliza esta información de proveedor y almacenado en transacciones como pedidos, entradas de mercancías y proveedores facturas.

Parte de la información de proveedor es específica de una empresa en particular (conocida como sociedad) o unidad de compras (conocida como organización de compras) dentro de su organización.

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

### Pasos preliminares

Contexto

En este paso, asigne los roles del capítulo Roles al usuario de prueba que son necesarios para los datos replicación. Antes de ejecutar este paso, asegúrese de haber creado y añadido la roles necesarios para el objeto específico para la replicación de datos.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | El Pantalla de inicio muestra. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar usuarios empresariales . |  |  |
| 3 | Introducir nombre de usuario | Introduzca el Nombre de usuario proporcionado por su sistema A continuación, seleccione el administrador Ir . |  |  |
| 4 | Seleccionar usuario | Seleccione el Usuario/a de la lista. |  |  |
| 5 | Editar | Seleccionar Editar . |  |  |
| 6 | Añadir roles empresariales | Seleccionar Añadir roles empresariales , introduzca el rol empresarial necesario en el Búsqueda campo y seleccione Intro . |  |  |
| 7 | Seleccionar roles empresariales | Seleccione el/la necesario/a Roles empresariales y seleccione OK . |  |  |
| 8 | Grabar | Seleccionar Grabar . | Se han guardado los roles empresariales. |  |
| 9 | Pantalla de inicio | Regrese a SAP Inicio pantalla. | Inicio se visualiza. |  |

### Unidades organizativas necesarias

Algunos segmentos de los datos maestros de proveedor dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos generales/centrales | Independiente de las unidades organizativas | ID, Nombre, Dirección, Cuenta bancaria, Número de identificación fiscal, y así sucesivamente. | Datos centrales solo existe una vez para un registro de datos maestros de proveedor. | n/d |
| Datos de sociedad | Sociedad | Cuenta asociada, condiciones de pago, responsable responsable, etc. | Pueden existir datos de sociedad para cada ID de sociedad de su estructura empresarial para la que se utiliza el registro de datos maestros de proveedor. | Sociedad:____________ |
| Datos de compras | Organización de compras | Moneda de pedido, condiciones de pago, grupo de compras, condiciones de expedición | Pueden existir datos de compras para cada organización de compras para la que se utiliza el registro de datos maestros de proveedor. | Organización de compras:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de proveedor pueden hacer referencia a otros datos maestros . La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un proveedor registro de datos maestros.

|  |
| --- |
| Nota Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo Datos maestros de proveedor. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Maestro de bancos | En la IU de socio comercial, encontrará la entrada de datos de cuenta bancaria en el Transacciones de pago sección. | Opcional | Si desea actualizar las cuentas bancarias del proveedor, debe haber creado el banco. maestro del banco correspondiente. En los registros maestros de cliente, A continuación, puede introducir el número de cuenta real junto con el banco datos maestros. |
| Cuenta asociada | En la IU de interlocutor comercial, encontrará la entrada de la reconciliación datos de cuenta Sociedad > Gestión de cuentas de proveedor | Obligatorio | Para la cuenta asociada, indique el libro mayor (LM) número de cuenta del libro auxiliar AR (Deudores).La cuenta de mayor que introduce debe haberse creado antes de poder utilizar es en el registro maestro de proveedores. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son siempre obligatorio para crear un registro de datos maestros de proveedor:

#### Agrupación de interlocutores comerciales y rangos de números

Las agrupaciones de interlocutores comerciales determinan los rangos de números para los IDs de interlocutor comercial. No puede modificar la asignación o los ID posteriormente. Si una agrupación de interlocutores comerciales está asignada a un rango de números interno, no podrá introducir el ID de interlocutor comercial manualmente. En este caso, deje el campo en blanco, ya que el sistema selecciona automáticamente un número del rango de números numérico asignado.

Las siguientes agrupaciones de interlocutores comerciales y los rangos de números correspondientes se definen para interlocutores comerciales (clientes, proveedores, contactos, empleados, etc.):

| Agrupación de interlocutores comerciales | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| BP01 | Rango de números numérico externo (bajo):1 – 999999 | Utilice esta agrupación, por ejemplo, para migrar registros de datos maestros numéricos |
| BP02 | Rango de números interno para uso estándar:1000000 – 9999999 | Si no se introduce ningún grupo de interlocutores comerciales, este rango de números se utiliza por defecto. |
| BP03 | Rango de números numérico externo (alto):10000000 – 999999999 | Reservado para objetos de datos maestros de muestra de SAP. |
| BPAB | Rango de números alfanuméricos externo:A – ZZZZZZZZZZ | Este rango debe comenzar con un carácter. |
| BPEE | Rango de números interno:9980000000 – 9999999999 | Reservado para interlocutores comerciales utilizados como empleados. |

#### ID de socio comercial

ID de socio comercial

Están disponibles las siguientes opciones para asignar el identificador de socio comercial (ID):

- Introduzca un ID junto con una agrupación de interlocutores comerciales para la numeración externa. Por ejemplo

| Agrupación de interlocutores comerciales | Entradas posibles para el ID de interlocutor comercial |
| --- | --- |
| BP01 | Cualquier número dentro del intervalo correspondiente 1 – 999999 |
| BPAB | Cualquier combinación alfanumérica de hasta 10 caracteres, siempre que empiece con un carácter, por ejemplo, Z-TEST01 |

Si no ha especificado la agrupación de interlocutores comerciales y deja el ID de interlocutor comercial en blanco, el sistema tomará el siguiente número libre de la agrupación de interlocutores comerciales BP02. Esta agrupación se define como agrupación estándar para ID de socio comercial numéricos internos.

#### Función de interlocutor comercial

Función de interlocutor comercial

La función de interlocutor comercial determina los derechos y responsabilidades de cada interlocutor. en una operación comercial.

Algunos ejemplos de funciones de interlocutor en Compras son: Proveedor, Emisor de la factura, Proveedor de mercancías y etc.

#### Grupo de cuentas

Los grupos de cuentas son parámetros de control principales para crear los segmentos de datos ERP de un proveedor registro maestro. Actualmente, el único grupo de cuentas admitido para los datos maestros de proveedor es SUPL .

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de proveedor - Datos generales](#unique_14) [página ] 9 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de proveedor (F1053A) | Se crea Maestro de proveedores – Datos generales. |
| [Creación de datos maestros de proveedor - Datos de sociedad](#unique_15) [página ] 16 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de proveedor (F1053A) | Se crea Maestro de proveedores – Datos de sociedad. |
| [Creación de datos maestros de proveedor - Datos de organización de compras](#unique_16) [página ] 23 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) o bien Gestionar datos maestros de proveedor (F1053A) | Se crea Maestro de proveedores – Datos de compras. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de datos maestros de proveedor - Datos generales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de proveedor. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Crear una organización de socio comercial | Seleccionar Organización . | El Crear organización se visualiza. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas y seleccione OK :Interlocutor comercial : <Introduzca un ID de socio comercial que empiece por una letra>Agrupación : seleccione, por ejemplo, Numeración alfanumérica externa .El Crear en rol IC el sistema rellena el campo con el Interlocutor comercial (gen.) Rol de . Mantenga esta opción.Nota Para obtener más información, consulte el anterior [Agrupación de interlocutores comerciales y rangos de números](#unique_9) [página ] 5 capítulo. |  |  |
| 5 | Introducir datos de dirección | El Dirección en la pestaña Nombre introduzca los siguientes datos:Título : <Empresa>Nombre : <Nombre> |  |  |
| 6 | Introducir término de búsqueda | El Dirección en la pestaña Concepto de búsqueda introduzca uno o más términos de búsqueda para el proveedor. |  |  |
| 7 | Introducir datos de dirección | En la Dirección estándar sección, en la Dirección introduzca la dirección. |  |  |
| 8 | Introducir huso horario y huso horario de transporte | En la Dirección sección, seleccione Más campos . Introduzca los siguientes datos:Huso horario : <Huso horario>Zona de transporte : <Zona de transporte> |  |  |
| Solo para Tailandia | Introducir datos de dirección (solo para Tailandia) | En la Dirección sección, seleccione Más e introduzca los siguientes datos:Código de edificio : <Edificio>Sala : <Número de sala>Planta : <Nº planta>Calle 2 : <Moo>Calle 3 : <Soi/Lane>Calle : <Carretera>Número : <no>Otra ciudad : <Subdistrito>Distrito : <Distrito/Sección>Población : <Provincia>Código postal : <Código postal> |  |  |
| 9 | Introducir datos de comunicación | El Dirección en la pestaña Comunicación introduzca los siguientes datos:Idioma : <Seleccione el idioma preferido del proveedor>Teléfono : <Número de teléfono>Correo electrónico : <Dirección de correo electrónico> |  |  |
| 10 | Introducir datos de identificación | El Identificación en la pestaña Datos organizativos introduzca los siguientes datos para el proveedor:Forma jurídica : <Forma jurídica> |  |  |
| Solo para Japón | Introducir datos de sector (solo para Japón) | El Identificación en la pestaña Sectores sección, seleccione Todos los sistemas sectoriales . Introduzca los siguientes datos:Sistema de ramos : Seleccionar Banco de Japón .Sector : <Seleccione un número de sector>Sector estándar : <No seleccionado> |  |  |
| Solo para Japón | Introducir datos de número de identificación fiscal (solo para Japón) | Pulsar Intro para confirmación.Atención Si selecciona la opción incorrecta, no podrá actualizar Japón: Mi número datos. |  |  |
| Solo para Japón | Introducir datos largos de número de identificación fiscal (solo para Japón) | El Identificación en la pestaña Números de identificación fiscal largos introduzca los siguientes datos:Categoría : JP4 Número de identificación de IVA de JapónNúmero de identificación fiscal largo : <Número de empresa del interlocutor comercial> |  |  |
| 11 | Introducir cuentas bancarias | El Transacciones de pago en la pestaña Datos bancarios introduzca los siguientes datos para el proveedor:País/Región : <País/Región>Clave de banco : <Clave de banco>Cuenta bancaria : <Cuenta bancaria>Atención Las claves de banco deben definirse previamente. Utilice la ayuda para entradas para obtener más información sobre las entradas permitidas en este campo. |  |  |
| 12 | Guardar los datos | Guarde las entradas. |  |  |

Procedimiento: Opción 2 - Gestionar datos maestros de proveedor

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de proveedor (F1053A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de proveedor (F1053A) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | En la Proveedores sección, seleccione, seleccione Crear > Organización . | El Crear organización se visualiza. |  |
| 4 | Introducir datos generales | En la Datos generales introduzca los siguientes datos y seleccione OK :Interlocutor comercial : Por ejemplo, Z … (es decir, cualquier ID alfanumérico externo, ya que debe empezar por una letra).Agrupación : Por ejemplo, <Numeración alfanumérica externa> .Título : Por ejemplo, Sociedad GL (0003)Nombre 1 : <Introduzca un nombre> | El Proveedor nuevo se visualiza. |  |
| 5 | Introducir datos básicos | El Proveedor nuevo pantalla, en la pantalla Datos básicos , efectúe las siguientes entradas:En la Información de proveedor introduzca los siguientes datos:Grupo de cuentas de referencia, Grupo de autorización de proveedor, etc. : selecciónelo en la ayuda para entradas.En la Datos organizativos introduzca los siguientes datos:Obligación de IVA, partición de impuestos, bloqueo de pago, etc. : seleccione los indicadores relevantes.Nota Para obtener más información sobre las agrupaciones de SC y cómo se relacionan con la numeración de ID, consulte el documento anterior. [Agrupación de interlocutores comerciales y rangos de números](#unique_9) [página ] 5 capítulo.En la Información adicional introduzca los siguientes datos:Función de bloqueo : selecciónelo en la ayuda para entradas.Centro : selecciónelo en la ayuda para entradas.Clave de instrucción : selecciónelo en la ayuda para entradas. |  |  |
| 6 | Elegir roles | El Proveedor nuevo seleccione el pulsador Roles pestaña. | Ha navegado a Roles sección. |  |
| 7 | Seleccione Crear. | En la Roles sección, seleccione Crear y seleccione un rol de la ayuda para entradas:Rol de interlocutor comercial : Por ejemplo, FLVN01 .Se debe crear un maestro de proveedores con el rol de interlocutor comercial FLVN00 (Proveedor FI) o con el rol de interlocutor comercial FLVN01 (proveedor con datos de compras) , o con ambos roles. El rol de interlocutor comercial FLVN00 (Proveedor FI) se utiliza en la contabilidad financiera y el rol de interlocutor comercial FLVN01 (proveedor con datos de compras) se utiliza en Ventas.Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. | Se ha añadido el Rol. |  |
| 8 | Introducir roles adicionales (opcional) | Repita los pasos 6 y 7 para añadir un rol adicional.Rol de interlocutor comercial : Por ejemplo, FLVN00 . | Después de introducir todos los roles de interlocutor comercial, se visualizan en la Roles sección de la Maestro nuevo pantalla. |  |
| 9 | Seleccionar dirección estándar | El Maestro de proveedores - Proveedor nuevo seleccione el pulsador Dirección y vaya a la pestaña Dirección estándar sección. | Ha navegado a Dirección estándar sección. |  |
| 10 | Introducir datos de dirección | En la Dirección - Dirección estándar , realice entradas para todos los campos relevantes según sus necesidades. Por ejemplo:Calle : <Nombre de la calle>Número : <Número de la dirección>Código postal : <Código postal de la dirección>Población : <Ciudad>País/Región : <Código de país/región>Nota (Solo se aplica a los Estados Unidos) Cuando crea un interlocutor comercial ubicado en los Estados Unidos, el código de domicilio fiscal se determina automáticamente. Sin embargo, debe introducir la dirección correcta y completa, ya que la jurisdicción se deriva en función de las entradas de País (EE. UU.), Estado y Código postal.En la Dirección - Comunicación estándar , realice las siguientes entradas:Idioma : <Idioma>Teléfono : <Introduzca el campo según sea necesario>Correo electrónico : Por ejemplo, contact@Z.com .Seleccionar Crear .En la Dirección - Detalles de dirección seleccione la entrada de dirección.El Dirección nueva pantalla, en la pantalla Utilizaciones de dirección , verifique que se visualice la siguiente información:Tipo de dirección : XXDEFAULT |  |  |
| 11 | Volver a la pantalla principal | Seleccionar Aplicar .Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. |  |  |
| 12 | Seleccionar cuentas bancarias | El Maestro de proveedores: nuevo proveedor... seleccione el pulsador Cuentas bancarias pestaña. | Ha navegado a Cuentas bancarias sección. |  |
| 13 | Seleccione Crear. | El Maestro de proveedores - Cuentas bancarias... , seleccione Crear . | Se añade una nueva cuenta bancaria. |  |
| 14 | Introducir datos bancarios | Introduzca los siguientes datos para la nueva cuenta bancaria:ID : Por ejemplo, BNK1 .País/región del banco : <Código de país/región>Clave de banco : <Clave de banco>Número de cuenta : <Número de cuenta>Realice entradas para todos los demás campos según sus necesidades. |  |  |
| 15 | Volver a la pantalla principal | Seleccionar Aplicar .Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. |  |  |
| 16 | Seleccionar número de identificación fiscal (opcional) | El Maestro de proveedores - Proveedor nuevo pantalla, en la pantalla Identificación , seleccione NÚMEROS DE IMPUESTOS . | Ha navegado a NÚMEROS DE IMPUESTOS sección. |  |
| 17 | Seleccione Crear (opcional). | En la Maestro de proveedores - Nuevo maestro de proveedores - NÚMERO DE IMPUESTOS … sección, seleccione Crear . |  |  |
| 18 | Introducir datos de número de identificación fiscal (opcional) | En la Números de identificación fiscal , realice las siguientes entradas:Categoría fiscal : <Indicador de impuestos>Número de identificación fiscal : <Número de identificación fiscal>Nota Los números de identificación fiscal que se introducen dependen de los requisitos específicos del país/región.Seleccione la categoría correcta que se aplica al país/región del cliente. Por ejemplo, para un socio comercial alemán, actualice un valor para la categoría DE1, que representa el número de identificación fiscal de IVA utilizado comúnmente (Umsatzsteuer-Identifikationsnummer).Realice solo entradas para los campos que necesite; de lo contrario, seleccione Borrar para eliminar el conjunto de datos (vacío). |  |  |
| 19 | Volver a la pantalla principal | Seleccione la flecha Atrás.Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. |  |  |
| 20 | Seleccione Crear. | En la Maestro de proveedores - Nuevo proveedor - Categorías fiscales sección, seleccione Crear . | El Categorías fiscales se visualiza. |  |
| 21 | Introducir datos de categorías fiscales (opcional) | Realice las siguientes entradas:Indicador de impuestos : Por ejemplo, IVA de compras IVA .Autorización de domiciliación de : <Fecha>Autorización de domiciliación a : <Fecha> |  |  |
| 22 | Introducir textos (opcional) | El Textos , efectúe las siguientes entradas:Idioma : Por ejemplo, ES .ID : Por ejemplo, 01 .Texto explicativo : <Introduzca un texto explicativo> |  |  |
| 23 | Introducir datos de proveedor adicionales (opcional) | Ir a Datos básicos > Datos de proveedor adicionales y seleccione Crear .Añada los datos necesarios como se describe en los pasos anteriores.Nota Este escenario es para varias asignaciones de proveedores a los mismos socios comerciales y, por lo tanto, se aplican los mismos datos maestros que se describen en los pasos anteriores.Si se requieren datos adicionales como Datos de compra y Datos de sociedad, consulte las secciones anteriores que describen los mismos. |  |  |
| 24 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que el objeto se ha grabado . |  |

### Creación de datos maestros de proveedor - Datos de sociedad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de proveedor. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Creación de datos maestros de proveedor - Datos generales](#unique_14) [página ] 9, antes de continuar con este capítulo.

Siga el procedimiento después de haber guardado las entradas de Datos generales, como se describe en el capítulo anterior, en la Visualizar organización: <Nombre del proveedor> pantalla.

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Cambiar a modo de modificación | Seleccionar Cambiar entre visualizar y modificar (F6) para cambiar al modo de modificación. |  |  |
| 4 | Modificar rol de interlocutor comercial | En la Modificación en rol IC seleccione el siguiente valor:Proveedor (contabilidad financiera)Nota La clave técnica de este rol de interlocutor comercial es FLVN00 . |  |  |
| 5 | Abrir datos de sociedad | Seleccionar Sociedad en la pantalla. | El Sociedad se visualiza. |  |
| 6 | Introducir sociedad | Introduzca la sociedad. Por ejemplo, 1010 . |  |  |
| Solo para Rusia | Introducir datos de contabilidad de proveedor - Central (solo para Rusia) | El Acreedor: Gestión de cuentas en la pestaña Gestión de cuentas introduzca una de las siguientes opciones:163107701 como central para IC de IVA 163117701163107701 como central para IC de IVA 163117701163107701 como central para el impuesto sobre bienes inmuebles BP 163127701163107702 como central para el impuesto sobre bienes inmuebles BP 163127702 |  |  |
| 7 | Introducir datos de contabilidad de acreedor | El Acreedor: Gestión de cuentas en la pestaña Gestión de cuentas introduzca los siguientes datos:Cuenta asociada : <21100000> (Acreedores nacionales)Clave de clasificación : <Clave de clasificación>Indicador de minoría : <Indicador de minoría> (Los valores del indicador de minoría se definen mediante el paso de configuración: Definir indicadores de minoría)Nota Puede haber otras cuentas de reconciliación de mayor para proveedores extranjeros o afiliados. |  |  |
| Solo para Japón | Introducir datos de contabilidad de proveedor - Retención de impuestos (solo para Japón) | El Acreedor: Gestión de cuentas en la pestaña Retención de impuestos introduzca los siguientes datos, si este proveedor es relevante para la retención de impuestos:Clv.P/R ret.imp. : <JP> (Japón) |  |  |
| Solo para Polonia | Introducir proveedor: Retención de impuestos (solo para Polonia) | El Acreedor: Retención de impuestos en la pestaña Tipos de retención de impuestos , realice las siguientes entradas:Asignar el Tipo de retención de impuestos y Código de retención de impuestos información para el interlocutor comercial.Intro Motivo de exención (DT), Porcentaje de exención (por ejemplo, 100% ), Número de exención , y Rango de validez para los códigos de retención de impuestos que son relevantes para el Tratado de doble imposición/Acuerdo de doble imposición. |  |  |
| 8 | Introducir datos de pago de proveedor | El Acreedor: Operaciones de pago en la pestaña Datos de pago , realice la siguiente entrada:Condiciones de pago : <Condiciones de pago>Nota Las condiciones de pago definidas en este paso se pueden sustituir por las condiciones de pago definidas en el nivel Compras. |  |  |
| 9 | Introducir datos de pago de proveedor | El Acreedor: Operaciones de pago en la pestaña Transacciones de pago automático introduzca los siguientes datos:Vías de pago : <Vías de pago>Banco propio : <Banco propio>Nota Pulsar F4 para abrir la selección en el campo Vías de pago. |  |  |
| 10 | Introducir datos de correspondencia de proveedor | El Acreedor: Correspondencia en la pestaña Correspondencia introduzca los siguientes datos:Cuenta con proveedor : <Cuenta con proveedor> |  |  |
| Solo para Japón | Retención de impuestos (solo para Japón) | El Retención de impuestos , realice la siguiente entrada si este proveedor es relevante para la retención de impuestos:Tipo de retención de impuestos : <Tipo de retención de impuestos>Código de retención de impuestos : <Código de retención de impuestos>Asunto : <seleccionado> |  |  |
| Solo para Japón | Japón: Mi número (solo para Japón) | Seleccionar Datos generales . En el campo Ampl.espec.país , realice la siguiente entrada si este interlocutor comercial no es una persona física:Número de empresa : <Número corporativo>El Ampl.espec.país , realice las siguientes entradas si este Proveedor es una persona física:Seleccionar Inicio de validez y Válido hasta y, a continuación, seleccione Visualizar .Estado : <Estado>Evidencia de identidad : <Evidencia para identidad>Evidencia para número : <Evidencia para el número>Retención hasta : <Retención hasta>Seleccionar Desenmascarar para introducir el Número individual . |  |  |
| Solo para Tailandia | Código de sucursal (solo para Tailandia) | Abrir datos generales, en la Ampl.espec.país ficha, actualice los datos de Código de sucursal junto con la dirección y el Código de sucursal por defecto para este interlocutor comercial.Para la dirección del código de sucursal, seleccione Dirección e introduzca los siguientes datos:Nombre (Primeras dos líneas): <Nombre del contribuyente>País : JUCódigo de edificio : <Nombre del edificio/Población>Sala : <Número de sala>Planta : <Planta>Calle 2 : <Moo>Calle 3 : <Trok/Soi>Calle : <Carretera>Número : <no>Otra ciudad : <Tumbol/Subsección>Distrito : <Distrito/Sección>Población : <Provincia>Código postal : <Código postal>Teléfono : <Número de teléfono>Nota Cuando hay más de un código de sucursal para un interlocutor comercial, debe actualizar cada código de sucursal junto con la dirección de cada código de sucursal. También debe fijar un Código de sucursal que el Interlocutor comercial suele utilizar por defecto. |  |  |
| Solo para Rusia | Atributos de pago de impuestos (solo para Rusia) | El Ampl.espec.país , efectúe las siguientes entradas para el interlocutor comercial.Para el impuesto sobre bienes inmuebles BP 163107701 y 163107702, introduzca los siguientes valores:Tipo de pago : Pagos a presupuestoEstado del pagador : 01Código de presupuesto : 182 1 06 02010 02 1000 110Para Pago de nómina BP 163107703, introduzca el siguiente valor:Tipo de pago : Pagos a presupuestoPara el IVA BP 163117701 y 163117702, introduzca los siguientes valores:Tipo de pago : Pagos a presupuestoEstado del pagador : 01Código de presupuesto : 18210301000011000110Para el impuesto sobre bienes inmuebles BP 163127701 y 163127702, introduzca los siguientes valores:Tipo de pago : Pagos a presupuestoEstado del pagador : 01Código de presupuesto : 18210602010021000110 |  |  |
| Solo para Arabia Saudí | Acreedor: Específico de país Ampl. (solo para Arabia Saudí) | El Acreedor: Ampl.esp.país , seleccione Insertar fila para agregar los certificados de proveedor. |  |  |
| 11 | Guardar los datos | Guarde las entradas. | La entrada en la Modificación en rol IC modificaciones de campo de Acreedor FI (nuevo) hasta Acreedor FI (definido) . |  |

Información de retención de impuestos (solo Brasil)

Utilice la siguiente tabla para determinar las entradas de retención de impuestos en el paso anterior solo para Brasil.

Para la organización empresarial:

| Tp.ret.imp. | Cód.ret.imp. | asunto | Comentarios |
| --- | --- | --- | --- |
| GA | GA | X | para el 4,65% |
| AP | AP | X | solo para PIS |
| CC | CC | X | solo para COFINS |
| SA | SA | X | solo para CSSL |
| RA | RA | X | solo para IRPJ (mediante TAXBRA) |
| RF | R1 a R3 | X | solo para IRPJ (mediante FI) |
| IW | IW | X | para ISS |
| IJ | I1 a I2 | X | para INSS PJ |

Para persona física:

| Tp.ret.imp. | Cód.ret.imp. | asunto | Comentarios |
| --- | --- | --- | --- |
| ID | De R0 a R5 | X | para INSS PF |
| EN | N1 | X | para INSS PR |

Procedimiento: Opción 2 - Gestionar datos maestros de proveedor

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de proveedor (F1053A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de proveedor (F1053A) . | Se abre la aplicación. |  |
| 3 | Introducir detalles de proveedor | En la ayuda para entradas, seleccione Interlocutor comercial . Además, puede seleccionar más detalles, como Calle .Seleccionar Ir . |  |  |
| 4 | Seleccionar proveedor | En la lista de resultados, seleccione un Proveedor. | El Proveedor se visualiza. |  |
| 5 | Seleccione Editar. | Seleccionar Editar .Nota Este paso asume que continúa con el paso anterior y que ya ha navegado a Datos maestros - Maestro de proveedores > Gestionar maestro de proveedores . Una vez guardados los datos generales de la sección anterior, el sistema estará en modo de visualización. Para continuar, debe estar en modo de edición. | El Gestionar maestro de proveedores se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 6 | Seleccionar sociedades | El Gestionar proveedor , seleccione Sociedades . |  |  |
| 7 | Seleccione Crear. | En la Sociedades sección, seleccione Crear . | Se muestra una vista detallada en modo de edición. |  |
| 8 | Introducir datos de sociedad | En la Sociedades seleccione una entrada para abrir una vista detallada. Realice las siguientes entradas:El Datos generales pestaña:Sociedad : introduzca la sociedad, por ejemplo, 1710 .El Correspondencia pestaña:Responsable : Por ejemplo: 01 Sra. Smith .Cuenta en proveedor : <Cuenta en proveedor>El Finanzas pestaña:Finanzas - ContabilidadCuenta asociada : Por ejemplo, 21100000 - Débitos nacionales .Clave de clasificación : Por ejemplo, 009 Número de documento externo .Grupo minoritario : <Grupo minoritario> (Esto solo es válido para el FLVN00 - Proveedor (contabilidad financiera) rol. Los valores de grupo de minorías se definen mediante el paso de configuración: Definir indicadores de minorías .)Finanzas: Datos de pagoCondiciones de pago : Por ejemplo, 0001 .Finanzas - Transacciones de pago automáticoVías de pago : Por ejemplo, E Débito directo .El Datos de reclamación pestaña:Procedimiento de reclamación, Bloqueo de reclamación, Destinatario de reclamación, Responsable de reclamación : Seleccione de la ayuda para entradas.Nivel de reclamación : Por ejemplo, 0 .Última reclamación : Por ejemplo, 10.02.2020 .Procedimiento de reclamación legal de : Por ejemplo, 11.02.2020 .El Textos pestaña:En la Textos sección, seleccione Crear y realice las siguientes entradas:.Idioma : Por ejemplo, ES .ID : Por ejemplo, 01 .Texto explicativo : <Introduzca un texto explicativo> |  |  |
| 9 | Volver a la pantalla principal | Seleccionar Crear y, a continuación, seleccione Aplicar .Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. |  |  |
| 10 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que el objeto se ha grabado . |  |

### Creación de datos maestros de proveedor - Datos de organización de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear datos maestros de proveedor. Las aplicaciones disponibles dependen de su rol asignado. Por lo tanto, se proporcionan dos opciones.

Requisito previo

Debe completar el capítulo anterior, [Creación de datos maestros de proveedor - Datos generales](#unique_14) [página ] 9, antes de continuar con este capítulo.

Siga el procedimiento después de haber guardado las entradas de Datos generales, como se describe en el capítulo anterior, en la Visualizar organización: <Nombre del proveedor> pantalla.

Procedimiento: Opción 1 - Actualizar interlocutor comercial

Siga este procedimiento cuando su acceso de usuario le presente el Actualizar interlocutor comercial (IC) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Cambiar a modo de modificación | Seleccionar Cambiar entre visualizar y modificar (F6) para cambiar al modo de modificación. |  |  |
| 4 | Modificar rol de interlocutor comercial | En la Modificación en rol IC seleccione el siguiente valor:ProveedorNota La clave técnica de este rol de interlocutor comercial es FLVN01 . |  |  |
| 5 | Abrir datos de organización de compras | Seleccionar Compras en la pantalla. | El Organización de compras se visualiza. |  |
| 6 | Introducir datos de compras | Introduzca los siguientes datos y pulse Intro :Organización de compras : <Organización de compras> |  |  |
| 7 | Introducir datos de compras | El Datos de compras en la pestaña Condiciones introduzca los siguientes datos:Moneda de pedido : <Moneda de pedido>Condiciones de pago : <Condiciones de pago> |  |  |
| 8 | Introducir datos de compras | El Datos de compras en la pestaña Datos de control introduzca los siguientes datos:Condiciones de expedición : <Condiciones de expedición>Verif.fact.bas.en EM : <Verificación de facturas basada en EM> |  |  |
| 9 | Introducir datos de compras | El Datos de compras en la pestaña Valores propuestos para material introduzca los siguientes datos:Grupo de compras : <Grupo de compras>Plazo entrega prev. : <Plazo de entrega previsto> |  |  |
| 10 | Introducir datos de funciones de interlocutor | El Funciones de interlocutor en la pestaña Funciones de interlocutor verifique que la LF entrada (o la NV si el idioma de trabajo es inglés). |  |  |
| 11 | Guardar los datos | Guarde las entradas. |  |  |

Procedimiento: Opción 2 - Maestro de proveedores

Siga este procedimiento cuando su acceso de usuario le presente el Gestionar datos maestros de proveedor (F1053A) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar datos maestros de proveedor (F1053A) . | Se abre la aplicación. |  |
| 3 | Seleccione Editar. | Seleccionar Editar .Nota Este paso asume que continúa con el paso anterior y que ya ha navegado a Datos maestros - Maestro de proveedores > Maestro de proveedores . Una vez guardados los datos de la sección anterior, el sistema estará en modo de visualización. Para continuar, debe estar en modo de edición. | El Maestro de proveedores se visualiza en modo de edición (los campos están listos para su entrada). |  |
| 4 | Seleccionar organizaciones de compras | En la Maestro de proveedores... , seleccione ORGANIZACIONES DE COMPRA . | El Maestro de proveedores - COMPRA Se muestra la sección. |  |
| 5 | Seleccione Crear. | En la Maestro de proveedores - COMPRA sección, seleccione Crear . | El Nueva organización de compras... se visualiza en modo de edición. |  |
| 6 | Introducir datos de organización de compras | El Nueva organización de compras , efectúe las siguientes entradas:El Datos generales pestaña:Organización de compras : <Código de organización de compras>Grupo de compras : Por ejemplo, 001 .El COMPRA pestaña:Para el Condiciones columna:Moneda de pedido : <Código de moneda>Valor mínimo de pedido : <Valor mínimo de pedido>Condiciones de pago : Por ejemplo, 0001 .Control de datos de determinación de precios : Por ejemplo, <Fecha actual> .Para el Datos de control columna:Condición de expedición : Por ejemplo, 01 .Pedido automático : <Pedido automático>Verificación de facturas basada en entrada de mercancías (casilla de selección) |  |  |
| 7 | Introducir datos de funciones de interlocutor | Nota Algunas funciones de interlocutor están predeterminadas en función de la personalización de los grupos de cuentas y las organizaciones de compras seleccionados.Para añadir más funciones de interlocutor, en la Funciones de interlocutor , seleccione Crear . Puede seleccionar entre las siguientes funciones:VN - ProveedorGS - Proveedor de mercancíasMN - Centro de fabricación |  |  |
| 8 | Introducir detalles de organización de compras | El Texto , seleccione Crear e introduzca los detalles de la organización de compras. |  |  |
| 9 | Volver a la pantalla principal | Seleccionar Aplicar .Nota Asegúrese de que el mensaje del sistema Borrador guardado se visualiza en la parte inferior de la pantalla antes de volver a la pantalla principal. |  |  |
| 10 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que el objeto se ha grabado . |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bne-591]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bne-589]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 47,546 chars in the whole document
