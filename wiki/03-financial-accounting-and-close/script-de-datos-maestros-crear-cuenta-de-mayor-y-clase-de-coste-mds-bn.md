---
id: 03-financial-accounting-and-close/script-de-datos-maestros-crear-cuenta-de-mayor-y-clase-de-coste-mds-bn
title: "Script de datos maestros: Crear cuenta de mayor y clase de coste - MDS (BNG) (BNG_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish master data script (BNG) for SAP S/4HANA Cloud Public Edition 2608: prerequisites and test steps to create a G/L account and cost element via Manage Your Solution (F1241)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_ES_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, g/l account master data, create g/l account, mandatory master data fields, master data scripts, cost elements, account types, account groups, business roles, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-600
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear cuenta de mayor y clase de coste - MDS (BNG) (BNG_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear cuenta de mayor y clase de coste - MDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894968)

[2 Requisitos previos 3](#_Toc233894969)

[2.1 Acceso al sistema 3](#_Toc233894970)

[2.2 Roles 3](#_Toc233894971)

[2.3 Unidades organizativas necesarias 3](#_Toc233894972)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894973)

[2.5 Parámetros principales para la creación de datos 6](#_Toc233894974)

[3 Tabla de resumen 7](#_Toc233894975)

[4 Procedimientos de prueba 8](#_Toc233894976)

[4.1 Crear cuenta de mayor 8](#_Toc233894977)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un registro maestro de cuenta de mayor contiene información sobre la cuenta que controla cómo se contabilizan las operaciones comerciales en él y cómo se gestionan.

El libro mayor de SAP proporciona una vista completa y totalmente actualizada de todos los activos fijos, cuentas a pagar y a cobrar, y está totalmente integrado con el resto de SAP módulos.

Dado que todos los módulos de SAP están integrados, algunas contabilizaciones de libro mayor se generan automáticamente por el sistema en proceso de fondo, por ejemplo, la contabilización en cuenta EM/RF (Mercancías Recibido/Facturas recibidas) y contabilizaciones de libro mayor de movimiento de inventario.

Algunas cuentas están «gestionadas por partidas abiertas». Se utilizan como cuenta de compensación, por lo que se pueden compensar cuando, por ejemplo, los pagos recibidos y efectuados y los materiales se procesado.

Otras cuentas, por ejemplo, las cuentas asociadas de deudor y acreedor no pueden contabilizadas directamente en, ya que solo son un reflejo de los interlocutores comerciales en la los libros auxiliares.

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

### Unidades organizativas necesarias

Algunos segmentos de datos maestros de cliente dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Cuenta de mayor | SociedadPlan de cuentasSociedad CO | Consulte [Datos maestros obligatorios y opcionales](#unique_6) [página ] 4 | Pueden existir datos de sociedad para cada ID de sociedad de su estructura empresarial para la que se utiliza el registro maestro de cuenta de mayor y clase de coste. | Sociedad:____________Plan de cuentas____________Sociedad CO____________ |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de cliente pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de cliente.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Plan de cuentas | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Control sección. | Obligatorio |  |
| Cuenta de mayor | En la IU de cuenta de mayor, encontrará la entrada en la Copiar Cuenta pantalla. | Obligatorio |  |
| Descripción | En la IU de cuenta de mayor, encontrará la entrada en la Copiar Cuenta pantalla. | Obligatorio |  |
| Tipo de cuenta | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Control sección. | Obligatorio |  |
| Grupo de cuentas | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Control sección. | Obligatorio |  |
| Área funcional | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Control sección. | Opcional | Se utiliza para las cuentas de pérdidas y ganancias. |
| Texto explicativo de cuenta de mayor | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Descripción sección. | Opcional |  |
| Casilla de selección Sociedad | En la IU de cuenta de mayor, encontrará la entrada en el General en la pestaña Definición en sociedad sección. | Obligatorio | Asignar a una o varias sociedades. |
| Bloqueado para creación | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Administración sección. | Opcional |  |
| Bloqueado para contabilización | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Administración sección. | Opcional |  |
| Bloqueado para planificación | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Administración sección. | Opcional |  |
| Marcado para borrar | En la IU de cuenta de mayor, encontrará la entrada en el General pestaña, en el Administración sección. | Opcional |  |
| Moneda de cuenta | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Control de cuenta sección. |  |  |
| Solo saldo en moneda local | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Control de cuenta sección. | Opcional |  |
| Categoría fiscal | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Control de cuenta sección. | Opcional |  |
| Contabilización sin impuestos permitida | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Control de cuenta sección. | Opcional |  |
| Número de cuenta alternativo | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Control de cuenta sección. | Opcional |  |
| Clave de clasificación | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Cuenta Gestión sección. | Opcional |  |
| Sociedad CO | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Configuración de contabilidad en Sociedad CO sección. | Obligatorio | Opcional para tipo de cuenta Balance Cuenta |
| Tipo de clase de coste | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Configuración de contabilidad en Sociedad CO sección. | Obligatorio | Opcional para tipo de cuenta Balance Cuenta |
| Registrar cantidad | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Datos de control > Configuración de contabilidad en Sociedad CO sección. | Opcional |  |
| Grupo de estados de campo | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Crear/Banco/Interés > Control de documento Creación sección. | Opcional |  |
| Contabilizar solo automáticamente | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Crear/Banco/Interés > Control de documento Creación sección. | Opcional |  |
| Complemento contab.autom. | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Crear/Banco/Interés > Control de documento Creación sección. | Opcional |  |
| Nivel de planificación | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Crear/Banco/Interés > Banco/Financiero Detalles sección. | Opcional |  |
| Relevante para flujo de caja | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Crear/Banco/Interés > Banco/Financiero Detalles sección. | Opcional |  |
| Bloqueado para contabilización | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Administración . | Opcional |  |
| Marcado para borrado | Después de crear una nueva cuenta de mayor, encontrará los detalles de Empresa Código en el Administración . | Opcional |  |
| Texto de traducción | En la IU de cuenta de mayor, encontrará la entrada en el Traducción pestaña, Idioma Clave sección. | Opcional | Traduzca las descripciones a los idiomas necesarios. |

### Parámetros principales para la creación de datos

En esta sección, se describen algunos parámetros básicos que influyen en el comportamiento de un registro maestro y que siempre son necesarios para crear un registro de datos maestros de cliente:

Tipo de cuenta

- Cuentas de balance
- Gastos o ingresos neutrales
- Costes o ingresos primarios
- Costes secundarios

Grupos de cuentas

- Cuenta asociada lista para la entrada
- Cuentas de activos fijos
- Cuentas de pérdidas y ganancias
- Cuentas de fondos líquidos
- Cuentas de gestión de materiales
- Cuentas de mayor (general)

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear cuenta de mayor](#unique_9) [página ] 8 | Experto en configuración - Configuración del proceso empresarial | Gestionar su solución (F1241) |  |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear cuenta de mayor

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Al crear nuevas cuentas de mayor, se recomienda utilizar un rango de números existente como referencia para las nuevas cuentas de mayor.

Procedimiento

En función de su entorno de configuración para SAP S/4HANA Cloud Public Edición , seleccione una de las siguientes opciones:

Configurar su solución :

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar su solución (F1241) . |  |  |
| 3 | Configuración de acceso | Abierto Configurar su solución . | El Configurar su solución: fase Realizar se visualiza. |  |
| 4 | Configuración de acceso | Realice las siguientes entradas:Área de aplicación : FinanzasÁrea de subaplicación : Libro mayor |  |  |
| 5 | Abierto | Seleccione la flecha a la derecha de la columna con la Plan de cuentas posición. |  |  |
| 6 | Seleccionar paso de configuración | Para el Gestionar datos maestros de cuenta de mayor seleccione Configurar . |  |  |
| 7 | Buscar su cuenta | Realice las siguientes entradas y seleccione Ir :Vista : Vista de plan de cuentasPlan de cuentas : YCOA | El sistema muestra una lista de cuentas de mayor coincidentes. |  |
| 8 | Seleccionar cuenta de mayor | Seleccione el Cuenta de mayor de los resultados de búsqueda.Nota Haga clic en el enlace azul del número de cuenta. | El Datos maestros de cuenta de mayor Aparece la pantalla. |  |
| 9 | Copiar cuenta | Seleccionar Copiar . | El Copia de <número de cuenta de mayor> se visualiza. |  |
| 10 | Crear cuenta | Realice las siguientes entradas y seleccione OK :Número de cuenta : <número de cuenta>Descripción en idioma de actualización (EN) : <descripción>Número de cuenta de grupo : <número de cuenta>Nota Este campo solo es visible cuando Consolidación está dentro del alcance. | Datos introducidos en la pantalla Datos maestros de cuenta de mayor muestra. |  |
| 11 | Añadir descripción | En la Información básica , realice las siguientes entradas:Plan de cuentas : YCOATexto explicativo de cuenta de mayor : <descripción> |  |  |
| 12 | Asignar sociedad | En la Asignación de sociedad sección, seleccione un Sociedad para asignarlo a la cuenta. |  |  |
| 13 | Añadir traducciones | En la Traducción introduzca los textos breves y explicativos para todos los idiomas requeridos. |  |  |
| 14 | Guardar los datos | Seleccionar Grabar . | El sistema confirma que la cuenta se ha grabado correctamente. |  |

SAP Central Business Configuration:

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la experiencia del proyecto en SAP Central Business Configuration. | Abrir workflow flexible activo |  |
| 2 | Acceder a la aplicación SAP Fiori | Vaya a Configuración de procesos empresariales aplicación y busque la siguiente actividad: Gestionar datos maestros de cuenta de mayor .Seleccione la partida individual en el resultado de la búsqueda para ver más detalles sobre esta actividad de configuración.Seleccione el Ir a actividad para navegar directamente a la SAP S/4HANA Cloud Public Edición sistema. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial . |  |  |
| 3 | Buscar su cuenta | Realice las siguientes entradas y seleccione Ir :Vista : Vista de plan de cuentasPlan de cuentas : YCOA | El sistema muestra una lista de cuentas de mayor coincidentes. |  |
| 4 | Seleccionar cuenta de mayor | Seleccione el Cuenta de mayor de los resultados de búsqueda.Nota Haga clic en el enlace azul del número de cuenta. | El Datos maestros de cuenta de mayor Aparece la pantalla. |  |
| 5 | Copiar cuenta | Seleccionar Copiar . | El Copia de <número de cuenta de mayor> se visualiza. |  |
| 6 | Crear cuenta | Realice las siguientes entradas y seleccione OK :Número de cuenta : <número de cuenta>Descripción en idioma de actualización (EN) : <descripción>Número de cuenta de grupo : <número de cuenta>Nota Este campo solo es visible cuando Consolidación está dentro del alcance. | Datos introducidos en la pantalla Datos maestros de cuenta de mayor muestra. |  |
| 7 | Añadir descripción | En la Información básica , realice las siguientes entradas:Plan de cuentas : YCOATexto explicativo de cuenta de mayor : <descripción> |  |  |
| 8 | Asignar sociedad | En la Asignación de sociedad sección, seleccione un Sociedad para asignarlo a la cuenta. |  |  |
| 9 | Añadir traducciones | En la Traducción introduzca los textos breves y explicativos para todos los idiomas requeridos. |  |  |
| 10 | Guardar los datos | Seleccionar Grabar . | El sistema confirma que la cuenta se ha grabado correctamente. |  |

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
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- related-to :: [[03-financial-accounting-and-close/mds-bng-603]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 20,175 chars in the whole document
