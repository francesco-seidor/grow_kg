---
id: 02-business-partner-and-product-master-data/script-de-datos-maestros-crear-jerarquia-de-productos-4dx-414
title: "Script de datos maestros: Crear jerarquía de productos (4DX) (4DX_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish SAP S/4HANA Cloud Public Edition master data script (4DX) for creating product hierarchies, incl. node configuration prerequisite and test steps; dated 02-07-26."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-hierarchy]
aliases: [4DX_S4CLD2608_Master_Data_ES_XX]
keywords: [Product Hierarchies, product hierarchy nodes, master data scripts, business roles, self-service configuration, sales orders, product master data, central business configuration, 4DX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-414
topic: 02-business-partner-and-product-master-data/product-hierarchy
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear jerarquía de productos (4DX) (4DX_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Product Hierarchies** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear jerarquía de productos (4DX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894692)

[2 Requisitos previos 3](#_Toc233894693)

[2.1 Acceso al sistema 3](#_Toc233894694)

[2.2 Roles 3](#_Toc233894695)

[2.3 Unidades organizativas necesarias 4](#_Toc233894696)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894697)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894698)

[2.5.1 Nodos de jerarquía de productos 4](#_Toc233894699)

[2.6 Pasos preliminares 5](#_Toc233894700)

[2.6.1 Crear nodos para jerarquías de productos 5](#_Toc233894701)

[3 Tabla de resumen 8](#_Toc233894702)

[4 Procedimientos de prueba 9](#_Toc233894703)

[4.1 Crear jerarquía de productos 9](#_Toc233894704)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear datos maestros de jerarquía de productos para su SAP S/4HANA Cloud Public Edición sistema. El descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector principalmente aprende qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Campos que no son relevantes para el alcance del SAP S/4HANA Cloud Public Edición contenido no se describen en este documento, aunque pueden visualizarse en la pantalla.

Los datos maestros de la jerarquía de productos que se crean se pueden utilizar para asignar la distribución cadenas con una jerarquía de productos, que a su vez se utiliza para el procesamiento posterior en Ventas Pedidos.

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
| Experto en configuración - Configuración del proceso empresarial | SAP_BR_BPC_EXPERT | Configuración de proceso empresarial / Configuración de proceso empresarial - Finanzas / Configuración del proceso empresarial - Aprovisionamiento / Gestionar su solución / Configuración de proceso empresarial: flujo de trabajo / Configuración empresarial - Gestión de funciones / Configuración de proceso empresarial - Explorador de ampliabilidad / Configuración empresarial - Transporte | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Productos / Control de productos | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. General Los datos (centrales) no dependen de una unidad organizativa o de la sociedad. El la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos de ventas | Centro, organización de ventas, canal de distribución | Datos fiscales , Tipo de posición Grupo , Grupo de carga , y así on. |  | Centro:____________Organización de ventas:____________Canal de distribución:______________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros pueden hacer referencia a otros datos maestros . La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un producto Registro de datos maestros de jerarquía.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Producto | En la Gestionar jerarquías de productos aplicación, se asigna una jerarquía con producto múltiple como nodo final/nodo final. | Obligatorio | Al asignar registros de producto creados en Gestionar maestro de productos Datos aplicación, como nodos finales en Gestionar producto Jerarquías proporciona integridad/negocio relevancia para la jerarquía. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son siempre obligatorio para crear un maestro de jerarquías de productos registro de datos.

#### Nodos de jerarquía de productos

La IU de configuración de autoservicio (paso de configuración) disponible para Producto, Configurar nodos para jerarquías de productos acceso mediante filtrado El área de aplicación para la base de datos y la gestión de datos debe actualizarse para poder seleccione o forme la estructura jerárquica.

Esta configuración proporciona la opción de crear varios valores de nodo y una descripción para cada nodo.

|  |
| --- |
| Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration. |

### Pasos preliminares

#### Crear nodos para jerarquías de productos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Las entradas creadas a partir del paso de configuración de autoservicio Configurar nodos para jerarquías de productos es un requisito previo para crear una jerarquía de productos.

|  |
| --- |
| Nota Este paso debe ser realizado por el Experto en configuración usuario en el escenario empresarial habitual. |

Procedimiento

|  |
| --- |
| Nota En función de su entorno de configuración, se puede acceder a los pasos de configuración en Configurar su solución en la rampa de lanzamiento SAP Fiori o en la Configuración de procesos empresariales en la experiencia en proyectos de SAP Central Business Configuration. |

Configurar su solución :

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | El Iniciar Aparece la página. |  |
| 2 | Abrir aplicación SAP Fiori | En la Cockpit de implementación seleccione la sección Gestionar su solución (F1241) . | Se abre una nueva página que muestra el Gestionar su solución (F1241) pantalla.Nota Esta aplicación forma parte de Experto en configuración - Configuración del proceso empresarial modelo de rol. |  |
| 3 | Seleccione Configurar su solución | En la Gestionar su solución aplicación, seleccione Configurar su solución . | Se abre una nueva página que muestra Configurar su solución: Fase de modificación . |  |
| 4 | Seleccionar el área de aplicación | En Configurar su solución aplicación, seleccione el filtro para Área de aplicación y seleccione Gestión de datos y bases de datos opción. | El número de entradas que se muestran en la tabla de resultados se reduce a pocos registros. |  |
| 5 | Seleccionar el área de subaplicación | En la Configurar su solución aplicación, seleccione el filtro para Sub Área de aplicación y seleccione Producto opción. | El número de registros proporcionado en la lista de resultados se reduce a uno. |  |
| 6 | Pasos de configuración de producto | De las entradas que se muestran en la tabla, seleccione en el registro con Producto como Área de subaplicación .Y, a continuación, seleccione el título de la sección Pasos de configuración . | La sección muestra la lista de varios pasos de configuración de producto. |  |
| 7 | Configurar nodos para jerarquía de productos | En el paso de configuración Configurar nodos para jerarquías de productos , seleccione Configurar . | La página de la aplicación Actualización de ID de subnodo de jerarquía de productos se abre. |  |
| 8 | Crear entradas nuevas | Seleccionar Entradas nuevas . | Se abre la página Editable para actualizar los nuevos subnodos con el título Entradas nuevas: Resumen de entradas añadidas . |  |
| 9 | Introducir subnodos nuevos | Proporcione varias entradas para los subnodos necesarios en la jerarquía de productos de destino.Por ejemplo, un <Bebidas> La jerarquía podría tener:Aquí los nodos de jerarquía de productos podrían ser <AERATED_DRINKS> , <NON_AERATED_DRINKS> etc.La descripción de los subnodos podría actualizarse como <Bebidas aireadas> , <Bebidas no aireadas> etc. |  |  |
| 10 | Grabar las entradas | Seleccionar Grabar en el pie de página inferior. | La página de la aplicación Actualización de ID de subnodo de jerarquía de productos vuelve a aparecer con las nuevas entradas proporcionadas. |  |
| 11 | Salir | Seleccionar Salir y cierre sesión. |  |  |

SAP Central Business Configuration:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la experiencia del proyecto en SAP Central Business Configuration. |  |  |
| 2 | Abrir workflow flexible activo | Vaya a Configuración de procesos empresariales aplicación. Para localizar la actividad en la vista de árbol, busque la siguiente actividad: Configurar nodos para jerarquías de productos .Seleccionar Abrir documentación para la partida individual encontrada para ver más detalles sobre esta actividad de configuración.Seleccione el enlace para navegar directamente a la SAP S/4HANA Cloud Public Edición sistema. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial . |  |  |
| 3 | Crear entradas nuevas | Seleccionar Entradas nuevas . | Se abre la página Editable para actualizar los nuevos subnodos con el título Entradas nuevas: Resumen de entradas añadidas . |  |
| 4 | Introducir subnodos nuevos | Proporcione varias entradas para los subnodos necesarios en la jerarquía de productos de destino.Por ejemplo, un <Bebidas> La jerarquía podría tener:Aquí los nodos de jerarquía de productos podrían ser <AERATED_DRINKS> , <NON_AERATED_DRINKS> etc.La descripción de los subnodos podría actualizarse como <Bebidas aireadas> , <Bebidas no aireadas> etc. |  |  |
| 5 | Grabar las entradas | Seleccionar Grabar en el pie de página inferior. | La página de la aplicación Actualización de ID de subnodo de jerarquía de productos vuelve a aparecer con las nuevas entradas proporcionadas. |  |
| 6 | Salir | Seleccionar Salir y cierre sesión. |  |  |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Segmento | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Crear jerarquía de productos](#unique_11) [página ] 9 | Especialista en datos maestros - Datos de producto | Gestionar jerarquías de productos (F4359) | Se ha creado el registro de datos maestros de jerarquía de productos. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear jerarquía de productos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El siguiente procedimiento proporciona instrucciones sobre cómo crear una jerarquía de productos con productos asignados a la jerarquía como nodos finales. Después de la activación de la jerarquía, se puede consumir durante la creación de pedidos de cliente.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori con sus credenciales de usuario. | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar jerarquías de productos (F4359) . | Se abre la aplicación. |  |
| 3 | Crear jerarquía de productos | El Gestionar jerarquías de productos , seleccione + (Crear una nueva jerarquía). | El Crear nueva jerarquía se visualiza. |  |
| 4 | Introducir datos de jerarquía de productos | El Crear nueva jerarquía , efectúe las siguientes entradas:Tipo : Por ejemplo, <Jerarquía de productos> .ID de jerarquía : Por ejemplo, <BEBIDAS> .Descripción de jerarquía : Por ejemplo, <Jerarquía de bebidas> .Inicio de validez : <Introduzca una fecha de inicio de validez de la jerarquía>Válido hasta : <Modifique la fecha predeterminada si es necesario para tener una jerarquía dependiente del tiempo> |  |  |
| 5 | Seleccione Crear. | El Crear nueva jerarquía , seleccione Crear . | La lista Jerarquía se filtra para mostrar la entrada Jerarquía de productos recién creada con la Estado visualizado como Borrador . |  |
| 6 | Seleccione la nueva jerarquía de productos | En la Gestionar jerarquías de productos (F4359) , seleccione la jerarquía de productos recién creada con la Borrador estado enumerado en el resultado. | La estructura de la jerarquía de productos se visualiza en formato de tabla de árbol. |  |
| 7 | Editar la jerarquía de productos | Seleccionar Editar desde el pie de página de la pantalla. | La pantalla se muestra en modo de edición, lo que le permite modificar valores o añadir nodos nuevos. |  |
| 8 | Añadir nodos para el nodo raíz | Seleccionar + (Añadir) para el primer nodo. | El Añadir nodo se visualiza. |  |
| 9 | Seleccionar subnodos de la raíz | El Añadir nodo pantalla, Subnodo está seleccionado de forma predeterminada.Introduzca datos para el Nodo campo. Los valores configurados en el paso preliminar [Crear nodos para jerarquías de productos](#unique_9) [página ] 5 se puede utilizar aquí.Por ejemplo, <AERATED_DRINKS> , <NON_AERATED_DRINKS> , etc.Nota La ayuda para entradas puede ayudarle a seleccionar varios nodos y asignarlos al nodo seleccionado de la jerarquía.Seleccionar OK . | Los nodos seleccionados se añaden como nodos subordinados en la estructura de tabla de árbol para el nodo raíz de la jerarquía de productos. |  |
| 10 | Añadir nodos a subnodos | Seleccionar + (Añadir) para que el nodo añada más subnodos.Por ejemplo, Seleccionar + (Añadir) para el <NON_AERATED_DRINKS> nodo. | El Añadir nodo se visualiza. |  |
| 11 | Seleccionar nodos para subnodos | El Añadir nodo seleccione otros nodos de la ayuda para entradas para añadirlos como subnodos de la <NON_AERATED_DRINKS> nodo (por ejemplo).Seleccionar OK . | Los nodos seleccionados se añaden como nodos subordinados en la estructura de tabla de árbol para el nodo seleccionado de la jerarquía de productos. |  |
| 12 | Añadir productos a jerarquía | Seleccionar + (Añadir) para que el nodo añada Productos a la jerarquía. | El Añadir nodo se visualiza. |  |
| 13 | Seleccionar producto | El Añadir nodo pantalla, seleccione Producto . | El Añadir nodo , el campo de entrada cambia a Producto . |  |
| 14 | Asignar productos a jerarquía | El Añadir nodo seleccione las entradas en la pantalla Producto para asignar los Productos necesarios al nodo Jerarquía.Nota La ayuda para entradas puede ayudarle a seleccionar varios productos y asignarlos al subnodo seleccionado de la jerarquía. | Los productos seleccionados se asignan al subnodo necesario de la jerarquía de productos. |  |
| 15 | Grabar la jerarquía de productos | Seleccionar Grabar . | Se han guardado las modificaciones. |  |
| 16 | Activar la jerarquía de productos | Seleccionar Activar . | La jerarquía de productos está activada y la Estado cambios de Borrador hasta Activo . |  |

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
- related-to :: [[02-business-partner-and-product-master-data/4dx-415]]
- related-to :: [[02-business-partner-and-product-master-data/4dx-417]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-hierarchy-4dx-413]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-hierarquia-de-produtos-4dx-416]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 20,837 chars in the whole document
