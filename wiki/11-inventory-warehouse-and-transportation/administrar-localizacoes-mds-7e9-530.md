---
id: 11-inventory-warehouse-and-transportation/administrar-localizacoes-mds-7e9-530
title: Administrar localizações - MDS (7E9) (7E9_S4CLD2608_Master_Data_PT_XX)
description: SAP S/4HANA Cloud 2608 master data script (PT) for creating locations (location master) via Manage Locations (F6225) as transportation master data specialist.
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-locations]
aliases: [7E9_S4CLD2608_Master_Data_PT_XX]
keywords: [Transportation Locations, locations, master data script, location types, un/locode, airport codes, transportation management, 7E9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-530
topic: 11-inventory-warehouse-and-transportation/transportation-locations
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Administrar localizações - MDS (7E9) (7E9_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Transportation Locations** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Administrar localizações - MDS (7E9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893941)

[2 Pré-requisitos 3](#_Toc233893942)

[2.1 Acesso ao sistema 3](#_Toc233893943)

[2.2 Funções 3](#_Toc233893944)

[2.3 Parâmetros principais para a criação de dados 3](#_Toc233893945)

[2.3.1 Tipos de localização 3](#_Toc233893946)

[2.3.2 Definir UN/LOCODE 4](#_Toc233893947)

[2.3.3 Definir códigos de aeroporto 4](#_Toc233893948)

[3 Tabela de síntese 5](#_Toc233893949)

[4 Procedimentos de teste 6](#_Toc233893950)

[4.1 Administrar localizações 6](#_Toc233893951)

## Objetivo

Neste documento você encontra uma descrição sobre como criar um registro de dados mestre da unidade gerencial para o seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". Você aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do SAP S/4HANA Cloud Public Edition, por SAP Best Practices, não são descritos neste documento, apesar de eles poderem aparecer na tela.

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em dados mestre - gestão de transportes | SAP_BR_TRANSP_MDSPEC | Dados mestre de transporte | SAP_BR_TRANSP_MDSPEC |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro <tipo> de dados mestre.

#### Tipos de localização

Estão disponíveis as seguintes opções para atribuir os tipos de localização:

| Nome | ID |
| --- | --- |
| Porta | 1100 |
| Aeroporto | 1110 |
| Estação ferroviária | 1120 |
| Junção ferroviária | 1190 |
| Ponto de carregamento | 1200 |

#### Definir UN/LOCODE

Você pode definir códigos das Nações Unidas para Locais de comércio e transporte (UN/LOCODES).

No ambiente de configuração, use a função de pesquisa para procurar cada atividade. Para mais informações, consulte [Ambiente de configuração de SAP S/4HANA Cloud Public Edition.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html)

#### Definir códigos de aeroporto

Você pode definir códigos de aeroporto.

No ambiente de configuração, use a função de pesquisa para procurar cada atividade. Para mais informações, consulte [Ambiente de configuração de SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/61e246f4b34c4e1790d8b7651c0b40a8/0b3f87579f345c08e10000000a441470.html?state=DRAFT).

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar localizações](#unique_10) [página ] 6 | Especialista em dados mestre - gestão de transportes | Administrar localizações(F6225) |  |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Administrar localizações

Objetivo

As etapas a seguir explicam como fazer isso.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre - gestão de transportes. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Administrar localizações(F6225). | A tela Administrar mestre de unidades gerenciais(F6225) é exibida. |  |
| 3 | Clicar em Criar | Clique em Criar. | A caixa de diálogo Criar é exibida. |  |
| 4 | Inserir detalhes | Na caixa de diálogo Criar, efetue as seguintes entradas:Localização:<sua localização>Tipo de localização:<seu tipo de localização> |  |  |
| 5 | Clique em Continuar | Clique em Continuar. | A tela Localização é exibida. |  |
| 6 | Inserir informações gerais | Na guia Informações gerais, efetue a seguinte entrada:depósito Da UG:<sua descrição da localização> |  |  |
| 7 | Inserir dados de endereço | Na guia Endereço, efetue as seguintes entradas:Rua:<rua>Código postal: <código postal>País/Região: <país/região>Número da casa: <número da casa>Cidade: <cidade>Região: <região>Fuso horário: <fuso horário>Critério de pesquisa 1: <critério de pesquisa> |  |  |
| 8 | Inserir dados de identificação | Na guia Identificação, efetue a seguinte entrada:UN/LOCODE: <UN/LOCODE>Código de aeroporto: <código de aeroporto> |  |  |
| 9 | Escolher Calcular coordenadas geográficas | Escolha Calcular coordenadas geográficas. | As coordenadas geográficas foram determinadas automaticamente e preenchidas na guia Coordenadas geográficas. |  |
| 10 | Clicar em Criar | Clique em Criar. | A seguinte mensagem do sistema é exibida:Localização <sua localização> criada com êxito |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/gestion-de-ubicaciones-mds-7e9-528]]
- related-to :: [[11-inventory-warehouse-and-transportation/manage-locations-mds-7e9-527]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-529]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-531]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 8,764 chars in the whole document
