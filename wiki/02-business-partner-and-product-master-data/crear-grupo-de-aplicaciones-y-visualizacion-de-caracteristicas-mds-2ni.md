---
id: 02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni
title: Crear grupo de aplicaciones y visualización de características - MDS (2NI) (2NI_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script 2NI: create an application group and characteristic display with characteristic assignment in SAP S/4HANA Cloud Public Edition."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_ES_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic display, application group, characteristic assignment, variant configuration, master data script, business roles, transaction types, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-270
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear grupo de aplicaciones y visualización de características - MDS (2NI) (2NI_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear grupo de aplicaciones y visualización de características - MDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894530)

[2 Requisitos previos 3](#_Toc233894531)

[2.1 Acceso al sistema 3](#_Toc233894532)

[2.2 Roles 3](#_Toc233894533)

[2.3 Datos maestros obligatorios y operativos 3](#_Toc233894534)

[2.4 Parámetros principales para la creación de datos 4](#_Toc233894535)

[2.4.1 Transacción 4](#_Toc233894536)

[3 Tabla de resumen 5](#_Toc233894537)

[4 Procedimientos de prueba 6](#_Toc233894538)

[4.1 Crear grupo de aplicaciones 6](#_Toc233894539)

[4.2 Crear visualización de características 7](#_Toc233894540)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, obtendrá una descripción de cómo crear un registro de visualización de características para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye datos relevantes para SAP S/4HANA Cloud Public Edición como aplicación Grupo, Visualización de características y Asignación de características. Campos que no son relevantes para el alcance de SAP S/4HANA Cloud Public Edición no se describen en este documento.

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
| Modelador de configuración de producto | SAP_BR_PRODUCT_CONFIG_MODELER | Configuración de variantes | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Datos maestros obligatorios y operativos

Los registros de visualización de características pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un material registro de datos maestros.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Características |  | Obligatorio | Las características se deben asignar a la visualización de características registro |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro y siempre son necesarios para crear una visualización de características.

#### Transacción

Con la ayuda de la transacción, el sistema determina en qué transacción debería estar disponible la visualización de características.

Para la edición 1711, solo se admite el documento comercial.

| Transacción | Comentario |
| --- | --- |
| Documento comercial | Para la edición 1711, solo el documento comercial es se admite para la visualización de características. |
| Orden de fabricación |  |
| Pedido abierto comercial |  |
| Pedido de compra |  |
| Entrada de mercancías |  |
| Confirmación de pedido |  |

## Tabla de resumen

En esta sección, una lista de pasos por los que pasa un usuario al crear un registro de datos maestros es proporcionado. Cada segmento lógico y significativo de un objeto de datos maestros debería llevar a un paso separado (por ejemplo: org.-segmentos de datos dependientes de unidad, etc.).

El elemento de alcance Crear grupo de aplicaciones y visualización de características - MDS consta de varios pasos de proceso se proporcionan en los siguientes cuadros:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso, informe o posición | Rol empresarial | Transacción/APP | Resultados previstos |
| --- | --- | --- | --- |
| [Crear grupo de aplicaciones](#unique_9) [página ] 6 | Modelador de configuración de producto | Actualizar caract. Visualizar para configuración (CU_CHAR_DISPLAY) | Se ha creado el grupo de aplicaciones |
| [Crear visualización de características](#unique_10) [página ] 7 | Modelador de configuración de producto | Actualizar caract. Visualizar para configuración (CU_CHAR_DISPLAY) | Se ha creado el grupo de aplicaciones |

## Procedimientos de prueba

En esta sección se describen los procedimientos para cada paso del proceso que pertenece a este elemento de alcance. También puede utilizar estos procedimientos para probar la creación de datos maestros.

### Crear grupo de aplicaciones

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar caract. Visualizar para configuración (CU_CHAR_DISPLAY) . | El Modificar vista "Grupo de aplicaciones": Resumen se visualiza. |  |
| 3 | Introducir grupo de aplicaciones | El Modificar vista "Grupo de aplicaciones": Resumen seleccione Entrada nueva . Y haga lo siguiente entradas:Transac. : <Seleccionar de la lista desplegable>Gpo.aplic. : <Cualquier código> | El Entradas nuevas: Resumen de entradas añadidas se visualiza. |  |
| 4 | Guardar los datos | Seleccionar Grabar . |  |  |

### Crear visualización de características

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Modelador de configuración de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar caract. Visualizar para configuración (CU_CHAR_DISPLAY) . | El Modificar vista "Grupo de aplicaciones": Resumen se visualiza. |  |
| 3 | Introducir grupo de aplicaciones | El Modificar vista "Grupo de aplicaciones": Resumen seleccione Visualización de características .Seleccionar Entrada nueva . Realice la siguiente entrada y pulse Intro :Visual.caract. : <Cualquier código> .Descripción : <Introduzca una descripción para la característica visualizar> .Gpo.aplic. : <Seleccione F4 para obtener ayuda> . | El Modificar vista "Visualización de características": Resumen se visualiza. |  |
| 4 | Asignar característica | Seleccione la visualización de características creada en el paso anterior y seleccione Característica Asignación .Realice las siguientes entradas:Sec. : <Introduzca el número de secuencia para determinar la secuencia de la característica> .Nombre de característica : <Buscar una característica por seleccionando Ayuda para búsqueda F4> .Col. : <Introduzca el ancho de columna adecuado para mostrar la descripción y el valor de la característica> . | El Modificar vista "Asignación de característica": Resumen pantalla se visualiza. |  |
| 5 | Guardar los datos | Seleccionar Grabar . |  |  |

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
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-271]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-273]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 12,164 chars in the whole document
