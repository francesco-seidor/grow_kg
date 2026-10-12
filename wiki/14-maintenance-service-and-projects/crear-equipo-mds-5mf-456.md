---
id: 14-maintenance-service-and-projects/crear-equipo-mds-5mf-456
title: Crear equipo - MDS (5MF) (5MF_S4CLD2608_Master_Data_ES_XX)
description: Spanish (machine-translated) master data script 5MF for creating an equipment record and installing it at a technical location in SAP S/4HANA Cloud 2608.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_ES_XX]
keywords: [Equipment Master Records, equipment master data, technical objects, technical location, maintenance work center, cost center, business roles, master data scripts, 5MF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-456
topic: 14-maintenance-service-and-projects/equipment
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear equipo - MDS (5MF) (5MF_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear equipo - MDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894798)

[2 Requisitos previos 3](#_Toc233894799)

[2.1 Acceso al sistema 3](#_Toc233894800)

[2.2 Roles 3](#_Toc233894801)

[2.3 Unidades organizativas necesarias 3](#_Toc233894802)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894803)

[3 Tabla de resumen 5](#_Toc233894804)

[4 Parámetros principales para la creación de datos 6](#_Toc233894805)

[4.1 Categoría de objeto técnico 6](#_Toc233894806)

[5 Procedimiento 7](#_Toc233894807)

[5.1 Crear equipo 7](#_Toc233894808)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, puede encontrar un procedimiento detallado sobre cómo crear datos maestros de equipo registros para su sistema S/4HANA. Incluye segmentos de datos que son relevantes para el datos maestros para trabajar en un entorno de sistema regular. Este documento también proporciona información sobre qué segmentos de datos y campos requieren valores de entrada.

Los campos que no son relevantes para el alcance de la entrega de contenido de S/4HANA por parte de SAP Best Las prácticas no se describen en este documento, aunque pueden aparecer en el usuario interfaz de usuario (IU).

## Requisitos previos

Esta sección resume todos los requisitos previos para crear un equipo.

### Acceso al sistema

El ensayo debe realizarse con el siguiente sistema:

Tabla 1:

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. Su administrador del sistema le proporciona la URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio) | ID (espacio) |
| --- | --- | --- | --- |
| Planificador de mantenimiento | SAP_BR_MD_SPECIALIST_EAM | Planificador de mantenimiento | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de los diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos para el equipo dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de equipo pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un equipo.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Puesto de trabajo de mantenimiento | En la interfaz de usuario (IU) del maestro de equipos, pestaña Datos organizativos, encontrará la entrada del puesto de trabajo de mantenimiento en las responsabilidades sección. | Opcional | El sistema utiliza el puesto de trabajo de mantenimiento como parámetro para determinar algunos valores, como configuración, máquina o mano de obra. |
| Centro de coste | En la interfaz de usuario (IU) del maestro de equipos, pestaña Datos organizativos, encontrará la entrada del centro de coste en la sección de responsabilidades. | Opcional | El sistema utiliza el centro de coste como parámetro para el cálculo del coste. |

## Tabla de resumen

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear equipo](#unique_8) [página ] 7 | SAP_BR_MD_SPECIALIST_EAM | Crear objeto técnico (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Se ha creado el equipo. |

## Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear un equipo.

### Categoría de objeto técnico

Los usos posibles pueden ser:

- Maquinaria
- Dispositivo
- Medio auxiliar de fabricación
- Equipo de cliente

Tabla 2:

| Categoría de objeto técnico | Descripción |
| --- | --- |
| M | Máquinas |

## Procedimiento

### Crear equipo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso de test se actualiza un registro para un equipo que está instalado en un ubicación técnica.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como SAP_BR_MD_SPECIALIST_EAM . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear objeto técnico (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) . | Se abre una ventana nueva que muestra la Crear técnico Objeto: Inicial Pantalla. |  |
| 3 | Crear equipo | El Crear objeto técnico pantalla, seleccione el tipo de objeto técnico: Equipo.En la siguiente pantalla, introduzca lo siguiente:Tipo de objeto técnico : EquipoObjeto técnico : dejar en blancoInicio de validez : de hoy fechaCategoría de objeto técnico : M (técnico) estándar de sistema)Seleccionar Continuar . |  |  |
| 4 | Actualizar datos generales | El Crear objeto técnico: <ID de equipo> pantalla, en el Datos generales introduzca la sección siguientes:Descripción : Para ejemplo, válvula de aislamiento manual>Tipo de objeto : Para ejemplo, 9400>Fecha de puesta en servicio : Para ejemplo, la fecha de hoy>País/región de fabricación : Por ejemplo, US>Mes/Año de construcción : Por ejemplo, 04/2011>Número de pieza de fabricante : Por ejemplo, HZZ-TD B4>Número de serie del fabricante : Por ejemplo, HZZ-TD B4/66>Valor de adquisición/Moneda : Por ejemplo,10.000,00/ USD >Fecha de adquisición : Para ejemplo, 04/10/2011 >Opcionalmente, actualice otros datos generales y, a continuación, navegue a la Datos de ubicación sección. | Aparecerá la pantalla Crear objeto técnico: datos generales. |  |
| 5 | Actualizar datos de ubicación | En la Datos de ubicación introduzca la sección siguientes:Centro de emplazamiento : Para ejemplo, 1710 para US>Ubicación : Por ejemplo, YB_1701 para EE.UU.>Área de empresa : Para ejemplo, YOH para US>Nota Los objetos técnicos que pertenecen a la misma estructura deben tienen asignado el mismo centro. Como alternativa, puede Deje la información de centro vacía para todos los objetos.Opcionalmente, actualice más detalles, como la dirección información. | Aparece la pantalla Crear objeto técnico: datos de ubicación. |  |
| 6 | Actualizar datos organizativos | En la Datos organizativos sección, introduzca lo siguiente:Grupo de planificación : Para ejemplo, 920 para US>Centro de planificación : Por ejemplo, 1710 para US>Puesto de trabajo de mantenimiento : Por ejemplo, RES-0100 para US>Centro de puesto de trabajo : Por ejemplo, 1710 para US>Centro de coste : Para ejemplo, 17101701 para US>Opcionalmente, puede actualizar información adicional como, por ejemplo, el interlocutor información, etc. en la sección Datos organizativos. | La pantalla Crear objeto técnico: Datos organizativos aparece. |  |
| 7 | Guardar equipo | Opcionalmente, puede actualizar información adicional para otras secciones.Seleccionar Verificar entradas botón.Seleccionar Grabar . | Se ha creado el equipo. |  |
| 8 | Instalar equipo en ubicación técnica | En la pantalla Modificar objeto técnico: <ID de equipo>, navegar al Estructura sección.Seleccionar Modificar estructura: Instalar .El Modificar lugar de montaje pantalla, introduzca lo siguiente:Objeto técnico superior : por ejemplo< 1710>Posición : <ausentismo vacío>Fecha/hora de instalación : <mantener propuesta de sistema>Seleccionar OK .Seleccionar Grabar . |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-equipment-mds-5mf-455]]
- related-to :: [[14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458]]
- related-to :: [[14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mf-457]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 12,454 chars in the whole document
