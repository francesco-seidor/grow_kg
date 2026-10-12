---
id: 10-procurement/script-de-datos-maestros-creacion-de-registro-info-de-compras-mds-bhd
title: Script de datos maestros - Creación de registro info de compras - MDS (BHD) (BHD_S4CLD2608_Master_Data_ES_XX)
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: test procedures to create and mass-change purchasing info records (BHD)."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_ES_XX]
keywords: [Purchasing Info Records, info record creation, consignment info records, subcontracting info records, pipeline info records, mass changes, mass price changes, business roles, number ranges, master data prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-564
topic: 10-procurement/purchasing-info-records
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de registro info de compras - MDS (BHD) (BHD_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de registro info de compras - MDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894923)

[2 Requisitos previos 3](#_Toc233894924)

[2.1 Acceso al sistema 3](#_Toc233894925)

[2.2 Roles 3](#_Toc233894926)

[2.3 Unidades organizativas necesarias 3](#_Toc233894927)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894928)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894929)

[2.5.1 Rangos de números 4](#_Toc233894930)

[3 Tabla de resumen 5](#_Toc233894931)

[4 Procedimientos de prueba 6](#_Toc233894932)

[4.1 Crear registro info de compras 6](#_Toc233894933)

[4.2 Crear registro info de compras para consignación 8](#_Toc233894934)

[4.3 Crear registro info de compras para subcontratación 10](#_Toc233894935)

[4.4 Crear registro info de compras para pipeline 12](#_Toc233894936)

[4.5 Modificaciones en masa en el registro info de compras 15](#_Toc233894937)

[4.6 Modificaciones de precio en masa en registro info de compras 16](#_Toc233894938)

[5 Apéndice 18](#_Toc233894939)

[5.1 Funciones relevantes 18](#_Toc233894940)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un registro info de compras contiene información específica de un material y el proveedor que proporciona el material.

Contiene información como el precio cargado por el proveedor, la cantidad de pedido estándar y las tolerancias para la entrega en exceso y entrega incompleta. Se utiliza en la transacción de pedido.

La información es específica de una unidad de compra en particular (conocida como organización de compras) y un sitio específico (conocido como planta) dentro de su organización.

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
| Comprador | SAP_BR_PURCHASER | Compras / Aprovisionamiento y contratación | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se han creado en su sistema ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos de compras | Organización de compras | Grupo de compras, Grupo de artículos, Tiempo de tratamiento de EM, etc. | Pueden existir datos de compras para cada organización de compras para la que el material utilizado en los procesos de compras. | Organización de compras:__________ |

### Datos maestros obligatorios y opcionales

Los registros info de compras pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en una información de compras registro.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material |  | Obligatorio | Para introducir el material, primero cree datos maestros de material. |
| Proveedor |  | Obligatorio | Para introducir el proveedor, primero cree datos maestros de proveedor. |

### Parámetros principales para la creación de datos

En esta sección se proporciona una descripción de los parámetros básicos que influyen en el comportamiento de un registro info de compras y que siempre son necesarios para crear un registro info de compras.

#### Rangos de números

Se han definido los siguientes rangos de números para el registro info de compras:

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Numérico interno | Rango de números interno para uso estándar:5300000000 – 5399999999 | Este rango de números se utiliza cuando el sistema asigna automáticamente un número numérico a un material. |
| Numérico externo | Rango de números numérico externo (alto):5400000000 – 5499999999 | Este rango de números está reservado para la asignación de números externa. |

## Tabla de resumen

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear registro info de compras](#unique_10) [página ] 6 | Comprador | Gestionar registros info de compras (F1982) | Se crean registros info de compras. |
| [Crear registro info de compras para consignación](#unique_11) [página ] 8 | Comprador | Gestionar registros info de compras (F1982) | Se crea el registro info de compras para el consignado. |
| [Crear registro info de compras para subcontratación](#unique_12) [página ] 10 | Comprador | Gestionar registros info de compras (F1982) | Se crea el registro info de compras para la subcontratación. |
| [Crear registro info de compras para pipeline](#unique_13) [página ] 12 | Comprador | Gestionar registros info de compras (F1982) | Se crea el registro info de compras para el pipeline. |
| [Modificaciones en masa en el registro info de compras](#unique_14) [página ] 15 | Comprador | Modificaciones en masa en registros info de compras (F2667) | Se aplican modificaciones en masa en el registro info de compras. |
| [Modificaciones de precio en masa en registro info de compras](#unique_15) [página ] 16 | Comprador | Modif.precio: Registros info | Se aplican modificaciones de precio en masa en el registro info de compras. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear registro info de compras

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de compras (F1982) . | El Gestionar registros info de compras (F1982) se visualiza. |  |
| 3 | Abrir nueva información de compras Registro | Seleccionar Crear . | El Pantalla de registro info de compras muestra. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas:Categoría de registro info de compras : <Estándar>Organización de compras : <Compras Organización>Proveedor : <Proveedor>Material : <Material>Centro : <Centro>Grupo de compras : <Compras Grupo> | Se han añadido los datos de cabecera. |  |
| 5 | Introducir información general | Realice las siguientes entradas:Disponible desde : DD/MM/AAAAFin de disponibilidad : DD/MM/AAAA | Información general Se ha añadido. |  |
| 6 | Introducir datos de compras | Realice las siguientes entradas:Incoterm : <Incoterm>Ubicación de incoterm 1 : <Ubicación de incoterm 1> | Datos de compras Se ha añadido. |  |
| 7 | Introducir entrega y cantidad Datos | Realice las siguientes entradas:Plazo de entrega en días : <XX días>Tolerancia de entrega incompleta en % : <XX>Tolerancia de exceso de suministro en % : <XX>Indicador de impuestos : <Impuesto Código>Nota Cuando los TDT (impuestos dependientes del tiempo) se activan mediante Paso de configuración 101016 (Definir indicadores de impuestos para Ventas y compras) para el país de la sociedad y Se indica el indicador de impuestos, el campo Inicio de validez del tipo impositivo es obligatorio. Puede introducir la fecha actual, que se ajustado a la fecha de inicio de validez del indicador de impuestos según la opción en el paso de configuración.Cuando el RITA (Registro para tributación indirecta) Extranjero) está activado, el país de registro fiscal es actualizado para sociedad en paso de configuración 103464 (Activar RITA y actualizar registro fiscal) Países) y se indica el indicador de impuestos, la Residencia fiscal El campo es obligatorio, en el que el ID de país de la sociedad se indica como valor de propuesta, pero puede modificar el ID de país válido que se actualiza en Paso de configuración correspondiente.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Unidad de medida de pedido : <Unidad de pedido>Cantidad de pedido estándar : <Pedido estándar Cantidad>Si es necesario, seleccione las siguientes entradas:Entrega ilimitadaFactura basada en entrada de mercancías VerificaciónSin recibo evaluado LiquidaciónRequisito de confirmación de pedidoControl de confirmación | Datos de entrega y cantidad Se ha añadido. |  |
| 8 | Introducir datos de condición | En la Condición seleccione la sección Crear ícono. Indique los siguientes datos:Inicio de validez : <Fecha de inicio de validez>Cantidad : <Importe>Unidad de determinación de precio : <Unidad de determinación de precio>Válido hasta : <Fecha de fin de validez>Moneda : <Moneda>Seleccionar Aplicar . | Se han añadido los datos de condición. |  |
| 9 | Introducir datos de referencia (opcional) | Opcionalmente, puede introducir datos de referencia. | Se han añadido los datos de referencia. |  |
| 10 | Guardar los datos | Seleccionar Crear . | Se graba un registro info de compras. |  |

### Crear registro info de compras para consignación

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de compras (F1982) | Aparece la pantalla Gestionar registros info de compras. |  |
| 3 | Abrir nuevo registro info de compras | Seleccionar Crear . | Aparece la pantalla Registro info de compras. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas:Registro info de compras Categoría : < Consignación>Organización de compras : <Compras Organización>Proveedor : <Proveedor>Material : <Material>Centro : <Centro>Grupo de compras : <Grupo de compras> | Se han añadido los datos de cabecera. |  |
| 5 | Introducir información general | Realice las siguientes entradas:Disponible desde : DD/MM/AAAAFin de disponibilidad : DD/MM/AAAA | Se ha añadido Información general. |  |
| 6 | Introducir datos de compras | Realice las siguientes entradas:Incoterm : <Incoterm>Ubicación de incoterm 1 : <Ubicación de incoterm 1> | Se han añadido los datos de compras. |  |
| 7 | Introducir datos de entrega y cantidad | Realice las siguientes entradas:Plazo de entrega en días : <XX días>Tolerancia de entrega incompleta en % : <XX>Tolerancia de exceso de suministro en % : <XX>Indicador de impuestos : <Indicador de impuestos>Nota Cuando los TDT (impuestos dependientes del tiempo) se activan mediante Paso de configuración 101016 (Definir indicadores de impuestos para Ventas y compras) para el país de la sociedad y Se indica el indicador de impuestos, el campo Inicio de validez del tipo impositivo es obligatorio. Puede introducir la fecha actual, que se ajustado a la fecha de inicio de validez del indicador de impuestos según la opción en el paso de configuración.Cuando el RITA (Registro para tributación indirecta) Extranjero) está activado, el país de registro fiscal es actualizado para sociedad en paso de configuración 103464 (Activar RITA y actualizar registro fiscal) Países) y se indica el indicador de impuestos, la Residencia fiscal El campo es obligatorio, en el que el ID de país de la sociedad se indica como valor de propuesta, pero puede modificar el ID de país válido que se actualiza en Paso de configuración correspondiente.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Unidad de medida de pedido : <Orden Unidad>Cantidad de pedido estándar : <Pedido estándar Cantidad> | Se han añadido los datos de entrega y cantidad. |  |
| 8 | Introducir datos de condición | En la sección Condición, seleccione Crear icono. Introduzca el datos siguientes:Inicio de validez : <Inicio de validez Fecha>Cantidad : <Importe>Unidad de determinación de precio : <Determinación de precios Unidad>Válido hasta : <Fin de validez Fecha>Moneda : <Moneda>Seleccionar Aplicar . | Se han añadido los datos de condición |  |
| 9 | Introducir datos de referencia (opcional) | Opcionalmente, puede introducir datos de referencia. | Se han añadido los datos de referencia. |  |
| 10 | Guardar los datos | Seleccionar Crear . | Se graba un registro info de compras. |  |

### Crear registro info de compras para subcontratación

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de compras (F1982) . | La pantalla Gestionar registros info de compras (F1982) se visualiza. |  |
| 3 | Abrir nuevo registro info de compras | Seleccionar Crear . | Aparece la pantalla Registro info de compras. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas:Registro info de compras Categoría : <Subcontratación>Organización de compras : <Compras Organización>Proveedor : <Proveedor>Material : <Material>Centro : <Centro>Grupo de compras : <Grupo de compras> | Se han añadido los datos de cabecera. |  |
| 5 | Introducir información general | Realice las siguientes entradas:Disponible desde : DD/MM/AAAAFin de disponibilidad : DD/MM/AAAA | Se ha añadido Información general. |  |
| 6 | Introducir datos de entrega y cantidad | Realice las siguientes entradas:Plazo de entrega en días : <XX Días>Tolerancia de entrega incompleta en % : <XX>Tolerancia de exceso de suministro en % : <XX>Indicador de impuestos : <Indicador de impuestos>Nota Cuando los TDT (impuestos dependientes del tiempo) se activan mediante Paso de configuración 101016 (Definir indicadores de impuestos para Ventas y compras) para el país de la sociedad y Se indica el indicador de impuestos, el campo Inicio de validez del tipo impositivo es obligatorio. Puede introducir la fecha actual, que se ajustado a la fecha de inicio de validez del indicador de impuestos según la opción en el paso de configuración.Cuando el RITA (Registro para tributación indirecta) Extranjero) está activado, el país de registro fiscal es actualizado para sociedad en paso de configuración 103464 (Activar RITA y actualizar registro fiscal) Países) y se indica el indicador de impuestos, la Residencia fiscal El campo es obligatorio, en el que el ID de país de la sociedad se indica como valor de propuesta, pero puede modificar el ID de país válido que se actualiza en Paso de configuración correspondiente.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Unidad de medida de pedido : <Unidad de pedido>Cantidad de pedido estándar : <Pedido estándar Cantidad> | Se han añadido los datos de entrega y cantidad. |  |
| 7 | Introducir datos de condición | En la sección Condición, seleccione Crear icono. Introduzca el datos siguientes:Inicio de validez : <Inicio de validez Fecha>Cantidad : <Importe>Unidad de determinación de precio : <Unidad de determinación de precio>Válido hasta : <Fin de validez Fecha>Moneda : <Moneda>Seleccionar Aplicar . | Se han añadido los datos de condición. |  |
| 8 | Introducir datos de referencia (opcional) | Opcionalmente, puede introducir datos de referencia. | Se han añadido los datos de referencia. |  |
| 9 | Guardar los datos | Seleccionar Crear . | Se graba un registro info de compras. |  |

### Crear registro info de compras para pipeline

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de compras (F1982) . | Se abre la aplicación. |  |
| 3 | Abrir nuevo registro info de compras | Seleccionar Crear . | El Pantalla de registro info de compras se visualiza. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas:Categoría de registro info de compras : <Pipeline>Organización de compras : <Organización de compras>Proveedor : <Proveedor>Material : <Material pipeline>Centro : <Centro>Grupo de compras : <Grupo de compras>Grupo de materiales : <Grupo de artículos> | Se han añadido los datos de cabecera. |  |
| 5 | Introducir información general | Realice las siguientes entradas:Disponible desde : DD/MM/AAAAFin de disponibilidad : DD/MM/AAAA | Se añade información general. |  |
| 6 | Introducir datos de compras | Realice las siguientes entradas:Incoterm : <Incoterm>Ubicación de incoterm 1 : <Incoterm Lugar 1> | Se han añadido los datos de compras. |  |
| 7 | Introducir datos de entrega y cantidad | Realice las siguientes entradas:Plazo de entrega en días : <XX días>Tolerancia de entrega incompleta en % : <XX>Tolerancia de exceso de suministro en % : <XX>Indicador de impuestos : <Indicador de impuestos>Nota Cuando los TDT (impuestos dependientes del tiempo) se activan mediante el paso de configuración 101016 (Definir Indicadores de impuestos para ventas y compras) para país de sociedad e indicador de impuestos indicados, el tipo impositivo El campo Inicio de validez es obligatorio. Puede introducir el valor actual fecha, que se ajustará a la fecha de inicio de validez del indicador de impuestos según la parametrización en Paso de configuración.Cuando RITA (Registro para tributación indirecta en el extranjero) está activado, el país de registro fiscal se actualiza para la sociedad en Paso de configuración 103464 (Activar RITA y actualizar países de registro fiscal) y el indicador de impuestos es indicado, el campo Residencia fiscal es obligatorio, en el que el ID de país de la sociedad se indica por defecto valor, pero puede cambiar al ID de país válido que se actualiza en el paso de configuración según corresponda.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Unidad de medida de pedido : <Unidad de medida de pedido>Cantidad de pedido estándar : <Cantidad de pedido estándar>Si es necesario, seleccione las siguientes entradas:Entrega ilimitadaFactura basada en entrada de mercancías VerificaciónSin recibo evaluado LiquidaciónConfirmación de pedido RequisitoControl de confirmación | Se han añadido los datos de entrega y cantidad. |  |
| 8 | Introducir datos de condición | En la Condición sección, seleccione Crear . Introduzca los siguientes datos:Inicio de validez : <Fecha de inicio de validez>Cantidad : <Importe>Unidad de determinación de precio : <Unidad de precio>Válido hasta : <Fecha de fin de validez>Moneda : <Moneda>Seleccionar Aplicar . | Se han añadido los datos de condición. |  |
| 9 | Introducir datos de referencia (opcional) | Opcionalmente, puede introducir datos de referencia. | Se han añadido los datos de referencia. |  |
| 10 | Guardar los datos | Seleccionar Crear . | Se graba un registro info de compras. |  |

### Modificaciones en masa en el registro info de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este procedimiento, se aplican modificaciones a varios Información de compras Registros en masa.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Modificaciones en masa en registros info de compras (F2667) . | Se abre la aplicación. |  |
| 3 | Buscar información de compras Registros | Para buscar registros info de compras, introduzca los siguientes valores para los filtros:Proveedor : <ID de proveedor>Grupo de compras : por ejemplo, 001Centro : <ID de centro>Seleccionar Ir . | Los resultados de la búsqueda muestran los detalles de los criterios de filtro correspondientes.Por defecto, todos los registros info de compras se seleccionan para las operaciones de modificación en masa. |  |
| 4 | Seleccionar registros info de compras | Seleccione el Registros info de compras en el Registros info de compras y Compras Organización pestaña.Seleccionar Edición en masa . |  |  |
| 5 | Fijar valores nuevos | Introduzca nuevos valores en las siguientes entradas:En la Datos generales sección:Nº mat.proveedorGrupo de artículos de proveedorEn la Datos de organización de compras sección:Grupo de comprasCantidad mínima de pedidoSeleccionar Aplicar modificaciones en masa .Aparece una ventana de diálogo para confirmar las modificaciones en masa.El Aplicar modificaciones en masa , seleccione Aplicar .Se muestra una ventana de diálogo con el ID JOB .Seleccionar Ver lista de tareas . | Los valores nuevos se aplican a los registros info de compras seleccionados. |  |
| 6 | Verificar jobs de aplicación | Introduzca los criterios de búsqueda y seleccione Ir.El Jobs de aplicación con la lista de IDs de job para toda la información de compras registros.Seleccionar Log para verificar el éxito de los registros info de compras seleccionados. |  |  |

### Modificaciones de precio en masa en registro info de compras

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este procedimiento, el Modif.precio: Registros info (MEKP) La aplicación se utiliza para actualizar en masa los precios de los registros info.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Modif.precio: Registros info (MEKP) . | Se abre la aplicación. |  |
| 3 | Introducir datos iniciales | Realice las siguientes entradas y seleccione Ejecutar :Organización de compras : <ID de organización de compras>Proveedor : <ID de proveedor>Material : <ID de material>Registros info sin material : <En blanco>Ejecución de test : <En blanco>Vaya a Modificar clase de condición o precio bruto y realice las siguientes entradas:Clase de condición : <ID de clase de condición> , por ejemplo, PPR0Importe absoluto : <Importe absoluto> , por ejemplo, 10Signo +/- : <Signo> , por ejemplo, +Precio bruto : <En blanco>Líneas de escala : <X>Vaya a Condiciones válidas y realice las siguientes entradas:Activado : <Fecha actual>O bien De <En blanco> Hasta <En blanco> | Se actualizan nuevos valores para los registros info de compras. |  |
| 4 | Verificar modificaciones de registros info de compras | El Modificación de precio para registros info de proveedor <XXXX> , verifique la Antiguo y Nuevo registra y confirma las modificaciones. | Se guardan las modificaciones de precio de los registros info de compras. |  |
| 5 | Salir | Seleccionar Salir . |  |  |

## Apéndice

### Funciones relevantes

Aquí se enumeran algunas funcionalidades de aplicación importantes relacionadas con el registro info de compras, que no se contemplan en los procedimientos de ensayo anteriores.

| Área funcional | Función | Información detallada | Comentario |
| --- | --- | --- | --- |
| Registros info de compras | Aplicaciones relacionadas con el registro info | WebGUI: Borrar registro info de compras (ME15)WebGUI: Visualizar registro info de compras por proveedor (ME1L)WebGUI: Actualizar modificaciones en registros info de compras (ME14)WebGUI: Actualizar condiciones de compras (MEKA)WebGUI: Actualizar perfil de redondeo (OWD1) |  |

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
- related-to :: [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563]]
- related-to :: [[10-procurement/criar-registro-info-para-compras-mds-bhd-566]]
- related-to :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]
- related-to :: [[10-procurement/mds-bhd-565]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 31,626 chars in the whole document
