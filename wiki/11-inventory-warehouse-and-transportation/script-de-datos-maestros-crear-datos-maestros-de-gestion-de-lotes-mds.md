---
id: 11-inventory-warehouse-and-transportation/script-de-datos-maestros-crear-datos-maestros-de-gestion-de-lotes-mds
title: Script de datos maestros - Crear datos maestros de gestión de lotes - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ES_XX)
description: "Spanish test script (SAP S/4HANA Cloud Public Edition 2608) for creating batch management master data: characteristics, classes, sort sequences, batch search and derivation strategies."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [2ZW_S4CLD2608_Master_Data_ES_XX]
keywords: [Batch Management Master Data, batch characteristics, batch classes, sort sequences, batch search strategies, batch determination, batch derivation strategies, business roles, test procedures, fiori launchpad access]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-300
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear datos maestros de gestión de lotes - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear datos maestros de gestión de lotes - MDS (2ZW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894589)

[2 Requisitos previos 3](#_Toc233894590)

[2.1 Acceso al sistema 3](#_Toc233894591)

[2.2 Roles 3](#_Toc233894592)

[3 Tabla de resumen 4](#_Toc233894593)

[4 Procedimientos de prueba 5](#_Toc233894594)

[4.1 Crear característica 5](#_Toc233894595)

[4.2 Crear clase 6](#_Toc233894596)

[4.3 Crear secuencia de clasificación 7](#_Toc233894597)

[4.4 Crear registros de estrategia de búsqueda de lotes para la gestión de stocks 9](#_Toc233894598)

[4.5 Crear registros de estrategia de búsqueda de lotes para producción 11](#_Toc233894599)

[4.6 Crear registros de estrategia de búsqueda de lotes para Comercial 12](#_Toc233894600)

[4.7 Crear estrategia de derivación para material emisor 14](#_Toc233894601)

[4.8 Crear estrategia de derivación para material receptor 16](#_Toc233894602)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Los datos maestros de gestión de lotes incluyen especificaciones de lotes, secuencias de clasificación (reglas de clasificación) y registros de estrategia de búsqueda de lotes en lotes determinación.

Las especificaciones de lote describen las propiedades técnicas, físicas y químicas de un lote. Almacena especificaciones de lote, como lote estado o potencia de la sustancia activa, como características en el sistema de clasificación.

Puede utilizar el sistema de clasificación para asignar las especificaciones de material al material de un lote. Estas especificaciones de material están asignados a la misma clase que los lotes de los materiales. Por lo tanto, puede almacenar los valores de destino de un lote con el correspondiente rango de tolerancia. Estos valores teóricos se utilizan, por ejemplo, en la inspección de calidad o durante la transacción de entrada de mercancías, si es necesario para clasificar inmediatamente un lote. Los valores también se utilizan para la verificación de la facilidad de uso.

En el material se almacenan los rangos de destino para todas las características. Como el lote pertenece a la misma clase que el material, el lote recibe automáticamente las características del material. Para cada lote individual, introduzca los valores reales exactos.

La determinación de lotes que tiene lugar en diferentes procesos (gestión de stocks, producción, ventas y distribución) tienen diferentes criterios. Las secuencias de clasificación y los registros de estrategia de búsqueda de lotes son necesarios para actualizar los criterios.

La secuencia de clasificación le indica si los lotes en el resultado de búsqueda de la determinación de lotes se clasifican en orden ascendente o descendente de valores de característica.

En una estrategia de búsqueda de lotes para la determinación de lotes, puede definir los valores según los cuales el sistema debe buscar lotes. incluidos los atributos para el proceso (por ejemplo, clase de movimiento, clase de orden o centro) y el número de material. Solo cuando los registros de condición están satisfechos pueden seguir clasificándose y determinándose estos lotes en función de las secuencias de clasificación y las especificaciones de los lotes.

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
| Responsable de listas de materiales | SAP_BR_BOM_ENGINEER | Listas de materiales | SAP_BR_BOM_ENGINEER |  |
| Especialista en datos maestros - Datos de lote | SAP_BR_BATCH_MASTER_SPCLST | Datos maestros - Lote | SAP_BR_BATCH_MASTER_SPCLST |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear característica](#unique_6) [página ] 5 | Responsable de listas de materiales | Gestionar características (CT04) | Se ha creado la característica. |
| [Crear clase](#unique_7) [página ] 6 | Responsable de listas de materiales | Gestionar clases (CL02) | Se ha creado la clase. |
| [Crear secuencia de clasificación](#unique_8) [página ] 7 | Especialista en datos maestros - Datos de lote | Crear secuencia de clasificación (CU70) | Se ha creado la secuencia de clasificación. |
| [Crear registros de estrategia de búsqueda de lotes para la gestión de stocks](#unique_9) [página ] 9 | Especialista en datos maestros - Datos de lote | Gestionar estrategias de búsqueda - Gestión de stocks (MBC2) | Se crean registros de estrategia de búsqueda de lotes. |
| [Crear registros de estrategia de búsqueda de lotes para producción](#unique_10) [página ] 11 | Especialista en datos maestros - Datos de lote | Gestionar estrategias de búsqueda - Producción (COB2) | Se crean registros de estrategia de búsqueda de lotes. |
| [Crear registros de estrategia de búsqueda de lotes para Comercial](#unique_11) [página ] 12 | Especialista en datos maestros - Datos de lote | Gestionar estrategias de búsqueda - Comercial (VCH2) | Se crean registros de estrategia de búsqueda de lotes. |
| [Crear estrategia de derivación para material emisor](#unique_12) [página ] 14 | Especialista en datos maestros - Datos de lote | Gestionar estrategias de derivación - Emisor (DVS2) | Se ha creado la estrategia de derivación para el material emisor. |
| [Crear estrategia de derivación para material receptor](#unique_13) [página ] 16 | Especialista en datos maestros - Datos de lote | Gestionar estrategias de derivación - Receptor (DVR2) | Se ha creado la estrategia de derivación para el material receptor. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear característica

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear la característica.

Procedimiento

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar características (CT04) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Responsable de listas de materiales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar características (CT04) . | El Características se visualiza.Nota Pantalla común para el modo de creación, modificación y visualización. |  |
| 3 | Introducir nombre de característica | Introduzca lo siguiente y seleccione Crear .Característica : <Su nombre de característica> | El Datos básicos visualización de opciones de pantalla.Nota El valor en el Inicio de validez El campo es rellenado automáticamente. |  |
| 4 | Introducir datos básicos | Introduzca lo siguiente y seleccione Grabar :Datos básicos sección:Descripción : <Introduzca su descripción>Estado : Liberado (predeterminado)Formato sección:Tipo de datos : <Seleccione un formato>Valoración sección:Seleccione el Valor individual botón de selección. | Nota Se requieren otros campos para el formato seleccionado en la Formato Sección . Actualice según corresponda. |  |
| 5 | Introducir valores para verificación | El Valores en la pestaña Permitido Valores introduzca los valores permitidos para este característica. |  |  |
| 6 | Grabar la característica | Seleccionar Grabar . | Se crea la característica. |  |

### Crear clase

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear una clase.

Requisito previo

Debe completar la sección anterior, [Crear característica](#unique_6) [página ] 5, antes de continuar con esto sección.

Procedimiento

Siga el siguiente procedimiento cuando su acceso de usuario le presente el Gestionar clases (CL02) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Responsable de listas de materiales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar clases (CL02) . | El Clase se visualiza.Nota Es una pantalla común para el modo de creación, modificación y visualización. |  |
| 3 | Introducir nombre de clase | Realice las siguientes entradas y seleccione Crear :Clase : <Clase nombre>Categoría de clase : 023 | El Crear clase se visualiza.Nota El Inicio de validez campo se rellena automáticamente en con un valor. |  |
| 4 | Introducir datos básicos | El Datos básicos pestaña, realice lo siguiente entradas:En la Datos básicos sección:Descripción : <Clase descripción>Estado : Liberado |  |  |
| 5 | Introducir tab.caract. | Seleccione el Caract. y realice la siguiente entrada para asignar características que ha creado a esta clase y, a continuación, pulse Intro :En la Caract. columna:Caract. : <Característica nombre> | El Descripción y Datos Tipo campos de características se rellenan automáticamente en con valores. |  |

### Crear secuencia de clasificación

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear secuencias de clasificación.

Requisito previo

Debe completar la sección Crear característica antes que usted continúe con esta sección.

Procedimiento

Utilice el siguiente procedimiento cuando su acceso de usuario le presente el Crear secuencia de clasificación (CU70) aplicación.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear secuencia de clasificación (CU70) . | El Crear secuencia de clasificación pantalla se visualiza. |  |
| 3 | Introducir nombre de secuencia de clasificación | Realice las siguientes entradas y seleccione el Crear icono:Secuencia de clasificación : <Ordenar Nombre de secuencia> | El Crear secuencia de clasificación: Datos básicos se visualiza la pantalla. |  |
| 4 | Introducir datos básicos | Actualice la descripción junto al Nombre de secuencia de clasificación y seleccionar Características .Descripción : <Ordenar Descripción de secuencia> | El Crear secuencia de clasificación: Características se visualiza la pantalla. |  |
| 5 | Indicar detalles de secuencia de clasificación | Seleccionar Entradas nuevas para actualizar el columnas siguientes y seleccione Grabar :Característica : <Nombre de característica>Ascendente : XDesglose : ‘ ’ | Se crea la secuencia de clasificación.Nota Puede especificar un orden ascendente o descendente. |  |

### Crear registros de estrategia de búsqueda de lotes para la gestión de stocks

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear estrategias de búsqueda para Determinación de lotes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Se muestra la rampa de lanzamiento SAP Fiori. | Abierto Gestionar estrategias de búsqueda - Gestión de stocks (MBC2) . | El Modificar estrategia de búsqueda de lotes: Inicial Pantalla muestra. |  |
| 3 | Introducir tipo de estrategia | Realice las siguientes entradas y seleccione Modif. :Tipo de estrategia : <Tipo de estrategia, p. ej. YB11>Nota el tipo de estrategia se puede configurar por autoservicio IU de configuración. | La ventana emergente Combinación de claves se visualiza. |  |
| 4 | Seleccionar Combinación de claves | En la ventana emergente Combinación de claves , seleccione uno de las siguientes opciones y seleccione Seleccionar :Clase de movimiento/Centro/MaterialCentro/MaterialClase de movimiento/MaterialClase de movimiento/CentroClase de movimiento | El Modificar IC: Número de lote (YB11): Selección muestra. | El Combinaciones de claves dependen de la Tipo de estrategia que elijas. Si solo hay una combinación de claves en la estrategia seleccionada, la ventana emergente no aparecerá. |
| 5 | Introduzca su selección | Para especificar sus registros, introduzca los siguientes atributos que visualizado en función de la combinación de claves seleccionada y seleccione Ejecutar :Clase de movimiento de mercancías : <Clase de movimiento de mercancías>Centro : <Centro>Material : <Material Número> | El Modificar IC: Número de lote (YB11): Rápido Entrada muestra. |  |
| 6 | Introduzca su registro de estrategia en detalle | Para crear un registro nuevo, debe introducir las siguientes entradas: y seleccione Grabar :Material : <Material Número>Si es necesario, también puede especificar los siguientes atributos para cada registro:Ctd.particiones lotesModificaciones permitidasDeterminación de lotes de diálogoVisualizar UMPropuesta de cantidadExceso de suministro permitidoTipo de selección |  |  |
| 7 | Actualizar criterios de selección (opcional) | Para seguir actualizando los criterios de selección para el lote Valor de característica del material en un registro, seleccione el registro y seleccione Criterios de selección . | El Modificar IC: Clasificación se visualiza. |  |
| 8 | Actualizar secuencia de clasificación (opcional) | Para actualizar la secuencia de clasificación para registros específicos, seleccione el registro y seleccione Clasificar . | El Modificar IC: Número de lote (YB11): Clasificar Regla muestra. |  |

### Crear registros de estrategia de búsqueda de lotes para producción

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear estrategias de búsqueda para Determinación de lotes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar estrategias de búsqueda - Producción (COB2) . | El Modificar estrategia de búsqueda de lotes: Inicial Pantalla muestra. |  |
| 3 | Introducir tipo de estrategia | Realice las siguientes entradas y seleccione Modificar:Tipo de estrategia : <Tipo de estrategia, p. ej., YB11>Nota El tipo de estrategia se puede configurar por autoservicio IU de configuración. | El Modificar IC: Número de lote (YB11): Selección muestra.Nota La combinación de claves no se muestra porque solo hay una clave combinación configurada para YB11 en producción |  |
| 4 | Introduzca su selección | Para especificar sus registros, introduzca los siguientes atributos que visualizado en función de la combinación de claves seleccionada y seleccione Ejecutar :Clase de orden : <Orden Tipo>Centro : <Centro>Material : <Material Número> | El Modificar IC: Número de lote (YB11): Rápido Entrada muestra. | El Combinaciones de claves dependen de la Tipo de estrategia que elijas. Si solo hay una combinación de claves en la estrategia seleccionada, la ventana emergente no aparecerá. |
| 5 | Introduzca su registro de estrategia en detalle | Para crear un registro nuevo, debe introducir las siguientes entradas: y seleccione Grabar :Material : <Material Número>Si es necesario, también puede especificar los siguientes atributos para cada registro:Ctd.particiones lotesModificaciones permitidasDeterminación de lotes de diálogoVisualizar UMPropuesta de cantidadExceso de suministro permitidoTipo de selección |  |  |
| 6 | Actualizar criterios de selección (opcional) | Para seguir actualizando los criterios de selección para el lote Valor de característica del material en un registro, seleccione el registro y seleccione Criterios de selección . | El Modificar IC: Clasificación se visualiza. |  |
| 7 | Actualizar secuencia de clasificación (opcional) | Para actualizar la secuencia de clasificación para registros específicos, seleccione el registro y seleccione Clasificar . | El Modificar IC: Número de lote (YB11): Clasificar Regla muestra. |  |

### Crear registros de estrategia de búsqueda de lotes para Comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear estrategias de búsqueda para Determinación de lotes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar estrategias de búsqueda - Comercial (VCH2) . | La pantalla Modificar estrategia de búsqueda de lotes: Pantalla inicial se visualiza. |  |
| 3 | Introducir tipo de estrategia | Realice las siguientes entradas y seleccione Modificar:Tipo de estrategia : <Tipo de estrategia, p. ej., YB11>Nota el tipo de estrategia se puede configurar por autoservicio IU de configuración. | La ventana emergente Combinación de claves se visualiza. |  |
| 4 | Seleccionar combinación de claves | En la ventana emergente Combinación de claves , seleccione uno de las siguientes opciones y seleccione Seleccionar :Cliente/MaterialMaterial | El Modificar IC: Número de lote (YB11): Selección muestra. | El Combinaciones de claves dependen de la Tipo de estrategia que elijas. Si solo hay una combinación de claves en la estrategia seleccionada, la ventana emergente no aparecerá. |
| 5 | Introduzca su selección | Para especificar sus registros, introduzca los siguientes atributos que visualizado en función de la combinación de claves seleccionada y seleccione Ejecutar :Cliente : <Cliente ID>Material : <Material Número> | El Modificar IC: Número de lote (YB11): Rápido Entrada muestra. |  |
| 6 | Introduzca su registro de estrategia en detalle | Para crear un registro nuevo, debe introducir las siguientes entradas: y seleccione Grabar :Material : <Material Número>Si es necesario, también puede especificar los siguientes atributos para cada registro:Ctd.particiones lotesModificaciones permitidasDeterminación de lotes de diálogoVisualizar UMPropuesta de cantidadExceso de suministro permitidoTipo de selección |  |  |
| 7 | Actualizar criterios de selección (opcional) | Para seguir actualizando los criterios de selección para el lote Valor de característica del material en un registro, seleccione el registro y seleccione Criterios de selección . | El Modificar IC: Clasificación se visualiza. |  |
| 8 | Actualizar secuencia de clasificación (opcional) | Para actualizar la secuencia de clasificación para registros específicos, seleccione el registro y seleccione Clasificar . | El Modificar IC: Número de lote (YB11): Clasificar Regla muestra. |  |

### Crear estrategia de derivación para material emisor

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear registros de estrategia que se utilizan para determinar atributos para el material emisor durante la derivación de lotes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar estrategias de derivación - Emisor (DVS2) . | El Derivación - Modificar estrategia de búsqueda: Inicial se visualiza. |  |
| 3 | Introducir tipo de estrategia | Realice la siguiente entrada y seleccione Modif. :Tipo de estrategia : <Clase de estrategia> | La ventana emergente Combinación de claves muestra. | Antes de este paso, debe finalizar los siguientes pasos de configuración en función de sus necesidades:Rangos de números para derivación de lotesDeterminar lotes emisores en derivación de lotes |
| 4 | Seleccionar combinación de claves | En la ventana emergente Combinación de claves , seleccione una de las siguientes opciones y seleccione Seleccionar :<Combinación de teclas 1><Combinación de teclas 2>… | El Modificar <Clase de estrategia>: Selección se visualiza. | El Combinaciones de claves dependen de la Tipo de estrategia que usted elija. |
| 5 | Introduzca su selección | Para especificar sus registros, introduzca los siguientes atributos que se visualizan en función de los seleccionados Combinación de claves , y seleccionar Ejecutar :Material emisor : <ID de material emisor><Campo clave> : <Valor clave>… | El Modificar <Clase de estrategia>: Entrada rápida se visualiza. |  |
| 6 | Introduzca su registro de estrategia | Para crear un registro nuevo, debe introducir la siguiente entrada y seleccionar Grabar :Material emisor : <ID de material emisor>Para seguir actualizando los detalles del material emisor, seleccione un registro y elija Detalles . | El Modificar <Clase de estrategia>: Detalles se visualiza. |  |
| 7 | Actualizar detalles de registro de estrategia | En la Atributos enviados (campos/características) , realice las siguientes entradas y seleccione Grabar :Atributo : <ID de material emisor>Campo : <Seleccionado por defecto>Característica : <No seleccionado por defecto> |  |  |

### Crear estrategia de derivación para material receptor

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear registros de estrategia que se utilizan para determinar atributos para el material receptor durante la derivación de lotes.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de lote . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar estrategias de derivación - Receptor (DVR2) . | El Derivación - Modificar estrategia de búsqueda: Inicial se visualiza. |  |
| 3 | Introducir tipo de estrategia | Realice la siguiente entrada y seleccione Modif. :Tipo de estrategia : <Clase de estrategia> | La ventana emergente Combinación de claves muestra. | Antes de este paso, debe finalizar los siguientes pasos de configuración en función de sus necesidades:Rangos de números para derivación de lotesDeterminar lotes de destino en derivación de lotes |
| 4 | Seleccionar combinación de claves | En la ventana emergente Combinación de claves , seleccione una de las siguientes opciones y seleccione Seleccionar :<Combinación de teclas 1><Combinación de teclas 2>… | El Modificar <Clase de estrategia>: Selección se visualiza. | El Combinaciones de claves dependen de la Tipo de estrategia usted seleccione. |
| 5 | Introduzca su selección | Para especificar sus registros, introduzca los siguientes atributos que se visualizan en función de los seleccionados Combinación de claves , y seleccionar Ejecutar :Material receptor : <ID de material receptor><Campo clave> : <Valor clave>… | El Modificar <Clase de estrategia>: Entrada rápida se visualiza. |  |
| 6 | Introduzca su registro de estrategia | Para crear un registro nuevo, debe introducir la siguiente entrada y seleccionar Grabar :Material receptor : <ID de material receptor>Para seguir actualizando los detalles del material receptor, seleccione un registro y elija Detalles . | El Modificar <Clase de estrategia>: Detalles se visualiza. |  |
| 7 | Actualizar detalles de registro de estrategia | En la pestaña Atributos , en la Atributos recibidos (campos/características) sección, introduzca las siguientes entradas y seleccione Grabar :Atributo : <ID de material de destinatario>Campo : <Seleccionado por defecto>Característica : <No seleccionado por defecto>Para actualizar las reglas para cada atributo, seleccione un atributo y elija la pestaña Reglas y, a continuación, puede actualizar las siguientes reglas:Reglas para controlar la derivaciónCampo emisor vacíoSobrescribir receptorNiveles en la referencia de utilización de lotesEl receptor no envíaReglas para la selección de valores si hay más de un emisorComparativoBooleanoCaracterísticas de varios valores |  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 32,378 chars in the whole document
