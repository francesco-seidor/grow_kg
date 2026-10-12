---
id: 06-management-accounting/script-de-datos-maestros-crear-datos-maestros-de-asignacion-universal
title: Script de datos maestros - Crear datos maestros de asignación universal - MDS (2US) (2US_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for universal allocation: plan/actual overhead and profit center cycles via Fiori F3338A."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2US_S4CLD2608_Master_Data_ES_XX]
keywords: [Universal Allocation Cycles, universal allocation, plan overhead allocation, actual overhead allocation, profit center distribution, allocation cycle upload, business roles, required master data, cost centers, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-288
topic: 06-management-accounting/universal-allocation
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear datos maestros de asignación universal - MDS (2US) (2US_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear datos maestros de asignación universal - MDS (2US) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894554)

[2 Requisitos previos 3](#_Toc233894555)

[2.1 Acceso al sistema 3](#_Toc233894556)

[2.2 Roles 3](#_Toc233894557)

[2.3 Unidades organizativas necesarias 3](#_Toc233894558)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894559)

[3 Tabla de resumen 5](#_Toc233894560)

[4 Procedimientos de prueba 6](#_Toc233894561)

[4.1 Planificar asignaciones 6](#_Toc233894562)

[4.1.1 Gestionar ciclos de subreparto de gastos generales de plan 6](#_Toc233894563)

[4.1.2 Editar ciclos de subreparto de gastos generales de plan 8](#_Toc233894564)

[4.2 Imputaciones reales 10](#_Toc233894565)

[4.2.1 Gestionar ciclos de subreparto de gastos generales reales 10](#_Toc233894566)

[4.2.2 Editar ciclos de subreparto de gastos generales reales 12](#_Toc233894567)

[4.3 Imputación de centro de beneficio plan 14](#_Toc233894568)

[4.3.1 Gestionar ciclos de distribución de centro de beneficio plan 14](#_Toc233894569)

[4.4 Imputación de centro de beneficio real 16](#_Toc233894570)

[4.4.1 Gestionar ciclos de distribución de centro de beneficio reales 16](#_Toc233894571)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

La asignación universal cubre el subreparto/las distribuciones plan y reales de los centros de coste en el Controlling de gastos generales utilizando varias combinaciones de importes emisor/receptor, porcentajes y porciones. Estos datos maestros admiten la planificación anual por redistribuir el coste mediante ciclos de imputación y distribución predefinidos dentro de una sociedad específica. Asignando las clases de coste a centros de coste en gastos generales Controlling de costes, puede controlar sus costes y comparar los costes plan y reales. En Además, los subrepartos/distribuciones plan y reales de los centros de beneficio también son admitido.

Este script proporciona algunos ejemplos generales de creación de datos maestros con Universal Asignación, pero se puede adaptar a sus necesidades empresariales específicas utilizando las diferentes combinaciones emisor/receptor de importes, porcentajes y partes.

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
| Contable de división | SAP_BR_DIVISION_ACCOUNTANT |  |  |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se han creado en su ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan centros de coste y grupos de centros de coste, según en el enfoque operativo de su empresa.

| Objeto de datos | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad CO | Datos generales | Obligatorio |  |
| Sociedad | Unidades organizativas | Obligatorio |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros del centro de coste y del grupo de centros de coste pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de opcional y objetos de datos maestros obligatorios que se deben utilizar en la asignación.

| Objeto de datos maestros | Obligatorio/Opcional | Comentarios |
| --- | --- | --- |
| Centro de coste | Obligatorio |  |
| Clase de coste | Obligatorio |  |
| Valor estadístico | Opcional |  |
| Centro de beneficio | Obligatorio |  |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

Planificar asignaciones

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Gestionar ciclos de subreparto de gastos generales de plan](#unique_8) [página ] 6 | Contable de costes - Gastos generales | Gestionar asignaciones (F3338A) | Los costes se asignan a grupos de centros de coste, centros de coste o rangos. |
| [Editar ciclos de subreparto de gastos generales de plan](#unique_9) [página ] 8 | Contable de costes - Gastos generales | Gestionar asignaciones (F3338A) | Se editan los ciclos de asignación de gastos generales de plan. |

Imputaciones reales

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Gestionar ciclos de subreparto de gastos generales reales](#unique_10) [página ] 10 | Contable de costes - Gastos generales | Gestionar asignaciones (F3338A) | Los costes se asignan a grupos de centros de coste, centros de coste o rangos. |
| [Editar ciclos de subreparto de gastos generales reales](#unique_11) [página ] 12 | Contable de costes - Gastos generales | Gestionar asignaciones (F3338A) | Se editan los ciclos de asignación de gastos generales reales. |

Imputación de centro de beneficio plan

| Paso de proceso | Rol empresarial | Transacción/Aplicación | RPesults previstos |
| --- | --- | --- | --- |
| [Gestionar ciclos de distribución de centro de beneficio plan](#unique_12) [página ] 14 | Contable de división | Gestionar asignaciones (F3338A) | Se crea la distribución del centro de beneficio plan. |

Imputación de centro de beneficio real

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Gestionar ciclos de distribución de centro de beneficio reales](#unique_13) [página ] 16 | Contable de división | Gestionar asignaciones (F3338A) | Se crea la distribución del centro de beneficio. |

## Procedimientos de prueba

### Planificar asignaciones

#### Gestionar ciclos de subreparto de gastos generales de plan

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

En este ejemplo, el ciclo de subreparto de gastos generales de plan utiliza clases de coste secundario para imputar costes desde un centro de coste o un grupo de centros de coste a otro centro de coste o grupo de centros de coste por un porcentaje fijo dentro del mismo sociedad.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Crear cabecera de ciclo | Seleccione el Crear y seleccione Crear nuevo Ciclo . | El Crear nuevo ciclo se visualiza la ventana de diálogo.Nota Carga en masa de Los ciclos de imputación son posibles para la creación de nuevos imputaciones y/o segmentos nuevos mediante el Gestionar Imputaciones con el Cargar/Descargar plantilla botón. Usted puede descargar una plantilla en blanco o seleccionar una existente ciclo de imputación para descargar como modelo. |  |
| 4 | Introducir valores | Realice las siguientes entradas y seleccione el Crear botón:Ciclo de imputación : <introduzca un ID de ciclo que empiece por Z>Contexto de asignación : <Coste Centros>Tipo de asignación : Gastos generales ImputaciónLedger : 0LVálido hasta : 31/12/2030Descripción de ciclo : <introduzca un ciclo descripción>Sociedad : 1010Real/Plan: PlanCategoría de plan : PLN | El <nuevo ciclo> se visualiza. |  |
| 5 | Introducir datos de segmento | En la sección inferior de la Nuevo ciclo de imputación en la vista Segmentos sección, seleccione la Crear botón y realice las siguientes entradas en el campo Crear nuevo Segmento y seleccione la Crear botón:Nombre de segmento : <introduzca un segmento que empieza por Z>Descripción del segmento: <introduzca un descripción> | El <segmento nuevo> se visualiza. |  |
| 6 | Introducir reglas | Seleccione el segmento nuevo y seleccione la flecha de la derecha.En la Reglas , efectúe las siguientes entradas:Cuenta de asignación de gastos generales : 94201000Regla de emisor : Contabilizado importesRegla de receptor : Fijo porcentajesCuota en %: 100Moneda : <introduzca su configuración local moneda> |  |  |
| 7 | Introducir detalles de emisor | En la Emisores , efectúe las siguientes entradas:Número de cuenta :Modifique el valor en el Valor Tipo columna a GrupoEn la Grupo columna, utilizar la lista desplegable para seleccionar 10_CE en el siguiente Seleccionar: número de cuenta verCentro de coste : 10101101 |  |  |
| 8 | Introducir detalles de receptor | En la Receptores , seleccione Añadir . En el Añadir receptores vista, seleccione Centro de coste y seleccione Añadir . Realice las siguientes entradas:Centro de costeModifique el valor en el Valor Tipo columna a GrupoEn la Grupo columna, utilizar la lista desplegable para seleccionar 1010300 en el siguiente Seleccionar: centro de coste ver |  |  |
| 9 | Base de receptor | En la Base de receptor , seleccione la pestaña … (adicional Opciones) y seleccione Distribuir equitativamente . | Puede ver que los importes se distribuyen equitativamente. |  |
| 10 | Grabar | Seleccione el Grabar botón. | Se han guardado los datos. |  |

#### Editar ciclos de subreparto de gastos generales de plan

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Esta actividad demuestra la capacidad de trabajar con asignaciones que tienen grandes cantidades de datos usando plantillas.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Introducir valores | Realice las siguientes entradas y seleccione el Ir botón:Contexto de asignación : <Centros de coste>Sociedad: 1010Ledger: 0LCiclo de imputación : <el ciclo que acaba de crear> | El Ciclos de imputación se visualiza. |  |
| 4 | Detalles de ciclo de imputación | Seleccione su ciclo de imputación y seleccione la flecha de la derecha para ir a los detalles. Seleccione el Editar botón. | El Gestionar asignaciones se visualiza. |  |
| 5 | Sección Segmentos | Desplácese hacia abajo hasta Segmentos y seleccione su segmento y elija > ( Detalles ) en el derecha. |  |  |
| 6 | Base de receptor | En la Base de receptor , seleccione Cargar/Descargar Valores . | El Cargar valores de receptor se visualiza. |  |
| 7 | Cargar valores de receptor | Seleccionar Descargar plantilla con valores . Descargue y guarde el fichero. |  |  |
| 8 | Actualizar porcentajes | En el archivo, actualice la columna de porcentaje con valores como se muestra a continuación:Centro de costePorcentaje001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | Se actualizan los porcentajes. |  |
| 9 | Base de receptor | Regrese a la Base de receptor y haga lo siguiente:Seleccionar Cargar/Descargar valores .En Cargar valores de receptor vista, seleccionar Explorar . Seleccione su guardado fichero. La pantalla indica si los valores se pueden cargar o si se requieren correcciones. Seleccione Confirmar .Seleccionar Grabar para guardar la asignación ciclo. | Puede ver que los datos se han actualizado mediante la carga del archivo csv. |  |

### Imputaciones reales

#### Gestionar ciclos de subreparto de gastos generales reales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

En este ejemplo, el ciclo de subreparto de gastos generales utiliza el coste secundario elementos para imputar costes de un centro de coste o un grupo de centros de coste a otro centro de coste o grupo de centros de coste por un porcentaje fijo dentro de la misma sociedad.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Crear cabecera de ciclo | Seleccione el Crear y seleccione Crear nuevo Ciclo . | El Crear nuevo ciclo se visualiza la ventana de diálogo. |  |
| 4 | Introducir valores | Realice las siguientes entradas y seleccione el Crear botón:Ciclo de imputación : <introduzca un ID de ciclo que empiece por Z>Contexto de asignación : <Centros de coste>Empresa Código : 1010Tipo de asignación : Gastos generales ImputaciónLedger : 0LVálido hasta : 31/12/2030Descripción de ciclo : <introduzca un ciclo descripción>Sociedad : 1010Real/Plan: Real | El Imputación: Crear ciclo de imputación de gastos generales plan: Datos de cabecera se visualiza. |  |
| 5 | Introducir datos de segmento | En la sección inferior de la Nuevo ciclo de imputación en la vista Segmentos seleccione la sección Añadir y realice las siguientes entradas en el Crear nuevo Segmento ventana:Nombre de segmento : <introduzca un segmento que empiece por Z>Descripción de segmento: <introduzca una descripción> | El Crear un nuevo ciclo se visualiza. |  |
| 6 | Introducir reglas | Seleccione el segmento nuevo y seleccione la flecha de la derecha.En la Reglas , efectúe las siguientes entradas:Cuenta de imputación de gastos generales : 94201000Regla de emisor : Importes contabilizadosRegla de receptor : Porcentajes fijos |  |  |
| 7 | Introducir detalles de emisor | En la Emisores , efectúe las siguientes entradas:Número de cuenta :Modifique el valor en el Tipo de valor columna a GrupoEn la Grupo utilice la lista desplegable para buscar y seleccionar 10_CE en el siguiente Seleccionar: número de cuenta verCentro de coste : 10101101Nota Además a centros de coste estándar y cuentas de mayor, puede ahora utilice atributos de asiento específicos como moneda, área funcional, centro de beneficio y segmento para permitir una selección de imputación más granular dentro de la regla emisora. Para ello, seleccione el Añadir y, a continuación, seleccione el opciones deseadas. |  |  |
| 8 | Introducir detalles de receptor | En la Receptores , seleccione la pestaña + (Añadir) botón.Seleccionar Centro de coste y seleccione la Añadir botón.Realice la siguiente entrada:Centro de costeModifique el valor en el Tipo de valor columna a GrupoEn la Grupo utilice la lista desplegable para buscar y seleccionar 1010300 en el siguiente Seleccionar: centro de coste ver |  |  |
| 9 | Base de receptor | En la Base de receptor , seleccione la pestaña … (adicional Opciones) y seleccione Distribuir equitativamente . | Puede ver que los importes se distribuyen equitativamente. |  |
| 10 | Grabar | Seleccione el Grabar botón. | Se han guardado los datos. |  |

#### Editar ciclos de subreparto de gastos generales reales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Esta actividad demuestra la capacidad de trabajar con asignaciones que tienen grandes cantidades de datos usando plantillas.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de costes - Gastos generales . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Introducir valores | Realice las siguientes entradas y seleccione el Ir botón:Contexto de asignación : <Centros de coste>Sociedad: 1010Ledger: 0LCiclo de imputación : <el ciclo que acaba de crear> | El Ciclos de imputación se visualiza. |  |
| 4 | Detalles de ciclo de imputación | Seleccione su ciclo de imputación y seleccione la flecha de la derecha para ir a los detalles. | El Gestionar asignaciones se visualiza. |  |
| 5 | Sección Segmentos | Desplácese hacia abajo hasta Segmentos y seleccione su segmento y elija > ( Detalles ) en el derecha. |  |  |
| 6 | Base de receptor | En la Base de receptor , seleccione la pestaña Cargar/Descargar Valores . | El Cargar valores de receptor se visualiza. |  |
| 7 | Cargar valores de receptor | Seleccionar Descargar plantilla con valores . Descargue y guarde el fichero. |  |  |
| 8 | Actualizar porcentajes | En el archivo, actualice la columna de porcentaje con valores como se muestra a continuación:Centro de costePorcentaje001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | Se actualizan los porcentajes. |  |
| 9 | Base de receptor | Regrese a la Base de receptor y haga lo siguiente:Seleccionar Cargar/Descargar valores .En Cargar valores de receptor vista, seleccionar Explorar . Seleccione su guardado fichero. La pantalla indica si los valores se pueden cargar o si se requieren correcciones. Seleccione Confirmar .Seleccionar Grabar para guardar la asignación ciclo. | Puede ver que los datos se han actualizado mediante la carga del archivo csv. |  |

### Imputación de centro de beneficio plan

#### Gestionar ciclos de distribución de centro de beneficio plan

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Este ejemplo muestra la distribución plan de saldos de cuentas de balance en y de varios centros de beneficio.

Requisito previo

Debe estar disponible una cuenta de mayor para la compensación de asignaciones. Cree Compensación de imputación CO LM 29500000 utilizando LM 29500100 como referencia. Para obtener más detalles sobre cómo crear un libro mayor, consulte Crear cuenta de mayor y clase de coste - MDS (BNG).

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de división . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Crear cabecera de ciclo | Seleccione el Crear y seleccione Crear nuevo ciclo . | El Crear nuevo ciclo se muestra la ventana de diálogo. |  |
| 4 | Introducir valores | Realice las siguientes entradas y seleccione el Crear botón:Ciclo de imputación : <introduzca un ID de ciclo que empiece por Z>Contexto de asignación : <Centros de beneficio>Empresa Código : 1010Asignación Tipo : DistribuciónLedger : 0LVálido hasta : 31/12/2030Descripción de ciclo : <introduzca un ciclo descripción>Sociedad : 1010Real/Plan: PlanCategoría de plan : PLN | El Gestionar asignaciones Aparece la vista. |  |
| 5 | Introducir datos de segmento | En la sección inferior de la Gestionar Imputaciones en la vista Segmentos seleccione la sección Crear botón y realice las siguientes entradas en el Crear Segmento nuevo ventana:Nombre de segmento : <introduzca otro segmento que empieza por ZD>Descripción de segmento : <indicar una descripción>Seleccionar OK . |  |  |
| 6 | Introducir reglas | En la Reglas pestaña, realice lo siguiente entradas:Moneda: <introduzca su configuración local moneda>Regla de emisor: Importes fijosCuota en % : 100Regla de receptor: Fijo porcentajesSeleccione el Emisores pestaña. |  |  |
| 7 | Introducir detalles de emisor | En la Emisores pestaña, realice lo siguiente entradas:Cuenta Número : 29500000Centro de beneficio : YB600Seleccione el Base de emisor pestaña. |  |  |
| 8 | Base de emisor | Realice la siguiente entrada:Cantidad : 100000Seleccione el Receptores pestaña. |  |  |
| 9 | Introducir detalles de receptor | En la Receptores , seleccione + Añadir . En la Añadir Receptores vista, seleccionar Beneficio Centro . Seleccione el Añadir botón y realice las siguientes entradas:Tipo de valor : IntervaloEntrada individual/De : YB700A valor : YB800Seleccione el Base de receptor pestaña. |  |  |
| 10 | Base de receptor | En la Base de receptor , seleccione la … (Opciones adicionales) y seleccione Distribuir equitativamente . | Puede ver que los importes se distribuyen equitativamente. |  |
| 11 | Grabar | Seleccione el Grabar botón. | Se crea la distribución del centro de beneficio plan. |  |

### Imputación de centro de beneficio real

#### Gestionar ciclos de distribución de centro de beneficio reales

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Contexto

Este ejemplo muestra la distribución real de saldos de cuentas de balance desde y hacia varios centros de beneficio.

Requisito previo

Debe estar disponible una cuenta de mayor para la compensación de asignaciones. Crear LM 29500000 CO Compensación de asignación utilizando LM 29500100 como referencia. Para obtener detalles sobre cómo crear LM, consulte Crear cuenta de mayor y clase de coste - MDS (BNG).

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de división . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar asignaciones (F3338A) . | El Gestionar asignaciones se visualiza. |  |
| 3 | Crear cabecera de ciclo | Seleccione el Crear y seleccione Crear nuevo ciclo . | El Crear nuevo ciclo se muestra la ventana de diálogo. |  |
| 4 | Introducir valores | Realice las siguientes entradas y seleccione el Crear botón:Ciclo de imputación : <introduzca un ID de ciclo que empiece por Z>Contexto de asignación : <Centros de beneficio>Empresa Código : 1010Asignación Tipo : DistribuciónLedger : 0LVálido hasta : 31/12/2030Descripción de ciclo : <introduzca un ciclo descripción>Sociedad : 1010Real/Plan: Real | El Imputación: Crear ciclo de distribución plan: Cabecera Datos Aparece la vista. |  |
| 5 | Introducir datos de segmento | En la sección inferior de la Gestionar Imputaciones en la vista Segmentos seleccione la sección Añadir y realice las siguientes entradas en el Crear segmento nuevo ventana:Nombre de segmento : <introduzca otro segmento que empieza por ZD>Descripción de segmento : <indicar una descripción> | El Imputación: Crear ciclo de distribución plan: Cabecera Datos Aparece la vista. |  |
| 6 | Introducir reglas | Seleccione el segmento recién creado y seleccione el inicio de sesión > derecha. En la Reglas , haga el siguientes entradas:Moneda: <introduzca su configuración local moneda>Regla de emisor: Fijo importesCuota en % : 100Regla de receptor: Fijo porcentajesSeleccione el Emisores pestaña. |  |  |
| 7 | Introducir detalles de emisor | En la Emisores pestaña, realice lo siguiente entradas:Cuenta Número : 29500000Centro de beneficio : YB600Seleccione el Base de emisor pestaña. |  |  |
| 8 | Base de emisor | Realice la siguiente entrada:Cantidad : 100000Seleccione el Receptores pestaña. |  |  |
| 9 | Introducir detalles de receptor | En la Receptores , seleccione + Añadir . En la Añadir Receptores vista, seleccionar Beneficio Centro . Seleccione el Añadir botón y realice las siguientes entradas:Tipo de valor : IntervaloEntrada individual/De : YB700A valor : YB800Seleccione el Base de receptor pestaña. |  |  |
| 10 | Base de receptor | En la Base de receptor , seleccione la … (Opciones adicionales) y seleccione Distribuir equitativamente . | Puede ver que los importes se distribuyen equitativamente. |  |
| 11 | Grabar | Seleccione el Grabar botón. | Se crea la distribución del centro de beneficio. |  |

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
- related-to :: [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287]]
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/mds-2us-291]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 31,334 chars in the whole document
