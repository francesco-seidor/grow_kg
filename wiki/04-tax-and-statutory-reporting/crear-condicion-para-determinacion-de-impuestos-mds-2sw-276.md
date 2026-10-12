---
id: 04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276
title: Crear condición para determinación de impuestos - MDS (2SW) (2SW_S4CLD2608_Master_Data_ES_XX)
description: "Spanish master data test script (2SW) for SAP S/4HANA Cloud Public Edition 2608: tax determination condition records and purchasing price conditions via Fiori apps."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_ES_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax determination conditions, purchasing price conditions, price condition changes, master data scripts, business roles, test procedures, fiori launchpad access, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-276
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear condición para determinación de impuestos - MDS (2SW) (2SW_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear condición para determinación de impuestos - MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894558)

[2 Requisitos previos 3](#_Toc233894559)

[2.1 Acceso al sistema 3](#_Toc233894560)

[2.2 Roles 3](#_Toc233894561)

[2.3 Datos maestros obligatorios y opcionales 3](#_Toc233894562)

[3 Tabla de resumen 5](#_Toc233894563)

[4 Procedimientos de prueba 6](#_Toc233894564)

[4.1 Crear registros de condición para determinación de impuestos 6](#_Toc233894565)

[4.2 Crear condiciones de precio 8](#_Toc233894566)

[4.3 Modificar condiciones de precio 9](#_Toc233894567)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un registro de condición para determinación de impuestos contiene información específica de un país/región y los diferentes indicador de impuestos para diferentes combinaciones de indicador de impuestos para indicador de material/impuesto para Indicador de centro/impuesto de importación.

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
| Especialista fiscal | SAP_BR_TAX_SPECIALIST | Tipos impositivos | SAP_BR_TAX_SPECIALIST |  |
| Comprador | SAP_BR_PURCHASER | Compras / Aprovisionamiento y contratación | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un material registro de datos maestros.

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear una condición de precio:

País de destino: por ejemplo, DE

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| País de destino | Pantalla inicial | Obligatorio |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se proporcionan en la siguiente tabla.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación SAP Fiori / Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear registros de condición para determinación de impuestos](#unique_7) [página ] 6 | Especialista fiscal | Fijar tipos impositivos - Compras (MEK2) | Se ha fijado la condición para determinación de impuestos. |
| [Crear condiciones de precio](#unique_8) [página ] 8 | Comprador | Crear condiciones de precio - Compras (MEK1) | Se han creado las condiciones de precio. |
| [Modificar condiciones de precio](#unique_9) [página ] 9 | Comprador | Modificar condiciones de precio - Compras (MEK2) | Se han modificado las condiciones de precio. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear registros de condición para determinación de impuestos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista fiscal . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Fijar tipos impositivos - Compras (MEK2) . | Se abre la aplicación. |  |
| 3 | Tipo de condición de determinación de precios | El Modificar registros de condición , realice la siguiente entrada y pulse Intro :Clase de condición : por ejemplo, TTX1 | El Combinación de claves se visualiza. |  |
| 4 | Combinación de claves | El Combinación de claves seleccione el pulsador Impuestos: Material, centro y origen y seleccione Seleccionar . | El Modificar T no deducible (TTX1): Selección se visualiza. |  |
| 5 | País de destino | El Modificar T no deducible (TTX1): Selección , realice la siguiente entrada y seleccione Ejecutar :País de destino : <Código de país/región> | El Modificar condición para determinación de impuestos no deducible (TTX1): Resumen se visualiza. |  |
| 6 | Modificar condición para determinación de impuestos | El Modificar condición para determinación de impuestos no deducible (TTX1): Resumen , efectúe las siguientes entradas:Ind.impto.mater. : <Indicador de impuestos para material>Ce.ind.imp. : <Indicador de impuestos: Centro>Importar : <Importar>Inicio de validez : <Inicio de validez>Válido hasta : <Fin de validez>Indicador de impuestos : <Indicador de impuestos> | Se actualiza el registro de condición para determinación de impuestos. |  |
| 7 | Grabar | Seleccionar Grabar . | Se guarda el registro de condición para determinación de impuestos. |  |
| 8 | Seleccione Atrás. | Seleccionar Volver dos veces. |  |  |
| 9 | Tipo de condición de determinación de precios | El Modificar registros de condición , realice la siguiente entrada y pulse Intro :Clase de condición : por ejemplo, TTX1 | El Combinación de claves se visualiza la ventana de diálogo. |  |
| 10 | Combinación de claves | En la Combinación de claves seleccione la ventana de diálogo Impuesto: Centro y origen de imputación y región marque la casilla de selección y seleccione Seleccionar . | El Modificar T no deducible (TTX1): Selección se visualiza. |  |
| 11 | País de destino | El Modificar T no deducible (TTX1): Selección , realice la siguiente entrada y seleccione Ejecutar :País de destino : <Código de país/región> | El Modificar condición para determinación de impuestos no deducible (TTX1): Resumen se visualiza. |  |
| 12 | Modificar condición para determinación de impuestos | El Modificar condición para determinación de impuestos no deducible (TTX1): Resumen , efectúe las siguientes entradas:Ce.ind.imp. : <Indicador de impuestos: Centro>Ind.impto.imputación : <Imputación de indicador de impuestos>Importar : <Importar>Región de indicador de impuestos : <Región>Inicio de validez : <Inicio de validez>Válido hasta : <Fin de validez>Indicador de impuestos : <Indicador de impuestos> | Se actualiza el registro de condición para determinación de impuestos. |  |
| 13 | Grabar | Seleccionar Grabar . | Se guarda el registro de condición para determinación de impuestos. |  |

### Crear condiciones de precio

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear condiciones de precio - Compras (MEK1) . | Se abre la aplicación. |  |
| 3 | Tipo de condición de determinación de precios | Realice la siguiente entrada y pulse Intro :Clase de condición : por ejemplo, PPR0 | El Combinación de claves se visualiza la ventana de diálogo. |  |
| 4 | Combinación de claves | El Combinación de claves seleccione el pulsador Registro info de material Específico de centro) y seleccione Seleccionar . | El Crear condición de precio bruto predeterminado (PPR0): Rápido Entrada se visualiza. |  |
| 5 | Crear condición bruta predeterminada | El Crear condición de precio bruto estándar (PPR0): Entrada rápida , efectúe las siguientes entradas:Proveedor : <Proveedor>Material : <Material>Organización de compras : <Organización de compras>Centro : <Centro>Infotipo : por ejemplo, 0 EstándarCantidad : <Importe>Unidad : <Unidad de determinación de precio>Por : <Por cantidad>UM : <Unidad>Inicio de validez : <Inicio de validez>Vailid to : <Fin de validez> | Se actualiza el registro de condición bruto predeterminado. |  |
| 6 | Grabar | Seleccionar Grabar . | Se graba el registro de condición. |  |

### Modificar condiciones de precio

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Comprador . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Modificar condiciones de precio - Compras (MEK2) . | Se abre la aplicación. |  |
| 3 | Tipo de condición de determinación de precios | Realice la siguiente entrada y pulse Intro :Clase de condición : por ejemplo, PPR0 | El Combinación de claves se visualiza. |  |
| 4 | Combinación de claves | El Combinación de claves seleccione el pulsador Registro info de material (específico de centro) y seleccione Seleccionar . | El Crear condición de precio bruto estándar (PPR0): Entrada rápida se visualiza. |  |
| 5 | Modificar condición bruta predeterminada | El Modificar condición de precio bruto por defecto (PPR0): Entrada rápida , efectúe las siguientes entradas:Proveedor : <Proveedor>Material : <Material>Organización de compras : <Organización de compras>Centro : <Centro>Infotipo : por ejemplo, 0 EstándarSeleccionar Ejecutar .Realice la siguiente entrada:Cantidad : <Importe> | Se modifica el registro de condición bruto predeterminado. |  |
| 6 | Grabar | Seleccionar Grabar . | Se graba el registro de condición. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-277]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-279]]
- related-to :: [[04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 15,126 chars in the whole document
