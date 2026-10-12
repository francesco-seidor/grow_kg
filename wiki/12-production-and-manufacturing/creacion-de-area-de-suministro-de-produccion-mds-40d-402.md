---
id: 12-production-and-manufacturing/creacion-de-area-de-suministro-de-produccion-mds-40d-402
title: Creación de área de suministro de producción - MDS (40D) (40D_S4CLD2608_Master_Data_ES_XX)
description: Spanish (machine-translated) SAP master data script for creating a production supply area via PK05S or F6935 in S/4HANA Cloud Public Edition 2608.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-supply-areas]
aliases: [40D_S4CLD2608_Master_Data_ES_XX]
keywords: [Production Supply Areas, production supply area, master data creation, business roles, mrp controller, plant and storage location, test procedures, 40D]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-402
topic: 12-production-and-manufacturing/production-supply-areas
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Creación de área de suministro de producción - MDS (40D) (40D_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Production Supply Areas** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de área de suministro de producción - MDS (40D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894736)

[2 Requisitos previos 3](#_Toc233894737)

[2.1 Acceso al sistema 3](#_Toc233894738)

[2.2 Roles 3](#_Toc233894739)

[2.3 Unidades organizativas necesarias 3](#_Toc233894740)

[2.4 Parámetros obligatorios y opcionales para la creación de datos 4](#_Toc233894741)

[3 Tabla de resumen 5](#_Toc233894742)

[4 Procedimientos de prueba 6](#_Toc233894743)

[4.1 Crear área de suministro de producción 6](#_Toc233894744)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear un área de suministro de producción para su SAP S/4HANA Cloud Public Edición sistema. La descripción incluye los segmentos de datos que son relevantes para el SAP S/4HANA Cloud Public Edición aplicación. Campos que no son relevantes para el alcance del SAP S/4HANA Cloud Public Edición contenido no se describen en este documento.

Un área de suministro de producción que se crea como se describe aquí se puede utilizar para la producción procesos.

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
| Planificador de producción - Fabricación mínima | SAP_BR_PRODN_PLNR_LEAN_MFG | Planificación de la producción - Fabricación mínima | SAP_BR_PRODN_PLNR_LEAN_MFG |  |

### Unidades organizativas necesarias

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Todos los datos | Centro |  | Todos los datos del área de suministro de producción dependen del centro. | Centro:__________ |
| Todos los datos | Almacén |  | Todos los datos para el área de suministro de producción dependen del almacenamiento ubicación. | Almacén:__________ |

### Parámetros obligatorios y opcionales para la creación de datos

Los registros del área de suministro de producción pueden hacer referencia a otros parámetros de entrada. La siguiente tabla proporciona un resumen de los parámetros de entrada opcionales y obligatorios que se utilizarán para crear un Área de suministro de producción.

| Objeto de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- |
| Responsable/Planificador de necesidades | Opcional | Responsable de una o varias áreas de suministro de producción |

## Tabla de resumen

Este elemento de alcance consta del paso del proceso enumerado en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear área de suministro de producción](#unique_8) [página ] 6 | Planificador de producción - Fabricación mínima | Área de suministro de producción - Entrada rápida (PK05S) o bien Gestionar áreas de suministro de producción (F6935) | Se ha creado el área de suministro de producción. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear área de suministro de producción

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

Opción 1:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de producción - Fabricación mínima . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Área de suministro de producción - Entrada rápida (PK05S) . | El Tratar vistas de tabla: Acceso muestra. |  |
| 3 | Introducir código de centro | El Determinar área de trabajo: Entrada introduzca el código de centro y seleccione Continuar . |  |  |
| 4 | Navegar a la pantalla Crear área de aprovisionamiento | Seleccionar Entradas nuevas . |  |  |
| 5 | Área de suministro | Introduzca los detalles del área de suministro de producción y pulse Intro .Área de suministro : <Área de suministro>Alm. : <Almacén>Res : <Un planificador de necesidades>Puesto de descarga : <"Puesto de descarga A">Nombre de área de suministro de producción : <Descripción del área de suministro de producción> |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . |  |  |
| 7 | Actualizar otros parámetros (opcional) | Puede introducir otros parámetros necesarios según un requisito específico. Por ejemplo:Actualice la dirección del área de suministro de producción mediante Más > Ir a > Dirección .Guarde las modificaciones. |  |  |

Opción 2:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/Fallido/Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de producción - Fabricación mínima . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar áreas de suministro de producción (F6935) . | Se abre la aplicación. |  |
| 3 | Crear | En la Áreas de suministro de producción sección, seleccione Crear . |  |  |
| 4 | Introducir datos | En la ventana de diálogo, efectúe las siguientes entradas y seleccione Continuar :Área de suministro de producción : <Área de suministro>Centro : <Centro>Almacén : <Almacén> |  |  |
| 5 | Introducir datos básicos | En la Datos básicos , realice las siguientes entradas:Persona responsable : <Un planificador de necesidades>Puesto de descarga : <"Puesto de descarga A"> |  |  |
| 6 | Introducir descripción | En la Descripción supeditada a clave de idioma , realice las siguientes entradas:Idioma : <Seleccione un código de idioma, por ejemplo, EN para inglés>Descripción : <Descripción del área de suministro de producción> |  |  |
| 7 | Guardar los datos | Seleccionar Crear . |  |  |
| 8 | Actualizar otros parámetros (opcional) | Puede introducir otros parámetros necesarios según un requisito específico. Por ejemplo:Actualice la dirección del área de suministro de producción mediante Crear dirección .Guarde las modificaciones. |  |  |

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
- related-to :: [[12-production-and-manufacturing/create-production-supply-area-mds-40d-401]]
- related-to :: [[12-production-and-manufacturing/criar-area-de-abastecimento-da-producao-mds-40d-404]]
- related-to :: [[12-production-and-manufacturing/mds-40d-403]]
- related-to :: [[12-production-and-manufacturing/mds-40d-405]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 11,224 chars in the whole document
