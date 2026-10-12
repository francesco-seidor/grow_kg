---
id: 13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma
title: "Script de datos maestros: Crear atributos de gestión de calidad para maestro de materiales/productos - MDS (BNY) (BNY_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish (machine-translated) SAP S/4HANA Cloud master data script BNY: create quality management attributes in the material master via MM01."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_ES_XX]
keywords: [Quality Management View of the Material Master, quality management, material master, inspection setup, automatic usage decision, quality info record, master data scripts, business roles, organizational units, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-690
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear atributos de gestión de calidad para maestro de materiales/productos - MDS (BNY) (BNY_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear atributos de gestión de calidad para maestro de materiales/productos - MDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895094)

[2 Requisitos previos 3](#_Toc233895095)

[2.1 Acceso al sistema 3](#_Toc233895096)

[2.2 Roles 3](#_Toc233895097)

[2.3 Unidades organizativas necesarias 3](#_Toc233895098)

[3 Tabla de resumen 5](#_Toc233895099)

[4 Procedimientos de prueba 6](#_Toc233895100)

[4.1 Atributos de gestión de calidad para material 6](#_Toc233895101)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Si se supone que se debe inspeccionar la calidad del material, el requisito previo es que la calidad vista de gestión en el maestro de materiales se actualiza para el centro correspondiente.

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
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

En esta sección se describen y explican todas las unidades organizativas que son relevantes para crear los registros de datos maestros.

Algunos segmentos de datos maestros de cliente dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Gestión de calidad | Centro |  | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales. | Centro: |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Atributos de gestión de calidad para material](#unique_7) [página ] 6 | Especialista en datos maestros - Datos de producto | Crear material (MM01) | Datos maestros de material – Se crean datos de gestión de calidad. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Atributos de gestión de calidad para material

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear material (MM01) . | Se abre la aplicación. |  |
| 3 | Introducir datos de material | El Crear material (pantalla inicial) , efectúe las siguientes entradas:Material : <Material número>Tipo de material : Comercio MercancíasPulsar Intro . | El Seleccionar vista(s) se visualiza. |  |
| 4 | Seleccionar vista de gestión de calidad | El Seleccionar vista(s) , seleccione el botón de selección Calidad Gestión y seleccione Org. Niveles . | Aparece una nueva pantalla para la entrada de datos organizativos. |  |
| 5 | Introducir datos de niveles de organización | El Niveles de organización en la pantalla Niveles de organización , realice la siguiente entrada y seleccione Continuar :Centro : <Centro código> | El Crear material... (mercaderías) se visualiza. |  |
| 6 | Introducir datos de gestión de calidad | El Crear material <XXX> (Mercaderías) pantalla, en la pantalla Gestión de calidad introduzca la descripción del material:Descr. : <Introduzca la descripción>En la Datos generales sección, en la Gestión de calidad , realice la siguiente entrada:Unidad de medida base : <Unidad de medida>Seleccionar Config.insp. . En la ventana de diálogo que se visualiza, seleccione Crear clases de inspección y realice las siguientes entradas:Cl.insp. : Por ejemplo, 01 .Cl.insp.preferente : XActivo : XSeleccionar Det.cl.insp. para ver los detalles.Asegúrese de que los siguientes campos estén marcados con X :Contab.en stock insp.Inspección con hoja de rutaAsignación automáticaInspeccionar caract.Seleccionar Continuar . |  |  |
| 7 | Activar/Desactivar decisión de empleo automatizada (opcional) | Marcar o desmarcar DE automática para activar o desactivar la decisión de empleo automatizada para esta combinación de material y tipo de inspección.Nota Se puede tomar una decisión de empleo automática después de la entrada de resultados para lotes de inspección con resultados de inspección positivos. Para habilitar esto proceso, su sistema debe estar configurado de forma correspondiente en el Gestionar su solución (F1241) aplicación. Verifíquelo[Ayuda de SAP](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html) para obtener más información técnica y requisitos previos. |  |  |
| 8 | Introducir datos de aprovisionamiento (opcional) | Si desea utilizar opcionalmente un registro info de calidad para el material, en la Gestión de calidad en la pestaña Datos de aprovisionamiento sección, haga lo siguiente entradas:Aprov.QM activo : XClave de control QM : Por ejemplo, 0001 . |  |  |
| 9 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b]]
- related-to :: [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-691]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-693]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 10,743 chars in the whole document
