---
id: 11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696
title: Crear nuevo período contable MM abierto - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data script BNZ: close MM period and open a new material-management posting period via Cerrar períodos (MMPV), SAP S/4HANA C"
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_ES_XX]
keywords: [MM Posting Periods, mm posting period, period closing, material master records, business roles, fiori launchpad, test procedures, BNZ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-696
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear nuevo período contable MM abierto - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear nuevo período contable MM abierto - MDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895069)

[2 Requisitos previos 3](#_Toc233895070)

[2.1 Acceso al sistema 3](#_Toc233895071)

[2.2 Roles 3](#_Toc233895072)

[3 Tabla de resumen 4](#_Toc233895073)

[4 Procedimientos de prueba 5](#_Toc233895074)

[4.1 Período de cierre MM y apertura de nuevo período contable 5](#_Toc233895075)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Información sobre el stock de material y determinados datos de valoración, como el valor total de stock, el stock total, la clase de elementos de evaluación, el precio El indicador de control y la unidad de precio se mantienen en el período contable financiero. El período debe configurarse al principio de cada nueva contabilización. período para garantizar que los valores y el movimiento de mercancías se contabilicen en el período correcto. Normalmente, solo el período contable actual está abierto para contabilización. Todos los demás períodos contables están cerrados.

Una contabilización retroactiva en un período anterior solo es posible si el indicador correspondiente está fijado en el registro de gestión. Este indicador es automático fijado en la inicialización y después de cada cambio de período. Sin embargo, en algunos casos puede ser necesario fijar el indicador manualmente.

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

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Período de cierre MM y apertura de nuevo período contable](#unique_6) [página ] 5 | Especialista en datos maestros - Datos de producto | Cerrar períodos (MMPV) | El período contable está actualizado. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Período de cierre MM y apertura de nuevo período contable

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Cerrar períodos (MMPV) .Nota Si no puede encontrar el Cerrar períodos de la lista desplegable en la parte superior derecha de Fiori Launchpad, seleccionar Catálogo de mosaicos . En la sección Datos maestros: Administración grupo, navegar al Cerrar períodos y añádalo al Mi página de inicio grupo. | Se abre la aplicación. |  |
| 3 | Introducir datos de selección | El Cerrar período para maestro de materiales Registros , efectúe las siguientes entradas:De sociedad : <Su sociedad>A sociedad : <Su sociedad>Período : <Período para abrir>Ejercicio fiscal : <Ejercicio en curso>Verificar y cerrar período : SeleccionadoNota En la Período introduzca un número de dos dígitos para el mes. Por ejemplo, enero equivale a 01 , octubre es igual a 10 , etc.Si desea abrir el período actual, introduzca el mes actual en los períodos siguientes. |  |  |
| 4 | Seleccione Ejecutar. | El Cerrar período para registros maestros de materiales seleccione Ejecutar . |  |  |
| 5 | Resultado de verificación | Si un log muestra que El período actual (mes/año) del registro de gestión es <período/año que ha introducido> , usted puede detenerse aquí.Nota Si el período contable aún se encuentra en el pasado, repita los pasos anteriores período a período hasta alcanzar el correcto (actual). Para ejemplo, el período visualizado es 04 2014 , pero desea abrir la 12 2015 período, no puede hacerlo directamente. En su lugar, debe abrir la 05 2014 período siguiente y, a continuación, 06 2014 , etc. hasta que alcance el actual período. Si desea cerrar períodos de inventario en el año anterior, es posible que aparezca un mensaje del sistema en Paso 3 que indica que está abriendo/cerrando un período en el año pasado. Debe confirmar este sistema mensaje. | El período contable está actualizado. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695]]
- related-to :: [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-bnz-699]]
- related-to :: [[11-inventory-warehouse-and-transportation/mm-mds-bnz-697]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 9,709 chars in the whole document
