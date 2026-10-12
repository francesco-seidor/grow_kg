---
id: 06-management-accounting/script-de-datos-maestros-crear-clase-de-actividad-y-jerarquia-de-clase
title: "Script de datos maestros: Crear clase de actividad y jerarquía de clases de actividad - MDS (BNN) (BNN_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script BNN for creating activity types and activity type hierarchies, with change log and usage analysis."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_ES_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchies, activity type change log, activity type usage, controlling area, cost elements, overhead cost accounting, business roles, BNN]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-642
topic: 06-management-accounting/activity-types
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear clase de actividad y jerarquía de clases de actividad - MDS (BNN) (BNN_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear clase de actividad y jerarquía de clases de actividad - MDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894999)

[2 Requisitos previos 3](#_Toc233895000)

[2.1 Acceso al sistema 3](#_Toc233895001)

[2.2 Roles 3](#_Toc233895002)

[2.3 Unidades organizativas necesarias 3](#_Toc233895003)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895004)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233895005)

[2.6 Pasos preliminares 4](#_Toc233895006)

[2.6.1 Opciones de usuario - Fijar sociedad CO 4](#_Toc233895007)

[3 Tabla de resumen 6](#_Toc233895008)

[4 Procedimientos de prueba 7](#_Toc233895009)

[4.1 Creación de datos maestros de clase de actividad 7](#_Toc233895010)

[4.2 Creación de datos maestros de jerarquía de clases de actividad 8](#_Toc233895011)

[4.3 Análisis 10](#_Toc233895012)

[4.3.1 Log de modificaciones de tipo de actividad 10](#_Toc233895013)

[4.3.2 Lista de utilización - Tipos de actividad 11](#_Toc233895014)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Las clases de actividad representan las actividades producidas por un centro de coste dentro de una sociedad CO. Las clases de actividad se utilizan para planificar y imputar actividades registradas y medidas en unidades de actividad. Los volúmenes de actividad se valoran mediante una tarifa que actualizado en el centro de coste.

Las clases de actividad se utilizan de la siguiente manera:

Para determinar la salida basada en cantidad de un centro de coste. Los volúmenes de actividad plan de los centros de coste de fabricación y servicio deben ser reconciliado con el plan maestro de producción en logística. Esto determina el volumen de actividad plan necesario, así como el plan capacidad.

Controlar los volúmenes de actividad en los centros de coste. Esto permite la medición del nivel de ocupación o la tasa de capacidad utilización de un centro de coste.

Además de la planificación manual de volúmenes de actividad, también puede utilizar la facturación indirecta de actividad para planificar volúmenes de actividad. automáticamente.

Las jerarquías de clases de actividad también son útiles en la planificación. Dado que no hay ninguna herramienta de selección múltiple disponible para las clases de actividad, Las actividades se pueden recopilar en jerarquías de clases de actividad para permitir la planificación de varias clases de actividad a la vez.

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
| Contable de costes - Gastos generales | SAP_BR_OVERHEAD_ACCOUNTANT | Contabilidad de gastos generales | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se crearon en el sistema ERP durante la implementación. La organización estructura refleja la estructura de su empresa. Los datos maestros representan las clases de actividad y las jerarquías de clases de actividad, dependiendo de el enfoque operativo de su empresa.

| Objeto de datos | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad CO | Datos generales | Obligatorio |  |

### Datos maestros obligatorios y opcionales

Valores propuestos

La estructura organizativa y los datos maestros de su empresa se han creado en su ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros en función del enfoque operativo de su empresa.

El proceso empresarial se habilita con estos datos maestros específicos de la organización, ejemplos se proporcionan en la siguiente sección.

Los registros de jerarquía de clase de actividad y clase de actividad pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de opcional y los objetos de datos maestros obligatorios que se utilizarán en un registro de datos de clase de actividad.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Clase de coste | Datos generales | Obligatorio | Clase de coste secundario (tipo de clase de coste "43") |
| Cuenta de mayor |  | Obligatorio | Para la clase de coste secundario (tipo de clase de coste "43") |

### Parámetros principales para la creación de datos

Este elemento de alcance no tiene condiciones empresariales.

### Pasos preliminares

#### Opciones de usuario - Fijar sociedad CO

| Paso # | Nombre de paso | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión en la rampa de lanzamiento SAP Fiori | Inicie sesión en el Rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Seleccione Opciones. | En el menú contextual de usuario, seleccione Opciones . | El Opciones de usuario Aparece la ventana. |  |
| 3 | Seleccionar valores predeterminados | Seleccionar Valores propuestos en la ventana. | El Valores propuestos Aparece la ventana. |  |
| 4 | Introducir datos | En la Sociedad CO , introduzca <Valor de sociedad CO> , luego seleccione Grabar . | Sociedad CO, por ejemplo, A000 , está definido para su usuario. |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de clase de actividad](#unique_10) [página ] 7 | Contable de costes - Gastos generales | Gestionar tipos de actividad (F1605A) | Las clases de actividad se pueden crear de acuerdo con los nuevos requisitos empresariales. |
| [Creación de datos maestros de jerarquía de clases de actividad](#unique_11) [página ] 8 | Contable de costes - Gastos generales | Gestionar jerarquías globales (F2918) | Las jerarquías de clases de actividad se pueden crear según nuevos requisitos empresariales. |
| [Log de modificaciones de tipo de actividad](#unique_12) [página ] 10 | Contable de costes - Gastos generales | Log de modificaciones - Clases de actividad (F3866) |  |
| [Lista de utilización - Tipos de actividad](#unique_13) [página ] 11 | Contable de costes - Gastos generales | Gestión de tipos de actividad (versión 2) (F1605A) |  |

## Procedimientos de prueba

En esta sección se describen los procedimientos para cada paso del proceso que pertenece a este elemento de alcance. También puede utilizar estos procedimientos para probar la creación de datos maestros.

### Creación de datos maestros de clase de actividad

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar tipos de actividad (F1605A) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | Seleccionar Crear . |  |  |
| 4 | Introducir datos de tipo de actividad | El Nuevo tipo de actividad: Nuevo pantalla, en la pantalla Datos generales , haga el siguientes entradas:Introducir tipo de actividad : Texto descriptivoUnidad de actividad : <Unidad de actividad>Nombre : <Nombre>Descripción de clase de actividad : <Introduzca una descripción>Inicio de validez : <Fecha actual>Válido hasta : <Fecha de fin de año>Clase de centro de coste : <Categoría de centro de coste>Tipo de clase de actividad : <Tipo de clase de actividad>Clase de coste de imputación : Por ejemplo, 94304000 .Indicador de precio : <Indicador de precio> | El Datos generales y se muestran varias pestañas.Nota Puede encontrar los valores recomendados por SAP para SAP S/4HANA Cloud Public Edición (como otros, aunque es posible que no se admitan visibles) a continuación:Tipo de clase de actividad : solo 1 (entrada manual e imputación manual) es admitido.Indicador de precio : solo 3 (el precio se fija manualmente).Tipo de clase de actividad real : debe estar en blanco.Indicador de tarifa real : debe estar en blanco de forma predeterminada. Solo si ha activado el elemento de alcance 33Q - Cálculo de costes real , debería uso 5 o bien 7 (para obtener detalles sobre estos dos valores, puede consultar la sección en el script de test de 33Q ). |  |
| 5 | Guardar los datos | Seleccionar Crear . | La clase de actividad se ha creado y grabado. |  |

### Creación de datos maestros de jerarquía de clases de actividad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Ha rellenado y grabado los datos básicos para el material como se describe en [Creación de datos maestros de clase de actividad](#unique_10) [página ] 7.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar jerarquías globales (F2918) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | En la Lista de jerarquías sección, seleccione Crear . | El Nueva jerarquía se visualiza. |  |
| 4 | Introducir nueva jerarquía de clases de actividad | El Nueva jerarquía , realice lo siguiente entradas y seleccione Crear :Tipo : Jerarquía de clases de actividadID de jerarquía : <Cualquier ID de hasta 10 caracteres>Atención La longitud total del ID de jerarquía y del ID de nodo no puede superar los 14 caracteres.Sociedad CO : A000Descripción de jerarquía : <Cualquier descripción> |  |  |
| 5 | Editar nueva jerarquía de tipos de actividad | El Lista de jerarquías , seleccione el icono de detalle > y seleccione Editar para su jerarquía de clases de actividad recién creada.Seleccione la jerarquía de clases de actividad recién creada, seleccione Más en la parte derecha de la pantalla, y a continuación, seleccione Entrada rápida .El Entrada rápida pantalla, seleccione Clase de actividad y hacer lo siguiente entrada:ID : <Seleccione los tipos de actividad que desea añadir mediante la búsqueda función>Seleccionar OK cuando termine y seleccione Grabar .Regrese a la Jerarquía de clases de actividad y seleccione Activar . | La jerarquía de tipos de actividad recién creada ahora está activada. |  |

### Análisis

#### Log de modificaciones de tipo de actividad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad se ejecuta el log de modificaciones para las clases de actividad.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Log de modificaciones - Clases de actividad (F3866) . | El Log de modificaciones: tipos de actividad ventana de diálogo se visualiza. |  |
| 3 | Criterios de selección | Realice las siguientes entradas:Clase de actividad : <Cualquier actividad tipo> |  |  |
| 4 | Seleccionar | Seleccionar Ir . | Se visualiza un informe que muestra el historial detallado de modificaciones. |  |

#### Lista de utilización - Tipos de actividad

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Esta actividad le permite ver dónde se utilizan los tipos de actividad en otros datos maestros como centros de beneficio e imputaciones de costes reales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de tipos de actividad (versión 2) (F1605A) . | Se abre la aplicación. |  |
| 3 | Criterios de selección | Realice las siguientes entradas:Clase de actividad : <Cualquier actividad tipo> |  |  |
| 4 | Utilización | Seleccione el centro de coste deseado y seleccione Utilización: Actividad Tipos . | Se visualiza un informe que muestra dónde se utilizan actualmente las clases de actividad. Para las colas de De's, tú puede seleccionar el tipo de objeto de datos maestros y seguir explorando. |  |

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
- related-to :: [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644]]
- related-to :: [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640]]
- related-to :: [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn]]
- related-to :: [[06-management-accounting/mds-bnn-643]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 18,817 chars in the whole document
