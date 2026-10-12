---
id: 13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552
title: Crear registro info de calidad - MDS (BF5) (BF5_S4CLD2608_Master_Data_ES_XX)
description: "Spanish master data script (BF5) for SAP S/4HANA Cloud Public Edition: creating quality info records, QM control keys and first-sample (PAPF) options."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_ES_XX]
keywords: [Quality Info Records in Procurement, quality info record, qm control keys, production part approval, first sample inspection, quality planner role, vendor release, master data scripts, goods receipt inspection, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-552
topic: 13-quality-ehs-and-compliance/quality-info-records
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear registro info de calidad - MDS (BF5) (BF5_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear registro info de calidad - MDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894895)

[2 Requisitos previos 3](#_Toc233894896)

[2.1 Acceso al sistema 3](#_Toc233894897)

[2.2 Roles 3](#_Toc233894898)

[2.3 Unidades organizativas necesarias 3](#_Toc233894899)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894900)

[3 Tabla de resumen 5](#_Toc233894901)

[4 Procedimientos de prueba 6](#_Toc233894902)

[4.1 Crear registro info de calidad en aprovisionamiento 6](#_Toc233894903)

[4.2 Crear registro info de calidad para materiales sin registro info de calidad (opcional) 7](#_Toc233894904)

[4.3 Asignar claves de control QM para aprovisionamiento 8](#_Toc233894905)

[4.4 Crear opciones para PAPF 9](#_Toc233894906)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Si se requiere un acuerdo de gestión de calidad o una liberación de proveedor para un material, un planificador de calidad debe crear una información de calidad registro (registro info de calidad). El registro info de calidad determina cómo se puede seguir procesando el material.

Cuando se crea un pedido, el sistema verifica si se requiere un registro info de calidad y si está disponible para la combinación de material y proveedor.

El sistema también verifica si la combinación de proveedor y material-proveedor está bloqueada o liberada para ofertas, pedidos y/o entrada de mercancías. La ejecución de esta verificación depende de las opciones de QM en la clave de control de aprovisionamiento en el material maestro.

Además, puede asignar sistemas QM e iniciar una posible inspección en consecuencia. También puede determinar, de una entrada de mercancías se desencadena una inspección y/o una inspección de recepción. También puede indicar que se requiere un proceso de autorización de piezas de fabricación (PAPF) para las que puede planificar inspecciones de primera muestra (IPM) en el registro info de calidad. Puede gestionar el PAPF aquí actualizando el PAPF Estado y código de valoración (basado en la decisión de empleo tomada). Además, puede asignar varios pedidos/posiciones a la vez para PAPF a realizar inspección de primer artículo (FAI).

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
| Planificador de calidad | SAP_BR_QUALITY_PLANNER | Planificación de calidad | SAP_BR_QUALITY_PLANNER |  |

Para obtener más información sobre los roles empresariales, consulte Asignación de roles empresariales a un usuario en la Guía de administración para la implementación de SAP S/4HANA Cloud Public Edición .

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de cliente dependen de las unidades organizativas de la empresa, los datos generales (centrales) no dependen de una unidad organizativa o de la empresa código. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Registro info de calidad | Centro |  | Pueden existir datos de centro para cada ID de centro de su empresa Estructura para la que se utiliza el registro maestro de materiales. | Centro: |

### Datos maestros obligatorios y opcionales

Los registros de datos de gestión de calidad pueden hacer referencia a otros datos maestros. La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en una información de calidad registro.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Maestro de materiales |  | Obligatorio | Con vista de gestión de calidad. Para obtener más información, consulte los datos maestros script, Creación de atributos de gestión de calidad para maestro de materiales/productos - MDS (BNY). |
| Maestro de proveedores |  | Obligatorio |  |

|  |
| --- |
| Nota Un registro info de calidad es necesario si la clave de aprovisionamiento QM requiere una liberación de proveedor. En este caso, para cada combinación de proveedor-material, una Calidad Se debe crear el registro info. |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear registro info de calidad en aprovisionamiento](#unique_8) [página ] 6 | Planificador de calidad | Crear registro info de calidad - Aprovisionamiento (QI01) | Se crea un registro info de calidad. |
| [Crear registro info de calidad para materiales sin registro info de calidad (opcional)](#unique_9) [página ] 7 | Planificador de calidad | Gestionar registros info de calidad (F2256A) | Se crea un registro info de calidad. |
| [Asignar claves de control QM para aprovisionamiento](#unique_10) [página ] 8 | Planificador de calidad | Asignar claves de control QM para aprovisionamiento - Procesar manualmente (QI05) | Se crea un registro info de calidad. |
| [Crear opciones para PAPF](#unique_11) [página ] 9 | Planificador de calidad | Gestionar registros info de calidad (F2256A) | Se crea un registro info de calidad. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear registro info de calidad en aprovisionamiento

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear registro info de calidad - Aprovisionamiento (QI01) . | El Crear registro info de calidad se visualiza. |  |
| 3 | Introducir datos generales | Realice las siguientes entradas:Material : <número de material>Proveedor : <código de proveedor>Centro : <código de centro>Seleccionar Continuar . |  |  |
| 4 | Introducir datos de liberación | En la Liberar introduzca los siguientes datos:Liberar hasta : fecha en el futuro, por ejemplo, en un añoOpcional:La cantidad de liberación está activa : marcadoCantidad de liberación : por ejemplo, 15 |  |  |
| 5 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

|  |
| --- |
| Nota En el registro info de calidad, también puede decidir si desea desactivar la inspección de entrada de mercancías o realizar una inspección de entrada y/o inspección de recepción. Para ello, seleccione la Control de inspección e introduzca los siguientes datos:Si desea realizar una inspección de recepción además de una inspección de entrada de mercancías, introduzca una clase de inspección para el inspección de recepción y un ciclo de fabricación en días.Si no desea realizar una inspección de entrada de mercancías aunque las opciones en el maestro de materiales especifiquen un inspección, fije el Sin inspección indicador.Si desea realizar una inspección de recepción en lugar de una inspección de entrada de mercancías, fije el indicador relevante.Si este indicador está fijado, el sistema no creará ningún lote de inspección para una entrada de mercancías si la inspección de recepción ejecutado. Si no se realiza ninguna inspección de recepción, se genera un lote de inspección para la entrada de mercancías.En el Control de inspección también puede introducir lo siguiente:Sistema QM del proveedorSi el proveedor tiene un sistema de gestión de calidad, aquí puede almacenar la descripción del sistema de gestión de calidad para este material específico.Aprobación de piezas de producciónPuede especificar que se requiere un proceso de aprobación de piezas de fabricación. Debe realizar más opciones para ello en el Gestionar registros info de calidad (F2256A) Aplicación (véase el capítulo) [Asignar claves de control QM para aprovisionamiento](#unique_10) [página ] 8). |

### Crear registro info de calidad para materiales sin registro info de calidad (opcional)

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de calidad (F2256A) . |  |  |
| 3 | Crear registro info de calidad (opcional) | Seleccionar Crear en la esquina superior derecha de la tabla de resultados y actualizar los siguientes datos en el Cabecera nivel:Material : material númeroProveedor : proveedor códigoCentro : centro códigoPara el Liberar consulte el capítulo anterior, paso 4. |  |  |
| 4 | Guardar los datos | Seleccionar Crear . | Sus datos se han grabado y se ha creado un nuevo registro info de calidad. |  |

### Asignar claves de control QM para aprovisionamiento

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Asignar claves de control QM para aprovisionamiento - Procesar manualmente (QI05). |  |  |
| 3 | Asignar clave de control QM | Puede ejecutar esta selección a nivel de centro y/o material. Seleccionar la clave de control QM a asignar.Material : material númeroCentro : centro códigoClave de control QM : GC Clave de controlImplementar modificación de base de datos : activo (si este indicador no está fijado, sólo se ejecuta una ejecución de test)Nota Solo aquellos materiales, en los que QM activo aprovis. está fijado en los datos maestros de material, seleccionado. |  |  |

### Crear opciones para PAPF

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Se consigue una inspección de primera muestra utilizando el modelo EM de utilización de plan de inspección dedicado Inspección, que está asignada a las siguientes claves de control para QM en Aprovisionamiento:

- 0001 Liberación de proveedor
- 9001 Liberación de proveedor (con mensaje de error)

En detalle, se deben cumplir las siguientes condiciones para que una inspección de primera muestra ejecutado:

- Existe un plan de inspección con la utilización Inspección de modelo de EM (51) para inspección de artículo.
- Una de las claves de control QM enumeradas anteriormente está asignada al material.
- Para este material existe un registro info de calidad con las siguientes opciones: bajo Aprobación de pieza de producción :
    - La aprobación de piezas de fabricación está activada y el nivel de PAPF y el PAPF se fija el status.
    - Se ha introducido al menos un pedido y una posición de pedido.

En la entrada de mercancías para la posición de pedido, se crea un lote de inspección para el primer artículo inspección. Para este lote de inspección, la utilización del plan IPM de la clave de control QM es tomado y la utilización actualizada para la clase de inspección.

Procedimiento

Puede activar el PAPF en Gestionar registros info de calidad (F2256A) aplicación. Aquí puedes especifique para un material que se debe realizar una inspección de primera muestra en las mercancías entrada para una o varias posiciones de pedido.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar registros info de calidad (F2256A) . |  |  |
| 3 | Crear registro info de calidad | Seleccionar Crear en la esquina superior derecha de la tabla de resultados y actualizar los siguientes datos en el Cabecera nivel:Material : número de materialProveedor : código de proveedorCentro : código de centroPara el Liberar consulte el paso 4 en la sección anterior capítulo.Como alternativa, seleccione un registro info de calidad existente para activar el PAPF. |  |  |
| 4 | Introducir datos de autorización de pieza de fabricación | Ir al Aprobación de pieza de producción Sección . Seleccione Activar .Asigne el nivel de PAPF correspondiente en el Nivel PAPF campo. |  |  |
| 5 | Guardar los datos | Seleccionar Crear . | Sus datos se han grabado y se ha creado un nuevo registro info de calidad. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551]]
- related-to :: [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-553]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-555]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 19,083 chars in the whole document
