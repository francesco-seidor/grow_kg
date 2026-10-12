---
id: 08-sales-order-management/script-de-datos-maestros-crear-sustitucion-y-exclusion-de-ubicacion-md
title: Script de datos maestros - Crear sustitución y exclusión de ubicación - MDS (5NG) (5NG_S4CLD2608_Master_Data_ES_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating plant and storage location substitutions and exclusions via Fiori apps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NG_S4CLD2608_Master_Data_ES_XX]
keywords: ["Product, Plant and Storage Location Substitution", plant substitution, plant exclusion, storage location substitution, storage location exclusion, substitution reasons, substitution groups, substitution controls, order fulfillment manager role, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-474
topic: 08-sales-order-management/product-and-location-substitution
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear sustitución y exclusión de ubicación - MDS (5NG) (5NG_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear sustitución y exclusión de ubicación - MDS (5NG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894822)

[2 Requisitos previos 3](#_Toc233894823)

[2.1 Acceso al sistema 3](#_Toc233894824)

[2.2 Roles 3](#_Toc233894825)

[2.3 Unidades organizativas necesarias 3](#_Toc233894826)

[2.4 Datos maestros obligatorios 4](#_Toc233894827)

[2.5 Pasos preliminares para la sustitución de centro 4](#_Toc233894828)

[2.5.1 Crear motivo para sustitución de centro (opcional) 4](#_Toc233894829)

[2.5.2 Crear grupo para sustitución de centro (opcional) 5](#_Toc233894830)

[2.5.3 Crear control para sustitución de centro (opcional) 7](#_Toc233894831)

[2.6 Pasos preliminares para la sustitución de almacén 8](#_Toc233894832)

[2.6.1 Crear motivo para sustitución de almacén (opcional) 8](#_Toc233894833)

[2.6.2 Crear grupo para sustitución de almacén (opcional) 10](#_Toc233894834)

[2.6.3 Crear control para sustitución de almacén (opcional) 11](#_Toc233894835)

[3 Tabla de resumen 13](#_Toc233894836)

[4 Procedimientos de prueba 14](#_Toc233894837)

[4.1 Sustitución de centro 14](#_Toc233894838)

[4.1.1 Crear sustitución de centro 14](#_Toc233894839)

[4.1.2 Crear exclusión de centro 15](#_Toc233894840)

[4.2 Sustitución de almacén 17](#_Toc233894841)

[4.2.1 Crear sustitución de almacén 17](#_Toc233894842)

[4.2.2 Crear exclusión de almacén 18](#_Toc233894843)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento, encontrará cómo crear datos maestros de sustitución y exclusión de ubicación para su SAP S/4HANA Cloud Public Edición sistema.

Los tipos de ubicación Centro y Almacén se admiten para la sustitución y exclusión.

La sustitución de centro es una técnica utilizada para sustituir un centro por otro. Se puede crear una sustitución de centro por varios motivos. Por ejemplo:

- El centro de origen está en mantenimiento
- El centro de origen está en la zona de contención
- El stock de producto no está disponible en el centro de origen

La exclusión de centro permite a los clientes excluir un centro de ser un sustituto. Por ejemplo, se puede crear una exclusión de centro para un centro que se ha cerrado temporalmente.

La sustitución de almacén es una técnica que se utiliza para sustituir un almacén por otro dentro del mismo centro. A La sustitución de almacén se puede crear por varios motivos. Por ejemplo:

- El almacén de origen no está disponible
- El stock de productos no está disponible en el almacén de origen dentro del centro

La exclusión de almacén permite a los clientes excluir un almacén de ser un sustituto.

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

### Unidades organizativas necesarias

La estructura organizativa refleja la estructura de su empresa.

Los sustitutos de centro pueden depender de las unidades organizativas (organización de ventas y canal de distribución) de la empresa. También puede ser independiente de la unidad organizativa.

El sustituto de almacén depende de la unidad organizativa (centro) de la empresa. Siempre depende de la unidad organizativa.

La siguiente tabla ofrece un resumen de las unidades organizativas relevantes.

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Sustitución de centro y exclusión de centro | Organización de ventas |  | La organización de ventas no es obligatoria en PlantSubstitution/Exclusion. La sustitución/exclusión de centro puede producirse sin restricción de organización de ventas. | Organización de ventas:____________ |
| Sustitución de centro y exclusión de centro | Canal de distribución |  | El canal de distribución no es obligatorio en la sustitución/exclusión de centro. La sustitución/exclusión de centro puede producirse sin restricción de canal de distribución. | Canal de distribución:____________ |
| Sustitución de almacén y exclusión de almacén | Centro |  | El centro es obligatorio en Sustitución/exclusión de almacén. La sustitución/exclusión de almacén no puede ocurrir sin el centro. | Centro: 1010 |

### Datos maestros obligatorios

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| N/A | N/A | N/A | N/A |

### Pasos preliminares para la sustitución de centro

#### Crear motivo para sustitución de centro (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un motivo para la sustitución/exclusión de centro. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar motivos de sustitución - Ubicaciones (F5313) . | El Gestión de motivos de sustitución - Ubicaciones la pantalla es visualizados. |  |
| 3 | Seleccione Crear. | El Gestión de motivos de sustitución - Ubicaciones pantalla, seleccionar Crear . | El Gestión de motivos de sustitución - Creación de ubicaciones pantalla se visualiza. |  |
| 4 | Introducir motivo | En la Cabecera , realice la siguiente entrada.Tipo de ubicación : <Centro>Motivo : <Introduzca el nuevo código de motivo para el centro sustitución, por ejemplo, NEW_PLANT> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Se ha creado el motivo . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de motivo se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para el motivo, por ejemplo, EN English>Descripción de motivo : <Introduzca un texto para describir el motivo, por ejemplo, Nuevo centro disponible> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción creada . |  |

#### Crear grupo para sustitución de centro (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear Grupo para sustitución/exclusión de centro. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar grupos de sustitución - Ubicaciones (F5311) . | El Gestión de grupos de sustitución - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | El Gestión de grupos de sustitución - Ubicaciones pantalla, seleccionar Crear . | El Gestión de grupos de sustituciones - Creación de ubicaciones pantalla se visualiza. |  |
| 4 | Introducir grupo | En la Cabecera , realice la siguiente entrada:Tipo de ubicación : <Centro>Grupo : <Introduzca el nuevo grupo para la sustitución, por ejemplo, SOUTH_REGION> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Grupo creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de grupo se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para el grupo, por ejemplo, EN Inglés>Descripción de grupo : <Introduzca el texto para describir el grupo, por ejemplo, Centros disponibles en la región sur> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción de grupo creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás). | El Gestión de grupos de sustituciones - Ubicaciones la pantalla es visualizados. |  |
| 10 | Activar datos de grupo | Seleccionar Fijar en activo . | El mensaje del sistema muestra que Estado modificado . |  |

#### Crear control para sustitución de centro (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear controles de sustitución/exclusión de centros. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Ubicaciones (F5312) . | El Gestión de controles de sustitución - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | El Gestión de controles de sustitución - Ubicaciones , seleccione Crear . | El Gestión de controles de sustitución - Creación de ubicaciones pantalla se visualiza. |  |
| 4 | Introducir control | En la Cabecera , realice la siguiente entrada.Tipo de ubicación : <Centro>Control : <Introduzca el nuevo control para la sustitución, por ejemplo, REGION> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Control creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de control se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para Control, por ejemplo, EN English>Descripción de control : <Introduzca un texto para describir el control, por ejemplo, Control para una región> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción de control creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás). | El Gestionar control de sustitución - Ubicaciones se visualiza. |  |
| 10 | Asignar grupos | En la Grupos asignados sección, seleccione Asignar . | El Asignar grupos a control se visualiza el diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control diálogo, busque y seleccione Grupo .Por ejemplo, seleccione Grupo <SOUTH_REGION>Seleccionar Asignar . | Se muestra el mensaje del sistema Se ha(n) asignado grupo(s). |  |

### Pasos preliminares para la sustitución de almacén

#### Crear motivo para sustitución de almacén (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear un motivo para la sustitución/exclusión de almacén. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar motivos de sustitución - Ubicaciones (F5313) . | El Gestión de motivos de sustitución - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | El Gestión de motivos de sustitución - Ubicaciones pantalla, seleccionar Crear . | El Motivo se visualiza. |  |
| 4 | Introducir motivo | En la Cabecera , realice la siguiente entrada.Tipo de ubicación : <Almacenamiento Ubicación>Motivo : <Introduzca el nuevo código de motivo para la sustitución de almacén, por ejemplo, NEW_SLOC> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Se ha creado el motivo. |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Descripción de motivo se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para el motivo, por ejemplo, EN English>Descripción de motivo : <Introduzca un texto para describir el motivo, por ejemplo, New storage location is available> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción creada . |  |

#### Crear grupo para sustitución de almacén (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear Grupo para sustitución/exclusión de almacén. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar grupos de sustitución - Ubicaciones (F5311) . | El Gestión de grupos de sustitución - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | El Gestionar grupos de sustitución - Ubicaciones , seleccione Crear . | El Gestión de grupos de sustituciones - Creación de ubicaciones pantalla se visualiza. |  |
| 4 | Introducir grupo | En la Cabecera , realice la siguiente entrada:Tipo de ubicación : <Almacenamiento Ubicación>Grupo : <Introduzca el nuevo grupo para la sustitución, por ejemplo, COLD_STORAGE> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Grupo creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de grupo se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para el grupo, por ejemplo, EN Inglés>Descripción de grupo : <Introduzca un texto para describir el grupo, por ejemplo, las posiciones Almacén para almacenamiento en frío> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción de grupo creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás) | El Gestionar grupos de sustituciones-Ubicaciones la pantalla es visualizados. |  |
| 10 | Activar datos de grupo | Seleccionar Fijar en activo . | El mensaje del sistema muestra que Estado modificado . |  |

#### Crear control para sustitución de almacén (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear el control para los controles de sustitución/exclusión de almacén. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Aparece la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar controles de sustitución - Ubicaciones (F5312) . | El Gestión de controles de sustitución - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | El Gestión de controles de sustitución - Ubicaciones pantalla, seleccionar Crear . | El Gestión de controles de sustitución - Creación de ubicaciones se visualiza. |  |
| 4 | Introducir control | En la Cabecera , realice la siguiente entrada.Tipo de ubicación : <Almacenamiento Ubicación>Control : <Introduzca el nuevo control para la sustitución, por ejemplo, STORAGE_TYPE> |  |  |
| 5 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Control creado . |  |
| 6 | Seleccione Crear. | En la Descripción sección, seleccione Crear . | El Crear descripción de control se visualiza. |  |
| 7 | Introducir datos de descripción | En la Descripción , realice las siguientes entradas:Clave de idioma : <Introduzca el idioma aplicable para Control, por ejemplo, EN English>Descripción de control : <Introduzca un texto para describir el control, por ejemplo, Control para el tipo de almacenamiento> |  |  |
| 8 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Descripción de control creada . |  |
| 9 | Seleccione Atrás. | En la Título sección, seleccione < (Atrás) . | El Gestionar ubicaciones de control de sustitución se visualiza. |  |
| 10 | Asignar grupos | En la Grupos asignados sección, seleccione Asignar . | El Asignar grupos a control se visualiza el diálogo. |  |
| 11 | Elegir grupo | En la Asignar grupos a control diálogo, busque y seleccione Grupo .Por ejemplo, seleccione Grupo <COLD_STORAGE>Seleccionar Asignar . | Se muestra el mensaje del sistema Se ha(n) asignado grupo(s). |  |

## Tabla de resumen

Este elemento de alcance consta de los segmentos de proceso proporcionados en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear sustitución de centro](#unique_14) [página ] 14 | Gestor de cumplimiento del pedido | Gestionar sustituciones - Ubicaciones (F5314) | Se ha creado el registro de sustitución de centro. |
| [Crear exclusión de centro](#unique_15) [página ] 15 | Gestor de cumplimiento del pedido | Gestionar exclusiones - Ubicaciones (F5315) | Se ha creado el registro de exclusión de centro. |
| [Crear sustitución de almacén](#unique_16) [página ] 17 | Gestor de cumplimiento del pedido | Gestionar sustituciones - Ubicaciones (F5314) | Se ha creado el registro de sustitución de almacén. |
| [Crear exclusión de almacén](#unique_17) [página ] 18 | Gestor de cumplimiento del pedido | Gestionar exclusiones - Ubicaciones (F5315) | Se ha creado el registro de exclusión de almacén. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Sustitución de centro

#### Crear sustitución de centro

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear una sustitución de centro. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar sustituciones - Ubicaciones (F5314) . | El Gestionar sustituciones - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | En la Gestionar sustituciones - Ubicaciones vista, en la vista Centro sección, seleccione Crear . | El Gestionar sustituciones - Ubicaciones disposición de columnas flexible con la pantalla Crear. |  |
| 4 | Introducir datos de cabecera | En la Cabecera , realice las siguientes entradas:Centro : <Indique el centro que requiere un sustituto>Centro sustituto : <Introduzca el suplente>Organización de ventas : <Número de organización de ventas>Canal de distribución : <Número de canal de distribución>Los datos de centro y centro de sustitución son obligatorios para crear una sustitución. |  |  |
| 5 | Introducir datos de información general | En la Información general , realice las siguientes entradas:Motivo : <Introduzca el motivo para crear el sustituto. Por ejemplo, NEW_PLANT>Grupo : <Introduzca el grupo de sustitución. Por ejemplo, SOUTH_REGION>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 6 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Sustitución creada . |  |
| 7 | Activar datos de sustitución de centro | Seleccionar Fijar en activo . | Se muestra el mensaje del sistema Estado modificado . |  |
| 8 | Visualizar gráfico | Seleccionar Ver gráfico | El Visualizar gráfico de red de centros se visualiza. |  |

#### Crear exclusión de centro

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear la exclusión de centro. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar exclusiones - Ubicaciones (F5315) . | El Gestión de exclusiones - Ubicaciones se visualiza. |  |
| 3 | Seleccione Crear. | En la Gestión de exclusiones - Ubicaciones (centro) , seleccione Crear . | El Exclusión de centro se visualiza. |  |
| 4 | Introducir datos de cabecera | En la Cabecera , realice las siguientes entradas:Centro : <Introduzca el centro que se debe excluir de la sustitución>Organización de ventas : <Número de organización de ventas>Canal de distribución : <Número de canal de distribución>El centro es obligatorio para crear una exclusión. |  |  |
| 5 | Introducir datos de información general | En la Información general , realice las siguientes entradas:Motivo : <Introduzca el motivo para excluir el centro>Grupo : <Introduzca el grupo aplicable para la exclusión de centro>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 6 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Exclusión creada . |  |
| 7 | Activar datos de exclusión de centro | Seleccionar Fijar en activo . | Se muestra el mensaje del sistema Estado modificado . |  |

### Sustitución de almacén

#### Crear sustitución de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear la sustitución de almacén. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar sustituciones - Ubicaciones (F5314) . | El Gestionar sustituciones - Ubicaciones se visualiza. |  |
| 3 | Seleccionar almacén | El Gestionar sustituciones - Ubicaciones seleccione el pulsador Almacén pestaña. | El Gestionar sustituciones - Ubicaciones (almacén) se visualiza. |  |
| 4 | Seleccione Crear. | El Almacén , seleccione Crear . | El Gestionar sustituciones - Ubicaciones disposición de columnas flexible con la pantalla Crear. |  |
| 5 | Introducir datos de cabecera | En la Cabecera , realice las siguientes entradas:Centro : <Número de centro>Almacén : <Introduzca el almacén que requiere un suplente>Almacén sustituto : <Indique el sustituto>Los datos de centro y almacén sustituto son obligatorios para crear una subutilización, mientras que el almacén es opcional. El centro es se selecciona por defecto cuando se selecciona Almacén. |  |  |
| 6 | Introducir datos de información general | En la Información general , realice las siguientes entradas:Motivo : <Introduzca el motivo para crear el sustituto. Por ejemplo, NEW_SLOC>Grupo : <Introduzca el grupo de sustitución. Por ejemplo, COLD_STORAGE>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 7 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Sustitución creada . |  |
| 8 | Activar datos de sustitución de almacén | Seleccionar Fijar en activo . | Se muestra el mensaje del sistema Estado modificado . |  |
| 9 | Visualizar gráfico | Seleccionar Ver gráfico . | El Visualizar gráfico de red de almacenes se visualiza. |  |

#### Crear exclusión de almacén

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones para crear la Exclusión de almacén. Las aplicaciones disponibles dependen de su rol asignado.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Gestor de cumplimiento del pedido . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar exclusiones - Ubicaciones (F5315) . | El Gestión de exclusiones - Ubicaciones se visualiza. |  |
| 3 | Seleccionar almacén | En la Gestión de exclusiones - Ubicaciones , seleccione Almacén . | El Gestión de exclusiones - Ubicaciones (almacén) se visualiza. |  |
| 4 | Seleccione Crear. | En la Gestión de exclusiones - Ubicaciones (almacén) , seleccione Crear . | El Gestión de exclusiones - Creación de ubicaciones se visualiza. |  |
| 5 | Introducir datos de cabecera | En la Cabecera , realice las siguientes entradas:Centro : <Número de centro>Almacén : <Introduzca el almacenamiento ubicación que debe excluirse de la sustitución>Tanto el centro como el almacén son obligatorios para la exclusión. |  |  |
| 6 | Introducir datos de información general | En la Información general , realice las siguientes entradas:Motivo : <Introduzca el motivo para excluir el almacén>Grupo : <Introduzca el grupo aplicable para la exclusión de almacén>Inicio de validez : <Introduzca la fecha y hora de inicio de validez>Válido hasta : <Introduzca la fecha y hora de fin de validez>Huso horario : <Introduzca el huso horario aplicable para la validez>Las entradas anteriores son opcionales. |  |  |
| 7 | Crear sus datos | Seleccionar Crear . | Se muestra el mensaje del sistema Exclusión creada . |  |
| 8 | Activar datos de exclusión de almacén | Seleccionar Fijar en activo . | Se muestra el mensaje del sistema Estado modificado . |  |

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
- related-to :: [[08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472]]
- related-to :: [[08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng]]
- related-to :: [[08-sales-order-management/mds-5ng-475]]
- related-to :: [[08-sales-order-management/mds-5ng-477]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 34,326 chars in the whole document
