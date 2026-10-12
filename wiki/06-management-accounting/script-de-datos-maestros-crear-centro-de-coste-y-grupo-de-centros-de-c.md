---
id: 06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c
title: Script de datos maestros - Crear centro de coste y grupo de centros de coste (BNM) (BNM_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script for creating cost centers and cost center groups, with usage analysis; dated 02-07-26."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_ES_XX]
keywords: [Cost Centers and Cost Center Groups, cost centers, cost center groups, standard hierarchy, global hierarchies, cost center usage analysis, business roles, master data prerequisites, master data replication, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-636
topic: 06-management-accounting/cost-centers-and-groups
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear centro de coste y grupo de centros de coste (BNM) (BNM_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear centro de coste y grupo de centros de coste - MDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233895009)

[2 Requisitos previos 3](#_Toc233895010)

[2.1 Acceso al sistema 3](#_Toc233895011)

[2.2 Roles 3](#_Toc233895012)

[2.3 Unidades organizativas necesarias 3](#_Toc233895013)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233895014)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233895015)

[3 Tabla de resumen 5](#_Toc233895016)

[4 Procedimientos de prueba 6](#_Toc233895017)

[4.1 Creación de datos maestros de centro de coste 6](#_Toc233895018)

[4.2 Creación de datos maestros de grupo de centros de coste 8](#_Toc233895019)

[4.3 Análisis 11](#_Toc233895020)

[4.3.1 Referencia de utilización - Centros de coste reales 11](#_Toc233895021)

[5 Apéndice 13](#_Toc233895022)

[5.1 Replicación de centro de coste desde SAP S/4HANA Cloud Public Edición a SAP Master Data Integration (opcional) 13](#_Toc233895023)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Los centros de coste representan las áreas de responsabilidad de la unidad organizativa a las que se pueden asignar costes. Dividir una organización en centros de coste le permite seguir varios objetivos.

La asignación de costes a centros de coste le permite determinar dónde se incurren los costes dentro del organización.

Si planifica costes a nivel de centro de coste, puede verificar la rentabilidad en el punto en el que se incurre en costes.

Si desea asignar gastos generales con precisión a productos, servicios o segmentos de mercado, debe seguir imputando los costes a esos centros de coste directamente implicado en la creación de los productos o servicios. Desde estos centros de coste puede utilizar diferentes métodos para asignar las actividades y los costes a los productos relevantes, servicios y segmentos de mercado.

Esto le permite valorar productos semielaborados y terminados en Controlling del producto. Controlling (CO-PC) y para calcular los márgenes de cobertura en la cuenta de resultados (CO-PA)

Los grupos de centros de coste representan una estructura jerárquica de centros de coste conocida como jerarquía estándar. Cada centro de coste que se crea debe asignarse a un grupo en el jerarquía estándar. Esto garantiza que la jerarquía estándar contenga todos los costes centros de coste en el grupo de Controlling. Al analizar la jerarquía estándar, el sistema SAP incluye automáticamente todos los centros de coste.

Tenga en cuenta que los centros de coste se pueden asignar a cualquier cantidad de grupos alternativos. Sin embargo, No se pueden crear grupos alternativos al actualizar la jerarquía estándar.

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

La estructura organizativa y los datos maestros de su empresa se han creado en su ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan centros de coste y grupos de centros de coste, según en el enfoque operativo de su empresa.

| Objeto de datos | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad CO | Datos generales | Obligatorio |  |
| Sociedad | Unidades organizativas | Obligatorio |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros del centro de coste y del grupo de centros de coste pueden hacer referencia a otros datos maestros. El La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios utilizado en un registro de datos de centro de coste.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Área de jerarquía | Unidades organizativas | Obligatorio |  |
| División | Unidades organizativas | Opcional |  |
| Área funcional | Unidades organizativas | Opcional |  |
| Centro de beneficio | Unidades organizativas | Obligatorio |  |

### Parámetros principales para la creación de datos

Este elemento de alcance no tiene condiciones empresariales.

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de centro de coste](#unique_9) [página ] 6 | Contable de costes - Gastos generales | Gestionar centros de coste - Versión anterior (F1443A) | Los centros de coste se pueden crear de acuerdo con los nuevos requisitos empresariales. |
| [Creación de datos maestros de grupo de centros de coste](#unique_10) [página ] 8 | Contable de costes - Gastos generales | Gestionar jerarquías globales (F2918) o bien Gestionar grupos de centros de coste (F1024) | Los grupos de centros de coste se pueden crear de acuerdo con los nuevos requisitos empresariales. |
| [Referencia de utilización - Centros de coste reales](#unique_11) [página ] 11 | Contable de costes - Gastos generales | Gestionar centros de coste - Versión anterior (F1443A) |  |

## Procedimientos de prueba

En esta sección se describen los procedimientos para cada paso del proceso que pertenece a este elemento de alcance. También puede utilizar estos procedimientos para probar la creación de datos maestros.

### Creación de datos maestros de centro de coste

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

|  |
| --- |
| Nota Nodo de jerarquía estándar 1~A partir de la edición 2502, para las nuevas instalaciones de cliente, la jerarquía estándar se entregará utilizando la funcionalidad de jerarquía global con el valor de 1~. Los clientes anteriores pueden seguir utilizando el valor de la jerarquía estándar basada en conjuntos de 0001.Al crear el primer centro de coste en el sistema productivo, debe seleccionar el valor 1~ en la lista desplegable de búsqueda de la Nodo de jerarquía estándar campo. Esto establece el nodo de nivel superior 1~ en la jerarquía estándar. Una vez creado el primer centro de coste en el sistema, el nodo de jerarquía estándar 1~ también se crea automáticamente. A partir de la edición 2502, SAP S/4HANA Cloud Public Edición El contenido predeterminado de Public Edition siempre se envía con la jerarquía estándar 1~ y debe utilizarse como nivel superior. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar centros de coste - Versión anterior (F1443A) . | Se abre la aplicación. |  |
| 3 | Crear un nuevo centro de coste | Seleccionar Crear para crear un nuevo centro de coste. |  |  |
| 4 | Introducir nuevo centro de coste | El Información general , efectúe las siguientes entradas:Centro de coste : <Texto>Nombre : <Texto>Descripción : <Texto>Persona responsable : <Persona responsable>Inicio de validez : <01/01/2017>Válido hasta : <31/12/9999>Clase de centro de coste : <Categoría de centro de coste>Opcionalmente, puede modificar los valores predeterminados para las fechas válidas y seleccionar una referencia de los datos maestros de centro de coste existentes. | Se abre una nueva sección que muestra la información general. |  |
| 5 | Introducir datos organizativos de centro de coste | En la Unidades organizativas sección, en la Centro de coste , efectúe las siguientes entradas:Nodo de jerarquía estándar : <1~>Sociedad : <Sociedad>Área funcional : <Área funcional>Centro de beneficio : <Centro de beneficio>Solo para PSM:Nota Si tiene Gestión Pública (PSM) instalados, estos campos estarán disponibles para la entrada después de seleccionar la sociedad PSM.Fondos : <Fondo>Asignación fija de fondos : <Sí/No>Subvención : <Subvención>Asignación fija de subvención : <Sí/No>Asignación fija de área funcional : <Sí/No>Nota El Asignación fija para Área funcional, Fondo y Subvención solo se visualiza después de introducir los datos maestros correspondientes.Centro de coste responsable del presupuesto : <Centro de coste>Perfil de control de disponibilidad de presupuesto : <Perfil>El control de disponibilidad de presupuesto está activo : <Sí/No> | La selección se desplaza y muestra los datos organizativos. |  |
| 6 | Crear | Seleccionar Crear . | Se crea el centro de coste. |  |

### Creación de datos maestros de grupo de centros de coste

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Requisito previo

Para este capítulo, los Datos básicos para el material ya deben estar rellenados como se describe en el capítulo: [Creación de datos maestros de centro de coste](#unique_9) [página ] 6. Inicie este procedimiento después de haber grabado las entradas de datos maestros en el capítulo anterior.

|  |
| --- |
| Nota Cualquiera de los dos Gestionar jerarquías globales (F2918) o bien Gestionar grupos de centros de coste (F1024) se puede utilizar al crear jerarquías alternativas, pero solo se debe seleccionar un método (Grupos de jerarquía global o Grupos basados en conjuntos). Ambos métodos se describen en las siguientes etapas.Los clientes existentes pueden seguir utilizando la aplicación relacionada Grupos basados en conjuntos Gestionar grupos de centros de coste (F1024) hasta que migren por completo y marquen el estado de migración como Completar utilizando el rol de experto BPC mediante esta vía de acceso: Configuración de proceso empresarial > Contabilidad > Opciones generales: Migrar grupos basados en conjuntos a jerarquías globales (F6228) .Los datos maestros de demostración del grupo de centros de coste proporcionados por SAP también se crean mediante grupos basados en conjuntos y también se pueden convertir.Encontrará más información sobre la conversión del grupo de centros de coste en jerarquía global mediante: [https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?estado=BORRADOR](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT). |

Procedimiento: Opción 1 - Grupos de jerarquía global

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar jerarquías globales (F2918) . | Se abre la aplicación. |  |
| 3 | Seleccione Crear. | En la Lista de jerarquías sección, seleccione Crear . | El Nueva jerarquía se visualiza. |  |
| 4 | Introducir nueva jerarquía de centros de coste | El Nueva jerarquía , efectúe las siguientes entradas y seleccione Crear :Tipo : Jerarquía de centros de costeID de jerarquía : <Cualquier ID de hasta 10 caracteres>Atención La longitud total del ID de jerarquía y del ID de nodo no puede superar los 14 caracteres.Sociedad CO : A000Descripción de jerarquía : <Cualquier descripción>Inicio de validez : <Fecha actual> |  |  |
| 5 | Editar nueva jerarquía de costes | El Lista de jerarquías , seleccione el icono de detalle > y seleccione Editar para la jerarquía de centros de coste recién creada.Seleccione la jerarquía de centros de coste recién creada, seleccione Más en la parte derecha de la pantalla y, a continuación, seleccione Entrada rápida .El Entrada rápida pantalla, seleccione Centro de coste y realice la siguiente entrada:ID : <Seleccione los centros de coste que desea añadir mediante la función de búsqueda>Seleccionar OK cuando termine y seleccione Grabar .Regrese a la Jerarquía de centros de coste y seleccione Activar . | La jerarquía de centros de coste recién creada ahora está activada. |  |

Procedimiento: Opción 2 - Grupos basados en conjuntos

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar grupos de centros de coste (F1024) . | Se abre la aplicación. |  |
| 3 | Crear un nuevo grupo de centros de coste | En la Lista de resultados: Grupo de centros de coste sección, seleccione Nuevo . |  |  |
| 4 | Introducir nuevo grupo de centros de coste | El Grupo de centros de coste: Nuevo , efectúe las siguientes entradas:Sociedad CO : <A000>Grupo de centros de coste : <Grupo de centros de coste>Seleccionar Continuar y realice la siguiente entrada:Nombre : <Nombre>Seleccionar Grabar .Opcionalmente, puede seleccionar una referencia de los grupos de centros de coste existentes. | El Grupos de centros de coste: Nuevo se visualiza. |  |
| 5 | Introducir datos organizativos de centro de coste | El Grupos de centros de coste: Nuevo , efectúe las siguientes entradas:En el nivel superior, puede crear nuevos datos maestros seleccionando Nuevo :Nuevo grupo secundario : <Grupo de centros de coste>En los niveles inferiores, puede añadir seleccionando Nuevo :Nuevo grupo secundario : <Grupo de centros de coste>Nuevo grupo hermano : <Grupo de centros de coste>En el nivel superior, puede añadir datos maestros existentes seleccionando Añadir :Añadir grupo secundario : <Grupo de centros de costeAñadir centro de coste : <Centro de coste>Añadir rango de centros de coste : <Centro(s) de coste>En los niveles inferiores, puede añadir seleccionando Nuevo :Nuevo grupo secundario : <Grupo de centros de coste>Nuevo grupo hermano : <Grupo de centros de coste>Añadir centro de coste : <Centro de coste>Añadir rango de centros de coste : <Centro(s) de coste> | Se muestran nuevos datos maestros en el Grupos de centros de coste: Nuevo pantalla. |  |
| 6 | Guardar los datos | Seleccionar Grabar . | Se crea y graba el grupo de centros de coste. |  |

### Análisis

#### Referencia de utilización - Centros de coste reales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Esta actividad le permite ver dónde se utilizan los centros de coste en otros datos maestros como la clase de actividad, los centros de beneficio y las imputaciones de costes reales.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar centros de coste - Versión nueva (F1443B) . | El Gestionar centros de coste se visualiza. |  |
| 3 | Criterios de selección | Realice la siguiente entrada y seleccione Ir :Centro de coste : <su centro de coste> |  |  |
| 4 | Utilización | Seleccione el centro de coste deseado y seleccione Utilización .Seleccione una opción de la lista desplegable. Por ejemplo, En todos los objetos . | Se visualiza un informe que muestra dónde se utilizan actualmente los centros de coste. Para obtener más detalles, puede seleccionar el objeto de datos maestros y siga explorando. |  |

|  |
| --- |
| Nota El Referencia de utilización - Centros de coste (F3549) también se puede utilizar para determinar dónde centros de coste se utilizan actualmente. |

## Apéndice

### Replicación de centro de coste desde SAP S/4HANA Cloud Public Edición a SAP Master Data Integration (opcional)

Este enlace describe la replicación de SAP S/4HANA Cloud Public Edición datos maestros de centro de coste mediante SAP Master Data Integration a otras aplicaciones en la nube, como SAP SuccessFactors :[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html).

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
- related-to :: [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635]]
- related-to :: [[06-management-accounting/mds-bnm-637]]
- related-to :: [[06-management-accounting/mds-bnm-639]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 22,113 chars in the whole document
