---
id: 12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b
title: Crear lista de materiales para material para producción y ventas - MDS (BNK) (BNK_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) master data test script (BNK) for creating change numbers, production BOMs and sales BOMs in SAP S/4HANA Cloud Public Edition 2608."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_ES_XX]
keywords: [Material BOMs for Production and Sales, bill of materials, production bom, sales bom, change number, bom usage, bom item categories, business roles, master data scripts, routing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-624
topic: 12-production-and-manufacturing/material-boms
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear lista de materiales para material para producción y ventas - MDS (BNK) (BNK_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear lista de materiales para material para producción y ventas - MDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894978)

[2 Requisitos previos 3](#_Toc233894979)

[2.1 Acceso al sistema 3](#_Toc233894980)

[2.2 Roles 3](#_Toc233894981)

[2.3 Unidades organizativas necesarias 3](#_Toc233894982)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894983)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894984)

[2.5.1 Utilización de lista de materiales 4](#_Toc233894985)

[3 Tabla de resumen 5](#_Toc233894986)

[4 Procedimientos de prueba 6](#_Toc233894987)

[4.1 Crear número de modificación 6](#_Toc233894988)

[4.2 Crear lista de materiales de producción 7](#_Toc233894989)

[4.3 Crear lista de materiales de ventas 9](#_Toc233894990)

[5 Apéndice 11](#_Toc233894991)

[5.1 Procesos siguientes: Crear hoja de ruta 11](#_Toc233894992)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Una lista de materiales de producción es una lista formalmente estructurada de los componentes que fabrican un producto o conjunto (parte de un producto). La lista contiene el número de objeto de cada componente, junto con la cantidad y la unidad de medida. Un componente puede ser un materia prima o material semielaborado que representa un conjunto.

Se utiliza en una ejecución de planificación para calcular las necesidades de material y en transacciones como un orden de fabricación. La información es específica de un sitio de producción (conocido como centro).

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
| Ingeniero de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC | Ingeniería de producción - Fabricación discreta | SAP_BR_PRODN_ENG_DISC |  |
| Responsable de listas de materiales | SAP_BR_BOM_ENGINEER | Listas de materiales | SAP_BR_BOM_ENGINEER |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se han creado en su durante la activación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan materiales, clientes y proveedores, por ejemplo, en función del enfoque operativo de su empresa.

Utilice sus propios datos maestros o los siguientes datos de muestra para pasar por el test procedimiento.

### Datos maestros obligatorios y opcionales

Los registros de datos de la lista de materiales pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de objetos de datos maestros opcionales y obligatorios que se deben utilizar en una lista de materiales

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Material | En la Crear lista de materiales para material: Acceso y Crear Lista de materiales para material: Vista de posición general, introduzca Número de material en Material y componente . | Obligatorio | Complete los siguientes scripts de datos maestros como requisito previo antes de iniciar el proceso Pasos:Creación de maestro de productos de tipo "Materia prima" - MDS (BNR)Creación de maestro de productos de tipo "Producto semielaborado" - MDS (BNS)Creación de maestro de productos de tipo "Producto terminado" - MDS (BNT)Creación de maestro de productos de tipo "Mercadería" - MDS (BNF) |

### Parámetros principales para la creación de datos

En esta sección se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear una lista de materiales:

#### Utilización de lista de materiales

La utilización de la lista de materiales (LMat) define el área (como Ventas o Producción) donde un material Se puede utilizar la lista de materiales.

| Utilización de lista de materiales | Descripción |
| --- | --- |
| 1 | Producción |
| 5 | Comercial |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear número de modificación](#unique_10) [página ] 6 | Responsable de listas de materiales | Crear registro maestro de modificación (CC01) |  |
| [Crear lista de materiales de producción](#unique_11) [página ] 7 | Ingeniero de producción - Fabricación discreta | Actualizar lista de materiales (versión 2) - Crear, modificar y visualizar listas de materiales (F1813A) |  |
| [Crear lista de materiales de ventas](#unique_12) [página ] 9 | Ingeniero de producción - Fabricación discreta | Actualizar lista de materiales - Crear, modificar y visualizar listas de materiales (F1813) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear número de modificación

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Creación del registro maestro de modificación que se utilizará para la creación de la lista de materiales en los siguientes pasos de producción y lista de materiales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Responsable de listas de materiales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear registro maestro de modificación (CC01) . |  |  |
| 3 | Introducir número de modificación | El Crear registro maestro de modificación: Acceso , introduzca los siguientes datos y pulse Intro .Número de modificación : <Introduzca su número de modificación, por ejemplo:CN001>Deje los valores predeterminados en otros campos. |  |  |
| 4 | Introducir datos maestros de modificación | El Crear registro maestro de modificación: Cabecera de modificación , introduzca los datos tal como se proporcionan en el siguiente ejemplo y pulse Intro :Campo al lado Número de modificación : Maestro de modificaciones para lista de materiales de fabricaciónInicio de validez : HoyStatus núm.modif. : 01 Activo |  |  |
| 5 | Marque las casillas de selección de la lista de materiales | El Crear registro maestro de modificación: Tipos de objeto pantalla, Tipos de objeto tabla, Lista de materiales fila, marque las siguientes casillas de selección:Act.ObjetoReg.gest. |  |  |
| 6 | Seleccione Guardar. | Seleccionar Grabar . | Se crea el registro maestro de modificación. |  |

### Crear lista de materiales de producción

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar lista de materiales (versión 2) - Crear, modificar y visualizar listas de materiales (F1813A) . |  |  |
| 3 | Crear lista de materiales | Seleccionar Crear lista de materiales . Sobre el Crear lista de materiales , introduzca lo siguiente datos y seleccione OK .Material : <Material terminado/semielaborado número>Número de modificación : <su modificación Número creado en paso anterior>Centro : <Su Centro>Utilización de lista de materiales : 1 (para producción solo) |  |  |
| 4 | Añadir datos de componentes | En la Componentes seleccione Añadir ícono para agregar uno o más componentes.Tp.pos.IC : <L para Posición de stock>Componente : <Número de material, Producto bruto/semi>Cantidad : <Cantidad>UM de componente : UN | Se han añadido datos de componentes. |  |
| 5 | Introducir tipo de posición de lista de materiales no de almacén ("N") | En la Componentes seleccione la sección Añadir icono para agregar uno o más componentes.Tp.pos.IC : <N para no stock posición>Componente : <Número de material, materia prima/semi producto>Cantidad de componente : <Cantidad>UM de componente : UNPulsar Intro para habilitar Componente y Componente Cantidad campos.Nota Este tipo de posición se utiliza para componentes que no se mantienen en stock, posiciones no de almacén se puede introducir en la lista de materiales con o sin un maestro registro. | Se añaden datos de componentes para posiciones no de almacén. |  |
| 6 | Introducir tamaño variable de tipo de posición de lista de materiales ("R") | En la Componentes seleccione la sección Añadir icono para agregar uno o más componentes.Tp.pos.IC : <R para tamaño variable posición>Componente : <Número de material, materia prima/semi producto>Seleccione la flecha para abrir el Detalles página.El Datos de posición de dimensión bruta realice las entradas necesarias.Dimensión bruta 1 : <Introduzca sus dimensiones de tamaño variable posiciones>Dimensión bruta 2 : <Introduzca sus dimensiones de tamaño variable posiciones>Tamaño3 : <Introduzca sus dimensiones de tamaño variable posiciones>Unidad de tamaño : <Introduzca su unidad de medida para el cantidad de una posición de dimensión bruta>Clave de fórmula : <Introduzca la fórmula para calcular posición de dimensión bruta>Número de posiciones de tamaño variable : <Cantidad>Cantidad de posición de dimensión bruta : <Una cantidad calculada para las posiciones de dimensión bruta>Seleccionar Aplicar .Nota Este tipo de posición le permite especificar diferentes secciones de tamaño de un componente con un material, como el tamaño de una chapa de acero necesaria para reparar algo de planificación. | Los datos de componentes para posiciones variables se añaden/calculan. |  |
| 7 | Introducir posición de texto de tipo de posición de lista de materiales ("T") | Para el nuevo Número de posición de lista de materiales línea, realice entradas similares a el siguiente ejemplo:Posición Categoría : Texto posiciónEn la Posición de lista de materiales Número línea,Seleccione la flecha para abrir el Detalles página.En el Actualizar lista de material-básica Detalles pantalla,Componente cantidad : 1UM de componente : UNSeleccione el Estado/Texto explicativo para visualizar el Texto de posición .Posición Texto : Documentación | Se añaden datos de documentos de texto para posiciones de texto. |  |
| 8 | Verificar cabecera | En la Atributos de cabecera sección, puede verifique los datos y modifíquelos si es necesario. |  |  |
| 9 | Guardar los datos | Guarde las entradas. | Mensaje Lista de materiales para material guardada muestra. |  |

### Crear lista de materiales de ventas

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Ingeniero de producción - Fabricación discreta . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Actualizar lista de materiales - Crear, modificar y visualizar listas de materiales (F1813) . |  |  |
| 3 | Crear lista de materiales | Seleccionar Crear lista de materiales . En el campo Crear lista de materiales introduzca los siguientes datos y seleccione OK .Material : <Número de material de cabecera de lista de materiales> , por ejemplo, SDBOMERLAHD o SDBOMLUMFHDCentro : <introduzca su centro>Número de modificación : <su número de modificación creado en el paso anterior>Utilización de lista de materiales : 5 |  |  |
| 4 | Añadir datos de componentes | En la Componentes seleccione la sección Añadir para añadir uno o más componentes.Tp.pos.IC : <L para posición de stock>Componente : <Número de material, mercaderías>Cantidad : <cantidad> | Se han añadido datos de componentes. |  |
| 5 | Verificar cabecera | En la Atributos de cabecera puede verificar los datos y modificarlos si es necesario. |  |  |
| 6 | Guardar los datos | Guarde las entradas. | Se muestra el mensaje Lista de materiales para material grabada. |  |

## Apéndice

### Procesos siguientes: Crear hoja de ruta

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Hoja de ruta |  |  | Para ejecutar esta actividad, complete la Crear hoja de ruta - MDS (BNL) Test script. |

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
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 18,182 chars in the whole document
