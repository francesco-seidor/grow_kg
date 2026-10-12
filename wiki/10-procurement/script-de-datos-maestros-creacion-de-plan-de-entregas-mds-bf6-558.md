---
id: 10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558
title: Script de datos maestros - Creación de plan de entregas - MDS (BF6) (BF6_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script BF6: prerequisites and test steps to create purchasing scheduling agreements (plan de entregas)."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_ES_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, standard procurement, consignment procurement, subcontracting procurement, number ranges, business roles, mandatory master data, organizational units, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-558
topic: 10-procurement/scheduling-agreements
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de plan de entregas - MDS (BF6) (BF6_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de plan de entregas - MDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894868)

[2 Requisitos previos 3](#_Toc233894869)

[2.1 Acceso al sistema 3](#_Toc233894870)

[2.2 Roles 3](#_Toc233894871)

[2.3 Unidades organizativas necesarias 3](#_Toc233894872)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894873)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894874)

[2.5.1 Rangos de números 4](#_Toc233894875)

[3 Tabla de resumen 5](#_Toc233894876)

[4 Procedimientos de prueba 6](#_Toc233894877)

[4.1 Crear plan de entregas para aprovisionamiento estándar 6](#_Toc233894878)

[4.1.1 Crear plan de entregas con documento de orden de entrega - Estándar 6](#_Toc233894879)

[4.1.2 Crear plan de entregas sin documento de orden de entrega - Estándar 8](#_Toc233894880)

[4.2 Crear plan de entregas para aprovisionamiento consignado 10](#_Toc233894881)

[4.3 Crear plan de entregas para aprovisionamiento de subcontratación 12](#_Toc233894882)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este documento proporciona una descripción para crear un plan de entregas para su SAP S/4HANA Cloud Public Edición sistema. El La descripción incluye los segmentos de datos que son relevantes para el SAP S/4HANA Cloud Public Edición como, por ejemplo, Datos de compras, Datos de material y Datos de proveedor. Campos que no son relevantes para el alcance de SAP S/4HANA Cloud Public Edición tal y como lo entrega SAP Best Practices no se describen en este documento.

Un plan de entregas es un acuerdo a largo plazo con un proveedor que cubre el aprovisionamiento de materiales sujeto a condiciones predeterminadas. Las condiciones son válidas para un período predefinido y una cantidad total predefinida.

Las principales ventajas de los planes de entregas son:

- Los planes de entregas pueden sustituir una gran cantidad de pedidos de compra o órdenes de entrega de contrato.
- Es un acuerdo a largo plazo, que le permite negociar mejores precios con un proveedor.

Existen los siguientes tipos de posición:

- Aprovisionamiento estándar
- Aprovisionamiento consignado
- Aprovisionamiento de subcontratación

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

La estructura organizativa y los datos maestros de su empresa se han creado en su ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos de compras | Organización de compras | Grupo de compras, Grupo de artículos, Tiempo de tratamiento de EM, etc. on. | Pueden existir datos de compras para cada organización de compras para qué material se utiliza en los procesos de compra. | Organización de compras:__________ |

### Datos maestros obligatorios y opcionales

El plan de entregas puede hacer referencia a otros datos maestros. La siguiente tabla proporciona una resumen de objetos de datos maestros opcionales y obligatorios que se deben utilizar en una programación acuerdo.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material |  | Obligatorio | Para introducir el material, primero cree datos maestros de material. |
| Proveedor |  | Obligatorio | Para introducir el proveedor, primero cree datos maestros de proveedor. |

### Parámetros principales para la creación de datos

En esta sección, se proporciona una descripción de los parámetros básicos que influyen en el comportamiento de un plan de entregas y que siempre son necesarios para crear una programación acuerdo.

#### Rangos de números

Se han definido los siguientes rangos de números para el plan de entregas:

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Numérico interno | Rango de números interno para uso estándar:5500000000 – 5599999999 | Este rango de números se utiliza cuando el sistema asigna automáticamente un Número numérico de un plan de entregas. |
| Numérico externo | Rango de números numérico externo:5600000000 – 5699999999 | Este rango de números está reservado para números externos asignación. |

## Tabla de resumen

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
|  |  |  |  |
| [Crear plan de entregas con documento de orden de entrega - Estándar](#unique_10) [página ] 6 | Comprador | Gestionar planes de entregas de compras (F2179) | Plan de entregas con documento de orden de entrega - Estándar |
| [Crear plan de entregas sin documento de orden de entrega - Estándar](#unique_11) [página ] 8 | Comprador | Gestionar planes de entregas de compras (F2179) | Plan de entregas sin documento de orden de entrega - Estándar |
| [Crear plan de entregas para aprovisionamiento consignado](#unique_12) [página ] 10 | Comprador | Gestionar planes de entregas de compras (F2179) | El plan de entregas para el aprovisionamiento consignado es creado |
| [Crear plan de entregas para aprovisionamiento de subcontratación](#unique_13) [página ] 12 | Comprador | Gestionar planes de entregas de compras (F2179) | Se crea el plan de entregas para el aprovisionamiento de subcontratación |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear plan de entregas para aprovisionamiento estándar

#### Crear plan de entregas con documento de orden de entrega - Estándar

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear un plan de entregas para el aprovisionamiento estándar.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar planes de entregas de compras (F2179) . | Se abre la aplicación. |  |
| 3 | Crear plan de entregas | Seleccionar Crear para crear un nuevo plan de entregas. | El Nuevo plan de entregas de compras se visualiza. |  |
| 4 | Introducir datos de cabecera | Cree un nuevo plan de entregas con los siguientes datos:Proveedor : <Proveedor>Tipo de acuerdo : LPA (plan de entregas con orden de entrega doc.)Inicio de validez : <MM/DD/AAAA>Válido hasta : <MM/DD/AAAA>Sociedad : <Empresa Código>Organización de compras : <Compras Organización>Grupo de compras : <Grupo de compras>Valor de destino : <Destino Valor> |  |  |
| 5 | Introducir notas de cabecera | Vaya a Notas e introduzca una de las siguientes cabeceras Notas:Texto de cabeceraNota de cabeceraClases de determinación de preciosPlazosCondiciones de entregaNormas de envíoCondiciones de pagoGarantíasSanción por incumplimiento de contratoGarantíasResponsables contractuales (cláusulas)Activo fijoOtra estipulación contractualEntrega entranteNota de proveedor (general)Nota de proveedor (org.compras) |  |  |
| 6 | Añadir posiciones a plan de entregas | Desde el Nuevo plan de entregas de compras seleccione la Posiciones y seleccione Crear . | El Posición de plan de entregas de compras se visualiza. |  |
| 7 | Introducir datos de posición | El Posiciones facetas, realice las siguientes entradas:Centro : <Centro>Material : <Material>Cantidad prevista : <Destino Cantidad>Precio neto de pedido : <Precio neto de pedido>Indicador de impuestos : <XX (el valor predeterminado de la información Registro)>Fecha de impuesto : <Uso Fecha de hoy como propuesta Valor>En la Control de salida sección, efectúe la siguiente entrada:Perfil de creación : <Creación Perfil>Seleccionar Aplicar en la parte inferior de la pantalla. |  |  |
| 8 | Crear | Volver a Nuevo plan de entregas de compras y seleccione Crear en la parte inferior de la pantalla.Anote el número de plan de entregas. | Se crea un plan de entregas. |  |

#### Crear plan de entregas sin documento de orden de entrega - Estándar

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear un plan de entregas para el aprovisionamiento estándar.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar planes de entregas de compras (F2179) . | El Gestionar planes de entregas de compras (F2179) muestra la página de lista |  |
| 3 | Crear plan de entregas | Seleccionar Crear para crear un nuevo plan de entregas | El Nuevo plan de entregas de compras vista de cabecera. |  |
| 4 | Introducir datos de cabecera | Cree un nuevo plan de entregas con los siguientes datos:Proveedor : <Proveedor>Tipo de acuerdo : LP (programación) Acuerdo)Inicio de validez : <MM/DD/AAAA>Válido hasta : <MM/DD/AAAA>Sociedad : <Empresa Código>Organización de compras : <Compras Organización>Grupo de compras : <Grupo de compras>Valor de destino : <Destino Valor> |  |  |
| 5 | Introducir notas de cabecera | Navegue a la Notas e introduzca algunas de las siguientes notas de cabecera:Texto de cabeceraNota de cabeceraClases de determinación de preciosPlazosCondiciones de entregaNormas de envíoCondiciones de pagoGarantíasSanción por incumplimiento de contratoGarantíasResponsables contractuales (cláusulas)Activo fijoOtra estipulación contractualEntrega entranteNota de proveedor (general)Nota de proveedor (org.compras) |  |  |
| 6 | Añadir posiciones a plan de entregas | Desde el Nuevo plan de entregas de compras , seleccione la vista Posiciones facetas y seleccione Crear . | El Posición de plan de entregas de compras se visualiza. |  |
| 7 | Introducir datos de posición | El Posiciones facetas, realice las siguientes entradas:Centro : <Centro>Material : <Material>Cantidad prevista : <Cantidad prevista>Precio neto de pedido : <Pedido neto Precio>Indicador de impuestos : <XX (el Valor propuesto de registro info)>Fecha de impuesto : <Uso Fecha de hoy como propuesta Valor>Seleccionar Aplicar en la parte inferior de la pantalla. |  |  |
| 8 | Crear | Volver a Nuevo plan de entregas de compras vista de cabecera y seleccionar Crear en la parte inferior de la vista.Anote el número de plan de entregas. | Se crea un plan de entregas. |  |

### Crear plan de entregas para aprovisionamiento consignado

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear un plan de entregas para el aprovisionamiento consignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar planes de entregas de compras (F2179) . | El Gestionar planes de entregas muestra la página de lista. |  |
| 3 | Crear plan de entregas | Seleccionar Crear para crear un nuevo plan de entregas. | El Nuevo plan de entregas vista de cabecera. |  |
| 4 | Introducir datos de cabecera | Cree un nuevo plan de entregas con los siguientes datos:Tipo de acuerdo : LP (Plan de entregas)Proveedor : <Proveedor>Inicio de validez : Predeterminado HoyFin de validez : MM/DD/AAAA, por ejemplo, hoy + 720 díasGrupo de compras : <Grupo de compras>Organización de compras : <Organización de compras>Sociedad : <Sociedad>Valor de destino : p. ej. XXXXX EUR |  |  |
| 5 | Añadir posiciones a plan de entregas | Desde el Nuevo plan de entregas de compras , seleccione el Posiciones y seleccione Crear . | El Nueva posición de plan de entregas se visualiza. |  |
| 6 | Introducir datos de posición | El Posición facetas, realice las siguientes entradas:Tipo de posición : K (consignación)Centro : <Centro>Material : <Material>Cantidad prevista : <Cantidad prevista>Indicador de impuestos : XX (por defecto) Valor de registro info)Fecha de impuesto : Predeterminado HoyNota Si RITA está activado y los países de registro fiscal se actualizan para la sociedad en Finanzas Paso de configuración 103464 (Activar RITA y actualizar países de registro fiscal), a continuación, la residencia fiscal se puede tomar o también puede seleccionar otra residencia fiscal valor de la lista.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Seleccionar Aplicar en la parte inferior de la vista. |  |  |
| 7 | Crear | Volver a Nuevo plan de entregas de compras y seleccione Crear en la parte inferior de la vista.Anote el número de plan de entregas. | Se crea un plan de entregas. |  |

### Crear plan de entregas para aprovisionamiento de subcontratación

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear un plan de entregas para el aprovisionamiento de subcontratación.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar planes de entregas de compras (F2179) . | El Gestionar planes de entregas muestra la página de lista |  |
| 3 | Crear plan de entregas | Seleccionar Crear para crear una nueva programación acuerdo | El Nuevo plan de entregas vista de cabecera se visualiza. |  |
| 4 | Introducir datos de cabecera | Cree un nuevo plan de entregas con los siguientes datos:Tipo de acuerdo : LP (Plan de entregas)Proveedor : <Proveedor>Inicio de validez : Predeterminado HoyFin de validez : MM/DD/AAAA, por ejemplo, hoy + 720 díasGrupo de compras : <Grupo de compras>Compras Organización : <Compra Organización>Sociedad : <Sociedad>Valor de destino : p. ej. XXXXX EUR |  |  |
| 5 | Añadir posiciones a plan de entregas | Desde el Nuevo plan de entregas de compras , seleccione el Posiciones y seleccione Crear . | El Nueva posición de plan de entregas se visualiza. |  |
| 6 | Introducir datos de posición | El Posiciones facetas, realice las siguientes entradas:Tipo de posición : L (Subcontratación)Centro : <Centro>Almacén : <Almacén>Material : <Material>Precio neto de pedido : Valor predeterminado de la información registroCantidad prevista : <Cantidad prevista>Indicador de impuestos : XX (por defecto) Valor de registro info)Fecha de impuesto : Predeterminado HoyNota Si RITA está activado y los países de registro fiscal se actualizan para la sociedad en Finanzas Paso de configuración 103464 (Activar RITA y actualizar países de registro fiscal), a continuación, la residencia fiscal se puede tomar o también puede seleccionar otra residencia fiscal valor de la lista.Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration.Seleccionar Aplicar en la parte inferior del vista. |  |  |
| 7 | Crear | Volver a Nueva programación de compras Acuerdo y seleccione Crear en la parte inferior de la vista.Anote el número de plan de entregas. | Se crea un plan de entregas. |  |

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
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 22,225 chars in the whole document
