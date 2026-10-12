---
id: 14-maintenance-service-and-projects/creacion-de-ubicacion-tecnica-mds-5lm-es-444
title: "Creación de ubicación técnica - MDS (5LM) [ES] (5LM_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish machine-translated SAP S/4HANA Cloud master data script 5LM for creating a technical location hierarchy (one parent, two child locations) for maintenance."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/functional-locations]
aliases: [5LM_S4CLD2608_Master_Data_ES_XX]
keywords: [Functional Locations, technical location, technical objects, plant maintenance, structure indicator, technical object category, maintenance work center, cost center, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-444
topic: 14-maintenance-service-and-projects/functional-locations
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Creación de ubicación técnica - MDS (5LM) [ES] (5LM_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Functional Locations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de ubicación técnica - MDS (5LM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894764)

[2 Requisitos previos 3](#_Toc233894765)

[2.1 Acceso al sistema 3](#_Toc233894766)

[2.2 Roles 3](#_Toc233894767)

[2.3 Unidades organizativas necesarias 3](#_Toc233894768)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894769)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894770)

[2.5.1 Indicador de estructura 4](#_Toc233894771)

[2.5.2 Categoría de objeto técnico 5](#_Toc233894772)

[3 Tabla de resumen 6](#_Toc233894773)

[4 Procedimiento 7](#_Toc233894774)

[4.1 Crear ubicación técnica 7](#_Toc233894775)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará un procedimiento detallado sobre cómo crear un maestro de ubicaciones técnicas. registros de datos para su sistema S/4HANA. Incluye segmentos de datos que son relevantes para los datos maestros para trabajar en un entorno de sistema regular. Este documento también proporciona información sobre qué segmentos de datos y campos requieren valores de entrada.

Los campos que no son relevantes para el alcance de la entrega de contenido de S/4HANA por parte de SAP Las mejores prácticas no se describen en este documento, aunque pueden aparecer en el usuario interfaz de usuario (IU). Una ubicación técnica que se crea como se describe aquí se puede utilizar para procesos de mantenimiento.

## Requisitos previos

En esta sección se resumen todos los requisitos previos necesarios para crear un ubicación.

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

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. General Los datos (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de los diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos de la ubicación técnica dependen del centro. | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de ubicación técnica pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se utilizarán en un ubicación.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Puesto de trabajo de mantenimiento | En la interfaz de usuario (IU) de la ubicación técnica, Datos organizativos ficha, encontrará la entrada del puesto de trabajo de mantenimiento en sección de responsabilidades. | Opcional | El sistema utiliza el puesto de trabajo de mantenimiento como parámetro para determinar algunos valores, como como configuración, máquina o mano de obra. |
| Centro de coste | En la interfaz de usuario (IU) de la ubicación técnica, Organización Datos encontrará la entrada del centro de coste en sección de responsabilidades. | Opcional | El sistema utiliza el centro de coste como parámetro para el cálculo del coste. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear una ubicación técnica:

#### Indicador de estructura

El indicador de estructura de una ubicación técnica determina la estructura de la Identificación de la ubicación técnica. Establece el siguiente factor:

- Cantidad de niveles de jerarquía de un sistema técnico
- Longitud clave de los niveles
- Separadores (guiones)

Tabla 2:

| Indicador de estructura | Descripción |
| --- | --- |
| YBPM | Indicador de estructura para Best Practice |

#### Categoría de objeto técnico

Esta es la clave que muestra el tipo de ubicación técnica.

Tabla 3:

| Categoría de objeto técnico | Descripción |
| --- | --- |
| M | Sistema técnico estándar |

## Tabla de resumen

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear ubicación técnica](#unique_11) [página ] 7 | SAP_BR_MD_SPECIALIST_EAM | Crear objeto técnico (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Se ha creado la ubicación técnica. |

## Procedimiento

### Crear ubicación técnica

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En este paso de test se actualiza una estructura de ubicación técnica que consta de una Ubicación técnica de nivel superior y dos ubicaciones técnicas subordinadas.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Especialista en datos maestros SAP_BR_MD_SPECIALIST_EAM . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear objeto técnico (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) . | Se abre una ventana nueva que muestra Crear objeto técnico: Inicial Pantalla. |  |
| 3 | Crear ubicación técnica | El Crear objeto técnico pantalla, seleccione el tipo de objeto técnico: Ubicación técnica.En la siguiente pantalla, introduzca lo siguiente:Tipo de objeto técnico : Ubicación técnicaIndicador de estructura : YBPM (indicador de estructura para Best) Práctica)Objeto técnico : <Por ejemplo, 1711 >Categoría de objeto técnico : M (técnico) estándar de sistema)Seleccionar Continuar . |  |  |
| 4 | Actualizar datos generales | El Crear objeto técnico: 1711 dynpro, en el Datos generales sección, introduzca lo siguiente:Descripción : <Por ejemplo, compresor de aire 1 planta >Opcionalmente, actualice otros datos generales y, a continuación, navegue a la Datos de ubicación sección. | Aparecerá la pantalla Crear objeto técnico: datos generales. |  |
| 5 | Actualizar datos de ubicación | En la Datos de ubicación introduzca la sección siguientes:Centro de emplazamiento : <Por ejemplo, 1710 para US>Nota Los objetos técnicos que pertenecen a la misma estructura deben tienen asignado el mismo centro. Como alternativa, puede Deje la información de centro vacía para todos los objetos.Opcionalmente, actualice más detalles, como la dirección información. | Aparece la pantalla Crear objeto técnico: datos de ubicación. |  |
| 6 | Actualizar datos organizativos | En la Datos organizativos sección, introduzca lo siguiente:Centro de planificación : <Por ejemplo, 1710 para US>Puesto de trabajo de mantenimiento : <Por ejemplo, RES-0100 para EE.UU.>Centro de coste : <Por ejemplo, 17101701 para US>Opcionalmente, puede actualizar información adicional como, por ejemplo, el interlocutor información, etc. en el Organizativo Datos sección. | La pantalla Crear objeto técnico: Datos organizativos aparece. |  |
| 7 | Grabar ubicación técnica | Opcionalmente, puede actualizar información adicional para otros secciones.Haga clic en Verificar entradas botón.Seleccionar Grabar .A continuación, vuelva a la pantalla Inicio. | Se ha creado la ubicación técnica. |  |
| 8 | Crear funcional subordinado Ubicación | Para actualizar una estructura de ubicación técnica, proceda como se describe en los pasos anteriores, y actualice las siguientes funciones ubicaciones:Objeto técnico : 1711-001Descripción : <para ejemplo, Compresor # 1 >En la Datos de ubicación introduzca la sección siguientes:Ubicación : <Por ejemplo, YB_1701>Área de empresa : GG AAEn la Datos organizativos sección, actualice las siguientes entradas:Grupo de planificación : <Por ejemplo, 920 para US>Centro de planificación : <Por ejemplo, 1710 para US>Puesto de trabajo de mantenimiento : <Por ejemplo, RES-0100 para EE.UU.>Centro de puesto de trabajo : <Por ejemplo, 1710 para US>Perfil de catálogo : <Por ejemplo, YB-PM0003 para EE. UU. >Opcionalmente, puede actualizar información adicional en otros secciones.Seleccionar Verificar entradas botón.Seleccionar Grabar .Introduzca lo siguiente:Objeto técnico : 1711-002Descripción : <para ejemplo, Compresor # 2 >En la Datos de ubicación introduzca la sección siguientes:Ubicación : < para ejemplo, YB_1702>Sección de planta: <OH>En la Datos organizativos sección, actualice las siguientes entradas:Grupo de planificación : <para ejemplo, 920 para US>Centro de planificación : <para ejemplo, 1710 para US>Trabajo de mantenimiento Centro: <por ejemplo, RES-0100 para US>Centro de puesto de trabajo : <por ejemplo, 1710 para US>Perfil de catálogo : <por ejemplo, YB-PM0003 para EE. UU. >Opcionalmente, puede actualizar información adicional para otros secciones.Haga clic en Verificar entradas botón.Seleccionar Grabar . | Se crean ubicaciones técnicas subordinadas. |  |
| 9 | Revisar objeto técnico en activo fijo Visor | En la página Inicio, seleccione Visualizar técnico Objeto mosaico.El Visualizar objeto técnico pantalla, actualice el objeto técnico relevante, por ejemplo, 1711, y luego seleccionar Continuar .Para revisar la estructura de la ubicación técnica y los detalles por objeto técnico, seleccione También puede: Visualizar Objeto técnico en Asset Viewer . |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-functional-location-mds-5lm-443]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-445]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-447]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-local-de-instalacao-mds-5lm-446]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 14,372 chars in the whole document
