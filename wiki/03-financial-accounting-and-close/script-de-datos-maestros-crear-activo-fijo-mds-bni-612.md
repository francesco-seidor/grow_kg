---
id: 03-financial-accounting-and-close/script-de-datos-maestros-crear-activo-fijo-mds-bni-612
title: Script de datos maestros - Crear activo fijo - MDS (BNI) (BNI_S4CLD2608_Master_Data_ES_XX)
description: "Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: prerequisites and test procedures to create, change, display, block, delete fixed assets (F3425A)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/fixed-asset-master-data]
aliases: [BNI_S4CLD2608_Master_Data_ES_XX]
keywords: [Fixed Asset Master Records, fixed asset master data, asset classes, number ranges, create fixed asset, subasset creation, legacy data transfer, balance carryforward, change fixed asset, display fixed asset]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-612
topic: 03-financial-accounting-and-close/fixed-asset-master-data
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear activo fijo - MDS (BNI) (BNI_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Fixed Asset Master Records** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear activo fijo - MDS (BNI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894945)

[2 Requisitos previos 3](#_Toc233894946)

[2.1 Acceso al sistema 3](#_Toc233894947)

[2.2 Roles 3](#_Toc233894948)

[2.3 Unidades organizativas necesarias 3](#_Toc233894949)

[2.4 Datos maestros obligatorios y opcionales 4](#_Toc233894950)

[2.5 Parámetros principales para la creación de datos 4](#_Toc233894951)

[2.5.1 Clases de activos fijos y rangos de números 4](#_Toc233894952)

[2.6 Pasos preliminares 6](#_Toc233894953)

[2.6.1 Validar disponibilidad de sistema de contabilidad de activos fijos 6](#_Toc233894954)

[2.6.1.1 Confirmar información de fecha de transferencia 6](#_Toc233894955)

[2.6.1.2 Confirmar ejecución de arrastre de saldos para ejercicio en curso 8](#_Toc233894956)

[3 Tabla de resumen 10](#_Toc233894957)

[4 Procedimientos de prueba 12](#_Toc233894958)

[4.1 Crear activo fijo 12](#_Toc233894959)

[4.2 Modificar activo fijo 14](#_Toc233894960)

[4.3 Visualizar activo fijo 15](#_Toc233894961)

[4.4 Bloquear activos 16](#_Toc233894962)

[4.5 Eliminar activo 17](#_Toc233894963)

[4.6 Crear activo fijo parcial 18](#_Toc233894964)

[4.7 Documentos de modificación para registro maestro de activos fijos 20](#_Toc233894965)

[4.8 Clave de amortización: Visualizar detalles 21](#_Toc233894966)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un activo fijo es un objeto, un derecho u otro elemento propiedad de una empresa que está previsto para un uso a largo plazo y que puede ser individual. identificado en el balance. La actualización de activos fijos implica crear, modificar y visualizar registros maestros de activos fijos.

Los diferentes elementos de información se estructuran según el área de uso y las funciones del sistema para facilitar a los usuarios crear, actualizar y evaluar datos maestros.

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
| Contable encargado de la gestión de activos fijos | SAP_BR_AA_ACCOUNTANT | Activos fijos | SAP_BR_AA_ACCOUNTANT |  |
| Contable de libro mayor | SAP_BR_GL_ACCOUNTANT | Libro mayor | SAP_BR_GL_ACCOUNTANT |  |

### Unidades organizativas necesarias

Los datos maestros de activos fijos dependen de la unidad organizativa de la empresa.

La siguiente tabla ofrece un resumen de esta unidad organizativa:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Datos de sociedad | Sociedad | ID, Descripción, Centro de coste, etc. | Pueden existir datos de sociedad para cada ID de sociedad de su estructura empresarial para la que se utiliza el registro maestro de activos fijos. | <su sociedad> |

### Datos maestros obligatorios y opcionales

Registros de datos maestros de activos fijos puede hacer referencia a otros datos maestros . El La siguiente tabla proporciona un resumen de los objetos de datos maestros opcionales y obligatorios utilizado en un registro de datos maestros de activos fijos.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de coste | En el maestro de activos fijos, encontrará la entrada del centro de coste en el Dependiente del tiempo pestaña. | Obligatorio | Para introducir el centro de coste del activo fijo, debe tener creado el centro de coste antes. En los registros maestros de activos fijos, A continuación, puede introducir el centro de coste real. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son siempre obligatorio para crear datos maestros de activos fijos registro:

#### Clases de activos fijos y rangos de números

Las clases de activos fijos determinan los rangos de números para los ID de registro maestro de activos fijos. No puede modificar la asignación o los ID posteriormente, sino solo transferirlos a otro registro maestro de activos fijos creado para otra clase de activo fijo. Si una clase de activos fijos está asignada a un rango de números interno, no puede introducir el ID de registro maestro de activos fijos manualmente. En este caso, deje el campo en blanco, ya que el sistema selecciona automáticamente un número del rango de números numérico asignado.

Las siguientes clases de activos fijos y los rangos de números correspondientes se definen para activos fijos en la sociedad 1010:

| Clase de activo fijo | Rango de números / ID de registro maestro de activos fijos | Comentarios |
| --- | --- | --- |
| 1000 | Rango de números interno:10000000 – 19999999 | Bienes inmuebles y derechos similares |
| 1100 | Rango de números interno:10000000 – 19999999 | Edificios |
| 1200No relevante para todos los países/regiones | Rango de números interno:10000000 – 19999999 | Mejoras en el terreno |
| 1500No relevante para todos los países/regiones | Rango de números interno:10000000 – 19999999 | Mejoras de arrendamiento |
| 2000 | Rango de números interno:20000000 – 29999999 | Maquinaria y equipo |
| 3000 | Rango de números interno:30000000 – 39999999 | Mobiliario y enseres |
| 3100 | Rango de números interno:50000000 – 59999999 | Vehículos |
| 3200 | Rango de números interno:60000000 – 69999999 | Hardware informático |
| 3210 | Rango de números interno:60000000 – 69999999 | Software informático |
| 3300 | Rango de números interno:30000000 – 39999999 | Equipo de oficina |
| 4000 | Rango de números interno:40000000 – 49999999 | Activos fijos en curso (materiales) |
| 4010 | Rango de números interno:40000000 – 49999999 | Activos fijos en curso (inmateriales) |
| 4001 | Rango de números interno:40000000 – 49999999 | AFC como medida de inversión (material) |
| 4011 | Rango de números interno:40000000 – 49999999 | AFC como medida de inversión (inmaterial) |
| 5000 | Rango de números interno:80000000 – 89999999 | Activos de poco valor |
| 8200 | Rango de números interno:90000000 – 99999999 | Fondo de comercio |
| 8300 | Rango de números interno:80000000 - 89999999 | Otros activos fijos inmateriales |
| 9000 | Rango de números interno:90000000 - 99999999 | Activos solo fiscales |

### Pasos preliminares

#### Validar disponibilidad de sistema de contabilidad de activos fijos

##### Confirmar información de fecha de transferencia

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, se confirman los valores para la fecha de transferencia de datos, el estado y la clase de documento para introducir activos fijos antiguos.

|  |
| --- |
| Nota Una vez finalizada la activación de contenido inicial, debe definir una fecha de transferencia. Esto define el ejercicio actual y el último ejercicio cerrado en la contabilidad de activos fijos. La fecha de transferencia es crítica para el procesamiento del sistema, ya que identifica el momento en el tiempo que Se cargan los valores de activos fijos antiguos. Para SAP S/4HANA Cloud Public Edición sistemas, normalmente es el día de fin del año anterior. Por ejemplo, si el sistema está en FY-2020 y la empresa está en un año fiscal natural estándar, la fecha de TAKEOVER es el 31/12/2020. |

|  |
| --- |
| Atención Esto implica que la carga de activos antiguos antiguos es a finales de 2020. |

Procedimiento

| Paso de proceso# | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado/No aprobado/Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación Fiori | Abierto Definir opciones de sociedad - Específico de contabilidad de activos fijos (F7312) . | El Visualizar opciones para sociedad en contabilidad de activos fijos se visualiza.Para cambiar entre modo de modificación y de visualización, seleccione Modificar / Visualizar . |  |
| 3 | Seleccionar sociedad | Seleccione su sociedad en la parte izquierda de la pantalla y seleccione Seleccionar sociedad . |  |  |
| 4 | Opciones generales | Seleccione el Opciones generales pestaña. |  |  |
| 5 | Verificar las opciones generales | Verifique el estado de su empresa. | El Información general muestra las opciones de la sociedad. El Estado de sociedad debería ser Para pruebas . |  |
| 6 | Actualizar parámetros para la transferencia de datos existentes | En la Transferencia de datos existentes sección, verificar o modifique las siguientes entradas:Nota Si es necesario, cree primero un nuevo segmento de transferencia existente seleccionando Crear segmento de transferencia existente .Fecha de transferencia : para fines de prueba esta fecha hasta el ÚLTIMO DÍA DEL FIN DEL EJERCICIO ANTERIOREstado de transferencia de datos existentes : para fines de prueba, fije este estado en ONGOING (otras contabilizaciones permitidas)Clase de documento : para fines de prueba esto a AANota Para el Fecha de transferencia valor, normalmente es una fecha de fin de año para un año anterior. Si se le indica que utilice una fecha de mitad de año, esta sería una fecha de fin de mes. La fecha siempre debe avanzar (no modificarla hacia atrás).Nota Para el Estado de transferencia de datos existentes valor, usted tienen cuatro opciones:En preparación: el sistema permite el Customizing incompleto opciones para la transferencia de datos existentes (no hay contabilizaciones de documentos permitido en esta fase).En curso: solo se permiten contabilizaciones de transferencia de datos existentes (para por ejemplo, otros tipos de contabilizaciones, altas, bajas son no permitido).En curso (otras contabilizaciones permitidas): Ambas transferencias de datos existentes Se permiten contabilizaciones y otras contabilizaciones. Este estado hace cuando realiza más transferencias de datos existentes en un sociedad que ya es productiva.Completada: la transferencia de datos existentes se ha completado. Datos antiguos Los traspasos no están permitidos y usted no puede crear activos fijos antiguos. |  |  |
| 7 | Grabar las modificaciones | Seleccionar Menú > General > Grabar . |  |  |

##### Confirmar ejecución de arrastre de saldos para ejercicio en curso

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, se confirma que el arrastre de saldos se ha ejecutado para el ejercicio en curso.

|  |
| --- |
| Nota Si su implementación no utiliza un ledger específico, ignore ese ledger. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable de libro mayor . |  |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Programación de tareas de libro mayor (F1927) . |  |  |
| 3 | Crear | Seleccionar Crear . |  |  |
| 4 | Introducir detalles | Realice las siguientes entradas y seleccione Paso 2 :Modelo de job : Arrastre de saldosNombre de job : Arrastre de saldos |  |  |
| 5 | Introducir detalles | Realice las siguientes entradas y seleccione Paso 3 :Iniciar inmediatamente : Seleccionado |  |  |
| 6 | Introducir detalles | Realice las siguientes entradas y seleccione Programar :Ledger : <ledger> , por ejemplo, 0LSociedad : <sociedad>Arrastrar a ejercicio : <ejercicio>Ejecución de test : Seleccionado | Ha programado la ejecución del job como una ejecución de prueba. |  |
| 7 | Revisar resultados | Para revisar los resultados de su ejecución de prueba, busque su ejecución en la Jobs y seleccione el botón de flecha a la derecha de su fila. |  |  |
| 8 | Detalles de ejecución | Seleccione el Detalles de ejecución pestaña. Revise el estado del log. |  |  |
| 9 | Ejecución productiva | Para realizar una ejecución productiva, repita este proceso, pero desmarque Ejecución de test . | Ha programado la ejecución del job como una ejecución productiva. |  |

## Tabla de resumen

Este elemento de alcance consta de los pasos de proceso que se enumeran en la siguiente tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear activo fijo](#unique_12) [página ] 12 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | El maestro de activos fijos se crea a nivel de sociedad (plan de valoración). |
| [Modificar activo fijo](#unique_13) [página ] 14 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | Se ha actualizado el maestro de activos fijos. |
| [Visualizar activo fijo](#unique_14) [página ] 15 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | Se visualiza el maestro de activos fijos. |
| [Bloquear activos](#unique_15) [página ] 16 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | El activo fijo está bloqueado. |
| [Eliminar activo](#unique_16) [página ] 17 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | Se ha borrado el maestro de activos fijos. |
| [Crear activo fijo parcial](#unique_17) [página ] 18 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | Se ha creado el subactivo. |
| [Documentos de modificación para registro maestro de activos fijos](#unique_18) [página ] 20 | Contable encargado de la gestión de activos fijos | Abierto Gestionar activos fijos (F3425A) | Se visualizan todas las modificaciones pasadas de un registro de datos maestros de activo fijo existente (activo principal o parcial). |
| [Clave de amortización: Visualizar detalles](#unique_19) [página ] 21 | Contable encargado de la gestión de activos fijos | Clave de amortización: Visualizar detalles (FAA_DEPRKEY_SHOW)Nota Si ha activado el feature toggle para el nuevo diseño, la aplicación Clave de amortización: Visualizar detalles (FAA_DEPRKEY_SHOW) no se aplicará. | Con esta aplicación, se proporciona la información sobre las opciones detrás de las claves de amortización suministradas por el contenido estándar. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Crear activo fijo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, puede crear un nuevo registro de datos principal de activo fijo como parte de sus operaciones diarias.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir detalles de maestro de activos | Seleccionar Crear > Crear activo principal .Realice las siguientes entradas:Sociedad : <Su sociedad>Clase de activo fijo : <Clase de activos fijos para la que desea crear un activo fijo nuevo>Postcapitalización : <Solo es necesario si desea utilizar este registro maestro para contabilizar una postcapitalización>Se pueden utilizar datos maestros de activos fijos de referencia. Si es necesario, el activo fijo que se debe utilizar como referencia debe introducirse en la Número principal de activo fijo en el campo Referencia sección.Seleccionar OK . | El Crear activo principal se visualiza. |  |
| 4 | Introducir descripción de activo fijo y unidad de medida base | Realice las siguientes entradas:Descripción : <Su descripción de activo>Unidad de medida base : <Introduzca la unidad de medida necesaria> |  |  |
| 5 | Seleccione la etiqueta Datos temporales. | Seleccione el Datos dependientes del tiempo pestaña. | El Datos dependientes del tiempo se visualiza. |  |
| 6 | Introducir centro de coste | Realice las siguientes entradas:Centro de coste : <Su centro de coste>Elemento PEP : <Su elemento PEP>Nota Centro de coste y/o Elemento PEP se pueden introducir como colector de costes para la amortización. |  |  |
| 7 | Introducir fecha de capitalización | Solo tiene que introducir la Capitalizado el fecha en la que el activo fijo se ha creado con el postcapitalización indicador.Capitalizado el : <Su fecha de capitalización> |  |  |
| 8 | Verificar otras fichas | Vaya a otras pestañas y realice las entradas o modificaciones necesarias. |  |  |
| 9 | Introducir, verificar o adaptar parámetros de amortización | Realice las siguientes entradas para todas las áreas de valoración disponibles:ClvD : <Su clave de amortización>Nota Si ha activado el feature toggle para el nuevo diseño, utilice el perfil de amortización en lugar de la clave de amortización.Vida útil : <Vida útil en años>Pr. : <Vida útil en períodos> | Todos los parámetros de amortización necesarios se han actualizado correctamente. |  |
| 10 | Grabar nuevo maestro de activos fijos | Seleccionar Crear para guardar sus entradas. | Se crea el registro maestro de activos fijos. El mensaje del sistema confirma la creación y muestra el nuevo número de activo fijo. |  |

### Modificar activo fijo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, puede modificar un registro de datos maestros de activos fijos existente (principal o subnúmero) como parte de sus operaciones diarias.

|  |
| --- |
| Nota La modificación de la clase de activos fijos solo es posible mediante una transferencia dentro de la sociedad a un nuevo registro maestro de activos fijos creado dentro de la nueva clase de activos fijos. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas:Sociedad : <Su sociedad>Activo fijo : <Su número de activo fijo>Seleccionar Ir .Seleccione su número de activo fijo de la tabla utilizando el enlace con su número de activo fijo.En la siguiente pantalla, seleccione Editar . | El Gestionar activos fijos se visualiza.Nota Las capacidades de visualización, modificación y borrado están disponibles seleccionando el activo, marcando la acción que se va a visualizar en la ventana de diálogo y, a continuación, seleccionando de nuevo esa acción. |  |
| 4 | Modificar maestro de activos fijos | Realice las modificaciones necesarias en los datos maestros del activo fijo. | Se realizan las modificaciones necesarias. |  |
| 5 | Grabar el maestro de activos fijos modificado | Seleccionar Crear para guardar sus entradas.Nota El sistema muestra un Correcto notificación. Debe verificar las modificaciones. | Se han grabado las modificaciones del maestro de activos fijos.Las modificaciones realizadas se visualizan en la Documento de modificación pestaña. |  |

### Visualizar activo fijo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, puede visualizar un registro de datos de activos fijos existente (principal o subnúmero) como parte de sus operaciones diarias.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas:Sociedad : <Su sociedad>Activo fijo : <Su número de activo fijo>Subnúmero : <Su subnúmero de activo fijo en caso>Seleccionar Ir .Seleccione su Número de activo fijo , de la tabla utilizando el enlace con su número de activo fijo.Revise su registro maestro de activos fijos seleccionando cada Pestaña página. |  |  |

### Bloquear activos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad se bloquea un registro de datos maestros de activos fijos existente (número principal o subnúmero) para otras altas.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas y seleccione Ir :Sociedad : <Su sociedad>Activo fijo : <Su número de activo fijo> | El Gestionar activos fijos se visualiza. |  |
| 4 | Fijar el indicador de bloqueo | Seleccione su Número de activo fijo de la tabla.En la nueva pantalla, seleccione Bloquear .Nota El Activo fijo <Número de activo fijo> bloqueado se visualiza la notificación. | El indicador de bloqueo está fijado.El activo fijo está bloqueado contra otras altas.Las modificaciones realizadas se visualizan en el Documento de modificación pestaña. |  |

### Eliminar activo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad puede borrar un registro de datos maestros de activo fijo existente (número principal o subnúmero).

|  |
| --- |
| Nota Solo se pueden borrar directamente los activos fijos sin fecha de capitalización y sin valores. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas y seleccione Ir :Sociedad : <Su sociedad>Activo fijo : <Su número de activo fijo> |  |  |
| 4 | Fijar el indicador de borrado | Seleccione su Número de activo fijo y, en la nueva pantalla, seleccione Borrar . | El indicador está fijado. |  |
| 5 | Confirmar | A ¿Desea eliminar el objeto? se muestra un mensaje en la pantalla. Seleccionar Borrar para confirmarlo. |  |  |

### Crear activo fijo parcial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, puede crear un nuevo registro de datos de activo parcial de activo fijo como parte de sus operaciones diarias.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir referencia de activo principal | El Gestionar activos fijos , seleccione Crear activo > Crear activo fijo parcial .Realice las siguientes entradas y pulse Intro :Sociedad : <Su sociedad>Activo fijo : <Número principal de activo para el que desea crear un activo parcial>Postcapitalización : <Solo es necesario si desea utilizar este registro maestro para contabilizar una postcapitalización> | El Crear subactivo se visualiza.El General se visualiza. |  |
| 4 | Introducir datos generales | El General , efectúe las siguientes entradas:Descripción de activo fijo : <Su descripción de activo>Unidad de medida : <Unidad de medida>Capitalizado el : <Su fecha> |  |  |
| 5 | Datos dependientes del tiempo | Seleccione el Datos dependientes del tiempo pestaña. |  |  |
| 6 | Centro de coste o elemento PEP | Realice, verifique o adapte las siguientes entradas:Centro de coste : <Su centro de coste>O bien Elemento PEP : <Su elemento PEP> |  |  |
| 7 | Verificar otras fichas | Vaya a las otras pestañas y realice las entradas o modificaciones necesarias. | Se han rellenado todos los campos maestros de activos fijos necesarios. |  |
| 8 | Introducir, verificar o adaptar parámetros de amortización | Para todas las áreas de valoración disponibles, si es necesario, realice o adapte las siguientes entradas:ClvD : <Su clave de amortización>Nota Si ha activado el feature toggle para el nuevo diseño, utilice el perfil de amortización en lugar de la clave de amortización.Vida útil : <Su vida útil en años>Pr. : <Su vida útil en períodos> | Todos los parámetros de amortización necesarios se han actualizado correctamente. |  |
| 9 | Grabar activo fijo parcial nuevo | Guarde las entradas. | Se crea el activo parcial maestro de activos.El subactivo empieza por 1, por ejemplo, xxxxx-1 . |  |

### Documentos de modificación para registro maestro de activos fijos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad, puede visualizar todas las modificaciones pasadas de un registro de datos maestros de activo fijo existente (número principal o subnúmero).

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar activos fijos (F3425A) . | El Gestionar activos fijos se visualiza. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas y seleccione Ir :Sociedad : <Su sociedad>Número de activo fijo : <Su número de activo fijo>Subnúmero de activo fijo : <Su subnúmero de activo fijo> | El Modificaciones en los registros maestros de activos fijos se visualiza. |  |

### Clave de amortización: Visualizar detalles

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta actividad puede visualizar todas las modificaciones pasadas de un registro de datos maestros de activo fijo existente. (activo principal o parcial).

|  |
| --- |
| Nota Si ha activado el feature toggle para el nuevo diseño, la aplicación Clave de amortización: Visualizar detalles (FAA_DEPRKEY_SHOW) no se aplicará. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Contable encargado de la gestión de activos fijos . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Clave de amortización: Visualizar detalles (FAA_DEPRKEY_SHOW) . | Se abre la aplicación. |  |
| 3 | Introducir información de activo fijo | Realice las siguientes entradas y seleccione Ejecutar :Plan de valoración : <Plan de valoración>Clave de amortización : <Clave de amortización> | El Clave de amortización <XXXX> en el plan de valoración <XXXX> se visualiza.Se visualizan las opciones detrás de la clave de amortización seleccionada. |  |

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
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6]]
- related-to :: [[03-financial-accounting-and-close/mds-bni-613]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 36,141 chars in the whole document
