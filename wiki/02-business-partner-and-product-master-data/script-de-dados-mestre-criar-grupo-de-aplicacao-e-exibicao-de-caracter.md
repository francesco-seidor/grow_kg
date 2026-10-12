---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-grupo-de-aplicacao-e-exibicao-de-caracter
title: Script de dados mestre - Criar grupo de aplicação e exibição de característica – MDS (2NI) (2NI_S4CLD2608_Master_Data_PT_XX)
description: Portuguese master data script (2NI) for creating an application group and characteristic display with characteristic assignment via CU_CHAR_DISPLAY in S/4HANA Cloud Public Edition 2608.
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_PT_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic display, application group, characteristic assignment, master data scripts, variant configuration, business roles, transaction types, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-272
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar grupo de aplicação e exibição de característica – MDS (2NI) (2NI_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar grupo de aplicação e exibição de característica – MDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893562)

[2 Pré-requisitos 3](#_Toc233893563)

[2.1 Acesso ao sistema 3](#_Toc233893564)

[2.2 Funções 3](#_Toc233893565)

[2.3 Dados mestre obrigatórios e operacionais 3](#_Toc233893566)

[2.4 Parâmetros principais para a criação de dados 4](#_Toc233893567)

[2.4.1 Transação 4](#_Toc233893568)

[3 Tabela de síntese 5](#_Toc233893569)

[4 Procedimentos de teste 6](#_Toc233893570)

[4.1 Criar grupo de aplicações 6](#_Toc233893571)

[4.2 Criar exibição de característica 7](#_Toc233893572)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar um registro de exibição de característica do seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui dados relevantes para o SAP S/4HANA Cloud Public Edition Appliance, como Grupo de aplicações, Exibição de características e Atribuição de características. Os campos não relevantes para o escopo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Modelador de configuração de produto | SAP_BR_PRODUCT_CONFIG_MODELER | Configuração de variantes | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Dados mestre obrigatórios e operacionais

Os registros da exibição de característica podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Características |  | Obrigatório | As características devem ser atribuídas ao registro de exibição de característica. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma exibição de característica.

#### Transação

A transação permite que o sistema determine em qual transação deve estar disponível a exibição de característica.

Para a edição 1711, só é permitido o documento de vendas e distribuição.

| Transação | Comentário |
| --- | --- |
| Documento de vendas e distribuição | Para a versão 1711, só é permitido o documento de vendas e distribuição para a exibição de característica. |
| Ordem de produção |  |
| Contrato comercial |  |
| Pedido |  |
| Entrada de mercadorias |  |
| Confirmação da ordem |  |

## Tabela de síntese

Nesta seção, é fornecida uma lista de etapas que um usuário segue ao criar um registro de dados mestre. Qualquer segmento lógico e relevante de um objeto de dados mestre deve levar a uma etapa separada (por exemplo: segmentos de dados dependentes da unidade organizacional, etc.).

O item de escopo Criar grupo de aplicação e exibição de característica – MDS é composto por várias etapas de processo fornecidas nas tabelas seguintes:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo, Relatório ou Item | Função empresarial | Transação/App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar grupo de aplicações](#unique_9) [página ] 6 | Modelador de configuração de produto | Atualizar exibição de característica para configuração(CU_CHAR_DISPLAY) | O grupo de aplicações é criado |
| [Criar exibição de característica](#unique_10) [página ] 7 | Modelador de configuração de produto | Atualizar exibição de característica para configuração(CU_CHAR_DISPLAY) | O grupo de aplicações é criado |

## Procedimentos de teste

Esta seção descreve os procedimentos para cada etapa do processo que pertence a este item de escopo. Você pode também pode usar estes procedimentos para testar a criação de dados mestre.

### Criar grupo de aplicações

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/ Reprovado /Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no SAP Fiori Launchpad como Modelador de configuração de produto . | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar exibição de característica para configuração(CU_CHAR_DISPLAY). | A visão Modificar visão “Grupo de aplicações": síntese é exibida. |  |
| 3 | Inserir grupo de aplicações | Na tela Modificar visão “Grupo de aplicações": síntese, selecione Nova entrada. E efetue as seguintes entradas:Trans. : <selecione da lista de opções>Grupo de aplicações: <qualquer código | A visão Novas entradas: síntese de entradas adicionadas é exibida. |  |
| 4 | Gravar os dados | Selecione Gravar. |  |  |

### Criar exibição de característica

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/ Reprovado /Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no launchpad do SAP Fiori como Modelador de configuração de produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | SelecioneAtualizar exibição de característica para configuração(CU_CHAR_DISPLAY). | A visão Modificar visão “Grupo de aplicações": síntese é exibida. |  |
| 3 | Inserir grupo de aplicações | Na tela Modificar visão “Grupo de aplicações": síntese, selecione Exibição de característica.Selecione Nova entrada. Efetue as seguintes entradas e pressione ENTER:Exib. características: <qualquer código.Descrição: <insira uma descrição para a exibição de característica>.Grp. apl.: <selecione Entradas possíveis para obter ajuda>. | A tela Modificar visão ''Exibição de característica'': síntese é exibida. |  |
| 4 | Atribuir característica | Selecione a exibição de característica criada na etapa anterior e marque Atribuição de características.Efetue as entradas seguintes:Seq.: <Insira o número sequencial para determinar a sequência de características>.Nome da característica: <procure uma característica selecionando a ajuda de pesquisa F4>.Col.: <Insira a largura de coluna apropriada para mostrar a denominação da característica e o valor>. | A tela Modificar visão ''Atribuição de característica'': síntese é exibida. |  |
| 5 | Gravar os dados | Selecione Gravar. |  |  |

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
> Flagged while digesting this document, not verified: Overview table gives the same expected result ('application group is created') for both create application group and create characteristic display; the 1711-only restriction may be outdated in a 2608 document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-271]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 11,420 chars in the whole document
