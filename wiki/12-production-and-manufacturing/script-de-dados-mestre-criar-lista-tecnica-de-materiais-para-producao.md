---
id: 12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao
title: "Script de dados mestre - Criar lista técnica de materiais para produção e vendas (BNK), PT (BNK_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create material BOMs for production and sales, with test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_PT_XX]
keywords: [Material BOMs for Production and Sales, bill of materials, production bom, sales bom, change number, business roles, bom usage, bom item categories, master data scripts, routing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-626
topic: 12-production-and-manufacturing/material-boms
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar lista técnica de materiais para produção e vendas (BNK), PT (BNK_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar lista técnica de materiais para produção e vendas – MDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894034)

[2 Pré-requisitos 3](#_Toc233894035)

[2.1 Acesso ao sistema 3](#_Toc233894036)

[2.2 Funções 3](#_Toc233894037)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894038)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894039)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894040)

[2.5.1 Utilização da lista técnica 4](#_Toc233894041)

[3 Tabela de síntese 5](#_Toc233894042)

[4 Procedimentos de teste 6](#_Toc233894043)

[4.1 Criar número da modificação 6](#_Toc233894044)

[4.2 Criar lista técnica de produção 7](#_Toc233894045)

[4.3 Criar lista técnica de vendas 9](#_Toc233894046)

[5 Anexo 11](#_Toc233894047)

[5.1 Processos subsequentes: Criar roteiro 11](#_Toc233894048)

## Objetivo

Uma lista técnica de produção é uma lista, estruturada de modo formal, dos componentes que compõem um projeto ou um conjunto (parte de um produto). A lista contém o número de objeto de cada componente juntamente com a quantidade e unidade de medida. Componente pode ser uma matéria-prima ou um material semiacabado que representa um conjunto.

É utilizado em uma execução de MRP para calcular as necessidades de material e em transações, como uma ordem de produção. As informações são específicas de um centro de produção (conhecido como centro).

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
| Engenheiro de produção - produção discreta | SAP_BR_PRODN_ENG_DISC | Engenharia de produção - produção discreta | SAP_BR_PRODN_ENG_DISC |  |
| Responsável pela lista técnica | SAP_BR_BOM_ENGINEER | Listas técnicas | SAP_BR_BOM_ENGINEER |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da empresa foram criados no seu sistema durante a ativação. A estrutura organizacional reflete a estrutura da sua empresa. Os dados mestre representam, por exemplo, materiais, clientes e fornecedores, dependendo do foco operacional da sua empresa.

Use seus próprios dados mestre ou os dados de amostra a seguir para realizar o procedimento de teste.

### Dados mestre obrigatórios e opcionais

Os registros de dados da lista técnica podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em uma lista técnica.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material | Em Criar lista técnica do material: 1ª tela e Criar lista técnica do material: visão Itens gerais, insira o número do material em Material e componente. | Obrigatório | Conclua os seguintes scripts de cadastro como pré-requisito antes de iniciar as etapas do processo:Criar mestre de produtos do tipo "Matéria-prima" – MDS (BNR)Criar mestre de produtos do tipo "Produto semiacabado" – MDS (BNS)Criar mestre de produtos do tipo "Produto acabado" – MDS (BNT)Criar mestre de produtos do tipo "Produto comercializável" – MDS (BNF) |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma lista técnica:

#### Utilização da lista técnica

A utilização da lista técnica (LT) define a área (como vendas ou produção) onde pode ser utilizada uma LT.

| Utilização da lista técnica | Descrição |
| --- | --- |
| 1 | Produção |
| 5 | Vendas e distribuição |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar número da modificação](#unique_10) [página ] 6 | Responsável pela lista técnica | Criar registro mestre de modificação(CC01) |  |
| [Criar lista técnica de produção](#unique_11) [página ] 7 | Engenheiro de produção - produção discreta | Atualizar lista técnica (versão 2) - Criar, modificar e exibir LTs(F1813A) |  |
| [Criar lista técnica de vendas](#unique_12) [página ] 9 | Engenheiro de produção - produção discreta | Atualizar lista técnica - Criar, modificar e exibir LTs(F1813) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar número da modificação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criação do registro mestre de modificação a ser utilizado na criação de lista técnica nas próximas etapas de Produção e Lista técnica.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Responsável pela lista técnica. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Criar registro mestre de modificação(CC01). |  |  |
| 3 | Inserir número da modificação | Na tela Criar registro mestre de modificação: 1ª tela, insira os seguintes dados e pressione Enter:Nº da alteração: <Insira o número da modificação, por exemplo: CN001>Deixe valores propostos nos outros campos. |  |  |
| 4 | Inserir dados do registro mestre de modificações | Na tela Criar registro mestre de modificação: cabeçalho da modificação, insira os dados fornecidos no seguinte exemplo e pressione Enter.Campo ao lado de Número da modificação: mestre de modificação de lista técnica da produçãoVálido desde: hojeStatus do número da modificação: 01 Ativo |  |  |
| 5 | Marcar campos de seleção para lista técnica | Na tela Criar registro mestre de modificação: tipos de objeto, tabela Tipos de objeto, linha Lista técnica, marque os seguintes campos de seleção:Ativ.ObjetoReg.ctrl. |  |  |
| 6 | Clicar em Salvar | Clique em Salvar. | O registro mestre de modificação é criado. |  |

### Criar lista técnica de produção

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar lista técnica (versão 2) - Criar, modificar e exibir LTs(F1813A). |  |  |
| 3 | Criar LT | Clique em Criar lista técnica. Na tela Criar lista técnica, insira os dados a seguir e clique em OK.Material: <Número do material acabado/semiacabado>Nº da alteração: <o seu número da modificação criado na etapa anterior>Centro: <Seu centro>Utilização da lista técnica: 1 (apenas para produção) |  |  |
| 4 | Adicionar dados de componentes | Na seção Componentes, selecione o ícone Adicionar para adicionar um ou mais componentes.ICT de categoria de item: <L para item do estoque>Componente: <Número do material, produto bruto/semiacabado>Quantidade: <quantidade>UM do componente: UN | Dados de componentes são adicionados. |  |
| 5 | Inserir categoria do item de LT não estocável ('N') | Na seção Componentes, selecione o ícone Adicionar para adicionar um ou mais componentes.ICT de categoria de item: <N para item não estocável>Componente: <Número do material, produto bruto/semiacabado>Quantidade do componente: <quantidade>UM do componente: UNPressione Enter para ativar os campos Componente e Quantidade do componente .Nota Essa categoria de item é utilizada para componentes que não são mantidos em estoque. Os items não estocáveis podem ser inseridos na LT com ou sem um registro mestre. | São adicionados dados de componentes para itens não estocáveis. |  |
| 6 | Inserir categoria de item da LT Dimensão variável ('R') | Na seção Componentes, selecione o ícone Adicionar para adicionar um ou mais componentes.ICT de categoria de item: <R para item de tamanho variável>Componente: <Número do material, produto bruto/semiacabado>Selecione a seta para abrir a página DetalhesEm Dados do item de dimensão variável, faça as entradas necessárias.Tamanho 1: <insira as dimensões dos itens de tamanho variável>Tamanho 2: <insira as dimensões dos itens de tamanho variável>Tamanho 3: <insira as dimensões dos itens de tamanho variável>Unidade de dimensão: <insira a unidade de medida para a quantidade de um item de dimensão variável>Chave de fórmula: <insira a fórmula para calcular o item de dimensão variável>Número de itens de dimensões variáveis: <quantidade>Quantidade de itens de dimensão variável: <uma quantidade calculada para os itens de dimensão variável>Clique em Aplicar.Nota Essa categoria de item permite especificar seções de diferentes tamanhos de um componente com um material, como o tamanho de uma chapa necessária para reparar um forro. | São adicionados/calculados os dados de componentes para itens variáveis. |  |
| 7 | Inserir item de texto da categoria do item da lista técnica (“T”) | Para a nova linha Número do item da LT, faça as entradas de acordo com o seguinte exemplo:Categoria do item: Item do textoNa linha Número do item da LT,Selecione a seta para abrir a página DetalhesNa tela Atualizar lista técnica – Detalhes básicos,Quantidade do componente: 1UM do componente: UNSelecione a guia Status/Texto descritivo para exibir o texto do item.Texto do item: documentação | Foram adicionados dados de documentos de texto nos itens de texto. |  |
| 8 | Verificar cabeçalho | Na seção Atributos do cabeçalho, você pode verificar e modificar os dados, se necessário. |  |  |
| 9 | Salvar os dados | Salve as entradas. | A mensagem Lista técnica do material salva é exibida. |  |

### Criar lista técnica de vendas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Clique em Atualizar lista técnica - Criar, modificar e exibir LTs(F1813). |  |  |
| 3 | Criar lista técnica | Clique em Criar lista técnica. Na tela Criar lista técnica, insira os dados a seguir e clique em OK.Material:<número do material do cabeçalho da lista técnica>, por exemplo, SDBOMERLAHD ou SDBOMLUMFHDCentro: < insira seu centro>Nº da alteração: <o seu número da modificação criado na etapa anterior>Utilização da lista técnica: 5 |  |  |
| 4 | Adicionar dados de componentes | Na seção Componentes, selecione o ícone Adicionar para adicionar um ou mais componentes.ICT de categoria de item: <L para item do estoque>Componente: <número do material, produtos comercializáveis>Quantidade: <quantidade> | Dados de componentes são adicionados. |  |
| 5 | Verificar cabeçalho | Na seção Atributos do cabeçalho, você pode verificar e modificar os dados, se necessário. |  |  |
| 6 | Salvar os dados | Salve as entradas. | A mensagem Lista técnica do material salva é exibida. |  |

## Anexo

### Processos subsequentes: Criar roteiro

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Roteiro |  |  | Para executar esta atividade, conclua o script de teste Criar roteiro – MDS (BNL). |

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
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 16,756 chars in the whole document
