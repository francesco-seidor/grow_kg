---
id: 14-maintenance-service-and-projects/script-de-datos-maestros-crear-datos-maestros-de-mantenimiento-para-se
title: Script de datos maestros - Crear datos maestros de mantenimiento para servicio - MDS (3U3) (3U3_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 3U3: create technical locations and equipment for service orders, confirmations and contracts."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [3U3_S4CLD2608_Master_Data_ES_XX]
keywords: [Technical Objects and BOMs for Service, technical locations, equipment master data, equipment installation, warranty, service orders, business roles, master data scripts, 3U3]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-372
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear datos maestros de mantenimiento para servicio - MDS (3U3) (3U3_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear datos maestros de mantenimiento para servicio - MDS (3U3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894671)

[2 Requisitos previos 3](#_Toc233894672)

[2.1 Acceso al sistema 3](#_Toc233894673)

[2.2 Roles 3](#_Toc233894674)

[3 Procedimientos 4](#_Toc233894675)

[3.1 Creación de datos maestros de ubicación técnica 4](#_Toc233894676)

[3.2 Creación de datos maestros de equipo 5](#_Toc233894677)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear una ubicación técnica y un equipo registros de datos maestros para su sistema S/4 HANA. La descripción incluye esos datos segmentos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente con qué segmentos de datos y campos se deben rellenar normalmente valores de entrada. Campos que no son relevantes para el alcance del contenido de S/4 HANA entrega por parte de SAP Best Practices no se describen en este documento, aunque pueden aparecen en la IU.

Los registros maestros de ubicación técnica y equipo que se crean como se describe aquí se pueden utilizar en órdenes de servicio, confirmaciones de servicio y contratos de servicio.

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
| Planificador de mantenimiento | SAP_BR_MAINTENANCE_PLANNER | Planificación de mantenimiento | SAP_BR_MAINTENANCE_PLANNER |

## Procedimientos

### Creación de datos maestros de ubicación técnica

Objetivo

En este paso de test se actualiza una estructura de ubicación técnica que consta de una ubicación técnica de nivel superior y dos ubicaciones técnicas subordinadas.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de mantenimiento . |  |  |
| 2 | Abrir aplicación | En la Objeto técnico seleccione la sección Crear objeto técnico mosaico. |  |  |
| 3 | Crear ubicación técnica | El Crear objeto técnico , seleccione el botón de selección Tipo de objeto técnico : Ubicación técnica .En la siguiente pantalla, actualice las siguientes entradas:Tipo de objeto técnico: Ubicación técnicaIndicador de estructura : YBPM (Indicador de estructura para Best Practice)Objeto técnico : <introduzca un identificador, por ejemplo> ZZ01Categoría de objeto técnico : S (Ubicación de cliente)Seleccionar Continuar . |  |  |
| 4 | Actualizar datos generales | El Crear objeto técnico: ZZ01 en la pantalla Datos generales actualice las siguientes entradas:Descripción : <por ejemplo, Edificio A >Opcionalmente, actualice otros datos generales y, a continuación, navegue al Datos de ubicación sección. |  |  |
| 5 | Actualizar datos de ubicación | En la Datos de ubicación actualice las siguientes entradas:Centro de emplazamiento : <actualice un centro relevante, por ejemplo, 1710 para EE. UU.>Nota Todos los objetos técnicos que pertenecen a la misma estructura deben tener el mismo centro asignado. Como alternativa, puede dejar la información del centro vacío para todos los objetos técnicos.Opcionalmente, actualice más detalles, como la información de dirección. |  |  |
| 6 | Grabar ubicación técnica | Opcionalmente, puede actualizar información adicional como, por ejemplo, información de socio, etc. en la Datos organizativos sección.Seleccione Grabar.A continuación, vuelva a Inicio pantalla. |  |  |
| 7 | Crear ubicación técnica subordinada | Para actualizar una estructura de ubicación técnica, proceda como se describe en los pasos anteriores y actualice las siguientes ubicaciones técnicas:Objeto técnico : ZZ01-001Descripción: 1er pisoObjeto técnico : ZZ01-002Descripción: 2º piso |  |  |
| 8 | Revisar objeto técnico en Asset Viewer | El Inicio seleccione la página Visualizar objeto técnico mosaico.El Visualizar objeto técnico actualice los datos relevantes Objeto técnico , por ejemplo, ZZ01 , luego seleccione Continuar .Para revisar la estructura de la ubicación técnica y los detalles por objeto técnico, seleccione También puede visualizar el objeto técnico en el Asset Viewer . |  |  |

### Creación de datos maestros de equipo

Objetivo

En este paso de test se actualiza un registro para un equipo que está instalado en una ubicación técnica.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de mantenimiento . |  |  |
| 2 | Abrir aplicación | Abierto Crear objeto técnico . |  |  |
| 3 | Crear equipo | El Crear objeto técnico , seleccione el botón de selección Tipo de objeto técnico : Equipo .En la siguiente pantalla, actualice las siguientes entradas:Teleguardar tipo de objeto personalizado: EquipoObjeto técnico : <vacío>Inicio de validez: <fecha de hoy>Categoría de objeto técnico : S (Equipo de cliente)Seleccionar Continuar . |  |  |
| 4 | Actualizar datos generales | El Crear objeto técnico: <ID de equipo> en la pantalla Datos generales actualice las siguientes entradas:Descripción : <por ejemplo, Impresora A1 >(Opcional) Garantía de cliente : Inicio/fin de garantía(Opcional) Garantía de proveedor : Inicio/fin de garantíaNota El proceso de reparación en taller (posición de alcance 3XK) admite y integra garantías basadas en fechas (garantía período). En Reparación en taller, puede utilizar las clases de garantía garantía de garantía de cliente y garantía de proveedor.Debe introducir la fecha de inicio y de fin de garantía fecha en los datos maestros del equipo. Si ha introducido el Fecha de fin para la garantía de cliente y/o proveedor de un equipo, el sistema verifica si la fecha de fin de garantía es antes de la fecha de creación de la reparación en taller.Un icono indica si la fecha de creación de la La reparación se encuentra dentro del período de garantía.Opcionalmente, actualice otros datos generales como información del fabricante, número de modelo, etc. y, a continuación, navegue al Datos de ubicación sección. |  |  |
| 5 | Asignar material y número de serie | Seleccionar Funciones adicionales > Mostrar datos de número de serie .Realice las siguientes entradas y seleccione Intro :Material : TG20 |  |  |
| 6 | Actualizar datos de ubicación | En la Datos de ubicación actualice las siguientes entradas:Centro de emplazamiento : <actualice un centro relevante, por ejemplo, 1710 para EE. UU.>Nota Todos los objetos técnicos que pertenecen a la misma estructura deben tener el mismo centro asignado. Como alternativa, puede dejar la información del centro vacío para todos los objetos técnicos.Opcionalmente, actualice más detalles, como la dirección o la información de la sala. |  |  |
| 7 | Guardar equipo | Opcionalmente, puede actualizar información adicional como, por ejemplo, el interlocutor información, etc. en el Organizativo Datos sección.Seleccione Grabar. |  |  |
| 8 | Instalar equipo en ubicación técnica | El Modificar objeto técnico: <ID de equipo> , navegue hasta la pantalla Estructura sección.Seleccionar Modificar estructura: Instalar .El Modificar lugar de montaje actualice las siguientes entradas:Objeto técnico superior : ZZ01-001Posición : <dejar en blanco>Fecha/hora de instalación : <mantener propuesta de sistema>Seleccionar OK .Seleccionar Grabar . |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/instandhaltungs-stammdaten-fur-service-anlegen-sds-3u3-370]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-plant-maintenance-master-data-for-service-md]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-373]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-375]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 11,511 chars in the whole document
