---
id: 05-treasury-and-cash-management/script-de-datos-maestros-crear-socio-comercial-para-treasury-and-risk
title: "Script de datos maestros: Crear socio comercial para Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_ES_XX)"
description: "Spanish master data test script (22G) for SAP S/4HANA Cloud Public Edition 2608: creating and maintaining business partners for Treasury and Risk Management."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-business-partners]
aliases: [22G_S4CLD2608_Master_Data_ES_XX]
keywords: [Business Partners for Treasury and Risk Management, business partner creation, treasury risk management, payment details, correspondence profiles, business partner roles, business partner authorizations, derived flows, company code reporting data, letter of credit]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-258
topic: 05-treasury-and-cash-management/treasury-business-partners
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros: Crear socio comercial para Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Business Partners for Treasury and Risk Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear socio comercial para Treasury and Risk Management - MDS (22G) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894534)

[2 Requisitos previos 3](#_Toc233894535)

[2.1 Acceso al sistema 3](#_Toc233894536)

[2.2 Roles 3](#_Toc233894537)

[2.3 Datos maestros, datos organizativos y otros datos 4](#_Toc233894538)

[3 Tabla de resumen 5](#_Toc233894539)

[4 Procedimientos de prueba 7](#_Toc233894540)

[4.1 Actualizar datos generales para socio comercial 7](#_Toc233894541)

[4.2 Actualizar datos de sociedad para socio comercial 10](#_Toc233894542)

[4.2.1 Actualizar detalles de pago para socio comercial 10](#_Toc233894543)

[4.2.2 Actualizar autorizaciones para socio comercial 13](#_Toc233894544)

[4.2.3 Actualizar movimientos derivados para socio comercial (opcional) 14](#_Toc233894545)

[4.2.4 Actualizar datos de informes en sociedad para socio comercial 16](#_Toc233894546)

[4.3 Actualizar datos de correspondencia para socio comercial 17](#_Toc233894547)

[4.3.1 Actualizar perfil y asignaciones de grupo de IC a destinatario externo 17](#_Toc233894548)

[4.3.2 Actualizar perfil y asignaciones de grupo de IC a destinatario interno 21](#_Toc233894549)

[4.4 Actualizar datos maestros de socio comercial para valores 25](#_Toc233894550)

[4.4.1 Crear rol de emisor para socio comercial 26](#_Toc233894551)

[4.4.2 Crear rol de banco de depósito para interlocutor comercial 27](#_Toc233894552)

[4.5 Actualizar datos maestros de socio comercial para carta de crédito documentario 28](#_Toc233894553)

[4.5.1 Crear rol de banco para socio comercial 28](#_Toc233894554)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

En este módulo se proporcionan los pasos manuales básicos para crear interlocutores comerciales para Treasury and Risk Management.

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
| Especialista en tesorería - Back office | SAP_BR_TREASURY_SPECIALIST_BOE | Back office de tesorería | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Especialista en datos maestros - Datos de socio comercial | SAP_BR_BUPA_MASTER_SPECIALIST | Datos maestros - Socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales / Gobernanza de socios comerciales | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Experto en configuración - Configuración del proceso empresarial | SAP_BR_BPC_EXPERT | Configuración de proceso empresarial / Configuración de proceso empresarial - Finanzas / Configuración del proceso empresarial - Aprovisionamiento / Gestionar su solución / Configuración de proceso empresarial: flujo de trabajo / Configuración empresarial - Gestión de funciones / Configuración de proceso empresarial - Explorador de ampliabilidad / Configuración empresarial - Transporte | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Datos maestros, datos organizativos y otros datos

La estructura organizativa y los datos maestros de su empresa se han creado en su durante la activación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan materiales, clientes y proveedores, por ejemplo, en función del enfoque operativo de su empresa.

Utilice sus propios datos maestros para realizar el procedimiento de test. Si ha instalado un paquete de línea base de SAP Best Practices, puede utilizar el después de los datos de muestra del paquete de referencia.

|  |
| --- |
| Atención Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

| Datos | Valor de muestra | Detalles | Comentarios |
| --- | --- | --- | --- |
| SOCIEDAD | Por ejemplo, 1010 |  |  |
| MONEDA | Por ejemplo, EUR |  |  |
| MONEDA EXTRANJERA 1 | Por ejemplo, USD |  |  |
| BANCO PROPIO | Por ejemplo, DEBK1 |  |  |
| CUENTA BANCARIA PROPIA ID 1 | Por ejemplo, DEAC1 |  |  |
| ID DE CUENTA BANCARIA PRINCIPAL 2 | Por ejemplo, USAC2 |  |  |
| INTERLOCUTOR COMERCIAL | 10537001 |  |  |

## Tabla de resumen

Crear socio comercial para Treasury and Risk Management - MDS (22G) consta de varios pasos de proceso proporcionados en las siguientes tablas:

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

Tabla 1: Actualizar datos para interlocutor comercial normal

| Paso de proceso, informe o posición | Rol empresarial | Transacción/APP | Resultados previstos |
| --- | --- | --- | --- |
| [Actualizar datos generales para socio comercial](#unique_7) [página ] 7 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se actualizan los datos generales para el socio comercial. |
| Actualizar datos de sociedad para socio comercial |  |  |  |
| [Actualizar detalles de pago para socio comercial](#unique_8) [página ] 10 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se actualizan los datos de detalles de pago para el socio comercial. |
| [Actualizar autorizaciones para socio comercial](#unique_9) [página ] 13 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se actualizan los datos de autorización para el socio comercial. |
| [Actualizar movimientos derivados para socio comercial (opcional)](#unique_10) [página ] 14 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se actualizan los datos de movimientos derivados para el socio comercial. |
| [Actualizar datos de informes en sociedad para socio comercial](#unique_11) [página ] 16 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se actualizan los datos de informes para el socio comercial. |
| Actualizar datos de correspondencia para socios comerciales |  |  |  |
| [Actualizar perfil y asignaciones de grupo de IC a destinatario externo](#unique_12) [página ] 17 | Especialista en datos maestros - Datos de socio comercial | Asignar perfil y grupo de IC - Destinatarios externos (FTR_EXT_ASSIGN) | Los perfiles de SC y los grupos de SC se actualizan para el destinatario externo. |
| [Actualizar perfil y asignaciones de grupo de IC a destinatario interno](#unique_13) [página ] 21 | Especialista en datos maestros - Datos de socio comercial | Asignar perfil y grupo de IC - Destinatarios internos (FTR_INT_ASSIGN) | Los perfiles de SC, los grupos de SC y los ID de usuario se actualizan para el destinatario interno. |
| Actualizar datos maestros de socio comercial para valores |  |  |  |
| [Crear rol de emisor para socio comercial](#unique_14) [página ] 26 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se ha creado el emisor de rol. |
| [Crear rol de banco de depósito para interlocutor comercial](#unique_15) [página ] 27 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se ha creado el rol Banco de depósito. |
| Actualizar datos maestros de socio comercial para carta de crédito documentario |  |  |  |
| [Crear rol de banco para socio comercial](#unique_16) [página ] 28 | Especialista en datos maestros - Datos de socio comercial | Actualizar interlocutor comercial (IC) | Se ha creado el rol Banco. |

## Procedimientos de prueba

Esta sección describe los procedimientos de test para cada paso del proceso que pertenece a este elemento de alcance.

### Actualizar datos generales para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta sección se describe el proceso de actualización de datos generales para el interlocutor comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Gemas. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Introducir datos en la pantalla inicial | El Actualizar interlocutor comercial , seleccione Organización . | El Crear organización se visualiza. |  |
| 4 | Introducir datos de dirección | El Crear organización introduzca los siguientes datos:Interlocutor comercial : Por ejemplo, 10537001 .Agrupación : Seleccionar TR02 Socio de tesorería (externo) .Crear en rol IC : Seleccionar 000000 Interlocutor comercial (Gen.) .Título : Seleccionar 0003 Empresa .Nombre : Por ejemplo, Banco 1 – BANCO DE MUESTRA .Tratamiento : Por ejemplo, Banco 1 .Concepto de búsqueda 1/2 : Por ejemplo, Banco 1 .Calle/Número : <Dirección>Código postal/Población : <Código postal y ciudad>País/Región : Seleccionar <Código de país/región> .Idioma : Seleccionar <Código de idioma> .Correo electrónico : <Dirección de correo electrónico>Dirección válida desde : Por ejemplo, <Fecha actual del año anterior> .Dirección válida hasta : Por ejemplo, 31 de diciembre del año 9999 .Seleccionar Grabar .Nota Permanezca en la pantalla para los pasos siguientes.Nota Si solo ve Interlocutor comercial (gen.) sin la clave 000000 , luego puede ir a Menú > Opciones - Diseño de interacción > Visualización > Lista desplegable > Mostrar listas desplegables con claves y actívelo. | El interlocutor comercial se ha creado correctamente. |  |
| 5 | Cambiar a modo de modificación | El Mostrar organización: 10537001 , seleccione Cambiar entre visualizar y modificar e introduzca los siguientes datos:Modificación en rol IC : Seleccionar TR0151 Parte contratante . | Más pestañas relacionadas con la parte contratante, como Datos legales y Valoración visualización. |  |
| 6 | Introducir datos legales | El Modificar organización: 10537001, nuevo rol Parte contratante , seleccione Menú de navegación .Nota El Menú de navegación está en la parte derecha de la pantalla. Se muestra como … , que está justo al lado del > símbolo.En la lista desplegable, seleccione Datos legales e introduzca los siguientes datos:País/Región : Por ejemplo, seleccione DE .Seleccionar Grabar .Nota Permanezca en la pantalla para los pasos siguientes. | Los datos legales se introducen y se guardan.El Modificar organización: 10537001, nuevo rol Parte contratante se visualiza. |  |
| 7 | Introducir datos de transacción de pago | El Modificar organización: 10537001, rol Parte contratante , seleccione Menú de navegación .En la lista desplegable, seleccione Transacciones de pago e introduzca los siguientes datos para dos filas:Fila 1 :ID : Código de moneda + 1, por ejemplo, EUR1 .P/R : <Código de país/región>Clave de banco : <Clave de banco>Cuenta bancaria : <Cuenta bancaria>IBAN : Seleccionar IBAN y seleccione Continuar en el IBAN ventana de diálogo.Fila 2 :ID : Código de moneda extranjera + 1, por ejemplo, USD1 .P/R : <Código de país/región>Clave de banco : <Clave de banco>Cuenta bancaria : <Cuenta bancaria>IBAN : Seleccionar IBAN y seleccione Continuar en el IBAN ventana de diálogo.Seleccionar Grabar .Nota Si un Información se muestra cuando selecciona IBAN , seleccione Continuar .Nota El IBAN se utiliza principalmente en países de la UE. Para EE. UU., omita los pasos relacionados con IBAN. | Se introducen los datos de la operación de pago y se graba el interlocutor comercial. |  |

### Actualizar datos de sociedad para socio comercial

#### Actualizar detalles de pago para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta sección se describen los pasos para actualizar los datos de detalles de pago para un socio comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Cambiar a modo de modificación | El Actualizar interlocutor comercial , seleccione IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccionar TR0151 Parte contratante | El Modificar organización: 10537001, rol Parte contratante se visualiza. |  |
| 4 | Indicar SI: Datos de detalles de pago | Activado Modificar organización: 10537001, rol Contraparte , seleccione Sociedad, e introduzca los siguientes datos:Sociedad : por ejemplo, 1010Seleccionar Intro y seleccione SI: Detalles de pago para introducir las siguientes cuatro filas de datos:Fila 1Moneda : por ejemplo, EURPay.Det.ID : por ejemplo, EURIBanco propio : por ejemplo, DEBK1ID de cuenta : por ejemplo, DEAC1Pagador : por ejemplo, déjelo en blancoBanco interlocutor : por ejemplo, déjelo en blancoSolicitud de pago : por ejemplo, DesmarcarMétodos de pago : por ejemplo, déjelo en blancoFila 2Moneda : por ejemplo, EURPay.Det.ID : por ejemplo, EUROBanco propio : por ejemplo, DEBK1ID de cuenta : por ejemplo, DEAC1Pagador : por ejemplo, 10537001Banco interlocutor : por ejemplo, EUR1Solicitud de pago : por ejemplo, seleccionarMétodos de pago : por ejemplo, TFila 3Moneda : por ejemplo, USDPay.Det.ID : por ejemplo, USDIBanco propio : por ejemplo, DEBK1ID de cuenta : por ejemplo, USDACPagador : por ejemplo, déjelo en blancoBanco interlocutor : por ejemplo, déjelo en blancoSolicitud de pago : por ejemplo, DesmarcarMétodos de pago : por ejemplo, déjelo en blancoFila 4Moneda : por ejemplo, USDPay.Det.ID : por ejemplo, USDOBanco propio : por ejemplo, DEBK1ID de cuenta : por ejemplo, USDACPagador : por ejemplo, 10537001Banco interlocutor : por ejemplo, USD1Solicitud de pago : por ejemplo, SeleccionarMétodos de pago : por ejemplo, FNota Permanezca en esta pantalla para los pasos siguientes.Nota Asegúrese de introducir la vía de pago en el campo Vías de pago en lugar del campo Vía de pago.Nota Si aparece una ventana de advertencia con el siguiente mensaje: Interlocutor comercial propuesto como pagador/receptor del pago (véase txt.expl.)¿Desea volver a visualizar este mensaje para este interlocutor comercial?Seleccionar No . | Se introducen los datos SI: Detalles de pago. |  |
| 5 | Asignar detalles de pago | Desde la pantalla del paso anterior, asigne detalles de pago. Por ejemplo, para EUR , seleccione el EUR EURI fila.Seleccionar Asignar , en la Modificación de parte contratante: Asignación de detalles de pago ventana de diálogo.Seleccionar Seleccionar todo lo entrante . El resultado es que EURI se muestra en IDPag-Ing .Seleccionar Continuar para cerrar la ventana de diálogo.Seleccione el EUR EURO fila.Seleccionar Asignar , en la Modificación de parte contratante: Asignación de detalles de pago ventana de diálogo.Seleccionar Seleccionar todo lo saliente . El resultado es que EURO se muestra en ID P sal. .Seleccionar Continuar para cerrar la ventana de diálogo.Repita el paso para USD :USDI : IDPag-IngUSDO : ID P sal.El Modificar organización: 10537001, rol Parte contratante , seleccione Grabar . | Se graban los detalles de pago y las asignaciones. |  |

#### Actualizar autorizaciones para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Esta sección describe los pasos para actualizar los datos de autorización para un interlocutor comercial para SAP Treasury and Risk Management .

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Cambiar a modo de modificación | El Actualizar interlocutor comercial , seleccione IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccionar TR0151 Parte contratante | El Modificar organización: 10537001, rol Contraparte se visualiza. |  |
| 4 | Introducir SI: Datos de autorizaciones | El Modificar organización: 10537001, rol Contraparte , seleccione Sociedad , seleccione SI: Autorizaciones .Seleccione el Autoriz. para todas las entradas y seleccione Grabar .Nota También puede autorizar un tipo de producto y un tipo de transacción específicos desplegando las carpetas. Con fines de prueba, proporcionamos todas las autorizaciones a todos los tipos de tipos de producto y tipos de transacción. | Se graban los datos de autorización. |  |

#### Actualizar movimientos derivados para socio comercial (opcional)

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta sección se describen los pasos para actualizar los datos de movimiento derivados para un socio comercial. Algunos países tributan los ingresos por tipo de interés lo que crea un tipo especial de impuesto que debe incluir para un socio comercial. En este procedimiento, fija cualquier impuesto sobre la renta de intereses específico de país/región para Producto tipo y Transacción type. Este paso es opcional.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Gemas. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | Se abre la aplicación. |  |
| 3 | Cambiar a modo de modificación | El Actualizar interlocutor comercial , seleccione IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Pulsar Intro .Seleccionar Cambiar entre visualizar y modificar e introduzca los siguientes datos:Modificación en rol IC : Seleccionar TR0151 Parte contratante . | El Modificar organización: 10537001, rol Contraparte se visualiza. |  |
| 4 | Introducir SI: Datos de movimientos derivados | El Modificar organización: 10537001, rol Contraparte , seleccione Sociedad , seleccione SI: Movimientos derivados , y despliegue: Mercado de dinero > Instrumento de tipo de interés > 51A Depósito a plazo fijo/préstamo > 100 Inversión .Seleccionar Marcar/Desmarcar línea entrante .En la Procedimiento para generar movimientos derivados 1 entrada ventana de diálogo, seleccione INTDE .Seleccionar OK .Los resultados son lo que INTDE se muestra en el Procedimiento columna.Seleccionar Grabar . | Los datos de Movimientos derivados se introducen y se guardan. |  |
| 5 | Repetir para clases de producto y transacción adicionales | Repita el paso anterior para cada una de las siguientes clases de producto y transacción:Clase de producto.…..Clase de operación52B.….10053A.….10053A.….10153A.….10254A.….10055A.….10058A.….300Consejo Las ubicaciones de los tipos de producto son las siguientes:52B está bajo Mercado de dinero > Depósito con preaviso .53A está bajo Mercado de dinero > Efecto comercial .54A está bajo Mercado de dinero > Operación de flujo de caja .55A es inferior a Mercado de dinero > Instrucción de tipo de interés .58A está bajo Mercado de dinero > Instrumento de tipo cuenta corriente . |  |  |

#### Actualizar datos de informes en sociedad para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

En esta sección se describen los pasos para actualizar la relación empresarial de un interlocutor comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Cambiar a modo de modificación | El Actualizar interlocutor comercial , seleccione IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccione TR0151 Parte contratante | El Modificar organización: 10537001, rol Contraparte se visualiza. |  |
| 4 | Introducir datos de informes en sociedad | El Modificar organización: 10537001, rol Contraparte , seleccione Sociedad , seleccione Datos de informes en sociedad,Nota Si no ves Datos de informes en sociedad en la pantalla y, a continuación, seleccione Menú de navegación y seleccione en el menú desplegable.Introduzca los siguientes datos:Rel.comp. : por ejemplo, 3 OtrosSeleccionar Grabar .Nota Rel.comp. refleja su relación con la parte contratante:1 afiliado y consolidado2 afiliado pero no consolidado3 no afiliado4 No lo utilicesSe utilizan para derivar las cuentas de mayor correctas. | Los datos de informes se introducen y se graban. |  |

### Actualizar datos de correspondencia para socio comercial

SAP Treasury Risk Management proporciona una funcionalidad de correspondencia estándar. Con esto la funcionalidad de correspondencia, cada vez que se guarda una transacción de Treasury Risk Management, el sistema envía un correo electrónico al socio comercial o imprime automáticamente un a la máquina de impresión designada.

Para utilizar esta funcionalidad de correspondencia, se deben asignar los siguientes datos a una empresa socio:

- Perfil de interlocutor comercial
- Grupo de interlocutores comerciales

#### Actualizar perfil y asignaciones de grupo de IC a destinatario externo

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este procedimiento describe la asignación de perfiles de interlocutor comercial y grupos de IC a una empresa externa interlocutor.

Los perfiles de interlocutor comercial y los grupos de interlocutores comerciales controlan las actividades de correspondencia en SAP Treasury Risk Gestión .

Se proporcionan los siguientes perfiles de interlocutor comercial predefinidos:

- PR_EMAIL
- PR_PRINT

Estos perfiles de interlocutor comercial predefinidos se pueden asignar a su interlocutor comercial. Por ejemplo, si la comunicación con su el interlocutor comercial es por correo electrónico y, a continuación, asigna PR_EMAIL al interlocutor comercial. Si la comunicación se realiza mediante el envío de una documento, asigne PR_PRINT al interlocutor comercial.

Se ha predefinido el siguiente grupo de interlocutores comerciales:

- BPG_DEFAULT

Asigne este grupo de interlocutores comerciales a su interlocutor comercial o utilice los pasos de configuración Definir grupo de interlocutores comerciales y asignar atributos para grupos de interlocutores comerciales para agregar su propio negocio Grupo de interlocutores y, a continuación, asigne los atributos adecuados según sus necesidades específicas. Diferentes perfiles de interlocutor comercial y Los grupos de IC se pueden asignar al mismo interlocutor comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en tesorería - Back office . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Asignar perfil y grupo de IC - Destinatarios externos (FTR_EXT_ASSIGN) . | El Asignar perfil y grupos de IC a destinatarios externos se visualiza. |  |
| 3 | Introducir datos de interlocutor comercial | A la izquierda de Asignar perfil y grupos de IC a destinatarios externos , seleccione Insertar Fila e introduzca los siguientes datos,Interl.cial. : por ejemplo, 10537001Soc. : por ejemplo, 1010Cl.entr./exped. : por ejemplo, seleccione el CONTRAPARTE fila,Pulsar Intro . | Se introduce la información del interlocutor comercial. |  |
| 4 | Asignar perfil empresarial y grupo de socios comerciales al socio comercial | En la parte superior derecha de la Asignación de perfiles y grupos de IC a destinatarios externos seleccione Desplegar nodo y expandir:BP:0010537001 /CoCd: 1010 / Rec/SendType: CONTRAPARTE > Mercado de dinero > Instrumento de tipo de interés > 51A Depósito a plazo fijo/préstamo > 100 Inversión .Seleccionar 10 Contrato .En la parte inferior derecha del Asignación de perfiles y grupos de IC a destinatarios externos seleccione Insertar fila y añada el correo electrónico o el perfil de impresión:Nota Normalmente, solo uno Perfil es asignado a una clase de producto/clase de operación/actividad Categoría. Si se deben asignar ambos perfiles, después de completa el primer perfil, seleccione Insertar Fila de nuevo para añadir el otro perfil.Ya sea cuando el perfil es un correo electrónico :Perfil : por ejemplo, PR_EMAILGrupo IC : por ejemplo, BPG_DEFAULTSeleccionar Grabar .O cuando se imprime el perfil :Perfil : por ejemplo, PR_PRINTGrupo IC : por ejemplo, BPG_DEFAULTSeleccionar Grabar . | Los perfiles de interlocutor comercial y los grupos de IC están asignados para el Clase de producto/Clase de operación/Tipo de actividad. |  |
| 5 | Repetir para clase de producto/clase de operación/categoría de actividad adicionales | Seleccionar Modificar fila en la parte superior izquierda de la pantalla y repita el paso anterior para asignar perfiles de IC y grupos de IC para el siguientes clases de producto y transacciones:Tipo de productoTipo de transacciónTipo de actividad51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1022060A1032060A1042060A1052060A1072060B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | Para todas las clases de producto/clases de transacción/actividad enumeradas Se han asignado categorías, perfiles de IC y grupos de IC. |  |

#### Actualizar perfil y asignaciones de grupo de IC a destinatario interno

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

El ID de destinatario interno está predefinido por SAP. Podría ser enlazado a ID(s) de usuario SAP. Una vez que se vincula a un ID de usuario de SAP, siempre que un objeto de correspondencia generado, SAP TRM intentará enviar correspondencia información de la dirección del ID de usuario SAP. En función de los diferentes perfiles (PR_EMAIL /PR_PRINT), el correo electrónico se puede enviar a la dirección de correo electrónico del usuario o un formulario es impresión.

En este paso se describe cómo asignar perfiles de interlocutor comercial y grupos de interlocutores comerciales a un interlocutor comercial interno.

|  |
| --- |
| Recordar Valores de muestra para los valores de datos maestros son específicos de país/región y los valores proporcionados en la siguiente tabla son para Alemania. Sustituir el Valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilizar maestro valores de datos que ha creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en tesorería - Back office . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Asignar perfil y grupo de IC - Destinatarios internos (FTR_INT_ASSIGN) . | El Asignación de perfiles y grupos de IC a destinatarios internos se visualiza. |  |
| 3 | Introducir datos de interlocutor comercial | En la parte izquierda de la Asignación de perfiles y grupos de IC a destinatarios internos , seleccione Insertar Fila e introduzca los siguientes datos,Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los siguientes valores de ejemplo son para Alemania. Sustituya su Valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin.IntRec : por ejemplo, INT.REC.Soc. : por ejemplo, 1010Cl.entr./exped. : por ejemplo, seleccione el INTERNO casilla de selección.Pulsar Intro . | Se introduce la información del interlocutor comercial. |  |
| 4 | Asignar perfil empresarial y grupo de socios comerciales al socio comercial | En la parte superior derecha del Asignación de perfiles y grupos de IC a destinatarios internos pantalla, expanda:IC:INT. RECP /Soc.: 1010 / Rec/SendType: INTERNO > Mercado de dinero > Instrumento de tipo de interés > 51A Depósito a plazo fijo/préstamo > 100 Inversión .Seleccionar 10 Contrato .En la parte inferior derecha de la Asignación de perfiles y grupos de IC a destinatarios internos seleccione Insertar fila .Introduzca la información de perfil para correo electrónico o impresión:Perfil : por ejemplo, para correo electrónico, PR_EMAILGrupo IC : por ejemplo, BPG_DEFAULTNombre de usuario : seleccione un <Usuario ID> .Seleccionar Grabar .Seleccionar Insertar fila de nuevo y añada otro entrada para impresión:Perfil : por ejemplo, para la opción de impresión, PR_PRINTGrupo IC : por ejemplo, BPG_DEFAULTNombre de usuario : seleccione un <Usuario ID> .Nota El <ID de usuario> es un usuario de back end ID.Seleccionar Grabar . | Se han asignado el perfil de interlocutor comercial, el grupo de IC y el ID de usuario para la clase de producto/clase de operación/tipo de actividad. |  |
| 5 | Repetir para clase de producto/clase de operación/categoría de actividad adicionales | Seleccionar Modificar fila en la parte superior izquierda de la pantalla y repita el paso anterior para asignar perfiles de IC y grupos de IC para el siguientes clases de producto y transacciones:Tipo de productoTipo de transacciónTipo de actividad51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1015560A1022060A1025560A1032060A1035560A1042060A1045560A1052060A1055560A1072060A1075560B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | Los perfiles de SC, los grupos de SC y los ID de usuario se asignan a todas las clases de producto/transacción enumeradas Tipos/Categorías de actividad. |  |

### Actualizar datos maestros de socio comercial para valores

Objetivo

Para instrumentos financieros relacionados con valores, por ejemplo, Fondo del mercado de dinero, a registre la información básica del emisor y del banco de depósito, cree lo siguiente roles de interlocutor comercial:

- TR0150 Emisor
- TR0152 Banco de depósito

#### Crear rol de emisor para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este paso describe los procesos para crear el rol Emisor para un interlocutor comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial : se visualiza la pantalla. |  |
| 3 | Crear rol de emisor | Seleccionar IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccionar TR0150 Emisory seleccione Grabar . | El Modificar organización: 10537001, rol Emisor se muestra la siguiente notificación:Se han guardado las modificaciones . |  |

#### Crear rol de banco de depósito para interlocutor comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Objetivo

Este paso describe los procesos para crear el rol Banco de depósito para un interlocutor comercial.

|  |
| --- |
| Recordar Los valores de muestra para los valores de datos maestros son específicos de país/región y los siguientes valores de ejemplo proporcionados son para Alemania. Sustituir los valores específicos de país/región proporcionados por SAP Best Practices for SAP S/4HANA Cloud Public Edition o utilice valores de datos maestros que haya creado para este fin. |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se visualiza la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación SAP Fiori | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Crear rol de banco de depósito | Seleccionar IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial : 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccionar TR0152 Banco de depósitoy seleccione Grabar . | El Modificar organización: 10537001, rol Banco de depósito se muestra la siguiente notificación:Se han guardado las modificaciones. |  |

### Actualizar datos maestros de socio comercial para carta de crédito documentario

#### Crear rol de banco para socio comercial

Administración de pruebas

Proyecto de cliente: Rellene las partes específicas del proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID de caso de test | <X.XX> | Fecha de prueba: |  |
| Nombre de usuario que ejecuta un test: |  | Duración: |  |
| Rol(es) empresarial(es): |  | Responsabilidad: | <Indique el proveedor de servicios, el cliente o el proveedor de servicios conjuntos y el cliente> |

Procedimiento

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Aprobado / Error / Comentario |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión en la rampa de lanzamiento SAP Fiori | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en datos maestros - Datos de socio comercial . | Se muestra la rampa de lanzamiento SAP Fiori. |  |
| 2 | Acceder a la aplicación | Abierto Actualizar interlocutor comercial (IC) . | El Actualizar interlocutor comercial se visualiza. |  |
| 3 | Crear rol de banco | Seleccionar IC abierto . En la ventana de diálogo, indique los siguientes datos:Interlocutor comercial: 10537001Seleccionar Intro .Seleccionar Cambiar entre visualizar y modificar , e introduzca los siguientes datos:Modificación en rol IC : seleccionar TR0703 Bancoy seleccione Grabar . | El Modificar organización: 10537001 rol Banco se muestra la siguiente notificación:Se han guardado las modificaciones. |  |

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
- related-to :: [[05-treasury-and-cash-management/create-business-partner-for-treasury-and-risk-management-mds-22g-257]]
- related-to :: [[05-treasury-and-cash-management/geschaftspartner-fur-treasury-and-risk-management-anlegen-mds-22g-256]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-259]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-261]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 46,561 chars in the whole document
