---
id: 14-maintenance-service-and-projects/script-de-datos-maestros-crear-lista-de-materiales-para-material-y-equ
title: Script de datos maestros - Crear lista de materiales para material y equipo para servicio - MDS (63J) (63J_S4CLD2608_Master_Data_ES_XX)
description: "Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 63J: create service products, a material BOM, equipment and an equipment BOM."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [63J_S4CLD2608_Master_Data_ES_XX]
keywords: [Technical Objects and BOMs for Service, service products, bill of materials, equipment master data, equipment bill of materials, material master, business roles, organizational units, profit center assignment, service contracts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_ES_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-492
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear lista de materiales para material y equipo para servicio - MDS (63J) (63J_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear lista de materiales para material y equipo para servicio - MDS (63J) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894846)

[2 Requisitos previos 3](#_Toc233894847)

[2.1 Acceso al sistema 3](#_Toc233894848)

[2.2 Roles 3](#_Toc233894849)

[2.3 Unidades organizativas necesarias 3](#_Toc233894850)

[2.4 Datos maestros obligatorios y operativos 4](#_Toc233894851)

[3 Tabla de resumen 5](#_Toc233894852)

[4 Procedimientos 6](#_Toc233894853)

[4.1 Crear lista de materiales para material 6](#_Toc233894854)

[4.1.1 Crear productos de servicio 6](#_Toc233894855)

[4.1.1.1 Crear producto de servicio - SRV_BOM_01_01 6](#_Toc233894856)

[4.1.1.2 Crear producto de servicio - SRV_BOM_02_01 7](#_Toc233894857)

[4.1.1.3 Crear producto de servicio - SRV_BOM_02_02 9](#_Toc233894858)

[4.1.2 Crear nueva lista de materiales 10](#_Toc233894859)

[4.2 Crear lista de materiales para equipo 13](#_Toc233894860)

[4.2.1 Crear equipo 13](#_Toc233894861)

[4.2.2 Crear lista de materiales para equipo 14](#_Toc233894862)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este documento encontrará una descripción de cómo crear registros de datos maestros de productos de servicio y cómo crear la lista de materiales con los productos de servicio creados. La descripción incluye aquellos segmentos de datos que son relevantes para que los datos maestros funcionen en un entorno de sistema "habitual". El lector aprende principalmente qué segmentos de datos y campos deben rellenarse normalmente con valores de entrada. Los campos que no son relevantes para el alcance no se describen en este documento, aunque pueden aparecer en la IU.

El registro maestro de productos de servicio que se crea como se describe aquí se puede utilizar para contratos de servicio.

| Tipo de producto | ID de producto de servicio | Descripción |
| --- | --- | --- |
| Maestro de materiales | SRV_BOM_01_01 | Producto de servicio con BOM 01_01 |
|  | SRV_BOM_02_01 | Producto de servicio con BOM 02_01 |
|  | SRV_BOM_02_02 | Producto de servicio con BOM 02_02 |
| Lista de materiales para material | SRV_BOM_01_01 | Producto de servicio con BOM 01_01 |
| Equipo | <ID de equipo> | Crear equipo |
| Lista de materiales para equipo | <Lista de materiales para equipo> | Lista de materiales para equipo |

## Requisitos previos

### Acceso al sistema

| Sistema | Detalles |
| --- | --- |
| Sistema | Accesible a través de la rampa de lanzamiento SAP Fiori. El administrador del sistema le proporciona el URL para acceder a las diferentes aplicaciones asignadas a su rol. |

### Roles

Cree roles empresariales utilizando los siguientes modelos de rol empresarial suministrados por SAP y asígnelos a sus usuarios de prueba individuales.

Como alternativa, si están disponibles, puede utilizar los siguientes espacios suministrados por SAP. Cree un espacio con páginas que contengan aplicaciones esenciales predefinidas y asígnelo al rol empresarial. A continuación, asigne este rol empresarial a sus usuarios individuales.

Para obtener más información, consulte. Cómo crear un rol empresarial a partir de un modelo en el [asistencia de producto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edición .

| Nombre (modelo de rol) | ID (modelo de rol) | Nombre (espacio de rampa de lanzamiento) | ID (espacio de rampa de lanzamiento) |
| --- | --- | --- | --- |
| Especialista en datos maestros - Datos de producto | SAP_BR_PRODMASTER_SPECIALIST | Datos maestros - Producto | SAP_CMD_SP_PR_MAINT |
| Responsable de listas de materiales | SAP_BR_BOM_ENGINEER | Listas de materiales | SAP_BR_BOM_ENGINEER |
| Planificador de mantenimiento | SAP_BR_MAINTENANCE_PLANNER | Planificación de mantenimiento | SAP_BR_MAINTENANCE_PLANNER |

### Unidades organizativas necesarias

Algunos segmentos de datos maestros dependen de las unidades organizativas de la empresa. Los datos generales (centrales) no dependen de una unidad organizativa o de la sociedad. La siguiente tabla ofrece un resumen de estos diferentes segmentos de datos y sus unidades organizativas relevantes:

| Segmento de datos | Depende de | Unidad organizativa que se utilizará para EE. UU. | Unidad organizativa a utilizar para DE |
| --- | --- | --- | --- |
| Crear material | Organización de ventas | 1710 (Org.ventas nac.US) | 1010 (Org.ventas nac.DE) |
| Crear material | Canal de distribución | 10 (Ventas directas) | 10 (Ventas directas) |

### Datos maestros obligatorios y operativos

Los registros de datos maestros de material pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se utilizarán en un registro de datos maestros de material.

|  |
| --- |
| Nota Los campos específicos de Brasil son obligatorios para obtener un cálculo de impuestos adecuado.Verificar Nota Fiscal Brasil - JD0 en Definir campos específicos de BR para Datos maestros capítulo para datos maestros de material. |

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de beneficio |  | Obligatorio | Se requiere la asignación de un centro de beneficio a un maestro de materiales (productos) para procesos de valoración correctos. |

## Tabla de resumen

Este registro maestro consta de varios segmentos que se proporcionan en la tabla siguiente.

Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.

Puede encontrar todas las demás aplicaciones no incluidas en la página de inicio utilizando la barra de búsqueda.

Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Configuración > Buscador de aplicaciones .

| ID (modelo de rol) | Rol empresarial | Aplicación/Transacción | Resultados previstos |
| --- | --- | --- | --- |
| Crear lista de materiales para material | SAP_BR_PRODMASTER_SPECIALIST | Crear material (MM01) | Se crean productos de servicio. |
| SAP_BR_BOM_ENGINEER | Actualizar lista de materiales - Crear, modificar y visualizar listas de materiales | Se ha creado la lista de materiales para material |  |
| Crear lista de materiales para equipo | SAP_BR_MAINTENANCE_PLANNER | Crear objeto técnico | Se ha creado el equipo |
| Crear lista de materiales para equipo | Se ha creado la lista de materiales para equipo |  |  |

## Procedimientos

Esta sección describe los procedimientos para cada segmento o paso de proceso que forma parte de este registro maestro.

### Crear lista de materiales para material

#### Crear productos de servicio

##### Crear producto de servicio - SRV_BOM_01_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto (MDG).. | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Crear material mosaico. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) | El Crear material (pantalla inicial) realice las siguientes entradas: ventana de diálogo, seleccione laMaterial: SRV_BOM_01_01Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.El Seleccionar vista(s) se visualiza la ventana de diálogo. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione el vistas siguientes:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2A continuación, seleccione Continuar (Intro) . | El Niveles de organización la ventana de diálogo es visualizados. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice la valores siguientes:Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_BOM_01_01 Se muestra la vista. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 , actualice los siguientes valores:Descr.: Producto de servicio con BOM 01_01Unidad de medida base: HR (hora)Grupo de materiales: P001 (Servicios)Gr.tp.pos.gen.: SRVP (producto de servicio)A continuación, seleccione Grabar . | Se actualizan los datos básicos y se graba el producto de servicio.Después de guardar, el Crear material (pantalla inicial) Se muestra la vista.Para cada idioma diferente utilizado en su empresa, la descripción correspondiente para el producto debe actualizarse por código de idioma. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 , actualice los siguientes valores:Datos generalesDescuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: org.ventas 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 , actualice la siguiente entrada:Grupo de tipos de posición : SRVP (producto de servicio)A continuación, seleccione Grabar . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |

##### Crear producto de servicio - SRV_BOM_02_01

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto (MDG).. | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Crear material mosaico. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) | El Crear material (pantalla inicial) realice las siguientes entradas: ventana de diálogo, seleccione laMaterial: SRV_BOM_02_01Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.El Seleccionar vista(s) se visualiza la ventana de diálogo. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione el vistas siguientes:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2A continuación, seleccione Continuar (Intro) . | El Niveles de organización la ventana de diálogo es visualizados. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice la valores siguientes:Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_BOM_ 02_01 la vista es visualizados. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 , actualice los siguientes valores:Descr.: Producto de servicio con BOM 02_01Unidad de medida base: HR (hora)Grupo de materiales: P001 (Servicios)Gr.tp.pos.gen.: SRVP (producto de servicio)A continuación, seleccione Intro . | Se actualizan los datos básicos y se graba el producto de servicio.Después de guardar, el Crear material (pantalla inicial) Se muestra la vista.Para cada idioma diferente utilizado en su empresa, la descripción correspondiente para el producto debe actualizarse por código de idioma. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 , actualice los siguientes valores:Datos generalesDescuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: org.ventas 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 , actualice la siguiente entrada:Grupo de tipos de posición : SRVP (producto de servicio)A continuación, seleccione Grabar . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |

##### Crear producto de servicio - SRV_BOM_02_02

Objetivo

Este material solo es relevante para la edición en la nube.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de producto (MDG).. | El Inicio Aparece la página. |  |
| 2 | Acceder a la aplicación SAP Fiori | Seleccione el Crear material mosaico. | El Crear material (pantalla inicial) se visualiza. |  |
| 3 | Actualizar datos básicos de material (para producto de servicio) | El Crear material (pantalla inicial) realice las siguientes entradas: ventana de diálogo, seleccione laMaterial: SRV_BOM_02_02Tipo de material: Producto de servicioA continuación, seleccione Continuar (Intro) . | Ha actualizado la información básica para el nuevo producto de servicio.El Seleccionar vista(s) se visualiza la ventana de diálogo. |  |
| 4 | Seleccionar vistas | El Seleccionar vista(s) ventana de diálogo, seleccione el vistas siguientes:Datos básicos 1Ventas: Datos org.ventas 1Ventas: Datos org.ventas 2A continuación, seleccione Continuar (Intro) . | El Niveles de organización la ventana de diálogo es visualizados. |  |
| 5 | Seleccionar niveles de organización | El Niveles de organización ventana, actualice la valores siguientes:Org.ventas: 1710 (Org.ventas nac.US)Canal distrib.: 10 (Ventas directas)A continuación, seleccione Continuar (Intro) . | Se han seleccionado datos organizativos.El Crear material SRV_BOM_02_02 la vista es visualizados. |  |
| 6 | Actualizar datos básicos | El Datos básicos 1 , actualice los siguientes valores:Descr.: Producto de servicio con BOM 02_02Unidad de medida base: HR (hora)Grupo de materiales: P001 (Servicios)Gr.tp.pos.gen.: SRVP (producto de servicio)A continuación, seleccione Intro . | Se actualizan los datos básicos y se graba el producto de servicio.Después de guardar, el Crear material (pantalla inicial) Se muestra la vista.Para cada idioma diferente utilizado en su empresa, la descripción correspondiente para el producto debe actualizarse por código de idioma. |  |
| 7 | Actualizar datos de organización de ventas (1) | El Ventas: org.ventas 1 , actualice los siguientes valores:Datos generalesDescuento por pronto pago: X <seleccionado>Datos fiscalesClasificación fiscal: 1 (Impuesto completo)A continuación, seleccione Intro . | Se actualizan los datos organizativos de ventas. El Ventas: org.ventas 2 Se visualiza la etiqueta. |  |
| 8 | Actualizar datos de organización de ventas (2) | El Ventas: org.ventas 2 , actualice la siguiente entrada:Grupo de tipos de posición : SRVP (proyecto)A continuación, seleccione Grabar . | Se actualizan los datos organizativos de ventas. El Ventas: General/Centro Se visualiza la etiqueta. |  |

#### Crear nueva lista de materiales

Objetivo

Este material solo es relevante para la edición en la nube. En este paso, puede crear una nueva lista de materiales.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como responsable de listas de materiales.. | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar lista de materiales (versión 2) - Crear, modificar y visualizar listas de materiales (F1813A) aplicación. |  |  |
| 3 | Seleccione Crear lista de materiales. | El Actualizar lista de materiales , seleccione Crear lista de materiales . | El Crear lista de materiales aparece la ventana de diálogo. |  |
| 4 | Actualizar datos de cabecera de lista de materiales | El Crear lista de materiales introduzca datos similares al siguiente ejemplo y seleccione OK:EjemploMaterial : SRV_BOM_01_01Utilización de lista de materiales : S (Gestión de servicios)Inicio de validez : Hoy | El Actualizar lista de materiales se visualiza y, por defecto, la Componentes Se abrirá la pestaña. |  |
| 5 | Actualizar datos de componente de lista de materiales | En la línea Número de posición de lista de materiales 0010, realice entradas similares al siguiente ejemplo:EjemploComponente: SRV_BOM_02_01Cantidad de componente: 10 RR. HH.(Pulse Intro para activar los campos Componente y Cantidad de componente)Nota El valor de categoría de posición es N (posición no de almacén) | Número de posición de lista de materiales 0010, Componente, Descripción de componente y Cantidad de componente se visualiza en la primera línea de la tabla. |  |
| 6 | Actualizar datos adicionales de componentes de LMat | Repita el paso anterior para el número de posición de lista de materiales 0020 con las siguientes entradas:Componente: SRV_BOM_02_02Cantidad de componente: 20 RR. HH.(Pulse Intro para activar los campos Componente y Cantidad de componente)Nota El valor de categoría de posición es N (posición no de almacén) | Número de posición de lista de materiales 0020, Componente, Descripción de componente y Cantidad de componente se visualiza en las líneas de tabla. |  |
| 8 | Navegar a detalle de posición | En la Línea 0010 de número de posición de lista de materiales , haga clic en la flecha de detalles en el extremo derecho de la tablaEl Actualizar lista de materiales , realice entradas similares al siguiente ejemplo en la pantalla Detalles básicos pestaña:EjemploCantidad de componente : 10UM de componente : RR. HH. | El Actualizar lista de materiales con la sección de detalles para la posición introducida. |  |
| 9 | Navegar a detalle de posición | En la Línea 0020 de número de posición de lista de materiales , haga clic en la flecha de detalles en el extremo derecho de la tablaEl Actualizar lista de materiales , realice entradas similares al siguiente ejemplo en la pantalla Detalles básicos pestaña:EjemploCantidad de componente : 20UM de componente : RR. HH. | El Actualizar lista de materiales con la sección de detalles para la posición introducida. |  |
| 10 | Seleccione Guardar. | El Actualizar lista de materiales seleccione Crear . | Se graba la lista de materiales.Nota Después de guardar, el estado de la lista de materiales se fijará automáticamente en 1 (Activo).Si el Estado de la lista de materiales 2 (Inactivo) es necesario para la lista de materiales, en la pantalla Actualizar lista de materiales, seleccione Mostrar detalles de cabecera, seleccione Datos administrativos y fije adecuadamente el Estado de la lista de materiales antes de volver a guardar.Número de modificación se añade en la ficha Cronología. |  |

### Crear lista de materiales para equipo

#### Crear equipo

Objetivo

En este paso de test se actualiza un registro para un equipo que está instalado en una ubicación técnica.

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Maintenance Planner, | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 3 | Acceder a la aplicación SAP Fiori | Abierto Crear objeto técnico | Se abre una ventana nueva que muestra la Crear objeto técnico: Pantalla inicial. |  |
| 4 | Crear equipo | El Crear objeto técnico seleccione el Tipo de objeto técnico: Equipo.En la siguiente pantalla, introduzca lo siguiente:Tipo de objeto técnico: EquipoObjeto técnico: dejar en blancoInicio de validez: fecha de hoyCategoría de objeto técnico: M (máquinas)Seleccionar Continúe (Intro). |  |  |
| 5 | Actualizar datos generales | El Crear objeto técnico: <ID de equipo> en la pantalla Datos generales introduzca lo siguiente:Descripción : Por ejemplo, Equipo de cabecera de lista de materiales para servicioTipo de objeto : Por ejemplo, 9400Fecha de puesta en servicio : Por ejemplo, la fecha de hoyPaís/región de fabricación : por ejemplo, EE. UU.Mes/Año de construcción : Por ejemplo, 04/2011Número de pieza de fabricante : Por ejemplo, HZZ-TD B4Número de serie del fabricante : Por ejemplo, HZZ-TD B4/66Valor de adquisición/Moneda : Por ejemplo, 10.000,00/ USDFecha de adquisición : Por ejemplo, 04/10/2011Nota Opcionalmente, actualice otros datos generales y, a continuación, vaya a la sección Datos de ubicación. | Aparecerá la pantalla Crear objeto técnico: datos generales. |  |
| 6 | Actualizar datos de ubicación | En la Datos de ubicación introduzca lo siguiente:Centro de emplazamiento : Por ejemplo, 1710 para EE. UU.Ubicación : Por ejemplo, YB_1701 para EE. UU.Área de empresa : Por ejemplo, YOH para EE. UU.Nota Los objetos técnicos que pertenecen a la misma estructura deben tener asignado el mismo centro. Como alternativa, puede dejar la información del centro vacía para todos los objetos técnicos.Opcionalmente, actualice más detalles, como la información de dirección. | Aparece la pantalla Crear objeto técnico: datos de ubicación. |  |
| 8 | Actualizar datos organizativos | En la Datos organizativos introduzca lo siguiente:Grupo de planificación : Por ejemplo, 920 para EE. UU.Centro de planificación : Por ejemplo, 1710 para EE. UU.Puesto de trabajo de mantenimiento : Por ejemplo, RES-0100 para EE. UU.Centro de puesto de trabajo : Por ejemplo, 1710 para EE. UU.Centro de coste : Por ejemplo, 17101701 para EE. UU.Opcionalmente, puede actualizar información adicional como, por ejemplo, información del socio, etc. en la sección Datos organizativos. | El Crear objeto técnico: Datos organizativos Aparece la pantalla. |  |
| 9 | Guardar equipo | Opcionalmente, puede actualizar información adicional para otras secciones.Seleccionar Verificar entradas botón.Seleccionar Grabar . | Se ha creado el equipo.Anote la ID de equipo creado. |  |

#### Crear lista de materiales para equipo

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en Rampa de lanzamiento SAP Fiori como Maintenance Planner, | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Crear lista de materiales para equipo | Se abre una ventana nueva que muestra la Crear lista de materiales para equipo: Pantalla inicial. |  |
| 3 | Crear equipo | El Crear lista de materiales para equipo: Pantalla inicial. introduzca lo siguiente:Equipo : ID de equipo generado en el capítulo anteriorUtiliz.LMat: SSeleccionar Continuar . |  |  |
| 4 | Actualizar datos de material | El Crear lista de materiales para equipo: Resumen general de posiciones en la pantalla Material introduzca lo siguiente:Componente : ID de material Por ejemplo SRV_BOM_02_02Tipo de posición : N (posición no de almacén)Cantidad : Por ejemplo, 10Unidad de medida : por ejemplo, RR. HH.Seleccionar Intro | Aparece la pantalla Crear lista de materiales para equipo: Resumen general de posiciones. |  |
| 5 | Guardar equipo | Seleccionar Grabar | Se ha creado la lista de materiales para equipo |  |

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
> Flagged while digesting this document, not verified: Step 8 of SRV_BOM_02_02 labels item category group SRVP as '(proyecto)' while the other products label it '(producto de servicio)'

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/bom-mds-63j-493]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6]]
- related-to :: [[14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490]]
- related-to :: [[14-maintenance-service-and-projects/mds-63j-495]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 26,455 chars in the whole document
