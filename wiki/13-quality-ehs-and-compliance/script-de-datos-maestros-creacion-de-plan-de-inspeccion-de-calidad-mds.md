---
id: 13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds
title: Script de datos maestros - Creación de plan de inspección de calidad - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_ES_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating quality inspection plans and prerequisites: catalogs, characteristics, sampling, dynamic modification."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/inspection-plans]
aliases: [BNQ_S4CLD2608_Master_Data_ES_XX]
keywords: [Quality Inspection Plans, inspection plans, inspection plan management, master inspection characteristics, class characteristic link, sampling schemes, sampling procedures, dynamic modification rules, code groups, selected sets]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-654
topic: 13-quality-ehs-and-compliance/inspection-plans
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Creación de plan de inspección de calidad - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Quality Inspection Plans** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Creación de plan de inspección de calidad - MDS (BNQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233895041)

[2 Requisitos previos 4](#_Toc233895042)

[2.1 Acceso al sistema 4](#_Toc233895043)

[2.2 Roles 4](#_Toc233895044)

[2.3 Unidades organizativas necesarias 4](#_Toc233895045)

[2.4 Datos maestros obligatorios y opcionales 5](#_Toc233895046)

[2.5 Condiciones empresariales 6](#_Toc233895047)

[2.6 Parámetros principales para la creación de datos 6](#_Toc233895048)

[2.6.1 Rangos de números 6](#_Toc233895049)

[3 Tabla de resumen 7](#_Toc233895050)

[4 Procedimientos de prueba 8](#_Toc233895051)

[4.1 Atributos de característica - Editar grupos de códigos para conjuntos de selección 8](#_Toc233895052)

[4.2 Editar conjuntos seleccionados para atributos de característica 9](#_Toc233895053)

[4.3 Editar grupos de códigos para defectos (opcional) 10](#_Toc233895054)

[4.4 Crear método de inspección (opcional) 11](#_Toc233895055)

[4.5 Crear características de inspección maestras (opcional) 13](#_Toc233895056)

[4.6 Crear característica de inspección maestra con referencia a característica de clase (opcional) 17](#_Toc233895057)

[4.7 Crear esquema de muestreo (opcional) 19](#_Toc233895058)

[4.8 Crear procedimiento de muestreo (opcional) 22](#_Toc233895059)

[4.9 Crear regla de dinamización (opcional) 23](#_Toc233895060)

[4.10 Crear plan de inspección 26](#_Toc233895061)

[4.11 Gestión de planes de inspección 28](#_Toc233895062)

[4.12 Copiar de planes de inspección existentes 32](#_Toc233895063)

[4.13 Visualizar lotes de inspección abiertos 33](#_Toc233895064)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Si se supone que se debe inspeccionar la calidad del material, uno de los requisitos previos es que un el plan de inspección está disponible. Por ejemplo, es posible que se requiera una inspección en las mercancías proceso de entrada del proveedor o de la orden de fabricación, el plan de inspección debe contienen algunos detalles sobre las características que se deben inspeccionar, cómo deben ser inspeccionado y, por ejemplo, cuántas muestras se deben verificar.

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
| Técnico de calidad | SAP_BR_QUALITY_TECHNICIAN | Inspección de calidad | SAP_BR_QUALITY_TECHNICIAN |  |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas del centro. la siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas:

| Segmento de datos | Depende de | Ejemplos de campos | Comentarios | Unidad organizativa a utilizar |
| --- | --- | --- | --- | --- |
| Conjuntos seleccionados para atributos de característica - Editar conjuntos seleccionados | Centro | Conjunto seleccionado, etc. | Los conjuntos seleccionados combinan diferentes grupos de códigos y códigos a nivel de centro que son útiles para determinadas aplicaciones | Centro: |
| Crear método de inspección | Centro | Método de inspección | El método de inspección se puede utilizar en un plan de inspección |  |
| Crear características de plan de inspección | Centro | Caract.insp.maestra, asignación conjunto selección, etc. | Las características de inspección maestras se pueden utilizar en un plan de inspección. | Centro: |
| Crear plan de inspección | Centro | Asignación a un número de material, utilización, estado, puesto de trabajo, etc. | Los datos de centro se asignan para cada ID de centro de su estructura empresarial para un plan de inspección | Centro: |

### Datos maestros obligatorios y opcionales

La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un registro de datos del plan de inspección de calidad.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Grupo de códigos/Conjunto seleccionado: para atributo de característica |  | Obligatorio | Debe crearse grupo de códigos/conjunto seleccionado para atributo de característica antes de crear un plan de inspección |
| Grupo de códigos – para defectos |  | Opcional | Grupo de códigos – para Defectos se puede crear antes de crear un plan de inspección |
| Métodos de inspección |  | Opcional | Los métodos de inspección se pueden crear antes de crear una inspección plan |
| Características de inspección maestras |  | Opcional | Las características de inspección maestras se pueden crear antes de crear un plan de inspección |
| Plan de muestreo |  | Opcional | El plan de muestreo define una colección de instrucciones de muestreo que se pueden creado antes de crear un plan de inspección |
| Procedimiento de muestreo |  | Opcional | El procedimiento de muestreo define las reglas que especifican cómo el sistema calcula el tamaño de la muestra y el procedimiento se puede crear antes crea un plan de inspección |
| Regla de dinamización |  | Opcional | La regla de dinamización contiene la definición de inspección etapas y la condición para el cambio de etapa de inspección. Una dinámica La regla de modificación se puede crear antes de crear una inspección plan |

### Condiciones empresariales

Antes de que se pueda probar este elemento de alcance, cumpla las siguientes condiciones empresariales.

| Elemento de alcance | Condición empresarial |
| --- | --- |
| BNY - Creación de atributos de gestión de calidad para maestro de materiales/productos - MDS | El maestro de materiales debe crearse antes de crear un plan de inspección. |
| 2ZW - Crear datos maestros de gestión de lotes - MDS (opcional) | Si los resultados de inspección se deben transferir a la clase de lote al realizar la utilización decisión, asegúrese de que se cumplen los siguientes requisitos previos. También tenga en cuenta que una característica de clase debe estar asignada a una inspección maestra característica (véase sección de este documento):Debe existir la característica de clase.Clase de lote (tipo 023) debe existir.Se debe asignar la característica de clase a la clase del tipo 023.El material debe gestionarse en lotes y La clase de lote se ha asignado al maestro de materiales en el vista de clasificación.Nota Si la decisión de empleo y el El índice de calidad correspondiente debe transferirse al lote clasificación, característica de clase LOBM_UDCODE y LOBM_QSCORE, respectivamente, debe asignarse a la clase de lote. Tenga en cuenta que allí no es necesario enlazar estas características con una inspección maestra característica en este caso. |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y siempre son necesarios para crear un plan de inspección.

#### Rangos de números

Los siguientes rangos de números se definen para los planes de inspección y los funcionalidad:

| Rango de números | Rango / ID de interlocutor comercial | Comentarios |
| --- | --- | --- |
| Numérico externo | 50000000 a 59999999 | Este rango es para el plan de inspección |

## Tabla de resumen

Este elemento de alcance consta de varios pasos de proceso que se enumeran a continuación tabla:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Paso de proceso | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| [Atributos de característica - Editar grupos de códigos para conjuntos de selección](#unique_11) [página ] 8 | Planificador de calidad | Editar grupos de códigos (QS41) | El grupo de códigos y los códigos de atributos de característica son creado. |
| [Editar conjuntos seleccionados para atributos de característica](#unique_12) [página ] 9 | Planificador de calidad | Editar conjuntos seleccionados (QS51) | Se ha creado el conjunto seleccionado para los atributos de característica. |
| [Editar grupos de códigos para defectos (opcional)](#unique_13) [página ] 10 | Planificador de calidad | Editar grupos de códigos (QS41) | Se han creado grupos de códigos. |
| [Crear método de inspección (opcional)](#unique_14) [página ] 11 | Planificador de calidad | Crear método de inspección (QS31) | Se ha creado el método de inspección. |
| [Crear características de inspección maestras (opcional)](#unique_15) [página ] 13 | Planificador de calidad | Crear característica de inspección maestra (QS21) | Se han creado características de inspección maestras. |
| [Crear característica de inspección maestra con referencia a característica de clase (opcional)](#unique_16) [página ] 17 | Planificador de calidad | Crear característica de inspección maestra (QS21) | Característica de inspección maestra cuantitativa con enlace a clase Se ha creado la característica. |
| [Crear esquema de muestreo (opcional)](#unique_17) [página ] 19 | Planificador de calidad | Crear esquema de muestreo (QDP1) | Se ha creado el esquema de muestreo. |
| [Crear procedimiento de muestreo (opcional)](#unique_18) [página ] 22 | Planificador de calidad | Crear procedimiento de muestreo (QDV1) | Se ha creado el procedimiento de muestra. |
| [Crear regla de dinamización (opcional)](#unique_19) [página ] 23 | Planificador de calidad | Crear regla de dinamización (QDR1) | Se ha creado la regla de dinamización. |
| [Crear plan de inspección](#unique_20) [página ] 26 | Planificador de calidad | Crear plan de inspección (QP01) | Se ha creado el plan de inspección. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Atributos de característica - Editar grupos de códigos para conjuntos de selección

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Atributos de característica hace referencia a un catálogo de gestión de calidad (QM) estándar que define los posibles estados de los atributos inspeccionados. Los códigos se agrupan en grupos de códigos para que se defina una estructura jerárquica.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Editar grupos de códigos (QS41) . | El Tratar catálogo: Imagen inicial muestra. |  |
| 3 | Introducir catálogo | En la Tratar catálogo: Imagen inicial efectúe las siguientes entradas:Catálogo : por ejemplo, 1Grupo de códigos : *Seleccionar Continuar . | El Modificar vista "Actualizar grupos de códigos": Pantalla de resumen muestra. |  |
| 4 | Actualizar grupos de códigos | Seleccionar uno Grupo de códigos , por ejemplo SUPERFICIE , y haga doble clic en Códigos en Estructura de diálogo . | El Modificar vista "Grupo de códigos": Pantalla de resumen muestra. |  |
| 5 | Crear códigos | El Modificar resumen de vista "Códigos" , seleccione Entradas nuevas y realice las siguientes entradas:Código : Por ejemplo, 0010 , 0020 , y así elTexto breve para código : <Introduzca su descripción> |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

### Editar conjuntos seleccionados para atributos de característica

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Los conjuntos seleccionados combinan diferentes grupos de códigos y códigos a nivel de centro. Estos conjuntos de selección son útiles para determinados escenarios como caracterizar posibles resultados de análisis para un determinado atributo de producto (por ejemplo, propiedades de superficie).

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Editar conjuntos seleccionados (QS51) . | Se abre la aplicación. |  |
| 3 | Introducir catálogo\centro\conjunto seleccionado | El Tratar conjunto de selección: Imagen inicial , efectúe las siguientes entradas:Catálogo : 1Centro : <código de centro>Conjunto seleccionado : *Pulsar Intro . | El Modificar vista "Conjuntos de selección": Resumen se visualiza. |  |
| 4 | Actualizar conjuntos seleccionados | Seleccione un Conjunto seleccionado , por ejemplo, SMOOTH y, a continuación, haga doble clic en Códigos de conjunto seleccionado en el Estructura de diálogo . | El Modificar resumen de vista "Códigos de conjunto de selección" se visualiza. |  |
| 5 | Crear códigos de conjunto de selección | El Modificar resumen de vista "Códigos de conjunto de selección" , seleccione Entradas nuevas y realice las siguientes entradas:Grupo de códigos : <valor de grupo de códigos>Código : <valor de código>Código de valoración : o Aceptado (OK) o bien Rechazado (no OK)Clase de defecto : Defecto mayor |  |  |
| 6 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

### Editar grupos de códigos para defectos (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Utilice grupos de códigos para categorizar o clasificar posibles defectos de calidad.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Editar grupos de códigos (QS41) . | El Editar catálogo: Vista inicial muestra. |  |
| 3 | Introducir datos iniciales | Realice las siguientes entradas:Catálogo : por ejemplo, 9Grupo de códigos por ejemplo, DEF-SURFSeleccionar Continuar . | El Modificar vista "Actualizar grupos de códigos": Resumen Aparece la vista. |  |
| 4 | Actualizar grupos de códigos | En el área de Actualizar grupos de códigos , efectúe las siguientes entradas:Texto breve : por ejemplo, Defectos de superficie | Asegúrese de que Estado de grupo de códigos es Liberado . |  |
| 5 | Actualizar códigos de grupos de códigos | En la Actualizar grupos de códigos seleccione una posición que haya creado.Navegar a Códigos en el estructura de diálogo y haga doble clic en "Códigos" . | El Modificar vista "Códigos": Resumen Aparece la vista. |  |
| 6 | Actualizar códigos de grupos de códigos | En la vista de Modificar vista "Códigos": Resumen , seleccione Entradas nuevas .Realice las siguientes entradas:Código : por ejemplo, 0010Texto breve para código : por ejemplo, Problema de superficieClase de defecto : por ejemplo, Defecto mayorPara grabar los datos, seleccione Grabar . | Se actualizan los grupos de códigos. |  |

### Crear método de inspección (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear método de inspección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear método de inspección (QS31) . | El Crear método de inspección: Inicial Pantalla aparece. |  |
| 3 | Introducir datos iniciales | Realice las siguientes entradas:Centro : <Centro Código>Método de inspección: por ejemplo, SUPERFICIEInicio de validez : por ejemplo, <fecha actual>Seleccionar Método de inspección . | El Crear método de inspección: Datos generales Aparece la pantalla. |  |
| 4 | Introducir datos generales | Realice las siguientes entradas:Estado : LiberadoTexto breve : por ejemplo, SuperficieCampo de búsqueda : por ejemplo, Superficie |  |  |
| 5 | Introducir texto explicativo | Seleccionar Crear texto explicativo junto al Texto breve campo e introduzca un texto descriptivo, por ejemplo:Inspeccione minuciosamente la superficie, especialmente en lo que respecta a la rugosidad y si hay arañazos o abolladuras .Seleccionar Volver . |  |  |
| 6 | Grabar datos | Para grabar los datos, seleccione Grabar |  |  |
| 7 | Acceder a la aplicación SAP Fiori | Seleccionar Modificar método de inspección . | El Modificar versión de método de inspección: Pantalla inicial muestra |  |
| 8 | Introducir datos iniciales | Realice las siguientes entradas:Centro : <Código de centro>Método de inspección : por ejemplo, SUPERFICIESeleccionar Método de inspección . | El Modificar versión de método de inspección: Datos generales ver aparece. |  |
| 9 | Seleccionar un documento para adjuntar | Seleccionar Documentos de General Información . |  |  |
| 10 | Crear anexo para documento | Seleccionar Crear documento .En la Modificar versión de método de inspección: Datos generales ventana de diálogo, seleccionar Continuar/Intro sin introducir datos.Confirme el mensaje de carga de archivo seleccionando OK y seleccione un archivo de su archivo sistema mediante doble clic.Seleccionar Transferir para volver a Modificar versión de método de inspección: General Datos pantalla. |  |  |
| 11 | Grabar datos | Para grabar los datos, seleccione Grabar . |  |  |

### Crear características de inspección maestras (opcional)

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear característica de inspección maestra (QS21) . | Crear característica de inspección maestra: Vista inicial aparece. |  |
| 3 | Introducir datos de centro | En la Crear característica de inspección maestra: Inicial ver , efectúe las siguientes entradas:Centro : <Centro Código>Caract.insp.maestra : <valor> , por ejemplo, YQUALI01Inicio de validez : <actual fecha>Seleccionar Característica de inspección maestra | Crear característica de inspección maestra: General Datos Aparece la vista. |  |
| 4 | Introducir datos generales para característica cualitativa | En la Crear característica de inspección maestra: General Datos , realice las siguientes entradas:Caract.cualitativa : marcadoTexto breve : por ejemplo, SuperficieCampo de búsqueda : por ejemplo, SuperficieEstado : Seleccionar Liberado y Referencia CaracterísticaSeleccionar Intro . | Aparece una ventana nueva, Editar control de característica IndicadoresCaracterística de referenciaSi utiliza la característica de inspección maestra en una inspección plan, primero se crea una referencia a esta característica. Sin embargo, puede cancelar esta referencia y modificar los datos individualmente, por ejemplo, tolerancias. Las opciones opcionales son en los pasos siguientes.Modelo de copia completoSi utiliza el maestro característica de inspección en un plan de inspección, la referencia para esta característica se cancela. Puede modificar inmediatamente los datos, por ejemplo, las tolerancias. Solo entonces, puede utilizar esta característica de inspección maestra como modelo para copiar.Modelo de copia incompletoSi utiliza el maestro característica de inspección en un plan de inspección, solo se puede utilizado en un modelo de copia. Este tipo de inspección maestra La característica no se puede utilizar en un material especificación. |  |
| 5 | Editar indicadores de control para cualitativo Características | En la Editar indicadores de control de característica vista, marque las siguientes opciones:Atributo caract.Procedimiento de muestreoGrabación de totalesCaract.oblig.Seleccionar Continuar para marcar más opciones.Alcance fijoSin documentaciónSeleccionar Continuar para salir de la edición. | El Editar indicadores de control de característica ver muestra. |  |
| 6 | Asignar catálogos de inspección | Desde el Catálogo de inspección asignado ventana de diálogo, seleccione un valor para el GrC/ConS campo, por ejemplo SMOOTH .Seleccionar Continuar . | Volver a Crear característica de inspección maestra: General Datos verNota El centro se actualiza automáticamente seleccionando Suavizar mediante la ayuda para entradas. |  |
| 7 | Asignar método de inspección (opcional) | Seleccionar Métodos de inspección y el Métodos de inspección asignados ver muestra.Realice las siguientes entradas:Método : SuperficieCentro : <Código de centro>Seleccionar Continuar . | Volver a Crear característica de inspección maestra: General Datos vista. |  |
| 8 | Guardar los datos | Seleccionar Grabar | Se han grabado los datos |  |
| 9 | Crear una inspección maestra cuantitativa Característica | Desde la rampa de lanzamiento SAP Fiori, abra Crear Característica de inspección maestra: Datos iniciales ver y efectúe las siguientes entradas:Centro : <Centro Código>Caract.insp.maestra : por ejemplo, YQUANT01Inicio de validez : <actual fecha>y seleccione Característica de inspección maestra | El Crear característica de inspección maestra: General Datos visualizaciones de vista |  |
| 10 | Introducir datos generales para característica cuantitativa | De Crear característica de inspección maestra: General Datos , efectúe las siguientes entradas:Caract.cuantitativa : marcadoTexto breve : por ejemplo, LongitudCampo de búsqueda : por ejemplo, LongitudEstado : 2 LiberadoSeleccionar Liberado y Referencia CaracterísticaSeleccionar Intro | Editar indicadores de control de característica ventana apareceCaracterísticas de referenciasi utiliza la característica de inspección maestra en un plan o especificación de material, primero se crea una referencia a esta característica. Sin embargo, puede cancelar esta referencia y modificar los datos individualmente, por ejemplo, para tolerancias.Modelo de copia completoSi utiliza la característica de inspección maestra en un plan, solo se puede utilizar en un modelo de copia. Este tipo de inspección maestra La característica no se puede utilizar en una especificación de material.Modelo de copia incompletoSi utiliza la característica de inspección maestra en un plan, solo se puede utilizar en un modelo de copia. Este tipo de inspección maestra La característica no se puede utilizar en una especificación de material. |  |
| 11 | Editar indicadores de control para cuantitativos Características | En la Editar indicadores de control de característica , marque las siguientes opciones:Lím.inferior especif.Lím.sup.especif.Procedimiento de muestreoGrabación de totalesCaract.oblig.Seleccionar Continuar y marcarlos como adicionales opciones:Alcance fijoSin documentaciónRegistrar valores medidosDoc.modif.RRSeleccionar Continuar |  |  |
| 12 | Introducir valor de destino | El Claves de tolerancia vista, realice lo siguiente entrada:Valor de destino : por ejemplo 150y seleccione Continuar |  |  |
| 13 | Introducir datos cuantitativos | El Datos cuantitativos vista, realice lo siguiente entradas:Decimales : por ejemplo, 2UM : por ejemplo cmLímite inferior : por ejemplo, 100Límite superior : por ejemplo, 200Seleccionar Continuar |  |  |
| 14 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |
| 15 | Activar la entrada de defectos para una inspección maestra existente Característica (opcional) | Abra la Modificar característica de inspección maestra (QS23) aplicación y abrir la característica de inspección maestra que desea modificar.Seleccionar Indicadores de control .En la Editar indicadores de control de característica cuadro de diálogo, active el Entrada de defectos opción en el Notificación de resultados y seleccione Continuar .Seleccionar Continuar de nuevo. |  |  |
| 16 | Asignar catálogos de inspección (opcional) | En Información general , seleccione el área Catálogos botón. | El Catálogos de inspección asignados ventana de diálogo aparece. |  |
| 17 | Actualizar códigos de defecto para rechazo (opcional) | En Códigos de defecto para rechazo de la Catálogos de inspección asignados ventana de diálogo, buscar e introduzca el grupo de códigos / código para general, límite superior y límite inferior infracción, respectivamente.Seleccionar Continuar . |  |  |
| 18 | Guardar los datos | Seleccionar Grabar . | Se han grabado los datos |  |

### Crear característica de inspección maestra con referencia a característica de clase (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El enlace entre las características de inspección maestra y las características de clase permite la transferencia automática de resultados de inspección a la clasificación de lotes, siempre que inspeccione con una hoja de ruta. Las características de clase de la clase de lote se valoran automáticamente al cierre de inspección, en función de los resultados de inspección.

Al introducir una característica de clase y vincularla a una característica de inspección maestra, determinados indicadores de control y valores de esta característica de clase se transfieren a la característica de inspección maestra.

El enlace entre las características de inspección maestra y las características de clase le permite transferir los resultados de una inspección de calidad a la clasificación de lotes.

|  |
| --- |
| Nota Solo puede tener una relación 1:1 entre una característica de clase y un maestro característica de inspección (es decir, no puede hacer referencia a la misma característica de clase en varias características de inspección maestra). La característica de clase está definida en el cliente y la característica de inspección maestra se definen a nivel de centro. Por lo tanto, si desea utilizar la valoración de lote para varios centros, es obligatorio definir características de clase específicas de centro y enlácelas con la inspección maestra correspondiente característica a nivel de centro. |

Requisitos previos

Los requisitos previos deben cumplirse para el enlace de la característica de inspección maestra con la característica de clase, consulte la Condiciones empresariales capítulo sobre 2ZW.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Comentarios de resultados previstos | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear característica de inspección maestra (QS21) . | El Crear característica de inspección maestra: Acceso se visualiza. |  |
| 3 | Introducir datos de centro | Activado Crear característica de inspección maestra: Acceso , efectúe las siguientes entradas:Centro : Código de centroCaract.insp.maestra : <valor>Inicio de validez : <fecha actual>Característica de clase : valorSeleccionar Característica de inspección maestra. | El Crear característica de inspección maestra: Datos generales se visualiza. |  |
| 4 | Ejecute los pasos 10-14 en el Capítulo anterior | Nota La característica de inspección maestra debe ser una característica de referencia.Algunos datos se copian de la característica de clase a la característica de inspección maestra. Además, en función de las opciones de la característica de clase, algunos indicadores de control de la característica de inspección maestra no se pueden modificar. | Se crea la característica de inspección maestra cuantitativa con enlace a la característica de clase. |  |
| 5 | Verificar características de lote después de la inspección de calidad (Opcional) | Crear lote de inspección manualmente o mediante movimiento de mercancías, ejecutar la inspección de calidad y tomar una decisión de empleo.Para revisar las características de lote, inicie sesión en la rampa de lanzamiento SAP Fiori como Técnico de calidad y acceder a SAP Aplicación Fiori Gestionar lotes (F2462) o bien Cockpit de información de lotes (BMBC) y verifique la características en Clasificación . | Los datos de inspección de calidad se han transferido a la característica de lote. |  |

### Crear esquema de muestreo (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Opcionalmente, puede crear un plan de muestreo. Un plan de muestreo es una colección de instrucciones de muestreo. Una instrucción de muestreo define la cantidad de muestras a inspeccionar (tamaño de muestra) en función del tamaño de lote. Además, se pueden definir criterios para aceptar o rechazar una muestra (por ejemplo, en función del grado de inspección actual). El grado de inspección define si se ejecuta una inspección normal, reducida o reforzada para que un planificador de calidad pueda adaptar de forma flexible el esfuerzo de inspección a la situación de calidad actual (por ejemplo, menos inspecciones, tamaño de muestra más pequeño o criterios de aceptación más altos cuando la situación de calidad actual es buena).

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear esquema de muestreo (QDP1) . | El Crear plan de muestreo: Vista inicial aparece. |  |
| 3 | Introducir nombre de esquema de muestreo de muestra | Introduzca un nombre de esquema de muestreo de muestra.Plan de muestreo : por ejemplo, QM2Seleccionar Continuar . | El Crear plan de muestreo: Datos de cabecera Aparece la vista. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas o seleccione:Plan de muestreo : por ejemplo, Plan de muestreo para gravedades (atributo)Parámetros de valoración : por ejemplo, Insp.atributivaTabla de muestreo para : por ejemplo, Gravedad insp.Seleccionar Continuar . | El Crear plan de muestreo: Parámetros aparece la ventana de diálogo. |  |
| 5 | Introducir parámetro de seguridad de inspección | En la Crear plan de muestreo: Parámetros , realice la siguiente búsqueda y entradas:Gravedad insp. : por ejemplo, 002(Inspección reducida)Consejo El grado de inspección define si se ejecuta una inspección normal, reducida o reforzada. Un planificador de calidad puede adaptar de forma flexible el esfuerzo de inspección, como menos inspecciones, tamaños de muestra más pequeños o criterios de aceptación más altos cuando la situación de calidad actual es buena.y seleccione Seleccionar | El Crear plan de muestreo: Tabla de muestreo Aparece la vista. |  |
| 6 | Crear planes de muestreo | En la Planes de muestreo tabla, realice lo siguiente entradas.Tamaño de lote : por ejemplo, 10.Tamaño de muestra : por ejemplo, 1.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 100.Tamaño de muestra : por ejemplo, 2.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 1000.Tamaño de muestra : por ejemplo, 5.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 10000000000.Tamaño de muestra : por ejemplo, 50.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1. | Se crea una instrucción de muestreo.Nº aceptación N : número más alto de unidades o defectos no conformes que se toleran para que se pueda aceptar el lote o atributo.Nº rechazo N : número más bajo de unidades o defectos no conformes que provocan un rechazo del lote o atributo.Recordar Si el número de unidades o defectos no conformes se encuentra entre los límites de aceptación y rechazo, el sistema determinará la siguiente instrucción de muestreo. |  |
| 7 | Crear otra tabla | En la Crear plan de muestreo: Tabla de muestreo vista, seleccionar Otra tabla (o Mayús + F5). | El Crear plan de muestreo: Parámetros aparece la ventana de diálogo. |  |
| 8 | Introducir parámetro de seguridad de inspección | En la Crear plan de muestreo: Parámetros diálogo , realice las siguientes entradas:Gravedad insp. : por ejemplo, 004 (inspección normal)y seleccione Seleccionar | El Crear plan de muestreo: Tabla de muestreo ver aparece. |  |
| 9 | Crear planes de muestreo | En la Planes de muestreo tabla, realice lo siguiente entradas.Tamaño de lote : por ejemplo, 10.Tamaño de muestra : por ejemplo, 1.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 100.Tamaño de muestra : por ejemplo, 5.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 1000.Tamaño de muestra : por ejemplo, 10.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 10000000000.Tamaño de muestra : por ejemplo, 100.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1. | Se crea la siguiente instrucción de muestreo. |  |
| 10 | Crear otra tabla | En la Crear plan de muestreo: Tabla de muestreo vista, seleccionar Otra tabla (o mayús + F5) | El Crear plan de muestreo: Parámetros ventana de diálogo aparece. |  |
| 11 | Introducir parámetro de seguridad de inspección | En la Crear plan de muestreo: Parámetros diálogo , realice las siguientes entradas:Gravedad insp. : por ejemplo, 006 (inspección intensificada)y seleccione Seleccionar | El Crear plan de muestreo: Tabla de muestreo ver aparece. |  |
| 12 | Crear planes de muestreo | En la Planes de muestreo tabla, realice lo siguiente entradas.Tamaño de lote : por ejemplo, 10.Tamaño de muestra : por ejemplo, 2.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 100.Tamaño de muestra : por ejemplo, 10.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 1000.Tamaño de muestra : por ejemplo, 25.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1.Tamaño de lote : por ejemplo, 10000000000.Tamaño de muestra : por ejemplo, 200.Aceptación nº 1 : por ejemplo, 0.Número de rechazo 1 : por ejemplo, 1. | Se crea la siguiente instrucción de muestreo |  |
| 13 | Grabar datos | Para grabar los datos, seleccione Grabar . | Plan de muestreo se ha creado. |  |

### Crear procedimiento de muestreo (opcional)

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccionar Crear procedimiento de muestreo (QDV1) . | El Crear procedimiento de muestreo: Acceso aparece. |  |
| 3 | Introducir nombre de procedimiento de muestra | Introduzca un nombre de procedimiento de muestra, por ejemplo, YPERCIN1 .Seleccionar Continuar . | Aparece una ventana nueva. |  |
| 4 | Introducir datos de procedimiento de muestra | Introduzca los datos para el procedimiento de muestra:Proporcione una descripción, por ejemplo 10% inspección sin puntos de inspecciónClase de muestreo : por ejemplo, Muestra porcentualModo de valoración : por ejemplo, Valoración según caract.código atrib.Puntos de inspección : por ejemplo, seleccione Sin puntos de inspecciónIndicador de utilización : Salga del Uso bloqueado campo, en blancoSeleccionar Continuar . | Se ha definido la regla de determinaciónNota Para utilizar Esquemas de muestreo , debe seleccionar Utilizar plan de muestreo en el Tipo de muestreo campo. A continuación, asigne el esquema de muestra que ha creado en el procedimiento anterior. |  |
| 5 | Actualizar plan de muestreo | Seleccionar Muestra e introduzca los siguientes datos:Tamaño como % de lote : por ejemplo, 10Seleccionar Continuar .Seleccionar Grabar . | Se han guardado los datos. |  |

### Crear regla de dinamización (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Crear regla de dinamización.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear regla de dinamización (QDR1) . | El Crear regla de dinamización: Inicial Pantalla aparece. |  |
| 3 | Introducir nombre de regla de modificación dinámica | Introduzca un nombre de regla de modificación, por ejemplo QM1 | El Crear regla de dinamización: Datos de cabecera Aparece la pantalla. |  |
| 4 | Introducir datos de cabecera | Realice las siguientes entradas:Texto breve : por ejemplo, Inspección/OmitirPara decisión de empleo : marcadoPeríodo de restablecimiento (días) : por ejemplo, 90Seleccionar Pantalla siguiente | El Crear regla de dinamización: Inspección Etapas Aparece la pantalla. |  |
| 5 | Introduzca los datos para la etapa de inspección 10 | Realice las siguientes entradas en la primera línea:Etapa : 10SecIns : 2Etapa de inspección inicial : marcadoTexto breve : Inspección inicial |  |  |
| 6 | Introduzca los datos para la etapa de inspección 20 | Realice las siguientes entradas en la segunda línea:Etapa : 20SecIns : dejar en blancoOmitir : marcadoTexto breve : Omitir |  |  |
| 7 | Introduzca los datos para la etapa de inspección 30 | Realice las siguientes entradas en la tercera línea:Etapa : 30SecIns : 4Texto breve : por ejemplo, <Inspección normal> |  |  |
| 8 | Actualizar cambio de etapa para etapa de inspección 10 | Seleccionar Etapa de inspección 10 y seleccione Cambio de etapa .En la Crear cambio de etapa , efectúe las siguientes entradas:OKNúmero de inspecciones : 1Nueva etapa insp. : 20No OKRechazos : 1Nueva etapa insp. : 30 | Las entradas se reflejan en la tabla. |  |
| 9 | Actualizar cambio de etapa para etapa de inspección 20 (omitir) | Seleccionar Etapa de inspección 20 y seleccione Cambio de etapa .En la Crear cambio de etapa , efectúe las siguientes entradas:OKCantidad de omisiones : 1Duración máxima de omisión : 90Nueva etapa insp. : 30No OKRechazos : 1Nva.insp. . Etapa: 30 | Las entradas se reflejan en la tabla. |  |
| 10 | Actualizar cambio de etapa para etapa de inspección 30 | Seleccionar Etapa de inspección 30 y seleccione Cambio de etapa .En la Crear cambio de etapa , efectúe las siguientes entradas:OKNúmero de inspecciones : 1Nueva etapa insp. : 20No OKRechazos : 1Nueva etapa insp. : 30 | Las entradas se reflejan en la tabla. |  |
| 11 | Guardar los datos | Grabe los datos. |  |  |

### Crear plan de inspección

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear plan de inspección (QP01) mosaico. | Crear plan de inspección (vista inicial) aparece. |  |
| 3 | Introducir datos | En la Crear plan de inspección (vista inicial) , efectúe las siguientes entradas:Material : <su número de material> , por ejemplo QM001Centro : <Código de centro>Fecha clave : por ejemplo, hoySeleccionar Continuar | El Crear plan de inspección: Detalles de cabecera aparece cuando no hay ningún plan disponible para la combinación de material/centro especificada.Nota Si existe es un plan disponible, seleccione un grupo de la ventana de diálogo y Crear plan de inspección: Resumen de hoja de ruta aparece. Seleccione Entradas nuevas para crear un nuevo plan de inspección. |  |
| 4 | Actualizar detalles de cabecera | Crear plan de inspección (detalles de cabecera) Introduzca los siguientes datos:Utilización : seleccione de la lista de ayuda para entradas con fines de utilización, por ejemplo, 5 Entrada de mercancíasEstado : seleccione de la lista de ayuda para entradas, por ejemplo, 4 Liberado (general)Tamaño de lote : Entre 1 y 99.999, por ejemplo, 999 un.Nivel dinamización (opcional): 1 Dinamización a nivel de loteNota Estos datos solo son necesarios si utiliza Reglas de modificación dinámicaRegla de dinamización (opcional): <sus datos>Nota Estos datos solo son necesarios si utiliza Reglas de modificación dinámicaCriterios de dinamización (opcional): por ejemplo, Proveedor y fabricanteNota Estos datos solo son necesarios si utiliza Reglas de modificación dinámicaSeleccionar Operaciones . | Crear plan de inspección: Resumen de operaciones aparece |  |
| 5 | Introducir datos de operación (resumen) | El Crear plan de inspección: Resumen de operaciones introduzca lo siguiente:Número de operación : por ejemplo, 0010Puesto de trabajo : seleccione el puesto de trabajo, por ejemplo, QMLABSClave de control : seleccione una clave de control, por ejemplo, QM01Descripción : Proporcione una descripciónMarque la casilla de selección partida individual de operación y, a continuación, seleccione Operación .Nota Si el Operación el botón no está disponible, seleccionar Más > Operación . | Crear plan de inspección: Detalles de operación aparece.Nota El Clave de control influye en la planificación y el procesamiento de la operación de inspección, por ejemplo, si las características de inspección deben actualizarse o no para una operación de inspección. |  |
| 6 | Datos de operación (detalles) | El Crear plan de inspección: Detalles de operación , desplácese para revisar el Vista de registro: "valores individuales y resultado resumido (vista predeterminada)"Seleccionar Volver para volver al Operación Resumen vista. |  |  |
| 7 | Introducir características de inspección | Marque la línea de operación y seleccione Inspección Característica .Asignar Características de inspección maestras , por ejemplo, una característica de inspección maestra relacionada con la calidad, como YQUALI01 para una característica cualitativa, o una que está relacionada con la cantidad, como YQUANTI01 para una característica cuantitativa.Asignar Procedimiento de muestreo (opcionalmente), para utilizar en combinación con la característica que se está inspeccionando.Asignar Modificación dinámica regla (opcional): por ejemplo QMINota La dinamización se puede asignar a nivel de cabecera o a nivel de característica de inspección.Seleccionar Intro . | Se visualiza la información detallada. |  |
| 8 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

### Gestión de planes de inspección

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Paso de test # Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de planes de inspección (F3788) . | Se abre la aplicación. |  |
| 3 | Filtrar datos | En la Gestión de planes de inspección (inicial) vista) , efectúe las siguientes entradas:Material : <Material> (adaptando los filtros dentro de la Plan de inspección Versión sección)Centro : <Código de centro>Estado del plan : <Estado global> , por ejemplo, 4 Liberado GeneralSeleccionar Ir . | La lista de planes de inspección muestra que cumplen los criterios de selección. |  |
| 4 | Seleccionar plan de inspección | Seleccione la entrada relevante y navegue hasta ella seleccionando > a la derecha de la línea seleccionada. | Ha navegado al plan de inspección relevante. |  |
| 5 | Modificar fecha clave | Dentro de la Gestión de planes de inspección (F3788) aplicación, seleccione Modificar fecha clave . Aparece una ventana de diálogo y puede actualizar la fecha clave insertando la fecha a partir de la cual debe ser válida la modificación:Fecha clave : <Fecha>Nota La fecha clave solo se tiene en cuenta para el objeto creado o borrado (por ejemplo, operaciones de inspección), pero es posible que no se tenga en cuenta para modificaciones. Es posible que las modificaciones en el objeto existente se visualicen inmediatamente. | Se modifica la fecha clave. |  |
| 6 | Actualizar datos generales | El Gestión de planes de inspección con la pantalla General, Asignación de material, Operaciones, Anexos y datos administrativos campo. Realice las siguientes entradas para actualizar los datos generales (seleccione Editar para modificar las entradas):Centro : seleccione de la lista de ayuda para entradas si aún no se ha insertado.Descripción de plan de inspección : modifique la descripción.Utilización : seleccione de la lista de ayuda para entradas con fines de utilización, por ejemplo, 5 Entrada de mercancías .Estado global : seleccione de la lista de ayuda para entradas, por ejemplo, 4 Liberado (general) .Tamaño de lote : Entre 1 y 99.999, por ejemplo, 999 un.Punto de inspección (opcional): Insertar 101 Relacionado con el tiempo si desea crear una inspección puntos basados en el tiempo.Nota Los siguientes datos solo son necesarios si utiliza Reglas de modificación dinámica .Nivel dinamización (opcional): 1 Dinamización en lote nivelNota Dentro de Reglas de modificación dinámica , se puede decidir en qué nivel es relevante una dinamización.Regla de dinamización (opcional): <sus datos>Nota Los siguientes datos solo son necesarios si utiliza Reglas de modificación dinámica .Criterios de dinamización (opcional): Por ejemplo, Proveedor y fabricante | Se actualizan los datos generales del plan de inspección. |  |
| 7 | Actualizar asignación de material | Actualice la Asignación de material información dentro de la Gestión de planes de inspección (seleccione Añadir para añadir entradas):Material : <Material>Centro : <Código de centro>Proveedor (opcional): <Número de proveedor>Cliente (opcional): <Número de cliente>Nota Se pueden visualizar otros criterios mediante Opciones . | Se actualiza la información de asignación de material del plan de inspección. |  |
| 8 | Actualizar operaciones | Actualice la Operaciones información dentro de la Gestión de planes de inspección (seleccione Crear para crear entradas):Descripción de la operación : <Descripción>Centro : <Código de centro>Cantidad base : <Cantidad>Unidad de medida : <Unidad>Nota Se pueden visualizar otros criterios mediante Opciones .Navegue a los detalles de la operación seleccionando > a la derecha de la línea seleccionada. | La información de la operación del plan de inspección se actualiza y navega a la posición. |  |
| 9 | Actualizar operación (resumen) | Actualice la Datos generales dentro de la Operación pantalla:Número de operación : <Número dado por el sistema>Clave de control : <Proporcionado por el sistema>Centro : <Código de centro>Descripción de la operación : <Descripción>Puesto de trabajo (opcional): Seleccione un puesto de trabajo, por ejemplo, QMLABSCantidad base : <Cantidad>Unidad de medida : <Unidad>Conversión de unidades de medida de cabecera a Operación.Nota Se pueden visualizar otros criterios mediante Opciones de punto de inspección . | Se actualizan los datos generales de la operación. |  |
| 10 | Actualizar operación (características) | Ir a Características dentro de la Operación Pantalla. Seleccione Asignar Características para copiar información de característica de inspección maestra o seleccione Añadir para añadir una nueva característica o características de inspección maestra.Nota Incluso después de elegir Añadir , es posible añadir una referencia a una característica de inspección maestra posteriormente.Realice las siguientes entradas:Descripción : <Descripción breve>Características de inspección maestras (opcional): <Características de inspección maestra>Indicadores de control : <Indicadores de control>Nota Se pueden visualizar otros criterios mediante Opciones de punto de inspección .Navegue a los detalles de la característica seleccionando > en el lado derecho. | La información de Característica de operación se actualiza y navega a la Característica. |  |
| 11 | Actualizar característica | Los detalles de la característica se visualizan y se pueden actualizar. Los siguientes datos pueden ser relevantes para la actualización:Nota En función de las opciones para los indicadores de control en el paso anterior, se pueden visualizar diferentes campos.Descripción : <Descripción breve>Ponderación de característica (opcional): Seleccione de la lista de ayuda para entradas, por ejemplo, <Ponderación>Método de inspección, versión, centro (opcional): Seleccione de la lista de ayuda para entradas, por ejemplo, <Método de inspección>Campos de información (opcional): <Más información>Conjunto de selección, centro : seleccione de la lista de ayuda para entradas, por ejemplo, <Conjunto seleccionado cualitativo Características>Dinamización para característica (opcional): Seleccione de la lista de ayuda para entradas, por ejemplo, <Otra característica>Regla de dinamización (opcional): seleccione de la lista de ayuda para entradas, por ejemplo, <Dinámico Regla de modificación>Nota La regla de dinamización solo se visualiza si la dinamización está en el nivel de característica.Puede encontrar más datos administrativos en el área relevante.Volver a Operaciones . | La información de característica se actualiza y se le dirige a la Operaciones pantalla. |  |
| 12 | Verificación de datos administrativos Operaciones | El Operaciones se visualiza y se puede actualizar.Puede encontrar más datos administrativos en el área relevante.Volver a Plan de inspección . | Los datos administrativos están disponibles y accederá a la Plan de inspección dynpro. |  |
| 13 | Añadir anexos al plan de inspección | El Plan de inspección y la pantalla Anexos se puede actualizar.Seleccionar Añadir para crear una URL con la descripción.Seleccionar Cargar para insertar un documento de el sistema de ficheros local.Puede encontrar más datos administrativos en el área relevante.Volver a Plan de inspección . | Los datos administrativos están disponibles y accederá a la Plan de inspección dynpro. |  |
| 14 | Guardar los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

### Copiar de planes de inspección existentes

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
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Planificador de calidad | El Iniciar Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestión de planes de inspección (F3788) . | Gestión de planes de inspección (vista inicial) aparece. |  |
| 3 | En la vista inicial Filtrar datos | En la Gestión de planes de inspección (inicial) vista) , efectúe las siguientes entradas:Material : <Material> , adaptando los filtros dentro de la sección Plan de inspección Versión .Centro : <Centro Código>Estado del plan : <Status global> , para, por ejemplo, 4 Liberado (general)Seleccionar Ir . | La lista de Planes de inspección aparecen cumpliendo los criterios de selección. |  |
| 4 | En la vista Filtrado, seleccione Inspección Plan | Seleccione la entrada relevante y navegue seleccionando > en la lado derecho de la línea seleccionada. | Se ha introducido el plan de inspección relevante. |  |
| 5 | Copiar de plan existente (inicio) | Gestión de planes de inspección aparece. Seleccione Copiar de planes existentes .Dentro de Copiar de planes existentes diálogo caja, inserte potencialmente algunos datos o elija inmediatamente OK :Centro : <Centro Código> , seleccione de la ayuda para entradas.Grupo y contador de grupos : <Identificador del plan> , Seleccione de la ayuda para entradas.Estado global : <Estado> , seleccione de la ayuda para entradas lista, por ejemplo, 4 Liberado GeneralFecha de inicio de validez : Elija uno de los Lista de ayuda para entradasNota Es posible que se visualicen más criterios mediante Adaptar filtros | Copiar del panel lateral Planes existentes aparece. |  |
| 6 | Copiar de plan existente (copiar) | Dentro de la Copiar del lado de los planes existentes Panel los planes de acuerdo con los se muestran los filtros seleccionados. Utilizando el > delante de cada uno línea los objetos de los planes se pueden contraer:Plan > Materiales > OperacionesDentro de Materiales un material puede ser seleccionado y seleccionando Copiar el la entrada seleccionada se copia en el plan de inspección actual.Dentro de Operaciones uno o varios La operación se puede seleccionar y seleccionar Copiar transferidos a la inspección plan.Operación > CaracterísticasDentro de Características asignado a individual se pueden seleccionar una o varias características y transferir a una operación de libre utilización seleccionando Copiar . También es posible marcar una operación y una o varias características correspondientes a Copie la operación incluyendo solo la(s) característica(s) marcada(s)Nota También es posible copiar de los planes existentes dentro de la Operación y Característica resumen dentro de la aplicación Gestión de planes de inspección . | Copiar del panel lateral Planes existentes aparece. |  |
| 7 | Grabe los datos | Seleccionar Grabar . | Se han guardado los datos. |  |

### Visualizar lotes de inspección abiertos

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El lote de inspección se utiliza para registrar los resultados de la operación de inspección. En este paso opcional, se verifican las referencias, así como el tamaño de la muestra utilizado para la calidad inspección revisada. La instrucción de toma de muestra se puede imprimir.

Requisito previo

Se crea el lote de inspección.

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Técnico de calidad | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Gestionar lotes de inspección (F2343) . | El Gestionar lotes de inspección se visualiza. |  |
| 3 | Introducir campos de filtro | Realice entradas de filtro y seleccione Ir | Si las referencias pertinentes (p. ej. pedido u orden de fabricación) no se visualizan en el Filtros , seleccione Adaptar Filtros . En la ventana de diálogo Adaptar Filtros , buscar Aprovisionamiento o Producción , seleccione Más Filtros . Seleccione el documento relevante y OK . Seleccione Ir . |  |
| 4 | Seleccionar lote de inspección | En la lista de lotes de inspección, seleccione el lote de inspección que ha creado antes. | Se visualiza el lote de inspección. |  |
| 5 | Imprimir instrucción de toma de muestra | Seleccionar Imprimir instrucción de toma de muestra .Seleccione un elemento de salida para imprimir, duplique potencialmente uno y seleccionar Enviar salida .Nota Si la impresión ya se ha generado para un lote de inspección, el Detalles de salida muestra un lista de posiciones de salida impresas anteriormente. | El Detalles de salida Se abre el diálogo, que muestra una lista de elementos de salida con canales de impresión y correo electrónico configurados. Un documento PDF que contiene la instrucción de toma de muestra se desencadena y se envía al Actualizar aplicación Colas de impresión para imprimir. |  |
| 6 | Instrucción de toma de muestra de correo | Seleccionar Imprimir instrucción de toma de muestra .Seleccione una posición de salida para el correo electrónico y seleccione Enviar Salida . | Se envía un correo electrónico con el PDF a los destinatarios previstos. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document is flagged as machine-translated and not reviewed for accuracy; wording may be unreliable.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Filename says 'Master_Data' ES while the extracted title heading is 'Objetivo'; real title taken from cover table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-655]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-657]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 65,035 chars in the whole document
