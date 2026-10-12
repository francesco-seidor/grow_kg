---
id: 08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420
title: Creación de sustitución de producto - MDS (4VO) (4VO_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script 4VO: test steps to create product substitution and product exclusion master data, with optional reason, group and control, in S/4HANA Cloud 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, substitution reasons, substitution groups, substitution controls, product master data, business roles, plant organizational units, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-420
topic: 08-sales-order-management/product-and-location-substitution
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Creación de sustitución de producto - MDS (4VO) (4VO_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de sustitución de producto - MDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894756)

[2 Requisitos previos 3](#_Toc233894757)

[2.1 Acceso al sistema 3](#_Toc233894758)

[2.2 Roles 3](#_Toc233894759)

[2.3 Unidades organizativas necesarias 3](#_Toc233894760)

[2.4 Datos maestros obligatorios 4](#_Toc233894761)

[2.5 Pasos preliminares 4](#_Toc233894762)

[2.5.1 Crear motivo para sustitución de producto (opcional) 4](#_Toc233894763)

[2.5.2 Crear grupo para sustitución (opcional) 5](#_Toc233894764)

[2.5.3 Crear control para sustitución (opcional) 7](#_Toc233894765)

[3 Tabla de resumen 9](#_Toc233894766)

[4 Procedimientos de prueba 10](#_Toc233894767)

[4.1 Crear sustitución de producto 10](#_Toc233894768)

[4.2 Crear exclusión de producto 11](#_Toc233894769)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, encontrará cómo crear datos maestros de sustitución y exclusión de producto para su SAP S/4HANA Cloud Public Edición sistema.

La sustitución de producto es una técnica utilizada para sustituir un producto por otro. Una sustitución de producto se puede crear por varios motivos. Por ejemplo:

- El producto ya no está en stock
- El producto está fuera de garantía
- El producto sustituto es abundante en stock

La exclusión de producto permite a los clientes excluir un producto de ser un sustituto. Por ejemplo, la exclusión se puede crear para un producto a reemplazar.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

La estructura organizativa refleja la estructura de su empresa. Los sustitutos de producto pueden ser en función de las unidades organizativas (centro) de la empresa. También puede ser independiente de la unidad organizativa. La siguiente tabla ofrece un resumen de los unidades organizativas.

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Sustitución de producto y exclusión de producto | Centro |  | El centro no es obligatorio en la sustitución/exclusión de producto. Producto La subestación/exclusión puede ocurrir sin restricción de planta. | Centro:____________ |

### Datos maestros obligatorios

Los datos de sustitución de producto hacen referencia a los datos maestros de producto. Los datos maestros obligatorios para el test El script representa Materiales/Productos. Cree sus propios datos maestros siguiendo la datos maestros de muestra proporcionados a continuación.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material | Crear sustitución de productoCrear exclusión de producto | Obligatorio | Para crear una sustitución de producto o una exclusión de producto, debería haber al menos 2 datos maestros de material/producto en su sistema |

Para obtener más información sobre la creación de objetos de datos maestros, consulte. [Scripts de datos maestros (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Tabla 1: Referencia de script de datos maestros

| HDM | Descripción |
| --- | --- |
| BNF | Creación de maestro de productos de tipo "Mercadería" - MDS |

### Pasos preliminares

#### Crear motivo para sustitución de producto (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear el Motivo de sustitución/exclusión de producto. Las aplicaciones disponibles son dependientes en su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar motivos de sustitución - Productos (F4789) . | El Gestión de motivos de sustitución - Productos se visualiza. |  |
| 3 | Seleccione Crear. | El Gestión de motivos de sustitución - Productos , seleccione Crear . | El Motivo se visualiza. |  |
| 4 | Introducir motivo | En la Cabecera , realice la siguiente entrada:Motivo : <Introduzca el nuevo código de motivo para la sustitución, por ejemplo, Upgrade> |  |  |
| 5 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 6 | Seleccione Crear. | En la Descripción seleccione Crear . | El Descripción de motivo se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción la sección, haga siguientes entradas:Clave de idioma : <Introduzca la clave de idioma aplicable para el motivo, por ejemplo, EN para Inglés>Descripción de motivo : <Introduzca un texto para describir el motivo, por ejemplo, Aplicable para productos en proceso de actualización> |  |  |
| 8 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que Descripción creada . |  |

#### Crear grupo para sustitución (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un grupo para producto Sustitución/Exclusión. Las aplicaciones disponibles dependen de su asignación rol.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar grupos de sustitución - Productos (F4788) . | El Gestionar grupos de sustitución - Productos se visualiza la pantalla. |  |
| 3 | Seleccione Crear. | El Gestionar grupos de sustitución – Productos seleccione Crear . | El Gestión de grupos de sustituciones - Productos Crear se visualiza. |  |
| 4 | Introducir grupo | En la Cabecera sección, haga lo siguiente entrada:Grupo : <Introduzca el nuevo grupo para sustitución, por ejemplo, STANDARD_DISPLAY> |  |  |
| 5 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 6 | Seleccione Crear. | En la Descripción seleccione Crear . | El Crear descripción de grupo la pantalla es visualizado. |  |
| 7 | Introducir datos de descripción | En la Descripción la sección, haga siguientes entradas:Clave de idioma : <Intro Idioma aplicable para grupo, por ejemplo, EN Inglés>Descripción de grupo : <Intro texto para describir el grupo, por ejemplo, Todos estándar visualización del ordenador> |  |  |
| 8 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás) | El Gestión de grupos de sustituciones - Productos se visualiza. |  |
| 10 | Activar datos de grupo | Seleccionar Fijar en activo . | El mensaje del sistema muestra que el objeto es activo . |  |

#### Crear control para sustitución (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un control para el producto grupos de sustitución/exclusión. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Productos (F4787) . | El Gestionar controles de sustitución - Productos se visualiza. |  |
| 3 | Seleccione Crear. | El Gestionar controles de sustitución – Productos seleccione Crear . | El Gestión de controles de sustitución - Productos Crear se visualiza. |  |
| 4 | Introducir control | En la Cabecera sección, haga lo siguiente entrada.Control : <Introduzca el nuevo Control para sustitución, por ejemplo, VENTA> |  |  |
| 5 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 6 | Seleccione Crear. | En la Descripción seleccione Crear . | El Crear descripción de control la pantalla es visualizado. |  |
| 7 | Introducir datos de descripción | En la Descripción la sección, haga siguientes entradas:Clave de idioma : <Intro Idioma aplicable para control, por ejemplo, EN Inglés>Descripción de control : <Intro texto para describir el control, por ejemplo, Para Venta> |  |  |
| 8 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás) . | El Gestión de controles de sustitución - Productos se visualiza la pantalla. |  |
| 10 | Asignar grupos | En la Grupos asignados sección, seleccione Asignar . | El Asignar grupos a control se visualiza el diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control diálogo, busque y seleccione Grupo .Por ejemplo, seleccione Grupo <STANDARD_DISPLAY>Seleccionar Asignar . | El mensaje del sistema muestra que el objeto es asignado . |  |

## Tabla de resumen

Este elemento de alcance consta de los segmentos de proceso proporcionados en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear sustitución de producto](#unique_11) [página ] 10 | Especialista en datos maestros - Datos de producto | Gestionar sustituciones - Productos (F4785) | Se ha creado el registro Product Substitution. |
| [Crear exclusión de producto](#unique_12) [página ] 11 | Especialista en datos maestros - Datos de producto | Gestionar exclusiones - Productos (F4786) | Se ha creado el registro Product Exclusion. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear sustitución de producto

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear una sustitución de producto. Aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar sustituciones - Productos (F4785) . | El Gestionar sustituciones - Productos se visualiza. |  |
| 3 | Seleccione Crear. | En la Gestionar sustituciones - Productos vista, seleccione Crear . | El Gestionar sustituciones - Productos disposición de columnas flexible con la pantalla Crear. |  |
| 4 | Introducir datos de cabecera | En la Cabecera sección, haga lo siguiente entradas:Producto : <Introduzca el producto que requiere un suplente>Producto sustituto : <Introduzca el suplente>Centro : <Centro número>Los datos de producto y de producto de sustitución son obligatorios para crear un sustitución. |  |  |
| 5 | Introducir datos de información general | En la Información general sección, hacer las siguientes entradas:Motivo : <Introduzca el motivo para crear el sustituto. Por ejemplo, Upgrade>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 6 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 7 | Activar datos de sustitución de producto | Seleccionar Fijar en activo . | El mensaje del sistema muestra que El objeto está activo . |  |

### Crear exclusión de producto

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear una Exclusión de producto. Aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar exclusiones - Productos (F4786) . | El Gestión de exclusiones - Productos se visualiza. |  |
| 3 | Seleccione Crear. | En la Gestión de exclusiones - Productos vista, seleccionar Crear . | El Gestión de exclusiones - Creación de productos se visualiza. |  |
| 4 | Introducir datos de cabecera | En la Cabecera sección, haga lo siguiente entradas:Producto : <Introduzca el producto que debe excluirse de Sustitución>Centro : <Centro número>El producto es obligatorio para crear una exclusión. |  |  |
| 5 | Introducir datos de información general | En la Información general sección, hacer las siguientes entradas:Motivo : <Introduzca el motivo para excluir el producto>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 6 | Guardar los datos | Seleccionar Crear . | El mensaje del sistema muestra que El objeto se ha grabado . |  |
| 7 | Activar datos de exclusión de producto | Seleccionar Fijar en activo . | El mensaje del sistema muestra que El objeto está activo . |  |

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
- related-to :: [[08-sales-order-management/create-product-substitution-mds-4vo-419]]
- related-to :: [[08-sales-order-management/mds-4vo-421]]
- related-to :: [[08-sales-order-management/mds-4vo-423]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 19,971 chars in the whole document
