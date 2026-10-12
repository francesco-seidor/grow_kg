---
id: 14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488
title: Criar produto de serviço para projeto – MDS (5TO) (5TO_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud master data script (5TO): create service product PROJETO with sales data via Create Material (MM01)."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_PT_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service product, product master data, material creation, sales organization data, business roles, profit center assignment, brazil tax fields, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-488
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar produto de serviço para projeto – MDS (5TO) (5TO_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar produto de serviço para projeto – MDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893830)

[2 Pré-requisitos 3](#_Toc233893831)

[2.1 Acesso ao sistema 3](#_Toc233893832)

[2.2 Funções 3](#_Toc233893833)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893834)

[2.4 Dados mestre obrigatórios e operacionais 4](#_Toc233893835)

[3 Tabela de síntese 5](#_Toc233893836)

[4 Procedimentos de teste 6](#_Toc233893837)

[4.1 Criar produto de serviços - PROJETO 6](#_Toc233893838)

## Objetivo

Neste documento, você pode encontrar uma descrição sobre como criar registros de dados mestre de produto dos serviços, incluindo preços. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na interface do usuário.

Um registro mestre do produto de serviço criado da forma aqui descrita pode ser utilizado para a ordem de solução.

| ID do produto de serviços | Descrição | Utilização |
| --- | --- | --- |
| PROJETO | Projeto | representa o projeto |

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - Produto | SAP_CMD_SP_PR_MAINT |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser utilizada para os EUA | Unidade organizacional a ser utilizada para DE |
| --- | --- | --- | --- |
| Criar material | Organização de vendas | 1710 ( Org.vendas nac.EUA) | 1010 ( Org.vendas nacional DE) |
| Criar material | Canal de distribuição | 10 (vendas diretas) | 10 (vendas diretas) |

### Dados mestre obrigatórios e operacionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.

Você pode encontrar todos os outros apps não incluídos na página inicial usando a barra de pesquisa.

Para personalizar a página inicial e incluir os apps ocultos, navegue até seu perfil do usuário e clique em Configurações > App Finder.

| ID (modelo de função) | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar produto dos serviços | SAP_BR_PRODMASTER_SPECIALIST | Criar material(MM01) | Os produtos dos serviços são criados. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar produto de serviços - PROJETO

Objetivo

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). |  |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para produto de serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:Material:PROJETOTipo de material:produto de serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Selecionar Visões | Na visão Selecionar visões Dados básicos 1, clique em Continuar (Enter). | A visão Criar material PROJETO é exibida. |  |
| 5 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:item do projetoUnidade de medida básica:AU (UNIDADE DE ATIVIDADE)Grupo de materiais:P001 (serviços)GrpItensGer.:SPRJ (projeto)Em seguida, clique em Salvar. | Os dados básicos são atualizados e o produto dos serviços é salvo.Após a gravação, a visão Criar material (primeira tela) é exibida.Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 6 | Ampliar detalhes do produto | Na visão Criar material (primeira tela), insira o material PROJETO e, em seguida, selecione Continuar (ENTER). | É exibida a caixa de diálogo Selecionar visões. |  |
| 7 | Selecionar Visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Em seguida, clique em Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 8 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material PROJETO é exibida. |  |
| 9 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto:X <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 10 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SPRJ (projeto)Em seguida, pressione Enter.Em seguida, clique em Salvar. | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-489]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,606 chars in the whole document
