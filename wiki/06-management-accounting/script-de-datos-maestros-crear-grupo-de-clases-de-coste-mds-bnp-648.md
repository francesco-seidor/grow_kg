---
id: 06-management-accounting/script-de-datos-maestros-crear-grupo-de-clases-de-coste-mds-bnp-648
title: "Script de datos maestros: Crear grupo de clases de coste - MDS (BNP) (BNP_S4CLD2608_Master_Data_ES_XX)"
description: Spanish (machine-translated) master data script BNP for creating cost element groups in SAP S/4HANA Cloud Public via app Gestionar grupos de clases de coste (F5373).
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_ES_XX]
keywords: [Cost Element Groups, master data scripts, overhead cost accounting, business roles, test scripts, cost reporting, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-648
topic: 06-management-accounting/cost-element-groups
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear grupo de clases de coste - MDS (BNP) (BNP_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear grupo de clases de coste - MDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894987)

[2 Requisitos previos 3](#_Toc233894988)

[2.1 Acceso al sistema 3](#_Toc233894989)

[2.2 Roles 3](#_Toc233894990)

[2.3 Unidades organizativas necesarias 3](#_Toc233894991)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894992)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894993)

[3 Tabla de resumen 5](#_Toc233894994)

[4 Procedimientos de prueba 6](#_Toc233894995)

[4.1 Creación de datos maestros de grupo de clases de coste 6](#_Toc233894996)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Contexto empresarial

Los grupos de clases de coste se suelen utilizar para agrupar clases de coste con clases de coste similares características para la presentación de informes. Los grupos de clases de coste se pueden utilizar en el sistema de información, por ejemplo. Puede utilizar la estructura del grupo de clases de coste para defina la estructura de filas de sus informes. Los totales se calculan en el informe para cada nodo.

También puede utilizar grupos de clases de coste siempre que desee procesar varios costes elementos en una transacción. Por ejemplo, en la planificación de centros de coste, la distribución o evaluación.

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
| Contable de costes - Gastos generales | SAP_BR_OVERHEAD_ACCOUNTANT | Contabilidad de gastos generales | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se crearon en el sistema ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan grupos de clases de coste, dependiendo del enfoque operativo de su empresa.

| Objeto de datos | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad CO | Datos generales | Obligatorio |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros del grupo de clases de coste pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un registro de datos de grupo de clases de coste.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Plan de cuentas | Unidades organizativas | Opcional |  |

### Parámetros principales para la creación de datos

Este elemento de alcance no tiene condiciones empresariales.

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de grupo de clases de coste](#unique_9) [página ] 6 | Contable de costes - Gastos generales | Gestionar grupos de clases de coste (F5373) | Los grupos de clases de coste se pueden crear según las nuevas necesidades empresariales. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de datos maestros de grupo de clases de coste

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Ha introducido y grabado los datos básicos para el material.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar grupos de clases de coste (F5373) . | Se abre la aplicación. |  |
| 3 | Introducir nuevo grupo de clases de coste | El Gestionar grupos de clases de coste , seleccione Crear . En el campo Crear clase de coste Grupo: Acceso , realice la siguiente entrada:Grupo de clases de coste : <Coste Grupo de elementos>Pulsar Intro .Opcionalmente, puede seleccionar una referencia del centro de coste existente. Grupos. | El Crear grupo de clases de coste: Estructura pantalla muestra. |  |
| 4 | Introducir clase de coste y/o grupo de clases de coste | Se muestran nuevos datos maestros en el Grupo de clases de coste: Estructura Efectúe la siguiente entrada:Descripción : <Descripción>Además, puede realizar las siguientes entradas situando el cursor en su selección y utilizando los siguientes botones de navegación:Nivel inferior : <Insertar un coste Grupo de elementos en el nivel inferior>Clase de coste : <(Insertar opción) - Añadir clases de coste o intervalos de clases>Mismo nivel : <Insertar adicional Grupos de clases de coste en el mismo nivel inferior> | Se muestran nuevos datos maestros en el Grupo de clases de coste: Estructura pantalla. |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Se crea y graba el grupo de clases de coste. |  |

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
- related-to :: [[06-management-accounting/create-cost-element-group-mds-bnp-647]]
- related-to :: [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650]]
- related-to :: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]
- related-to :: [[06-management-accounting/mds-bnp-649]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 10,287 chars in the whole document
