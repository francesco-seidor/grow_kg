---
id: 03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684
title: Crear mandato SEPA - MDS (BNV) (BNV_S4CLD2608_Master_Data_ES_XX)
description: "Spanish master data script (BNV) for creating, displaying, listing and managing SEPA direct debit mandates in SAP S/4HANA Cloud Public Edition, dated 02-07-26."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_ES_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, create sepa mandate, display sepa mandates, sepa mandate list, manage sepa mandates, business roles, organizational units, master data scripts, BNV]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-684
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear mandato SEPA - MDS (BNV) (BNV_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear mandato SEPA - MDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895038)

[2 Requisitos previos 3](#_Toc233895039)

[2.1 Acceso al sistema 3](#_Toc233895040)

[2.2 Roles 3](#_Toc233895041)

[2.3 Unidades organizativas necesarias 3](#_Toc233895042)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895043)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233895044)

[3 Tabla de resumen 5](#_Toc233895045)

[4 Procedimientos de prueba 6](#_Toc233895046)

[4.1 Crear mandatos SEPA 6](#_Toc233895047)

[4.2 Visualizar mandatos SEPA 7](#_Toc233895048)

[4.3 Visualizar listas de mandatos SEPA 8](#_Toc233895049)

[4.4 Gestionar mandatos SEPA 9](#_Toc233895050)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un mandato de la Zona Única de Pagos en Euros (SEPA) para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye los segmentos de datos que son relevantes para el SAP S/4HANA Cloud Public Edición aplicación. Campos que no son relevantes para el alcance de SAP S/4HANA Cloud Public Edición tal y como lo entrega SAP Best Practices no se describen en este documento.

El deudor completa un mandato SEPA (un cliente que compra mercancías o servicios) para autorizar al acreedor (un minorista o un servicio) proveedor) para cobrar pagos mediante débito directo SEPA. Al mismo tiempo, el mandato SEPA incluye la autorización del banco deudor para pagar estos cobros.

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
| Contable de deudores | SAP_BR_AR_ACCOUNTANT | Contabilidad de deudores | SAP_BR_AR_ACCOUNTANT |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de cliente dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Mandato | Interlocutor comercial | Número de cliente, IBAN y SWIFT/BIC | Solo válido para clientes europeos con SEPA directo Debe. | Número de cliente: <su número |
| Mandato | Sociedad | Sociedad | Pueden existir datos de sociedad para cada ID de sociedad de su Estructura de la empresa para la que se utiliza el mandato SEPA. | Sociedad: su código |

### Datos maestros obligatorios y opcionales

La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios utilizado en un registro de datos maestros de centro de beneficio.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Número de cliente | Pantalla inicial | Obligatorio |  |
| Sociedad | Pantalla inicial | Obligatorio |  |

### Parámetros principales para la creación de datos

Esta sección describe algunos parámetros básicos que afectan al comportamiento de un registro maestro y que siempre son necesarios para crear un SEPA. mandato:

Sociedad:

Por ejemplo, XX10 .

Interlocutor comercial - Deudor:

Por ejemplo, número de cliente XX100003 .

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación SAP Fiori / Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear mandatos SEPA](#unique_9) [página ] 6 | Contable de deudores | Crear mandatos SEPA (FSEPA_M1) | Se ha creado el mandato SEPA. |
| [Visualizar mandatos SEPA](#unique_10) [página ] 7 | Contable de deudores | Visualizar mandatos SEPA (FSEPA_M3) | Se visualiza el mandato SEPA. |
| [Visualizar listas de mandatos SEPA](#unique_11) [página ] 8 | Contable de deudores | Visualizar listas de mandatos SEPA (FSEPA_M4) | Se visualiza la lista de mandatos SEPA. |
| [Gestionar mandatos SEPA](#unique_12) [página ] 9 | Contable de deudores | Gestionar mandatos SEPA (F5158) | Se visualiza el mandato SEPA. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear mandatos SEPA

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de deudores . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear mandatos SEPA (FSEPA_M1) . | Se abre la aplicación. |  |
| 3 | Cambiar aplicación | El Crear mandato: Acceso , seleccione Cambiar aplicación. Seleccionar finanzas Contabilidad en el Seleccionar aplicación y seleccione Continuar . |  |  |
| 4 | ID de pagador | En la Cliente , introduzca XX100003 . |  |  |
| 5 | ID de receptor del pago | En la Sociedad pagadora , introduzca XX10 y pulse Intro para continuar.Nota Si se visualiza una pantalla de mandatos con un estado activado, significa que esos mandatos ya se han creado. Marque un mandato y seleccione Continuar para verificar y modificar el mandato. | El Crear mandato: Imagen detallada se visualiza. |  |
| 6 | Completar datos | Seleccionar Completar datos . | Los campos se rellenan automáticamente. |  |
| 7 | Datos básicos | El Datos básicos , efectúe las siguientes entradas:Estado : IntroducidoCasilla de selección Mandato B2B : SeleccionarUbicación de firma : <Ubicación>Fecha de firma : <Fecha> |  |  |
| 8 | Pagador | El Pagador en la pestaña Datos bancarios del pagador verifique que la IBAN y SWIFT/BIC Se han rellenado campos.Nota Estos datos forman parte de sus datos maestros de cliente y ya debería estar creado y disponible. |  |  |
| 9 | Receptor del pago | El Receptor del pago , realice la siguiente entrada:ID de acreedor : <ID de acreedor> |  |  |
| 10 | Guardar los datos | Guarde las entradas. | El mensaje del sistema Mandato 0000000000## creado muestra. |  |

### Visualizar mandatos SEPA

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Ya existe un mandato.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de deudores . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Visualizar mandatos SEPA (FSEPA_M3) . | Se abre la aplicación. |  |
| 3 | ID de pagador | En la Cliente , introduzca XX100003 . |  |  |
| 4 | ID de receptor del pago | En la Sociedad pagadora , introduzca XX10 y pulse Intro para continuar. | El Visualizar mandato: Imagen detallada se visualiza. |  |
| 5 | Navegación | Seleccione las diferentes pestañas:Datos básicos , Pagador , y/o Receptor del pago . | Se muestra la información. |  |
| 6 | Volver | Seleccionar Salir . |  |  |

### Visualizar listas de mandatos SEPA

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Ya existe un mandato.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de deudores . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Visualizar listas de mandatos SEPA (FSEPA_M4) . | Se abre la aplicación. |  |
| 3 | Seleccione Ejecutar. | Si aparece una ventana de diálogo, seleccione Financiero Contabilidad en el Seleccionar Aplicación y, a continuación, seleccione Continuar .Si no aparece ninguna ventana de diálogo, verifique la Técnico Selecciones y verifique que el Aplicación El campo está fijado en Gestión financiera .Seleccionar Ejecutar . | El Mandatos Se abre la pantalla, que muestra una lista de mandatos existentes. |  |
| 4 | Seleccionar un mandato | Seleccione un Número de referencia de mandato . | El Modificar mandatos muestra los detalles de la lista del mandato seleccionado. |  |
| 5 | Revisar | Aunque es posible modificar los datos del mandato cuando sea necesario, no modifique ningún dato y solo revise los datos del mandato. |  |  |
| 6 | Salir | Seleccionar Continuar dos veces o seleccione Cancelar para salir. |  |  |

### Gestionar mandatos SEPA

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Ya existe un mandato.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de deudores . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar mandatos SEPA (F5158) . | Se abre la aplicación. |  |
| 3 | Seleccionar mandato | En la Aplicación , seleccione Financiero Contabilidad . |  |  |
| 4 | Seleccionar mandato | En la Sociedad pagadora , introduzca XX10 .Seleccionar Ir .Seleccione la línea que desea editar y seleccione Editar . | El Modificar mandato: Detalle se visualiza. |  |
| 5 | Revisar y editar | Revise y edite cualquiera de los campos disponibles de las siguientes pestañas:Datos básicosPagadorReceptor del pago |  |  |
| 6 | Grabe sus entradas | Seleccionar Grabar para guardar sus entradas. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]
- related-to :: [[03-financial-accounting-and-close/sepa-mds-bnv-685]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 15,797 chars in the whole document
