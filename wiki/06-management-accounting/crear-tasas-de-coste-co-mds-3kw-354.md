---
id: 06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354
title: Crear tasas de coste CO - MDS (3KW) (3KW_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script 3KW: creating CO cost rates (services, plan, actual) with test steps and display report."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_ES_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", cost rates, service cost rates, plan cost rates, actual cost rates, display cost rates, intercompany offsetting accounts, intercompany margin accounts, business roles, activity allocation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-354
topic: 06-management-accounting/cost-rates
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Crear tasas de coste CO - MDS (3KW) (3KW_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear tasas de coste CO - MDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894650)

[2 Requisitos previos 3](#_Toc233894651)

[2.1 Acceso al sistema 3](#_Toc233894652)

[2.2 Roles 3](#_Toc233894653)

[2.3 Pasos preliminares 3](#_Toc233894654)

[2.3.1 Opcional: Actualizar cuentas de compensación multisociedad (solo para contabilizaciones multisociedad) 3](#_Toc233894655)

[2.3.2 Opcional: Actualizar cuentas de margen (solo para contabilizaciones multisociedad con tasas multisociedad) 5](#_Toc233894656)

[3 Tabla de resumen 7](#_Toc233894657)

[4 Procedimientos de prueba 8](#_Toc233894658)

[4.1 Gestión de tasas de coste - Servicios 8](#_Toc233894659)

[4.2 Gestión de tasas de coste - Plan 11](#_Toc233894660)

[4.3 Gestión de tasas de coste - Reales 13](#_Toc233894661)

[5 Análisis 15](#_Toc233894662)

[5.1 Visualizar tasas de coste 15](#_Toc233894663)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Las siguientes aplicaciones están disponibles para actualizar tasas de coste (precios de actividad). Cada aplicación tiene un propósito diferente, dependiendo de cómo se puedan definir las tasas y qué objetos pueden recibir facturaciones de actividad.

| Aplicación | Elementos de alcance afectados | Comentarios |
| --- | --- | --- |
| Gestión de tasas de coste - Servicios (F3161) | Registro de tiempos (1Q4)Contabilidad de gastos generales (J54)Registro de tiempos – Servicios basados en proyectos (J12)Supervisión y gestión de órdenes de servicio (3D2) | Registro de tiempos |
| Gestión de tasas de coste - Plan (F3162) | Cálculo de costes estándar (BEG)Cierre del período – Centro (BEI)Cierre del período – Órdenes de mantenimiento (BF7) | Confirmaciones de fabricación, confirmaciones de planificación de pedidos y reales |
| Gestión de tasas de coste - Real (F3422) | Cálculo de costes real (33Q) | Se utiliza para introducir tasas de coste reales para actividades de centro de coste.Las tasas de coste reales solo son necesarias si un cliente desea utilizar el cálculo del coste real. |

Este documento proporciona un procedimiento detallado para probar este elemento de alcance después de la activación de la solución, reflejando el alcance predefinido de la solución. Cada paso, informe o posición de proceso se trata en su propia sección, proporcionando las interacciones del sistema (pasos de test) en una vista de tabla. Los pasos que no están dentro del alcance del proceso pero que son necesarios para las pruebas se marcan en consecuencia. Deben añadirse pasos específicos del proyecto.

|  |
| --- |
| Nota Los valores en este script de test (notación decimal, formatos de fecha, etc.) se presentan en la notación estándar de EE. UU. Si su sistema de prueba está configurado para utilizar una notación diferente, introduzca valores según corresponda. |

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

### Pasos preliminares

#### Opcional: Actualizar cuentas de compensación multisociedad (solo para contabilizaciones multisociedad)

Uso

Esta actividad le permite crear y actualizar cuentas de compensación para contabilizaciones multisociedad. Las cuentas de compensación ICO se derivan de la cuenta de mayor de la actividad.

Procedimiento

En función de su entorno de configuración para SAP S/4HANA Cloud Public Edición , seleccione una de las siguientes opciones:

Configurar su solución :

1. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial .
2. Abierto Gestionar su solución (F1241) .
3. Si es necesario, seleccione Fijar versión local para cambiar el país.
4. Seleccionar Configurar su solución .
5. En la Pasos de configuración sección, en la Nombre columna, para la Determinación automática de cuentas (100297), seleccione Configurar .
6. Continúe con el procedimiento en la siguiente tabla.

SAP Central Business Configuration:

1. Inicie sesión en la experiencia del proyecto en SAP Central Business Configuration.
2. Vaya a Configuración de procesos empresariales aplicación. Para localizar la actividad en la vista de árbol, busque la Determinación automática de cuentas actividad.
3. Seleccionar Abrir documentación para la partida individual encontrada para ver más detalles sobre esta actividad de configuración.
4. Seleccione el enlace para navegar directamente a la SAP S/4HANA Cloud Public Edición sistema. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial .
5. Continúe con el procedimiento en la siguiente tabla.

| Paso # | Nombre de paso | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Seleccionar área | Para la fila visualizada, realice las siguientes entradas y seleccione Paso 2 :Área: ControllingSubárea: Contabilidad de centros de costeProceso: Asignar cuenta de compensación multisociedad para contabilizaciones reales |  |  |
| 2 | Seleccionar parámetros | Realice la siguiente entrada y seleccione Paso 3 :Plan de cuentas : YCOA |  |  |
| 3 | Actualizar determinación de cuentas | Añada una cuenta que sea relevante para la compensación ICO.Nota El contenido predeterminado se suministra con la cuenta de mayor de compensación 68888800 - Cuenta de compensación ICO - Viajes y 99999900 - Cuenta de compensación ICO - Consultoría. Puede utilizar esta referencia para crear sus propias cuentas, si es necesario (con el tipo de cuenta de mayor Gastos o ingresos N-no operativos). |  |  |

#### Opcional: Actualizar cuentas de margen (solo para contabilizaciones multisociedad con tasas multisociedad)

Uso

Esta actividad le permite crear y actualizar cuentas de margen para contabilizaciones multisociedad. Este paso es necesario si actualiza y contabiliza con tasas ICO. Las cuentas de compensación de mayor de margen se derivan en función de la cuenta de mayor de facturación de actividad.

Procedimiento

En función de su entorno de configuración para SAP S/4HANA Cloud Public Edición , seleccione una de las siguientes opciones:

Configurar su solución :

1. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial .
2. Abierto Gestionar su solución (F1241) .
3. Si es necesario, seleccione Fijar versión local para cambiar el país.
4. Seleccionar Configurar su solución .
5. En la Pasos de configuración sección, en la Nombre columna, para la Determinación automática de cuentas (100297), seleccione Configurar .
6. Continúe con el procedimiento en la siguiente tabla.

SAP Central Business Configuration:

1. Inicie sesión en la experiencia del proyecto en SAP Central Business Configuration.
2. Para localizar la actividad en la vista de árbol, busque la Determinación automática de cuentas actividad.
3. Seleccionar Abrir documentación para la partida individual encontrada para ver más detalles sobre esta actividad de configuración.
4. Seleccione el enlace para navegar directamente a la SAP S/4HANA Cloud Public Edición sistema. Inicie sesión en la rampa de lanzamiento SAP Fiori como Experto en configuración - Configuración del proceso empresarial .
5. Continúe con el procedimiento en la siguiente tabla.

| Paso # | Nombre de paso | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Seleccionar área | Para la fila visualizada, realice las siguientes entradas y seleccione Paso 2 :Área: ControllingSubárea: Contabilidad de centros de costeProceso: Asignar cuentas de margen multisociedad |  |  |
| 2 | Seleccionar parámetros | Realice la siguiente entrada y seleccione Paso 3 :Plan de cuentas : YCOA |  |  |
| 3 | Actualizar determinación de cuentas | Añada una cuenta que sea relevante para el margen ICO para el libro mayor de facturación de actividad.Nota El contenido predeterminado se suministra con la cuenta de margen 97777700 - Margen ICO. Puede utilizarlo como referencia para crear su propia cuenta de margen, si es necesario (con la cuenta de mayor Gastos e ingresos primarios P). |  |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Gestión de tasas de coste - Servicios](#unique_8) [página ] 8 | Contable de costes - Gastos generales | Gestión de tasas de coste - Servicios (F3161) | Las tasas de coste se actualizan para los servicios. |
| [Gestión de tasas de coste - Plan](#unique_9) [página ] 11 | Contable de costes - Gastos generales | Gestión de tasas de coste - Plan (F3162) | Las tasas de coste se actualizan para el plan. |
| [Gestión de tasas de coste - Reales](#unique_10) [página ] 13 | Contable de costes - Gastos generales | Gestión de tasas de coste - Real (F3422) | Las tasas de coste se actualizan para los datos reales. |

## Procedimientos de prueba

### Gestión de tasas de coste - Servicios

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Utilice esta aplicación para introducir tasas de coste basadas en una variedad de criterios. Las tasas de coste son se utiliza en facturaciones de actividad a los siguientes objetos receptores mediante el registro de tiempos o Facturación directa de actividad:

- Centros de coste
- Elementos PEP de proyectos
- Órdenes de servicio

Esta aplicación le permite definir tasas de coste para niveles de coste de servicio y empleados, por lo que es útil para los proveedores de servicios profesionales. Sin embargo, también puede ser utilizado por las empresas de fabricación si hay una necesidad de tasas de coste para el servicio niveles de coste y empleados.

Los siguientes campos están disponibles para la actualización de precios:

- La sociedad (suministradora) siempre se rellena, por lo tanto, no es relevante para el acceso Secuencia
- Empresa a facturar (receptora)
- Precio ICO (indicador)
- Centro de coste (proveedor)
- Clase de actividad (proveedor)
- Nivel de coste de servicio (proveedor)
- Número de personal (proveedor)
- Work item (nuevo) (receptor)
- Elemento PEP (receptor)

El orden de la lista muestra las claves con la prioridad más alta al final de la lista (elemento PEP).

Las siguientes reglas se verifican al actualizar la tabla de precios.

- La sociedad emisora es obligatoria
- Se deben rellenar uno o más de los siguientes campos: Actividad Tipo , Nivel de coste de servicio o bien Personal Número (solo se admite el centro de coste)
- El Número de personal y Centro de coste campos excluidos entre sí como campos clave para un precio. O bien la persona tiene un tasa de coste o el promedio tasa del centro de coste es válida.
- El Número de personal y Nivel de coste de servicio campos se excluyen entre sí como campos clave para un precio. La persona tiene un tasa de coste específica o el promedio uno de los niveles de coste de servicio es válido.
- El centro de coste y el nivel de coste auxiliar son una combinación clave permitida
- Las clases de centro de coste definidas en la clase de actividad controlan los combinaciones de centro de coste y clase de actividad.
- Si se introduce una tasa de coste dentro de la sociedad, se dejará la empresa receptora espacio en blanco
- Las tasas de coste específicas de PEP se pueden utilizar para la actividad entre empresas y dentro de la empresa asignaciones. Si se introduce una empresa receptora y un elemento PEP, el El sistema verifica si el elemento PEP está asignado a la empresa receptora (el El sistema no deriva automáticamente la empresa receptora del PEP elemento, ya que esto puede provocar problemas con las tasas de coste migradas).
- Verificar y fijar el indicador ICO
    - Si la sociedad receptora está vacía, utilice el indicador ICO del usuario entrada
    - Si la sociedad receptora no es igual a la empresa emisora Código, fije el indicador ICO en verdadero
    - De lo contrario, fije el indicador ICO en falso

| Centro de coste | Clase de actividad | Nivel de coste de servicio | Número de personal (empleado) | Work item (recepción) | PEP+Elemento (entrada) | Sociedad a facturar (receptora) | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Emisor | Receptor |  |  |  |  |  |  |
|  | X |  |  |  |  |  | Al menos un campo (clase de actividad, nivel de coste de servicio, Número de personal) debe rellenarse |
|  |  | X |  |  |  |  |  |
| NUNCA |  | NUNCA | X |  |  |  |  |
| NUNCA | X | NUNCA | X |  |  |  | Nº pers.sin CeCo, sin niv.coste serv. |
| X | X |  |  |  |  |  | CeCo + cl.act. |
| X |  | X |  |  |  |  | CeCo + nivel de coste de servicio |
| X | X | X |  |  |  |  | CeCo + tipo act. + nivel de coste de servicio |
|  | X | X |  |  |  |  | clase de actividad + nivel de coste de servicio |
|  | X |  |  | (X) | (X) |  | Se puede rellenar PEP o work item |
|  |  | X |  | (X) | (X) |  |  |
| NUNCA |  | NUNCA | X | (X) | (X) |  |  |
| NUNCA | X | NUNCA | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | Tasas ICO |
|  |  | X |  | (X) | (X) | X |  |
| NUNCA |  | NUNCA | X | (X) | (X) | X |  |
| NUNCA | X | NUNCA | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de tasas de coste - Servicios (F3161) . | El Gestión de tasas de coste - Servicios se visualiza. |  |
| 3 | Sociedad | Realice la siguiente entrada y seleccione Añadir :Sociedad: <sociedad> |  |  |
| 4 | Actualizar tasas de coste de servicios | Realice las siguientes entradas y seleccione Grabar :Empresa receptora : <dejar en blanco>Nota Este campo debería solo se utiliza en el caso de tasas de coste multisociedades; de lo contrario, Dejar en blanco.Centro de coste : <centro de coste>Clase de actividad : <clase de actividad>Elemento PEP : <Esto es opcional campo>De ejercicio : <año actual>De período : <período actual>Tasa : 100Nota Esta tasa se utiliza para contabilizar en todos los ledgers.Moneda : <moneda>Por : 1Unidad de actividad : H | Se crean tasas de coste. |  |

### Gestión de tasas de coste - Plan

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Esta actividad se utiliza para planificar tasas de coste para actividades de centro de coste en una fabricación Entorno. Las tarifas se utilizan en:

- Facturaciones de actividad a órdenes de fabricación y órdenes de mantenimiento
- Cálculo del coste de material

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de tasas de coste - Plan (F3162) . | El Gestión de tasas de coste - Plan se visualiza. |  |
| 3 | Añadir | Seleccionar Añadir . |  |  |
| 4 | Actualizar tasas de coste plan | Realice las siguientes entradas y seleccione Grabar :Coste Centro : <coste centro>Actividad Tipo : <actividad tipo>De fiscal Año : <año actual>De período : <actual período>Moneda : <moneda>Tasa fija : <importe>Variable Tasa : <importe>Nota Esta tasa se utiliza para contabilizar en todos los ledgers. | Las tasas de coste se actualizan para el plan. |  |

### Gestión de tasas de coste - Reales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Esta actividad se utiliza para introducir tasas de coste reales para el centro de coste actividades utilizadas en el cálculo de costes real. Las tasas de coste reales se pueden actualizar por ledger.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de tasas de coste - Real (F3422) . | El Gestión de tasas de coste - Reales se visualiza. |  |
| 3 | Añadir | Seleccionar Añadir . |  |  |
| 4 | Actualizar tasas de coste reales | Realice las siguientes entradas y seleccione Grabar :Coste Centro : <coste centro>Actividad Tipo : <actividad tipo>Ledger : <por ejemplo, 0L o su lead ledger>NotaSi utiliza el cálculo de tasas de coste reales, el sistema calcula las tasas de coste reales por ledger. Si quieres para ver o corregir costes calculados automáticamente tasas, debe introducir un ledger. Tasas de coste reales con campo de ledger en blanco se utilizan para contabilizaciones en todos ledgers. Si existen tasas de coste reales específicas de ledger, el sistema utiliza las tasas específicas de ledger.Para ver la columna de ledger, adapte las opciones en la lista de tasas de coste y seleccione el ledger.De ejercicio : <actual año>De período : <actual período>Moneda : <moneda>Fijo Tasa : <importe>Variable Tasa : <importe>Nota Esta tasa se utiliza para contabilizar en todos los ledgers. | Las tasas de coste se actualizan para los datos reales. |  |

## Análisis

### Visualizar tasas de coste

Objetivo

Este informe le permite seleccionar y visualizar los diferentes tipos de tasa de coste.

Requisito previo

Las tasas de coste ya deben existir.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Visualizar tasas de coste (F5150) . | El Visualizar tasas de coste se visualiza. |  |
| 3 | Criterios de selección | Realice las siguientes entradas y seleccione Ir :Ledger : <deje este campo vacío>Nota Si deja el campo de selección en blanco, se mostrarán las tarifas que son las mismas y se aplican a todos los ledgers (por ejemplo, tarifa plan). Especificación de un libro en la selección limita la visualización de la tasa de coste a las tasas solo actualizado para el/los ledger(s) específico(s) seleccionado(s) y aplicable solo a tasas reales.Centro de coste : <para ejemplo, 10101101>Actividad Tipo : <por ejemplo, 11>De ejercicio Período : <actual período>A ejercicio Período : <actual período> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-355]]
- related-to :: [[06-management-accounting/co-mds-3kw-357]]
- related-to :: [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 24,797 chars in the whole document
