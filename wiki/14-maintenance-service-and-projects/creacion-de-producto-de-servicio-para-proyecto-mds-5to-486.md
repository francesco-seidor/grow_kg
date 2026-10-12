---
id: 14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486
title: Creación de producto de servicio para proyecto - MDS (5TO) (5TO_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP master data script for creating service product PROYECTO with MM01 in S/4HANA Cloud Public Edition 2608, for solution orders."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_ES_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service product, material master, master data creation, sales organization data, profit center, business roles, brazil tax fields, test procedures, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-486
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Creación de producto de servicio para proyecto - MDS (5TO) (5TO_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de producto de servicio para proyecto - MDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894787)

[2 Requisitos previos 3](#_Toc233894788)

[2.1 Acceso al sistema 3](#_Toc233894789)

[2.2 Roles 3](#_Toc233894790)

[2.3 Unidades organizativas necesarias 3](#_Toc233894791)

[2.4 Datos maestros obligatorios y operativos 4](#_Toc233894792)

[3 Tabla de resumen 5](#_Toc233894793)

[4 Procedimientos de prueba 6](#_Toc233894794)

[4.1 Crear producto de servicio - PROYECTO 6](#_Toc233894795)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear registros de datos maestros de productos de servicio, incluidos los precios. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance no se describen en este documento, aunque pueden aparecer en la IU.

El registro maestro de productos de servicio que se crea como se describe aquí se puede utilizar para la orden de solución.

| ID de producto de servicio | Descripción | Utilización |
| --- | --- | --- |
| PROYECTO | Proyecto | representa el proyecto |

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
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Producto | SAP_CMD_SP_PR_MAINT |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Unidad organizativa que se utilizará para EE. UU. | Unidad organizativa a utilizar para DE |
| --- | --- | --- | --- |
| Crear material | Organización de ventas | 1710 (Org.ventas nac.US) | 1010 (Org.ventas nac.DE) |
| Crear material | Canal de distribución | 10 (Ventas directas) | 10 (Ventas directas) |

### Datos maestros obligatorios y operativos

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de material.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.

Puede encontrar todas las demás aplicaciones no incluidas en la página de inicio utilizando la barra de búsqueda.

Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Configuración > Buscador de aplicaciones .

| ID (modelo de rol) | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear producto de servicio | SAP_BR_PRODMASTER_SPECIALIST | Crear material (MM01) | Se crean productos de servicio. |

## Procedimientos de prueba

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear producto de servicio - PROYECTO

Objetivo

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Producto Datos (MDG) . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Crear material (MM01) mosaico. | El Crear material (pantalla inicial) es visualizados. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) ) | El Crear material (pantalla inicial) efectúe las siguientes entradas:Material: PROYECTOTipo de material: Servicio ProductoA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.El Seleccionar vista(s) diálogo Se muestra la ventana. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s)datos básicos 1 ver, luego seleccionar Continuar (Intro) . | El Crear PROYECTO de material la vista es visualizados. |  |
| 5 | Actualizar datos básicos | El Datos básicos 1 vista, actualice lo siguiente valores:Descr.: Proyecto PosiciónUnidad base de Medida: AU (ACTIVIDAD) UNIDAD)Material Grupo: P001 (Servicios)Gr.pos.gen.: SPRJ (Proyecto)A continuación, seleccione Grabar . | Se actualizan los datos básicos y se graba el producto de servicio.Después guardando, el Crear material (pantalla inicial) la vista es visualizados.Para cada idioma diferente utilizado en su empresa, la descripción correspondiente para el producto debe actualizarse por idioma código! |  |
| 6 | Ampliar detalles de producto | El Crear material (pantalla inicial) vista, introducir material PROYECTO , luego seleccione Continuar (Intro) . | El Seleccionar vista(s) la ventana de diálogo es visualizados. |  |
| 7 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione el vistas siguientes:Ventas: Org.ventas Datos 1Ventas: Org.ventas Datos 2A continuación, seleccione Continuar (Intro) . | El Niveles de organización la ventana de diálogo es visualizados. |  |
| 8 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice la valores siguientes:Org.ventas: 1710 (Dom. Org.ventas EE. UU.)Distr. Canal: 10 (Ventas directas)Entonces seleccionar Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear PROYECTO de material Se muestra la vista. |  |
| 9 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 vista, actualice la valores siguientes:General datosEfectivo Descuento: X <seleccionado>Datos fiscalesImpuesto clasificación: 1 (Impuesto completo)Entonces seleccionar Intro . | Se actualizan los datos organizativos de ventas. El Ventas: Ventas Org. 2 Se visualiza la etiqueta. |  |
| 10 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 vista, actualice la entrada siguiente:Tipo de posición grupo: SPRJ (proyecto)A continuación, seleccione Intro .A continuación, seleccione Grabar . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |

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
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-489]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 11,245 chars in the whole document
