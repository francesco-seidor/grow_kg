---
id: 13-quality-ehs-and-compliance/script-de-datos-maestros-crear-ubicacion-ehs-mds-3sr-360
title: "Script de datos maestros: Crear ubicación EHS - MDS (3SR) (3SR_S4CLD2608_Master_Data_ES_XX)"
description: Spanish (machine-translated) master data script 3SR for creating an EHS location and assigning it to the EHS location structure in S/4HANA Cloud Public Edition.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_ES_XX]
keywords: [EHS Locations, ehs location, master data scripts, location structure, business roles, fiori launchpad access, environment health safety, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-360
topic: 13-quality-ehs-and-compliance/ehs-locations
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear ubicación EHS - MDS (3SR) (3SR_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear ubicación EHS - MDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894636)

[2 Requisitos previos 3](#_Toc233894637)

[2.1 Acceso al sistema 3](#_Toc233894638)

[2.2 Roles 3](#_Toc233894639)

[3 Tabla de resumen 4](#_Toc233894640)

[4 Procedimientos 5](#_Toc233894641)

[4.1 Crear datos maestros de ubicación EHS - Datos generales 5](#_Toc233894642)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este documento le ayuda a crear una ubicación EHS dentro de la estructura de ubicación. EHS La ubicación es un objeto de datos maestros central que se utiliza en Medio ambiente, Salud, y seguridad . La creación de ubicaciones EHS organizadas en una ubicación forma parte de la configuración inicial de la solución y las ubicaciones se utilizan en que forman parte de la solución.

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
| Especialista en seguridad en el trabajo (Incidente Gestor) | SAP_BR_INDUSTRIAL_HYGIENIST | Seguridad en el lugar de trabajo | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| Responsable medioambiental | SAP_BR_EHS_ENV_MGMT | Medio ambiente, Salud y Seguridad | SAP_BR_EHS_ENV_MGMT |  |
| Coordinador de gestión de cambios | SAP_BR_CHG_MGMT_COORDINATOR | Gestión de modificaciones | SAP_BR_CHG_MGMT_COORDINATOR |  |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear datos maestros de ubicación EHS - Datos generales](#unique_6) [página ] 5 | Especialista en seguridad en el trabajoResponsable medioambientalCoordinador de gestión de cambios | Gestionar ubicaciones (EHFND_UI_LOC_ENTRY) | Se crea una ubicación EHS y se asigna a la estructura de ubicación EHS. |

## Procedimientos

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear datos maestros de ubicación EHS - Datos generales

Objetivo

El siguiente procedimiento proporciona instrucciones para crear una ubicación EHS y asignar a la estructura de ubicación EHS.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con uno de los siguientes roles:Especialista en seguridad en el trabajoResponsable medioambientalCoordinador de gestión de cambios | La rampa de lanzamiento SAP Fiori se visualiza con las secciones y mosaicos para las respectivas rol. |  |
| 2 | Navegar a la estructura de ubicación | Abierto Gestionar ubicaciones (EHFND_UI_LOC_ENTRY) . | El Ubicaciones se visualiza. Inicialmente, la estructura de ubicación tiene Todas las ubicaciones establecer como nivel superior. |  |
| 3 | Crear una ubicación | Seleccionar Editar estructura de ubicación .El Estructura de ubicación pantalla:Seleccione el Todas las ubicaciones fila.Seleccionar Nuevo .El Crear ubicación pantalla:Introduzca un <Nombre de ubicación> en el Ubicación campo.Seleccione un <Tipo de ubicación> mediante la ayuda para entradas para el Tipo de ubicación campo.Introducir fecha 01.01.2000 en el Inicio de revisión Fecha campo.Seleccionar Grabar .Seleccionar Volver a la estructura de ubicación .El Estructura de ubicación pantalla:Guarde las entradas. | Una ubicación con el nombre <Nombre de ubicación> se crea y graba en la estructura de ubicación. |  |
| 4 | Editar una ubicación | El Estructura de ubicación pantalla:En la Nombre seleccione la columna <Ubicación nombre> enlace. | El Editar ubicación Se visualiza la aplicación. |  |
| 5 | Añadir información básica | El Ubicación : <Nombre de ubicación> dynpro, debajo de la Información básica pestaña:Añadir un <descripción de ubicación> texto en el Descripción campo.Seleccionar Traducciones junto al Ubicación campo. Añadir texto traducido para diferentes idiomas.Seleccionar Traducciones junto al Descripción campo. Añadir traducido texto para diferentes idiomas.Seleccionar Cargar imagen para añadir una imagen para la ubicación.Guarde las entradas. | Se guardan los datos de la ubicación. |  |
| 6 | Añadir dirección | El Ubicación : <Nombre de ubicación> dynpro, debajo de la Dirección pestaña:Intro <Nombre línea 1> en el Línea de nombre 1 campo.Intro <Nombre línea 2> en el Línea de nombre 2 campo.Intro <Nombre de la calle> en el Calle campo.Intro <Código postal> en el Postal Código campo.Intro <Nombre de ciudad> en el Población campo.Seleccionar <País/Región> en el País/Región mediante el campo Ayuda para entradas.Seleccionar <Región> en el Región campo mediante la ayuda para entradas.Deje el valor predeterminado UTC valor en el Hora Zona campo.Introduzca datos adicionales en el campo Número de teléfono , Fax Número , Latitud , Longitud y Elevación campos.Guarde las entradas. | Se guardan los datos de la ubicación. |  |
| 7 | Añadir persona responsable | Este paso solo es relevante para los siguientes roles:SAP_BR_INDUSTRIAL_HYGIENIST ( Especialista en seguridad en el trabajo )SAP_BR_EHS_ENV_MGMT ( Responsable medioambiental )El Ubicación : <Nombre de ubicación> dynpro, debajo de la Responsables pestaña:En la Responsables por roles tabla, seleccione su <nombre de usuario> en el Nombre columna mediante el valor ayuda.En la Rol columna, seleccione Incidente Gestor o bien Medioambiental Gestor de la lista desplegable.Guarde las entradas. | Se guardan los datos de la ubicación. |  |
| 8 | Añadir documentos | El Ubicación : <Nombre de ubicación> dynpro, debajo de la Documentos pestaña:En la Documentos y enlaces tabla, seleccione Añadir Fichero para añadir un documento para la ubicación.Guarde las entradas. | El documento seleccionado se añade a la tabla.Se guardan los datos de la ubicación. |  |
|  | Activar ubicación | El Ubicación : <Nombre de ubicación> dynpro:Seleccionar Fijar estado en el encabezado de página.Seleccione el Activo opción. | La ubicación está activada.El Estado El campo está fijado en Activo en el encabezado de página.Se guardan los datos de la ubicación. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-361]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-363]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 10,979 chars in the whole document
