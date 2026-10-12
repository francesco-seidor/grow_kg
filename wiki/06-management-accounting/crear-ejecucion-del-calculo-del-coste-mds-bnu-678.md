---
id: 06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678
title: Crear ejecución del cálculo del coste - MDS (BNU) (BNU_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script BNU: creating and executing a product cost estimate run with variant PYC1."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_ES_XX]
keywords: [Product Costing Runs and Standard Cost Updates, costing run, product cost estimate, costing variant, price update, organizational units, master data prerequisites, inventory accountant role, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-678
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear ejecución del cálculo del coste - MDS (BNU) (BNU_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear ejecución del cálculo del coste - MDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895051)

[2 Requisitos previos 3](#_Toc233895052)

[2.1 Acceso al sistema 3](#_Toc233895053)

[2.2 Roles 3](#_Toc233895054)

[2.3 Unidades organizativas necesarias 3](#_Toc233895055)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895056)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233895057)

[2.5.1 Variante de cálculo del coste 4](#_Toc233895058)

[3 Tabla de resumen 6](#_Toc233895059)

[4 Procedimientos de prueba 7](#_Toc233895060)

[4.1 Crear ejecución del cálculo del coste 7](#_Toc233895061)

[4.2 Efectuar ejecución del cálculo del coste 8](#_Toc233895062)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Este documento contiene pasos de proceso que se deben realizar como requisito previo antes de poder empezar a trabajar con los scripts de test estándar de los escenarios de logística seleccionados.

En este documento encontrará una descripción de cómo crear y ejecutar un cálculo del coste del producto. para materiales utilizados en su empresa / centro. El objetivo es planificar costes para materiales sin referencia a pedidos y precios fijados para materiales y otros costes objetos contables.

Puede utilizar la planificación de costes del producto para analizar los costes de los productos de su empresa, como como:

- Materiales fabricados
- Servicios
- Otros bienes intangibles

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
| Contable de costes - Inventario | SAP_BR_INVENTORY_ACCOUNTANT | Contabilidad de existencias | SAP_BR_INVENTORY_ACCOUNTANT |  |

### Unidades organizativas necesarias

Para crear una ejecución del cálculo del coste, debe especificar la Sociedad CO y el Sociedad .

|  |
| --- |
| Nota En la Unidad organizativa a utilizar introduzca su valor para el segmento de datos que es relevante para su entorno de sistema. Para la sociedad : por ejemplo, 10 = Alemania, 17 = EE.UU. |

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos del cálculo del coste | Sociedad CO |  |  | Sociedad CO:____________ |
|  | Sociedad |  |  | Sociedad:__________ |
| Selección | Centro |  |  | Centro:__________ |

### Datos maestros obligatorios y opcionales

Los registros de datos de la lista de materiales pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de objetos de datos maestros opcionales y obligatorios que se deben utilizar en una lista de materiales.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Materiales | Crear cálculo del coste > Etapa del flujo > Selección | Obligatorio | Normalmente, se especifican los tipos de material para indicar para qué materiales, la ejecución del cálculo del coste debe crear un cálculo del coste del producto. |
| Datos maestros de producción (lista de materiales, hoja de ruta, puesto de trabajo, etc.). | En la Crear cálculo del coste Etapa de flujo Estructura Desglose | Opcional (o) Obligatorio | En caso de que se utilicen productos fabricados en la ejecución del cálculo del coste (para ejemplo, productos del tipo de material "FERT" (productos terminados) o "HALB" (Productos semielaborados), estos productos tienen una lista de materiales que "desglosado" en la ejecución del cálculo del coste.Al mismo tiempo, la(s) hoja(s) de ruta está(n) seleccionados. Datos adicionales de centros de trabajo, centros de coste asignados y clases de actividad utilizadas, junto con las tasas de coste se determinan para calculando los datos del postcálculo del coste. |

### Parámetros principales para la creación de datos

En esta sección se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear una lista de materiales:

#### Variante de cálculo del coste

La variante de cálculo del coste define un enlace entre la aplicación y el Customizing, ya que todos los costes Los cálculos se llevan a cabo y se graban con referencia a una variante de cálculo del coste.

| Variante de cálculo del coste | Descripción | Comentario |
| --- | --- | --- |
| PYC1 | Cálculo del coste estándar | Esta variante de cálculo del coste se utiliza para crear cálculos del coste del producto estándar para los materiales. En función del resultado, los datos de valoración de material se actualizado. |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Nombre de transacción/aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear ejecución del cálculo del coste](#unique_10) [página ] 7 | Contable de costes - Inventario | Gestionar ejecuciones de cálculo del coste - Costes estimados (F1865) | Se visualizan los datos de cabecera con la etiqueta de datos de cálculo del coste. |
| [Efectuar ejecución del cálculo del coste](#unique_11) [página ] 8 | Contable de costes - Inventario | Gestionar ejecuciones de cálculo del coste - Costes estimados (F1865) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear ejecución del cálculo del coste

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad se crea una ejecución del cálculo del coste.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Inventario . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar ejecuciones de cálculo del coste - Costes estimados (F1865) . | El Gestionar ejecuciones de cálculo del coste Costes estimados se visualiza. |  |
| 3 | Creación de ejecución del cálculo del coste | Seleccionar Crear . | El Crear nueva ejecución del cálculo del coste se visualiza. |  |
| 4 | Introducir parámetros para ejecución del cálculo del coste | Realice las siguientes entradas y pulse Intro .Ejecución del cálculo del coste : Test1Fecha de ejecución del cálculo del coste : <Indique la fecha actual>Descripción : Test de ejecución del cálculo del coste 1Variante de cálculo del coste : PYC1Versión del cálculo del coste : 1Sociedad CO : A000Sociedad : 1010Fecha de inicio del cálculo del coste : <Fecha actual>Fecha de fin de cálculo del coste : Tomar valor propuestoFecha de estructura cuantitativa : <Fecha actual>Fecha de valoración : <Fecha actual> |  |  |
| 5 | Grabar ejecución del cálculo del coste | Seleccionar Grabar . |  |  |

### Efectuar ejecución del cálculo del coste

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, se realiza la ejecución del cálculo del coste. Los materiales configurados no se incluyen.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Inventario . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar ejecuciones de cálculo del coste - Costes estimados (F1865) . | El Gestionar ejecuciones de cálculo del coste Costes estimados se visualiza. |  |
| 3 | Seleccionar ejecución del cálculo del coste | Busque la ejecución del cálculo del coste creada en el paso anterior y haga clic en entrada y seleccione Editar para acceder a los detalles de la ejecución del cálculo del coste. |  |  |
| 4 | Abrir ejecución del cálculo del coste | Realice la siguiente entrada:Ejecución del cálculo del coste : Introduzca la ejecución del cálculo del coste creada en el paso anterior y seleccione Intro .Expanda la Procesando sección. |  |  |
| 5 | Crear cálculos del coste | En la Procesando tabla, para cada fila, hay un Modificar parámetro en el botón Parámetros columna. Seleccione el de la línea de selección y efectúe las siguientes entradas:Tipo de material : HALB, ROH, FERTCentro : 1010Desmarcar Ejecución en proceso de fondo y seleccione una opción EXPLO .Grabe sus entradas y seleccione Volver .Seleccionar Ejecutar , que se muestra en el Ejecutar y el semáforo de estado de la fila Selección se vuelve verde. | Se ejecuta la selección. |  |
| 6 | Crear cálculos del coste | Para el Cálculo de costes fila, seleccione la Modificar parámetro botón. En el botón Ejecución del cálculo del coste: Cálculo del coste - Modificar parámetros , desmarque Ejecución en proceso de fondo y, a continuación, seleccione Grabar .Seleccionar VolverSeleccionar Ejecutar , que se muestra en el Ejecutar y el semáforo de estado de la fila Cálculo de costes se vuelve verde. | Ejecución del cálculo del coste. |  |
| 7 | Crear cálculos del coste | En el menú, seleccione Editar > Resultados del cálculo del coste .Si la luz de estado de esta fila está en rojo, revise el informe Niveles de cálculo del coste. Corrija los errores en el informe. Para volver a ejecutar el cálculo del coste (si es necesario), repita los pasos para Estruct. Líneas de desglose y cálculo del coste. | Ejecución del cálculo del coste. |  |
| 8 | Crear cálculos del coste | El Análisis fila, seleccione la Modificar parámetro botón. Seleccionar SAP&11 para la configuración de parámetros. En la Ejecución del cálculo del coste: Análisis - Modificar parámetros , desmarque Ejecución en proceso de fondo y, a continuación, seleccione Grabar .Seleccionar Volver .Seleccionar Ejecutar , que se muestra en el Ejecutar columna. | Ejecución del cálculo del coste. |  |
| 9 | Crear cálculos del coste | El Marca fila, seleccione la Bloquear botón.El Actualización de precio: Organizativo Medida , seleccione el botón de selección Empresa Código : 1010 .En la ventana de diálogo que aparece, introduzca la variante de cálculo del coste de PYC1 y la versión del cálculo del coste de 1 y, a continuación, seleccione Intro . La luz de estado de la fila gira verde.Seleccionar Volver .Seleccionar Modif. Parámetro y anule la selección Proceso de fondo Procesando .Seleccionar Grabar .Seleccionar Volver , y seleccione Ejecutar . | Ejecución del cálculo del coste. |  |
| 10 | Crear cálculos del coste | El Liberar fila , seleccione Modificar parámetro y anule la selección Ejecución de test y Ejecución en proceso de fondo .Seleccionar Grabar .Seleccionar Volver y seleccione Ejecutar . | Los precios actuales se actualizarán en los datos maestros de material. |  |

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
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]
- related-to :: [[06-management-accounting/mds-bnu-679]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 16,304 chars in the whole document
