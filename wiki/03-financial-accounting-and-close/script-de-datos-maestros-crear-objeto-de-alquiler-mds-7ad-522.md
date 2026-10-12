---
id: 03-financial-accounting-and-close/script-de-datos-maestros-crear-objeto-de-alquiler-mds-7ad-522
title: "[DEPRECATED] Script de datos maestros - Crear objeto de alquiler – MDS (7AD) (7AD_S4CLD2608_Master_Data_ES_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (7AD, Spanish): creating usable and rentable generic rental objects, incl. intercompany, with test steps."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/real-estate-contracts-and-leasing]
aliases: [7AD_S4CLD2608_Master_Data_ES_XX]
keywords: [Real Estate Rental Objects and Lease Accounting, generic rental objects, usable objects, rentable objects, intercompany leasing, usage categories, usage types and number ranges, measurements, real estate architectural objects, master data integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_ES_XX.docx]
confidence: high
status: deprecated
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-522
topic: 03-financial-accounting-and-close/real-estate-contracts-and-leasing
language: ES
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de datos maestros - Crear objeto de alquiler – MDS (7AD) (7AD_S4CLD2608_Master_Data_ES_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_ES_XX.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de datos maestrosSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Crear objeto de alquiler – MDS (7AD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233894825)

[2 Requisitos previos 4](#_Toc233894826)

[2.1 Acceso al sistema 4](#_Toc233894827)

[2.2 Roles 4](#_Toc233894828)

[2.3 Unidades organizativas necesarias 4](#_Toc233894829)

[2.4 Datos maestros obligatorios y opcionales 5](#_Toc233894830)

[2.5 Parámetros principales para la creación de datos 5](#_Toc233894831)

[2.5.1 Categoría de uso 5](#_Toc233894832)

[2.5.2 Tipos de utilización y rangos de números 6](#_Toc233894833)

[2.5.3 ID de propiedad 7](#_Toc233894834)

[2.5.4 ID de portafolio 7](#_Toc233894835)

[2.5.5 Mediciones 8](#_Toc233894836)

[2.5.6 Tipo de objeto arquitectónico de bienes inmuebles y rango de números 9](#_Toc233894837)

[2.5.7 Jerarquía de objetos arquitectónicos de bienes inmuebles 9](#_Toc233894838)

[2.6 Pasos preliminares 9](#_Toc233894839)

[2.6.1 Validar disponibilidad de servicio MDI 9](#_Toc233894840)

[3 Tabla de resumen 10](#_Toc233894841)

[4 Procedimiento de test 11](#_Toc233894842)

[4.1 Crear objeto utilizable sin estructura de portafolio 11](#_Toc233894843)

[4.2 Crear objeto utilizable con estructura de portafolio 12](#_Toc233894844)

[4.3 Crear objeto alquilable sin estructura de portafolio 14](#_Toc233894845)

[4.4 Modificar objeto alquilable con estructura de portafolio 15](#_Toc233894846)

[4.5 Crear objeto alquilable multisociedad con estructura de portafolio 16](#_Toc233894847)

[4.6 Crear objeto alquilable multisociedad sin estructura de portafolio 17](#_Toc233894848)

[4.7 Crear objeto utilizable multisociedad con estructura de portafolio 19](#_Toc233894849)

[4.8 Crear objeto utilizable multisociedad sin estructura de portafolio 20](#_Toc233894850)

## Objetivo

ATENCIÓN Se trata de un documento traducido automáticamente que no se ha revisado para comprobar su exactitud. Para enviar comentarios sobre la traducción, puede crear un ticket de cliente en la página del elemento de alcance para su versión de país en SAP Signavio Process Navigator.

Un objeto de alquiler genérico puede ser un objeto utilizable o alquilable.

Un objeto utilizable es un objeto arrendado en una empresa o que es propiedad de esta y define el alcance para uso propio, contrato de alquiler externo o entre empresas. El objeto utilizable puede ser objeto de un contrato de toma en alquiler de bienes inmuebles. La empresa actúa desde la perspectiva del cliente.

Un objeto alquilable es un objeto que puede arrendar una empresa a un arrendatario o empresa afiliada. El objeto alquilable puede ser objeto de un bien inmueble contrato de alquiler. La empresa actúa desde la perspectiva del proveedor.

Los objetos de alquiler genéricos se utilizan en los diferentes escenarios de la siguiente manera:

a) Objetos externos de toma en alquiler o de propiedad

Los objetos externos en alquiler o de propiedad se definen como objetos utilizables. Puede utilizar la utilización categoría Objeto utilizable con estructura de portafolio (UP) o Objeto utilizable sin estructura de portafolio (UW) para ello. Utilizable objetos son necesarios para todos los procesos subsiguientes.

b) Objetos de contrato de alquiler externos

Los objetos de contrato de alquiler externos se definen como objetos alquilables. Puede utilizar el tipo de utilización Objeto alquilable con estructura de portafolio (RP) o Objeto alquilable sin estructura de portafolio (RW) para ello. Cada El objeto alquilable necesita una relación con un objeto utilizable. Por lo tanto, debe haber creado un objeto utilizable primero (consulte a)).

c) Objetos de leasing entre empresas

Para configurar un proceso de leasing multisociedad, se requieren los siguientes objetos:

1. Objeto utilizable (alquiler o propiedad externa) (véase a))
2. Objeto alquilable entre sociedades (categoría de uso) Objeto alquilable multisociedad con Estructura de portafolio (I3) o bien Alquilable entre empresas Objeto sin estructura de portafolio (I4) ) con una relación a un objeto utilizable (véase 1.) dentro de la sociedad del arrendador
3. Objeto utilizable multisociedad (categoría de uso) Objeto utilizable multisociedad con Estructura de portafolio (I1) o bien Utilizable entre empresas Objeto sin estructura de portafolio (I2) ) dentro del arrendatario Sociedad con una relación con un objeto alquilable entre sociedades dentro de la Sociedad arrendadora (véase 2.)

A continuación, puede continuar con 2. y 3. para configurar un proceso de leasing multisociedad adicional para una tercera sociedad o con b) para crear un objeto de contrato de alquiler externo. El objeto alquilable adicional entre sociedades u objeto alquilable externo en este caso tiene un relación con el objeto utilizable entre empresas.

## Requisitos previos

Esta sección resume todos los requisitos previos para realizar la prueba en términos de sistemas, usuarios, datos maestros, datos organizativos, otros datos de test y condiciones empresariales.

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
| Especialista en bienes inmuebles - Gestión de ubicaciones | SAP_BR_RE_SPECIALIST_LOCAT | Gestión de ubicaciones | SAP_FIN_SPT_RE_LOCATION_PC |  |
| Especialista en contratos - Leasing | SAP_BR_RECM_SPECIALIST | Gestión de contratos de leasing / Gestión de contratos de leasing - Alquiler basado en el volumen de negocios | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |

### Unidades organizativas necesarias

La estructura organizativa y los datos maestros de su empresa se crearon en el sistema ERP durante la implementación. La estructura organizativa refleja la estructura de su empresa. Los datos maestros representan objetos utilizables, en función del enfoque operativo de su empresa.

| Objeto de datos | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Sociedad | Datos generales | Obligatorio |  |

### Datos maestros obligatorios y opcionales

Los registros de datos maestros de objetos utilizables y alquilables pueden hacer referencia a otros datos maestros. La siguiente tabla ofrece un resumen de los objetos de datos maestros opcionales y obligatorios que se deben utilizar en un registro de datos utilizable/alquilable.

| Objeto de datos maestros | Utilizado en segmento de datos | Obligatorio/Opcional | Comentarios |
| --- | --- | --- | --- |
| Centro de coste | Objeto de imputación | Obligatorio | Centro de coste o elemento PEP |
| Elemento PEP | Objeto de imputación | Obligatorio | Centro de coste o elemento PEP |

### Parámetros principales para la creación de datos

En esta sección, describimos algunos parámetros básicos que influyen en el comportamiento de un maestro registro y son necesarios para crear un alquiler genérico objeto.

#### Categoría de uso

Las categorías de uso determinan el tipo y el comportamiento empresarial de un objeto de alquiler genérico. Se admiten las siguientes categorías de utilización:

1. Objeto utilizable con estructura de portafolio (UP) – Estos objetos utilizables requieren uso del servicio de integración de datos maestros en BTP (MDI) para establecer Relación con objetos arquitectónicos de bienes inmuebles suministrados por un aplicación.
2. Objeto utilizable sin estructura de portafolio (UW): para estos objetos utilizables se La relación con objetos arquitectónicos de bienes inmuebles no es posible.
3. Objeto alquilable con estructura de portafolio (RP): Estos objetos alquilables requieren el uso del servicio de integración de datos maestros en BTP (MDI) para establecer Relación con objetos arquitectónicos de bienes inmuebles suministrados por un aplicación.
4. Objeto alquilable sin estructura de portafolio (RW): Para estos objetos alquilables La relación con objetos arquitectónicos de bienes inmuebles no es posible.
5. Objeto alquilable entre sociedades con estructura de portafolio (I3): Estos los objetos se utilizan en un escenario de alquiler entre empresas y requieren el uso de el servicio de integración de datos maestros en BTP (MDI) para establecer Relación con objetos arquitectónicos de bienes inmuebles suministrados por un aplicación.
6. Objeto alquilable entre sociedades sin estructura de portafolio (I4): Estos son alquilables Los objetos se utilizan en un escenario de contrato de alquiler multisociedad sin una relación con objetos arquitectónicos de bienes inmuebles.
7. Objeto utilizable entre sociedades con estructura de portafolio (I1) – Estos objetos utilizables se utilizan en un escenario de toma en alquiler entre empresas y requieren una relación con un Objeto alquilable del tipo de uso Objeto alquilable entre sociedades con portafolio Estructura (I3).
8. Objeto utilizable entre sociedades sin estructura de portafolio (I2) – Utilizable los objetos se utilizan en un escenario de toma en alquiler entre empresas y requieren una relación a un objeto alquilable del tipo de uso Objeto alquilable multisociedad sin Estructura de portafolio (I4).

#### Tipos de utilización y rangos de números

Para cada tipo de utilización se pueden definir diferentes tipos de utilización para diferenciar los objetos y su comportamiento empresarial dentro de la categoría. Los tipos de uso determinan el número rangos para los ID de registro maestro de objeto. No puede modificar la asignación o los IDs después. Si un tipo de uso está asignado a un rango de números interno, no puede introducir el ID de registro maestro manualmente. En este caso, deje el campo en blanco como el sistema selecciona automáticamente un número del rango de números numérico asignado.

Los siguientes tipos de utilización y los rangos de números correspondientes están predefinidos:

| Tipo de uso | Categoría de uso | Rango de números | Comentarios |
| --- | --- | --- | --- |
| DP/Hardware (SU01) | Objeto utilizable sin estructura de portafolio (UW) | 010000000 - 019999999 |  |
| Equipamiento (SU02) | Objeto utilizable sin estructura de portafolio (UW) | 020000000 - 029999999 |  |
| Maquinaria (SU03) | Objeto utilizable sin estructura de portafolio (UW) | 030000000 - 039999999 |  |
| Vehículos (SU04) | Objeto utilizable sin estructura de portafolio (UW) | 040000000 - 049999999 |  |
| Equipo de oficina (SU05) | Objeto utilizable sin estructura de portafolio (UW) | 050000000 - 059999999 |  |
| Edificio de oficinas (SU06) | Objeto utilizable con estructura de portafolio (UP) | 060000000 - 069999999 | Solo propósito de demostración |
| Comercio minorista (SU07) | Objeto utilizable con estructura de portafolio (UP) | 070000000 - 079999999 | Solo propósito de demostración |
| Residencial (SU08) | Objeto utilizable con estructura de portafolio (UP) | 080000000 - 089999999 | Solo propósito de demostración |
| Oficina (SR01) | Objeto alquilable con estructura de portafolio (RP) | 1000000000 - 1099999999 | Solo propósito de demostración |
| Tienda (SR02) | Objeto alquilable con estructura de portafolio (RP) | 1100000000 - 1199999999 | Solo propósito de demostración |
| Apartamento (SR03) | Objeto alquilable con estructura de portafolio (RP) | 1200000000 - 1299999999 | Solo propósito de demostración |
| Vehículos (SR04) | Objeto alquilable sin estructura de portafolio (RW) | 1300000000 - 1399999999 | Solo propósito de demostración |
| LO Oficina ICO (SRI1) | Multisociedad Objeto alquilable con estructura de portafolio (I3) | 3100000000 - 3199999999 | Demostración sólo finalidad |
| PI Oficina ICO (SUI1) | Multisociedad Objeto utilizable con estructura de portafolio (I1) | 3000000000 - 3099999999 | Demostración sólo finalidad |
| LO Equipo de oficina ICO (SRI2) | Multisociedad Objeto alquilable sin estructura de portafolio (I4) | 6100000000 - 6199999999 | Demostración sólo finalidad |
| PI Equipo de oficina ICO (SUI2) | Multisociedad Objeto utilizable sin estructura de portafolio (I2) | 6000000000 - 6099999999 | Demostración sólo finalidad |

Para configurar rangos de números y tipos de utilización utilice las siguientes SSCUI:

- Definir rangos de números para objetos de alquiler genéricos (ID: 106591)
- Definir tipos de uso para objetos de alquiler genéricos (ID: 106592)

#### ID de propiedad

Los objetos utilizables pueden estar sujetos a un control legal diferente. El tipo de control legal debe ser actualizado mediante el atributo ID de propiedad. Los valores de característica de la propiedad El ID se puede definir en la configuración.

Los siguientes ID de propiedad están predefinidos:

- Toma en alquiler (S001)
- Propiedad (S002)

Para configurar los ID de propiedad, utilice la SSCUI: Definir IDs de propiedad para objetos utilizables (ID: 106593).

#### ID de portafolio

Los objetos utilizables del tipo de utilización "Objeto utilizable sin estructura de portafolio (UW)" se pueden agrupado por un ID de portafolio. Los valores de característica del ID de portafolio se pueden definir en la configuración.

Los siguientes ID de portafolio para la subagrupación de equipos de oficina y vehículos están predefinidos con fines de demostración:

- Automóvil diésel (S401)
- Coche de gasolina (S402)
- Coche eléctrico (S403)
- Electrodomésticos de oficina (S501)
- Muebles de oficina (S502)
- Soluciones de montaje (S503)

Para configurar los ID de portafolio, utilice la SSCUI: Definir ID de portafolio para objetos utilizables (ID: 106594).

#### Mediciones

Los objetos utilizables y/o alquilables pueden tener mediciones. Basándose en estas mediciones, Los importes de condición se pueden calcular en contratos. Las mediciones de diferentes tipos pueden ser totalizado hasta una medición total.

Los siguientes tipos de medición están predefinidos para fines de demostración:

| Tipo de medición | Unidad por defecto | Medición de área | Medición total | Comentarios |
| --- | --- | --- | --- | --- |
| Área de oficina (SG11) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Zona de reunión (SG13) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Despensa (SF04) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Baño (SD01) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Sala técnica (SC04) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Ascensor (SA02) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Corredor (SE01) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Tienda (SG22) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Espacio habitable (SG41) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Lobby Foyer (SE02) | Metro cuadrado (M2) | X |  | Totalizado a área utilizable (ST99) |
| Plaza de aparcamiento (SK01) | Metro cuadrado (M2) | X |  |  |
| Área utilizable (ST99) | Metro cuadrado (M2) | X | X |  |

Para configurar los tipos de medición y las mediciones totales, utilice las siguientes SSCUI:

- Definir tipos de medición (ID: 105394)
- • Definir mediciones totales (ID: 105395)

#### Tipo de objeto arquitectónico de bienes inmuebles y rango de números

Objetos de alquiler genéricos del tipo de uso "Objeto utilizable con estructura de portafolio (UP)" o "Objeto alquilable con estructura de portafolio (RP)" hace referencia a Arquitectura de bienes inmuebles Objetos proporcionados por una aplicación externa mediante el servicio de integración de datos maestros en BTP (MDI). Para la sincronización, los tipos de objeto arquitectónico de bienes inmuebles deben ser configurado. El tipo de objeto arquitectónico de bienes inmuebles determina el objeto arquitectónico categoría y rango de números utilizado en el sistema.

Los siguientes tipos de objeto arquitectónico de bienes inmuebles y los rangos de números correspondientes son predefinido para fines de demostración:

| Objeto arquitectónico Tipos | Arquitectura Objetos Categoría | Número Rangos | Comentarios |
| --- | --- | --- | --- |
| Sitio (S1SI) | Sitio (1) | 10000000 - 19999999 |  |
| Edificio (S2BU) | Edificio (2) | 20000000 - 29999999 |  |
| Terreno (S2LA) | Terreno (3) | 30000000 - 39999999 |  |
| Planta (S3FL) | Otros (99) | 40000000 - 49999999 |  |
| Sala (S4RO) | Otros (99) | 50000000 - 59999999 |  |

Para configurar rangos de números y tipos de objeto arquitectónico de bienes inmuebles, utilice lo siguiente SSCUIs:

- Definir rango de números para objeto arquitectónico (ID: 106628)
- Definir tipo de objeto arquitectónico (ID: 106629)

#### Jerarquía de objetos arquitectónicos de bienes inmuebles

En función de los tipos de objeto de arquitectura, se puede definir una jerarquía. Se utiliza esta jerarquía en los informes.

Para configurar una jerarquía de tipos de objeto arquitectónico, utilice SSCUI: Definir Tipos de objeto arquitectónico superiores permitidos (ID: 106630).

### Pasos preliminares

#### Validar disponibilidad de servicio MDI

Si desea crear objetos utilizables/alquilables con estructura de portafolio (tipo de uso UP y RP o I1 y I3), una conexión a una aplicación externa que proporciona objetos arquitectónicos de bienes inmuebles a través del servicio de integración de datos maestros en BTP (MDI).

Para obtener instrucciones de configuración y requisitos previos, consulte el elemento de alcance 77V - Integración de datos maestros para la gestión de contratos y de leasing .

## Tabla de resumen

Este elemento de alcance consta de varios procesos proporcionados en las siguientes tablas.

|  |
| --- |
| Nota Si el administrador del sistema ha activado espacios y páginas en la rampa de lanzamiento SAP Fiori, la página de inicio solo contendrá las aplicaciones esenciales para realizar las tareas típicas de un rol empresarial.Puede encontrar todas las demás aplicaciones (de búsqueda) no incluidas en la página de inicio utilizando la barra de búsqueda ([2434549](https://me.sap.com/notes/2434549)).Si desea personalizar la página de inicio e incluir las aplicaciones ocultas, vaya a su perfil de usuario y seleccione Buscador de aplicaciones . |

| Diagrama de proceso | Roles empresariales | Transacción/Aplicación | Resultados previstos |
| --- | --- | --- | --- |
| [Crear objeto utilizable sin estructura de portafolio](#unique_17) [página ] 11 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objetos utilizables |  |
| [Crear objeto utilizable con estructura de portafolio](#unique_18) [página ] 12 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objetos utilizables |  |
| [Crear objeto alquilable sin estructura de portafolio](#unique_19) [página ] 14 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objeto alquilable |  |
| [Modificar objeto alquilable con estructura de portafolio](#unique_20) [página ] 15 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objeto alquilable |  |
| [Crear objeto alquilable multisociedad con estructura de portafolio](#unique_21) [página ] 16 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objeto alquilable |  |
| [Crear objeto alquilable multisociedad sin estructura de portafolio](#unique_22) [página ] 17 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar objeto alquilable |  |
| [Crear objeto utilizable multisociedad con estructura de portafolio](#unique_23) [página ] 19 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar utilizable Objetos |  |
| [Crear objeto utilizable multisociedad sin estructura de portafolio](#unique_24) [página ] 20 | Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones | Gestionar utilizable Objetos |  |

## Procedimiento de test

### Crear objeto utilizable sin estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objetos utilizables | Abierto Gestionar objetos utilizables . | El Gestionar objetos utilizables Aparece la pantalla. |  |
| 3 | Crear objetos utilizables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto utilizable : <Su nombre de objeto>Categoría de uso : Objeto utilizable sin portafolio Estructura (UW)Tipo de utilización de objeto utilizable : <Seleccione un tipo de uso, por ejemplo, Vehículos (SU04)>Sociedad : <Seleccione una empresa código, por ejemplo, Sociedad (1010) >Objeto utilizable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:ID de portafolio (opcional) : <Seleccione un ID de portafolio, por ejemplo, Diesel Car (S401)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>ID de propiedad : <Seleccione un/a ID de propiedad, por ejemplo, toma en alquiler (S001)>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido, por ejemplo, actual fecha>Fecha de fin de validez : <Fecha hasta qué objeto es válido>En la Objeto de imputación principal sección, seleccione Crear y hacer lo siguiente entradas.Tipo de objeto del objeto asignado : <Seleccione un tipo de objeto, por ejemplo, Centro de coste (KS)>Objeto de imputación : <Su imputación objeto>Nota Se debe asignar un objeto de imputación principal para el validez total del objeto. El objeto de imputación puede modificarse durante la validez del objeto. Sin embargo, no hay solapamientos ni discontinuidades puede ocurrir. Objetos utilizables que pertenecen al mismo ID de portafolio puede utilizar la misma imputación principal o diferente objetos. Un objeto de imputación principal utilizado para un ID de portafolio no se puede utilizar como imputación principal objeto en otro ID de portafolio.Seleccionar Aplicar .Opcional:Para el Medición seleccione Crear y hacer lo siguiente entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se crea el objeto utilizable. |  |

### Crear objeto utilizable con estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objetos utilizables | Abierto Gestionar objetos utilizables . | El Gestionar objetos utilizables Aparece la pantalla. |  |
| 3 | Crear objetos utilizables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto utilizable : <Su nombre de objeto>Categoría de uso : Objeto utilizable con portafolio Estructura (UP)Tipo de utilización de objeto utilizable : <Seleccione un tipo de uso, por ejemplo, Edificio de oficinas (SU06)>Sociedad : <Seleccione una sociedad, para ejemplo, Sociedad (1010) >Objeto utilizable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:Número de objeto de edificio/terreno : <Seleccione el objeto de arquitectura (edificio/terreno) para al que hace referencia el objeto utilizable (superior objeto)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>ID de propiedad : <Seleccione un/a ID de propiedad, por ejemplo, toma en alquiler (S001)>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido, por ejemplo, actual fecha>Fecha de fin de validez : <Fecha hasta qué objeto es válido>En la Objeto de imputación principal sección, seleccione Crear y hacer lo siguiente entradas.Tipo de objeto del objeto asignado : <Seleccione un tipo de objeto, por ejemplo, Centro de coste (KS)>Objeto de imputación : <Su imputación objeto>Nota Se debe asignar un objeto de imputación principal para el validez total del objeto. El objeto de imputación puede modificarse durante la validez del objeto. Sin embargo, no hay solapamientos ni discontinuidades puede ocurrir. Objetos utilizables que pertenecen al mismo edificio o El terreno puede utilizar la misma imputación principal o diferente objetos. Un objeto de imputación principal utilizado para un edificio o terreno no se puede utilizar como objeto de imputación principal en otro edificio o terreno.Seleccionar Aplicar .En la Utilización de objeto arquitectónico sección, seleccionar Crear y hacer lo siguiente entradas.Nota Los objetos utilizables requieren el uso de la integración de datos maestros servicio en BTP (MDI) para establecer la relación con real Objetos arquitectónicos de bienes inmuebles proporcionados por un aplicación.Tipo de objeto arquitectónico : <Seleccione el tipo de objeto de arquitectura, por ejemplo, Edificio (S2BU)>Número de objeto arquitectónico : <Seleccione el objeto de arquitectura, es decir, representado por el objeto utilizable>Nota Puede agrupar varios objetos arquitectónicos de bienes inmuebles a un objeto utilizable.Opcional:En la Estado del sistema seleccione Bloqueo para configuración multisociedad Si quieres para evitar que los objetos alquilables (RP) se sincronicen desde un tercer La solución de gestión de bienes inmuebles de parte se asignará automáticamente a objetos utilizables siempre que su configuración multisociedad no sea finalizado.Su objeto utilizable tiene el estado Alquiler multisociedad Sólo que impide un alquiler externo.Seleccionar Desbloquear para configuración multisociedad después de usted ha finalizado la configuración multisociedad.Para el Medición seleccione Crear y hacer lo siguiente entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se crea el objeto utilizable. |  |

### Crear objeto alquilable sin estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objeto alquilable | Abierto Gestionar objeto alquilable . | El Gestionar objetos alquilables pantalla aparece. |  |
| 3 | Crear objetos alquilables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Alquilable Nombre de objeto : <Su objeto nombre>Categoría de uso : Objeto alquilable sin portafolio Estructura (RW)Tipo de uso de objeto alquilable : <Seleccione un tipo de uso, por ejemplo, Vehículos (SR04)>Sociedad : <Seleccione una sociedad, para ejemplo, Sociedad (1010) >Objeto alquilable : <Su objeto ID en caso de rango de números externo; de lo contrario, deje el campo vacío>En la Información general sección:Categoría de objeto alquilable : <Seleccione una categoría de objeto alquilable, por ejemplo, Externo (E)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido, por ejemplo, actual fecha>Fecha de fin de validez : <Fecha hasta qué objeto es válido>En la Asignación de objeto utilizable sección, seleccionar Crear y hacer lo siguiente entradas.Objeto utilizable : <Asigne el objeto utilizable para el que el objeto alquilable hace referencia>Seleccionar Aplicar .Opcional:Para el Medición seleccione Crear y hacer lo siguiente entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se ha creado el objeto alquilable. |  |

### Modificar objeto alquilable con estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objeto alquilable | Abierto Gestionar objeto alquilable . | El Gestionar objetos alquilables pantalla aparece. |  |
| 3 | Modif. Objetos alquilables | Busque el objeto alquilable con el ID de objeto.Seleccionar el Objeto alquilable. Seleccione Editar y realice las siguientes entradas.En la Información general sección:Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>En la Asignación de objeto utilizable sección, el Se puede crear o actualizar la siguiente entrada:Objeto utilizable : <Asigne el objeto utilizable para el que el objeto alquilable hace referencia>Nota Tenga en cuenta que aquí solo puede haber una asignación.Seleccionar Aplicar .Opcional:En el Medición sección, el Se puede crear o actualizar la siguiente entrada:Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccione Grabar . | El objeto alquilable es modificado. |  |

### Crear objeto alquilable multisociedad con estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objeto alquilable | Abierto Gestionar objeto alquilable . | El Gestionar objetos alquilables pantalla aparece. |  |
| 3 | Crear objetos alquilables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto alquilable : <Su nombre de objeto>Categoría de uso : Multisociedad Objeto alquilable con estructura de portafolio (I3)Tipo de uso de objeto alquilable : <Seleccione un tipo de uso, por ejemplo, LO Office ICO (SRI1)>Sociedad : <Seleccione una empresa código, por ejemplo, Sociedad (1010)>Objeto alquilable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:Número de objeto de edificio/terreno obligatorio:Número de objeto de edificio/terreno : <Seleccione el objeto de arquitectura (edificio/terreno) para a la que hace referencia el objeto alquilable entre sociedades (superior objeto)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido, por ejemplo, actual fecha>Fecha de fin de validez : <Fecha hasta qué objeto es válido>En la Asignación de objeto utilizable sección, haga lo siguiente entradas.Objeto utilizable : <Asigne el objeto utilizable puede ser un objeto utilizable entre empresas (I1) o un objeto no utilizable Objeto utilizable multisociedad (UP) para el que el objeto utilizable multisociedad objeto alquilable se refiere>Seleccionar Aplicar .Para el Utilización de objeto arquitectónico sección, seleccionar Crear y hacer lo siguiente entradas.Tipo de objeto arquitectónico : <Seleccione el tipo de objeto de arquitectura, por ejemplo, Sala (S4RO)>Número de objeto arquitectónico : <Seleccione el objeto de arquitectura, es decir, representado por el objeto utilizable>Utilización basada en medición : <Como por defecto, Sí>Seleccionar Ir a pantalla completa en la parte superior derecha. En Medición de uso de arquitectura , seleccione Crear y hacer lo siguiente entradas:Tipo de medición : <Su Tipo de medida> , por ejemplo, Oficina Área (SG11)Cantidad : <Su importe>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido>Fecha de fin de validez : <Fecha hasta qué objeto es válido>Seleccionar Aplicar .Seleccionar Crear . | Se ha creado el objeto alquilable. |  |

### Crear objeto alquilable multisociedad sin estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objeto alquilable | Abierto Gestionar objeto alquilable . | El Gestionar objetos alquilables pantalla aparece. |  |
| 3 | Crear objetos alquilables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto alquilable : <Su nombre de objeto>Categoría de uso : Multisociedad Objeto alquilable sin estructura de portafolio (I4)Tipo de uso de objeto alquilable : <Seleccione un tipo de uso, por ejemplo, LO Equip.oficina ICO (SRI2)>Sociedad : <Seleccione una empresa código, por ejemplo, Sociedad (1010)>Objeto alquilable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>Fecha de inicio de validez : <Fecha de inicio qué objeto es válido, por ejemplo, actual fecha>Fecha de fin de validez : <Fecha hasta qué objeto es válido>En la Asignación de objeto utilizable sección, seleccionar Crear y hacer lo siguiente entradas.Objeto utilizable : <Asigne el utilizable el objeto puede ser un objeto utilizable entre empresas (I2) o un objeto no Objeto utilizable multisociedad (UW) al que multisociedad objeto alquilable se refiere>Seleccionar Aplicar .Opcional:Para el Medición seleccione Crear y hacer lo siguiente entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se ha creado el objeto alquilable. |  |

### Crear objeto utilizable multisociedad con estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objetos utilizables | Abierto Gestionar utilizable Objetos . | El Gestionar objetos utilizables Aparece la pantalla. |  |
| 3 | Crear objetos utilizables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto utilizable : <Su objeto nombre>Categoría de uso : Utilizable entre empresas Objeto con estructura de portafolio (I1)Tipo de utilización de objeto utilizable : <Seleccione un tipo de uso, por ejemplo, LI Office ICO (SUI1)>Sociedad : <Seleccione una empresa código, por ejemplo, Sociedad (1020)>Objeto utilizable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:Número de objeto de edificio/terreno : <Seleccione el objeto de arquitectura (edificio/terreno) para al que hace referencia el objeto utilizable multisociedad (superior objeto)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>Nota La fecha de inicio de validez y la fecha de fin de validez se determinado a partir del objeto alquilable entre sociedades asignado.En la Objeto de imputación principal sección, seleccione Crear y hacer lo siguiente entradas.Tipo de objeto del objeto asignado : <Seleccione un tipo de objeto, por ejemplo, Centro de coste (KS)>Objeto de imputación : <Su Objeto de imputación>Nota Se debe asignar un objeto de imputación principal para el validez total del objeto. El objeto de imputación puede modificarse durante la validez del objeto. Sin embargo, no hay solapamientos ni discontinuidades puede ocurrir. Objetos utilizables que pertenecen al mismo edificio o El terreno puede utilizar la misma imputación principal o diferente objetos. Un objeto de imputación principal utilizado para un edificio o terreno no se puede utilizar como objeto de imputación principal en otro edificio o terreno.Seleccionar Aplicar .En la Asignación de objeto alquilable multisociedad sección, seleccione Crear y hacer lo siguiente entradas.Objeto alquilable multisociedad : <Asigne el objeto alquilable entre sociedades al que el objeto utilizable multisociedad hace referencia>Seleccionar Aplicar .Nota El alcance del arrendamiento entre empresas se limita al arrendamiento alcance por la empresa asociada. Un objeto alquilable entre sociedades de la sociedad del arrendador debe estar asignada.Opcional:En la Estado del sistema seleccione Bloqueo para configuración multisociedad Si quieres para evitar que los objetos alquilables (RP) se sincronicen desde un tercer La solución de gestión de bienes inmuebles de parte se asignará automáticamente a objetos utilizables siempre que su configuración multisociedad no sea finalizado.Su objeto utilizable multisociedad tiene el estado Solo alquiler válido para todas las empresas lo que impide un alquiler externo.Seleccionar Desbloquear para configuración multisociedad después de usted ha finalizado la configuración multisociedad.Para el Medición sección, seleccione Crear y realice las siguientes entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se crea el objeto utilizable. |  |

### Crear objeto utilizable multisociedad sin estructura de portafolio

| Paso de test # | Nombre de paso de test | Instrucción | Resultado previsto | Comentarios |
| --- | --- | --- | --- | --- |
| 1 | Iniciar sesión | Inicie sesión en la rampa de lanzamiento SAP Fiori como Especialista en contratos - Leasing o bien Especialista en bienes inmuebles - Gestión de ubicaciones . | El Iniciar Aparece la página. |  |
| 2 | Abrir Gestionar objetos utilizables | Abierto Gestionar utilizable Objetos . | El Gestionar objetos utilizables Aparece la pantalla. |  |
| 3 | Crear objetos utilizables | Seleccionar Crear y hacer lo siguiente entradas.En la Cabecera sección:Nombre de objeto utilizable : <Su objeto nombre>Categoría de uso : Utilizable entre empresas Objeto sin estructura de portafolio (I2)Tipo de utilización de objeto utilizable : <Seleccione un tipo de uso, por ejemplo, LI Office Equipo ICO (SUI2)>Sociedad : <Seleccione una empresa código, por ejemplo, Sociedad (1020)>Objeto utilizable : <Su ID de objeto en caso de rango de números externo, de lo contrario deje el campo vacío>En la Información general sección:ID de portafolio (opcional) : <Seleccionar un ID de portafolio, por ejemplo, Electrodomésticos de oficina (S501)>Grupo de autorizaciones (opcional) : <Seleccione un grupo de autorización (este campo solo es visible si un grupo de autorización es configurado)>Nota La fecha de inicio de validez y la fecha de fin de validez se determinado a partir del objeto alquilable entre sociedades asignado.En la Objeto de imputación principal sección, seleccione Crear y hacer lo siguiente entradas.Tipo de objeto del objeto asignado : <Seleccione un tipo de objeto, por ejemplo, Centro de coste (KS)>Objeto de imputación : <Su Objeto de imputación>Nota Se debe asignar un objeto de imputación principal para el validez total del objeto. El objeto de imputación puede modificarse durante la validez del objeto. Sin embargo, no hay solapamientos ni discontinuidades puede ocurrir. Objetos utilizables que pertenecen al mismo edificio o El terreno puede utilizar la misma imputación principal o diferente objetos. Un objeto de imputación principal utilizado para un edificio o terreno no se puede utilizar como objeto de imputación principal en otro edificio o terreno.Seleccionar Aplicar .En la Asignación de objeto alquilable multisociedad sección, seleccione Crear y hacer lo siguiente entradas.Objeto alquilable multisociedad : <Asigne el objeto alquilable entre sociedades al que el objeto utilizable multisociedad hace referencia>Nota El alcance del arrendamiento entre empresas se limita al arrendamiento alcance por la empresa asociada. Un objeto alquilable entre sociedades de la sociedad del arrendador debe estar asignada.Seleccionar Aplicar .Opcional:Para el Medición sección, seleccione Crear y realice las siguientes entradas.Tipo de medición : <Seleccione un Tipo de medida>Cantidad : <Importe del medición>Seleccionar Aplicar .Seleccionar Crear . | Se crea el objeto utilizable. |  |

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
- related-to :: [[03-financial-accounting-and-close/create-rental-object-master-data-script-7ad-521]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-7ad-525]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_ES_XX.docx` — full document · extracted with `mammoth` · 44,881 chars in the whole document
