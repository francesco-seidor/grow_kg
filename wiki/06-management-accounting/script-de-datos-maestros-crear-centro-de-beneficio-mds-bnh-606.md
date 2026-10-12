---
id: 06-management-accounting/script-de-datos-maestros-crear-centro-de-beneficio-mds-bnh-606
title: Script de datos maestros - Crear centro de beneficio - MDS (BNH) (BNH_S4CLD2608_Master_Data_ES_XX)
description: Spanish master data script (MDS BNH) with prerequisites and test steps to create and maintain profit center master data in SAP S/4HANA Cloud Public Edition.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_ES_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit center master data, profit centers, validity periods, mandatory master data, business roles, organizational units, segment reporting, BNH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-606
topic: 06-management-accounting/profit-centers
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear centro de beneficio - MDS (BNH) (BNH_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear centro de beneficio - MDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894957)

[2 Requisitos previos 3](#_Toc233894958)

[2.1 Acceso al sistema y roles 3](#_Toc233894959)

[2.2 Unidades organizativas necesarias 3](#_Toc233894960)

[2.3 Datos maestros obligatorios y opcionales 4](#_Toc233894961)

[2.4 Parámetros principales para la creación de datos 5](#_Toc233894962)

[3 Tabla de resumen 6](#_Toc233894963)

[4 Procedimientos de prueba 7](#_Toc233894964)

[4.1 Creación de datos maestros de centro de beneficio 7](#_Toc233894965)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un centro de beneficio es una unidad organizativa en contabilidad que refleja una estructura orientada a la gestión de la organización para el control interno. Dividir su empresa en centros de beneficio le permite determinar el beneficio para centros de beneficio internos áreas de responsabilidad y delegar la responsabilidad en unidades descentralizadas.

Los datos maestros de un centro de beneficio incluyen el nombre del centro de beneficio, sociedad CO a la que está asignada y el período de validez del centro de beneficio, como información sobre la persona responsable del centro de beneficio, el centro de beneficio asignación a un nodo de la jerarquía estándar y datos necesarios para la comunicación (dirección, número de teléfono, etc.).

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar el test en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

### Acceso al sistema y roles

Realice el test en los siguientes sistemas:

| Sistema | Detalles |
| --- | --- |
| SAP S/4HANA Cloud Public Edición | ID de sistema: ###Mandante: ### |

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) | Iniciar sesión |
| --- | --- | --- | --- | --- |
| Contable de división | SAP_BR_DIVISION_ACCOUNTANT | Contabilidad por sectores | SAP_BR_DIVISION_ACCOUNTANT |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de cliente dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos básicos de centro de beneficio | Sociedad COGrupo de centros de beneficioSegmento | Nombre, texto explicativo, período de validez, usuario responsable, responsable | Los grupos de centros de beneficio permiten al controlador abordar los grupos de centros de beneficio proporcionando el nombre del grupo en lugar de nombres de centros de beneficio individuales, por ejemplo, en el Customizing o en la gestión de informes. En la gestión de informes, esto permite un análisis de ratios de Controlling en un nivel agregado.Normalmente, el segmento no se contabiliza explícitamente. Los datos se derivan de objetos de imputación como centros de beneficio. A su vez, el centro de beneficio normalmente no se contabiliza explícitamente. Los datos se derivan de objetos de imputación primarios como centros de coste, órdenes CO, etc. | Sociedad CO:____________Grupo de centros de beneficio:____________Segmento:____________ |
| Asignación de sociedad de centro de beneficio | Sociedad | Sociedad | Pueden existir datos de sociedad para cada ID de sociedad de su estructura empresarial para la que se utiliza el registro maestro de centros de beneficio. | Sociedad:____________ |

### Datos maestros obligatorios y opcionales

La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de centro de beneficio.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad CO | Datos básicos de centro de beneficio | Obligatorio | Una sociedad CO de referencia se puede utilizar para crear un nuevo beneficio centro. |
| Centro de beneficio | Datos básicos de centro de beneficio | Obligatorio | Un centro de beneficio de referencia se puede utilizar para crear un nuevo centro de beneficio centro. |
| Inicio de validez | Datos básicos de centro de beneficio | Obligatorio |  |
| Válido hasta | Datos básicos de centro de beneficio | Obligatorio |  |
| Nombre | Datos básicos de centro de beneficio | Obligatorio |  |
| Texto explicativo | Datos básicos de centro de beneficio | Opcional |  |
| Usuario responsable | Datos básicos de centro de beneficio | Opcional |  |
| Persona responsable | Datos básicos de centro de beneficio | Obligatorio |  |
| Grupo de centros de beneficio | Datos básicos de centro de beneficio | Obligatorio |  |
| Departamento | Datos básicos de centro de beneficio | Opcional |  |
| Segmento | Datos básicos de centro de beneficio | Opcional | Si el centro de beneficio es válido para una empresa de EE. UU., recomendamos completar el campo de segmento; de este modo, se puede ejecutar el reporting de segmento. |
| Modelo de planificación | Datos básicos de centro de beneficio | Opcional |  |
| Campos Dirección y Comunicación | Dirección de centro de beneficio y datos de comunicación | Todos son opcionales |  |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son siempre obligatorio para crear un maestro de centros de beneficio registro de datos:

Sociedad CO: A000

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/APP | Resultados previstos |
| --- | --- | --- | --- |
| [Creación de datos maestros de centro de beneficio](#unique_8) [página ] 7 | Contable de división | Gestionar centros de beneficio - Versión anterior (F3516) | Se abre una ventana nueva en la que se muestra Datos maestros para centro de beneficio pantalla. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Creación de datos maestros de centro de beneficio

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de división . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar centros de beneficio - Versión anterior (F3516) . | El Datos maestros para centro de beneficio se visualiza. |  |
| 3 | Buscar centro de beneficio | Busque el centro de beneficio.Seleccionar Ir . | Aparece una lista de centros de beneficio en la pantalla. |  |
| 4 | Añadir centro de beneficio | Seleccionar Crear . | El Centro de beneficio: Nuevo se visualiza. |  |
| 5 | Introducir nuevos datos de centro de beneficio | En la Nuevo centro de beneficio introduzca la sección Datos siguientes:Centro de beneficio : <Nombre> , por ejemplo, YBXXXNota La longitud máxima es de 10 caracteres. No utilizar especial caracteres como %, !, $, &, @, etc. Causarán La aplicación se bloquea y no se puede eliminar.Inicio de validez : <Inicio de validez fecha>Válido hasta : <Fin de validez fecha>Nombre : <Cualquiera descripción>Persona responsable : <Nombre de la persona responsable> |  |  |
| 6 | Introducir datos básicos | El Unidad organizativa introduzca la etiqueta Datos siguientes:Nodo de jerarquía estándar : <Grupo de centros de beneficio>Segmento : <Segmento> |  |  |
| 7 | Asignación de sociedad | Marque o desmarque la casilla de selección para asignar sociedades al nuevo centro de beneficio. |  |  |
| 8 | Guardar los datos | Guarde las entradas. |  |  |
| 9 | Fijar nuevo período de validez (opcional) | Seleccionar Editar .En el centro de beneficio que ha creado, seleccione Período de validez > Nuevo período de validez .Realice entradas para el Inicio de validez y Válido hasta y seleccione una fuente de datos período.Seleccionar Crear .Nota Si el nuevo período de validez se solapa con el existente, el tiempo solapado se excluirá del período actual.Si existe una discontinuidad entre el nuevo período de validez y otros períodos, el sistema evitará esta acción. |  |  |
| 10 | Modificar campos dependientes del tiempo (opcional) | Puede modificar los siguientes campos dependientes del tiempo en los nuevos período de validez.DepartamentoResponsable para PCUsuario responsableTítuloNombreNombre 2Nombre 3Nombre 4Indicador de bloqueoSeleccionar Grabar .Nota Si modifica campos que no son dependientes del tiempo, las modificaciones se se aplica en todos los períodos de validez.Si no hay diferencia entre el nuevo período y el anterior o período siguiente, el nuevo período se fusionará con el período existente uno. | Se crea un nuevo período de validez.Los registros de modificación se visualizan en el Log de modificaciones sección. |  |

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
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/mds-bnh-609]]
- related-to :: [[06-management-accounting/profitcenter-anlegen-sds-bnh-604]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 13,905 chars in the whole document
