---
id: 11-inventory-warehouse-and-transportation/gestion-de-ubicaciones-mds-7e9-528
title: Gestión de ubicaciones - MDS (7E9) (7E9_S4CLD2608_Master_Data_ES_XX)
description: Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script (7E9) for creating transportation locations with Manage Locations (F6225).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-locations]
aliases: [7E9_S4CLD2608_Master_Data_ES_XX]
keywords: [Transportation Locations, locations, location types, un/locode, airport codes, transportation management, business roles, master data scripts, 7E9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-528
topic: 11-inventory-warehouse-and-transportation/transportation-locations
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Gestión de ubicaciones - MDS (7E9) (7E9_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Transportation Locations** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Gestión de ubicaciones - MDS (7E9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894885)

[2 Requisitos previos 3](#_Toc233894886)

[2.1 Acceso al sistema 3](#_Toc233894887)

[2.2 Roles 3](#_Toc233894888)

[2.3 Parámetros principales para la creación de datos 3](#_Toc233894889)

[2.3.1 Tipos de ubicación 3](#_Toc233894890)

[2.3.2 Definir UN/LOCODE 4](#_Toc233894891)

[2.3.3 Definir códigos de aeropuerto 4](#_Toc233894892)

[3 Tabla de resumen 5](#_Toc233894893)

[4 Procedimientos de prueba 6](#_Toc233894894)

[4.1 Gestionar ubicaciones 6](#_Toc233894895)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un registro de datos maestros de ubicación para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". Principalmente aprenderá qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance del SAP S/4HANA Cloud Public Edición entrega de contenido de SAP Best Practices no se describen en este documento, aunque pueden aparecer en la pantalla.

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de Rampa de lanzamiento SAP Fiori . El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignado a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Especialista en datos maestros - Gestión de transporte | SAP_BR_TRANSP_MDSPEC | Datos maestros de transporte | SAP_BR_TRANSP_MDSPEC |

### Parámetros principales para la creación de datos

En esta sección, algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear un <tipo> Se describen registros de datos maestros.

#### Tipos de ubicación

Están disponibles las siguientes opciones para asignar los tipos de ubicación:

| Nombre | ID |
| --- | --- |
| Puerto | 1100 |
| Aeropuerto | 1110 |
| Estación ferroviaria | 1120 |
| Conexión ferroviaria | 1190 |
| Puesto de carga | 1200 |

#### Definir UN/LOCODE

Puede definir códigos de las Naciones Unidas para ubicaciones de comercio y transporte (UN/LOCODES).

En su entorno de configuración, utilice la función de búsqueda para encontrar cada actividad. Para obtener más información, consulte. [Entorno de configuración de SAP S/4HANA Cloud Public Edición .](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html)

#### Definir códigos de aeropuerto

Puede definir códigos de aeropuerto.

En su entorno de configuración, utilice la función de búsqueda para encontrar cada actividad. Para obtener más información, consulte. [Entorno de configuración de SAP S/4HANA Cloud Public Edición](https://help.sap.com/docs/SAP_S4HANA_CLOUD/61e246f4b34c4e1790d8b7651c0b40a8/0b3f87579f345c08e10000000a441470.html?state=DRAFT).

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Gestionar ubicaciones](#unique_10) [página ] 6 | Especialista en datos maestros - Gestión de transporte | Gestionar ubicaciones (F6225) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Gestionar ubicaciones

Objetivo

Los siguientes pasos muestran cómo crear ubicaciones.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Gestión de transporte . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abierto Gestionar ubicaciones (F6225) . | El Gestionar maestro de ubicaciones (F6225) Aparece la pantalla. |  |
| 3 | Seleccione Crear. | Seleccionar Crear . | El Crear aparece la ventana de diálogo. |  |
| 4 | Introducir detalles | En la Crear , efectúe las siguientes entradas:Ubicación: <su ubicación>Tipo de ubicación: <su tipo de ubicación> |  |  |
| 5 | Seleccione Continuar. | Seleccionar Continuar . | El Ubicación Aparece la pantalla. |  |
| 6 | Introducir información general | El Información general , realice la siguiente entrada:Descripción de ubicación: <su descripción de ubicación> |  |  |
| 7 | Introducir datos de dirección | El Dirección , efectúe las siguientes entradas:Calle: <calle>Código postal: <código postal>País/Región: <país/región>Número: <número de casa>Población: <ciudad>Región: <región>Huso horario: <huso horario>Concepto de búsqueda 1: <concepto de búsqueda> |  |  |
| 8 | Introducir datos de identificación | El Identificación , realice la siguiente entrada:UN/LOCODE: <UN/LOCODE>Código de aeropuerto: <código de aeropuerto> |  |  |
| 9 | Seleccione Calcular coordenadas geográficas | Seleccionar Calcular coordenadas geográficas . | Las coordenadas geográficas se han determinado y rellenado automáticamente en el Coordenadas geográficas pestaña. |  |
| 10 | Seleccione Crear. | Seleccionar Crear . | Aparece el siguiente mensaje del sistema:Ubicación <su ubicación> creada correctamente |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/administrar-localizacoes-mds-7e9-530]]
- related-to :: [[11-inventory-warehouse-and-transportation/manage-locations-mds-7e9-527]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-529]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-531]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 9,269 chars in the whole document
