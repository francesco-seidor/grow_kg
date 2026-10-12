---
id: 10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560
title: Script de dados mestre - Criar programa de remessas – MDS (BF6) (BF6_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (BF6) for SAP S/4HANA Cloud Public Edition: creating scheduling agreements (programas de remessas) for standard, consignment and subcontracting procurement."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_PT_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, standard procurement, consignment procurement, subcontracting procurement, number ranges, business roles, master data prerequisites, test procedures, BF6]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-560
topic: 10-procurement/scheduling-agreements
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar programa de remessas – MDS (BF6) (BF6_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar programa de remessas – MDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893917)

[2 Pré-requisitos 3](#_Toc233893918)

[2.1 Acesso ao sistema 3](#_Toc233893919)

[2.2 Funções 3](#_Toc233893920)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893921)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893922)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893923)

[2.5.1 Intervalos de numeração 4](#_Toc233893924)

[3 Tabela de síntese 5](#_Toc233893925)

[4 Procedimentos de teste 6](#_Toc233893926)

[4.1 Criar programa de remessas para suprimento padrão 6](#_Toc233893927)

[4.1.1 Criar programa de remessas com documento de liberação - Padrão 6](#_Toc233893928)

[4.1.2 Criar programa de remessas sem documento de liberação - Padrão 8](#_Toc233893929)

[4.2 Criar programa de remessas para suprimento em consignação 10](#_Toc233893930)

[4.3 Criar programa de remessas para suprimento de subcontratação 12](#_Toc233893931)

## Objetivo

Este documento fornece uma descrição sobre como criar um programa de remessas para seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados relevantes para o appliance SAP S/4HANA Cloud Public Edition, como os dados de compras, os dados do material e os dados do fornecedor. Os campos que não são relevantes para o escopo do conteúdo do SAP S/4HANA Cloud Public Edition, uma vez que foram fornecidos pelo SAP Best Practices, não estão descritos neste documento.

Um programa de remessas é um contrato plurianual com um fornecedor que cobre o suprimento de materiais sujeito a condições pré-determinadas. As condições são válidas para uma quantidade total e um período predefinidos.

As principais vantagens dos programas de remessa são:

- programas de remessa podem substituir um grande número de pedidos ou solicitações sobre contratos.
- Trata-se de um contrato plurianual que permite a você negociar melhores preços com um fornecedor.

Existem as seguintes categorias de item:

- Suprimento padrão
- Suprimento em consignação
- Suprimento de subcontratação

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
| Comprador | SAP_BR_PURCHASER | Compras / Determinação da fonte de suprimento e contratação | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura de sua empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados de compras | Organização de compras | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material é utilizado em processos de compras. | Organização de compras:__________ |

### Dados mestre obrigatórios e opcionais

O programa de remessas pode se referir a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um programa de remessas.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material |  | Obrigatório | Para inserir o material, crie primeiro os dados mestre de materiais. |
| Fornecedor |  | Obrigatório | Para inserir o fornecedor, crie primeiro os dados mestre de fornecedores. |

### Parâmetros principais para a criação de dados

Nesta seção é fornecida uma descrição para os parâmetros básicos que influenciam o comportamento de um programa de remessas e que são sempre necessários para a criação de um programa de remessas

#### Intervalos de numeração

Os seguintes intervalos de numeração estão definidos para programa de remessas:

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Numérico interno | Intervalo de numeração numérico interno para utilização padrão:5500000000 – 5599999999 | Este intervalo de numeração é utilizado quando o sistema atribui automaticamente um valor numérico a um programa de remessas. |
| Numeração externa | Intervalo de numeração numérico externo:5600000000 – 5699999999 | Este intervalo de numeração está reservado para uma atribuição externa de números de numeração. |

## Tabela de síntese

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
|  |  |  |  |
| [Criar programa de remessas com documento de liberação - Padrão](#unique_10) [página ] 6 | Comprador | Administrar programas de remessas das compras(F2179) | Programa de remessas com documento de liberação – Padrão |
| [Criar programa de remessas sem documento de liberação - Padrão](#unique_11) [página ] 8 | Comprador | Administrar programas de remessas das compras(F2179) | Programa de remessas sem documento de liberação – Padrão |
| [Criar programa de remessas para suprimento em consignação](#unique_12) [página ] 10 | Comprador | Administrar programas de remessas das compras(F2179) | Programa de remessas para suprimento em consignação é criado |
| [Criar programa de remessas para suprimento de subcontratação](#unique_13) [página ] 12 | Comprador | Administrar programas de remessas das compras(F2179) | Programa de remessas para suprimento de subcontratação é criado |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar programa de remessas para suprimento padrão

#### Criar programa de remessas com documento de liberação - Padrão

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar programa de remessas para suprimento padrão.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar programas de remessas das compras(F2179). | O app é aberto. |  |
| 3 | Criar programa de remessas | Clique em Criar para criar um programa de remessas. | A tela Novo programa de remessas das compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Crie um novo programa de remessas com os seguintes dados:Fornecedor: <fornecedor>Tipo de acordo: LPA (SA com documento de liberação)Início da validade: <MM/DD/AAAA>Válido até: <MM/DD/AAAA>Empresa: <Empresa>Organização de compras: <organização de compras>Grupo de compradores: <grupo de compradores>Valor fixado: <valor fixado> |  |  |
| 5 | Inserir notas de cabeçalho | Vá para a seção Notas e insira algumas das seguintes notas de cabeçalho:Texto do cabeçalhoNota do cabeçalhoTipos de determinação do preçoPrazosCondições de remessaNormas de expediçãoCondições de pagamentoGarantiasMulta por quebra de contratoAvaisCláusulas contratuaisAtivoOutra estipulação contratualRecebimentoNota do fornecedor (geral)Nota do fornecedor (org.compras) |  |  |
| 6 | Adicionar itens ao programa de remessas | Na tela Novo programa de remessas das compras, clique nas facetas Itens e em Criar. | A tela Item do programa de remessas das compras é exibida. |  |
| 7 | Inserir dados do item | Na tela de facetas Itens, efetue as seguintes entradas:Centro: <centro>embalagem: <Material>Quantidade prevista: <quantidade prevista>Preço líquido do pedido: <preço líquido do pedido>Código de imposto: <XX (valor padrão do registro info)>Data do imposto: <use a data de hoje como valor padrão>Na seção Controle de saída, efetue a seguinte entrada:Perfil de criação: <perfil de criação>Clique em Aplicar na parte inferior da tela. |  |  |
| 8 | Criar | Volte à tela Novo programa de remessas das compras e clique em Criar na parte inferior da tela.Anote o número do programa de remessas. | É criado um programa de remessas. |  |

#### Criar programa de remessas sem documento de liberação - Padrão

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar programa de remessas para suprimento padrão.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar programas de remessas das compras(F2179). | A página detalhada Administrar programas de remessas das compras(F2179) é exibida. |  |
| 3 | Criar programa de remessas | Clique em Criar para criar um programa de remessas | A visão de cabeçalho Novo programa de remessas das compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Crie um novo programa de remessas com os seguintes dados:Fornecedor: <fornecedor>Tipo de acordo: LP (Programa de remessas)Início da validade: <MM/DD/AAAA>Válido até: <MM/DD/AAAA>Empresa: <Empresa>Organização de compras: <organização de compras>Grupo de compradores: <grupo de compradores>Valor fixado: <valor fixado> |  |  |
| 5 | Inserir notas de cabeçalho | Navegue para a seção Notas e insira algumas das notas de cabeçalho seguintes:Texto do cabeçalhoNota do cabeçalhoTipos de determinação do preçoPrazosCondições de remessaNormas de expediçãoCondições de pagamentoGarantiasMulta por quebra de contratoAvaisCláusulas contratuaisAtivoOutra estipulação contratualRecebimentoNota do fornecedor (geral)Nota do fornecedor (org.compras) |  |  |
| 6 | Adicionar itens ao programa de remessas | Na visão Novo programa de remessas das compras, escolha as facetas Itens e clique em Criar. | A visão Novo item de programa de remessas das compras é exibida. |  |
| 7 | Inserir dados do item | Na tela de facetas Itens, efetue as seguintes entradas:Centro: <centro>embalagem: <Material>Quantidade prevista: <quantidade prevista>Preço líquido do pedido: <preço líquido do pedido>Código de imposto: <XX (valor padrão do registro info)>Data do imposto: <use a data de hoje como valor padrão>Clique em Aplicar na parte inferior da tela. |  |  |
| 8 | Criar | Volte para a visão de cabeçalho Novo programa de remessas das compras e clique em Criar na parte inferior da visão.Anote o número do programa de remessas. | É criado um programa de remessas. |  |

### Criar programa de remessas para suprimento em consignação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar programa de remessas para suprimento em consignação.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar programas de remessas das compras(F2179). | A página da lista Administrar programas de remessas é exibida. |  |
| 3 | Criar programa de remessas | Clique em Criar para criar um novo programa de remessas | A visão de cabeçalho Novo programa de remessas é exibida. |  |
| 4 | Inserir dados de cabeçalho | Crie um novo programa de remessas com os seguintes dados:Tipo de acordo: LP (Programa de remessas)Fornecedor: <fornecedor>Início da validade: padrão hojeFim da validade: MM/DD/AAAA, por exemplo, a data de hoje + 720 diasGrupo de compradores: <grupo de compras>Organização de compras: <organização de compras>Empresa: <empresa>Valor fixado: por exemplo, XXXXX EUR |  |  |
| 5 | Adicionar itens ao programa de remessas | Na visão Novo programa de remessas das compras, escolha as facetas Itens e clique em Criar. | A visão Novo item de programa de remessas é exibida. |  |
| 6 | Inserir dados do item | Na visão de facetas Item, efetue as seguintes entradas:Categoria do item: K (consignação)Centro: <centro>Material: <material>Quantidade prevista: <quantidade prevista>Código de imposto: XX (valor padrão do registro info)Data do imposto: padrão hojeNota Se o RITA estiver ativado e os países de identificação fiscal forem atualizados para a empresa na Etapa de configuração de finanças 103464 (Ativar RITA e atualizar países de identificação fiscal), o país do imposto poderá ser extraído ou escolhido um valor de País do imposto diferente da lista.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Clique em Aplicar na parte inferior da visão. |  |  |
| 7 | Criar | Volte à visão Novo programa de remessas das compras e clique em Criar na parte inferior da visão.Anote o número do programa de remessas. | É criado um programa de remessas. |  |

### Criar programa de remessas para suprimento de subcontratação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar programa de remessas para suprimento de subcontratação.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar programas de remessas das compras(F2179). | A página da lista Administrar programas de remessas é exibida |  |
| 3 | Criar programa de remessas | Clique em Criar para criar um programa de remessas | A visão de cabeçalho Novo programa de remessas é exibida. |  |
| 4 | Inserir dados de cabeçalho | Crie um novo programa de remessas com os seguintes dados:Tipo de acordo: LP (Programa de remessas)Fornecedor: <fornecedor>Início da validade: padrão hojeFim da validade: MM/DD/AAAA, por exemplo, a data de hoje + 720 diasGrupo de compradores: <grupo de compras>Organização de compras: <organização de compras>Empresa: <empresa>Valor fixado: por exemplo, XXXXX EUR |  |  |
| 5 | Adicionar itens ao programa de remessas | Na visão Novo programa de remessas das compras, escolha as facetas Itens e clique em Criar. | A visão Novo item de programa de remessas é exibida. |  |
| 6 | Inserir dados do item | Na visão de facetas Itens, efetue as seguintes entradas:Categoria do item: L (Subcontratação)Centro: <centro>Depósito: <depósito>Material: <material>Preço líquido do pedido: valor padrão do registro infoQuantidade prevista: <quantidade prevista>Código de imposto: XX (valor padrão do registro info)Data do imposto: padrão hojeNota Se o RITA estiver ativado e os países de identificação fiscal forem atualizados para a empresa na Etapa de configuração de finanças 103464 (Ativar RITA e atualizar países de identificação fiscal), o país do imposto poderá ser extraído ou escolhido um valor de País do imposto diferente da lista.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Clique em Aplicar na parte inferior da visão. |  |  |
| 7 | Criar | Volte à visão Novo programa de remessas das compras e clique em Criar na parte inferior da visão.Anote o número do programa de remessas. | É criado um programa de remessas. |  |

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
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 21,299 chars in the whole document
