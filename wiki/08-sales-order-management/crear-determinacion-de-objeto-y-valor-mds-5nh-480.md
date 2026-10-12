---
id: 08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480
title: Crear determinación de objeto y valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 5NH: create substitution controls, characteristic combination and access for object and value determination."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NH_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product, Plant and Storage Location Substitution", object and value determination, substitution controls, characteristic combination, access sequences, product substitution, plant substitution, storage location substitution, advanced available-to-promise, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-480
topic: 08-sales-order-management/product-and-location-substitution
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear determinación de objeto y valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear determinación de objeto y valor - MDS (5NH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894804)

[2 Requisitos previos 3](#_Toc233894805)

[2.1 Acceso al sistema 3](#_Toc233894806)

[2.2 Roles 3](#_Toc233894807)

[2.3 Unidades organizativas necesarias 3](#_Toc233894808)

[2.4 Datos maestros obligatorios 4](#_Toc233894809)

[2.5 Pasos preliminares 4](#_Toc233894810)

[2.5.1 Crear control para sustitución de producto (opcional) 4](#_Toc233894811)

[2.5.2 Crear control para sustitución de centro (opcional) 6](#_Toc233894812)

[2.5.3 Crear control para sustitución de almacén (opcional) 7](#_Toc233894813)

[3 Tabla de resumen 10](#_Toc233894814)

[4 Procedimientos de prueba 11](#_Toc233894815)

[4.1 Crear combinación de características 11](#_Toc233894816)

[4.2 Crear acceso 12](#_Toc233894817)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, encontrará cómo crear una combinación y el acceso con valores de característica para los datos maestros de la combinación para su SAP S/4HANA Cloud Public Edición sistema.

La determinación de objeto y valor permite a un usuario configurar las características para determinar un control que se utilizaría para sustituir un producto/centro/almacén en el pedido de cliente durante la verificación de disponibilidad.

Esto permite la integración de la sustitución de datos maestros con la confirmación basada en alternativa (ABC) de la funcionalidad AATP.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Gestor de cumplimiento del pedido | SAP_BR_ORDER_FULFILLMNT_MNGR | Gestión de cumplimiento de pedidos | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

No se requieren datos organizativos específicos.

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Datos maestros obligatorios

No se requieren datos maestros específicos.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
|  |  |  |  |

Para obtener más información sobre la creación de objetos de datos maestros, consulte. Tabla 1: Datos maestros Referencia de script :

| HDM | Descripción |
| --- | --- |
|  |  |

### Pasos preliminares

#### Crear control para sustitución de producto (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre la creación de control para grupos de sustitución/exclusión de productos. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Productos (F4787) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | El Gestionar controles de sustitución - Productos pantalla, seleccionar Crear . | El Gestionar controles de sustitución - Crear productos se visualiza. |  |
| 4 | Introducir control | En la Cabecera , realice la siguiente entrada:Control : <Introduzca el nuevo control para la sustitución, por ejemplo, SALE> |  |  |
| 5 | Seleccione Crear. | Seleccionar Crear . | El mensaje del sistema muestra que Control creado . |  |
| 6 | Crear descripción | En la Descripción sección, seleccione Crear . | El Crear descripción de control se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para el control, por ejemplo, EN para Inglés>Descripción de control : <Introduzca un texto para describir el control, por ejemplo, Para venta> |  |  |
| 8 | Seleccione Crear. | Seleccionar Crear . | El mensaje del sistema muestra que Descripción de control creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás). | El Gestión de controles de sustitución - Productos se visualiza. |  |
| 10 | Asignar grupos | En la Grupos asignados sección, seleccione Asignar . | El Asignar grupos a control se visualiza la ventana de diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control ventana de diálogo, busque y seleccione Grupo .Por ejemplo, seleccione STANDARD_DISPLAY Grupo.Nota Si no se visualiza ningún grupo disponible, primero puede pasar por el paso del proceso Crear grupo para sustitución (Opcional) en script de datos maestros Crear sustitución de producto - MDS - 4VO .Seleccionar Asignar . | El mensaje del sistema muestra que Objeto asignado . |  |

#### Crear control para sustitución de centro (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre la creación de controles de sustitución/exclusión de centros. Las aplicaciones disponibles son depende de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Ubicaciones (F5312) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | El Gestión de controles de sustitución - Ubicaciones , seleccione Crear . | El Gestión de controles de sustitución - Creación de ubicaciones se visualiza. |  |
| 4 | Introducir control | En la Cabecera , realice las siguientes entradas:Tipo de ubicación : <Centro>Control : <Introduzca el nuevo control para la sustitución, por ejemplo, REGIÓN> |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | El mensaje del sistema muestra que Control creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de control se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca la clave de idioma aplicable para el control, para ejemplo, EN para inglés>Descripción de control : <Introduzca texto para describir el control, por ejemplo, Control para una región> |  |  |
| 8 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que Descripción de control creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás). | El Gestión de controles de sustitución - Ubicaciones se visualiza. |  |
| 10 | Asignar grupos | En la Grupos asignados seleccione Asignar . | El Asignar grupos a control se visualiza la ventana de diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control ventana de diálogo, busque y seleccione Grupo .Por ejemplo, seleccione <SOUTH_REGION> Grupo.Nota Si no se visualiza ningún grupo disponible, primero puede pasar por el paso del proceso Crear grupo para centro Sustitución (opcional) en script de datos maestros Crear sustitución y exclusión de ubicación - MDS - 5NG .Seleccionar Asignar . | El mensaje del sistema muestra que Se ha(n) asignado grupo(s) . |  |

#### Crear control para sustitución de almacén (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre la creación de controles para los controles de sustitución/exclusión de almacén. Aplicaciones disponibles depende de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Ubicaciones (F5312) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | El Gestión de controles de sustitución - Ubicaciones , seleccione Crear . | El Gestión de controles de sustitución - Creación de ubicaciones se visualiza. |  |
| 4 | Introducir control | En la Cabecera , realice las siguientes entradas:Tipo de ubicación : <Almacén>Control : <Introduzca el nuevo Control para la sustitución, por ejemplo, STORAGE_TYPE> |  |  |
| 5 | Seleccione Crear. | Seleccionar Crear . | El mensaje del sistema muestra que Control creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de control se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca la clave de idioma aplicable para el control, para ejemplo, EN para inglés>Descripción de control : <Introduzca texto para describir el control, por ejemplo, Control para tipo de almacenamiento> |  |  |
| 8 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que Descripción de control creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás). | El Gestión de controles de sustitución - Ubicaciones se visualiza. |  |
| 10 | Asignar grupos | En la Grupos asignados seleccione Asignar . | El Asignar grupos a control se visualiza la ventana de diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control ventana de diálogo, busque y seleccione Grupo .Por ejemplo, seleccione <COLD_STORAGE> Grupo.Nota Si no se visualiza ningún grupo disponible, primero puede pasar por el paso del proceso Crear grupo para Sustitución de almacén (opcional) en script de datos maestros Crear sustitución y exclusión de ubicación - MDS - 5NG .Seleccionar Asignar . | El mensaje del sistema muestra que Se ha(n) asignado grupo(s) . |  |

## Tabla de resumen

Este elemento de alcance consta de los segmentos de proceso proporcionados en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear combinación de características](#unique_11) [página ] 11 | Gestor de cumplimiento del pedido | Gestionar combinaciones de características (F5303) . | Se ha creado la combinación de características. |
| [Crear acceso](#unique_12) [página ] 12 | Gestor de cumplimiento del pedido | Gestionar secuencias de acceso - Sustituciones (F5302) | El acceso se crea para la combinación creada en los segmentos anteriores y Los valores de característica se definen para los accesos. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear combinación de características

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre la creación de una combinación de características. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar combinaciones de características (F5303) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | El Gestionar combinación de características , seleccione Crear . | El Gestionar creación de combinación de características se visualiza. |  |
| 4 | Introducir datos de cabecera | En la Cabecera , realice las siguientes entradas:Combinación : <Introduzca el nombre de la combinación>Descripción de combinación : <Introduzca la descripción de la combinación>Utilización : <Sustitución>Tipo de catálogo : <Base (documento de ventas) con uso SUBSTN>La combinación, la utilización y el tipo de catálogo son obligatorios para crear una sustitución. |  |  |
| 5 | Asignar características | En la Características introduzca las siguientes entradas para asignar las Características:Seleccionar AsignarSeleccione las características en la pantallaSeleccionar Asignar en la pantallaFije el orden de las características utilizando la Arriba o bien Abajo flecha |  |  |
| 6 | Seleccione Crear. | Seleccionar Crear . | El mensaje del sistema muestra que Combinación creada . |  |

### Crear acceso

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear el acceso para la combinación y definir los valores CVC para el acceso. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar secuencias de acceso - Sustituciones (F5302) | El Gestionar secuencias de acceso - Sustitución se visualiza. |  |
| 3 | Seleccione Crear. | En la Gestionar secuencias de acceso - Sustitución ver, en el Productos , seleccione Crear ( 3 pestañas Productos , Centro y Almacén están disponibles). | El Gestionar secuencias de acceso - Sustitución Crear. |  |
| 4 | Introducir los detalles | En la Ventana emergente , realice las siguientes entradas:Combinación : <Seleccione la combinación de la ayuda para entradas>Estado : <Seleccione el estado requerido de la lista desplegable> El campo Estado está predeterminado con En Activo estado.Seleccionar CrearLa combinación es obligatoria para crear un acceso. | El mensaje del sistema muestra que se ha creado el acceso. |  |
| 5 | Introducir detalles de controles asignados | En la Controles asignados añada la sección Características y los Detalles de control:Seleccionar AñadirCaracterísticas : <Introduzca los valores de características o seleccione de la ayuda para entradas>Estado : <El estado es Activo por defecto>Ejecutar sustitución : <Activado de forma predeterminada>Control: <Opcional - Introduzca la sustitución de producto Control>Añada varios valores según sea necesario. | Las columnas de características que se muestran en el Controles asignados son las asignadas a la combinación seleccionada al crear la acceso. |  |
| 6 | Crear acceso | Seleccionar Crear . | El mensaje del sistema muestra que Acceso creado . |  |

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
- related-to :: [[08-sales-order-management/5nh-483]]
- related-to :: [[08-sales-order-management/create-object-and-value-determination-mds-5nh-479]]
- related-to :: [[08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482]]
- related-to :: [[08-sales-order-management/mds-5nh-481]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 20,688 chars in the whole document
