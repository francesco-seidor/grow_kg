---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-hierarquia-de-produtos-4dx-416
title: Script de dados mestre - Criar hierarquia de produtos (4DX) (4DX_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition master data script (4DX): configure hierarchy nodes and create/activate a product hierarchy in Fiori app F4359."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-hierarchy]
aliases: [4DX_S4CLD2608_Master_Data_PT_XX]
keywords: [Product Hierarchies, product hierarchy, master data scripts, product hierarchy nodes, self-service configuration, business roles, product master data, sales order processing, central business configuration, 4DX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-416
topic: 02-business-partner-and-product-master-data/product-hierarchy
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar hierarquia de produtos (4DX) (4DX_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Hierarchies** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar hierarquia de produtos (4DX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893729)

[2 Pré-requisitos 3](#_Toc233893730)

[2.1 Acesso ao sistema 3](#_Toc233893731)

[2.2 Funções 3](#_Toc233893732)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893733)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893734)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893735)

[2.5.1 Nós da hierarquia de produtos 4](#_Toc233893736)

[2.6 Etapas preliminares 5](#_Toc233893737)

[2.6.1 Criar nós para hierarquias de produtos 5](#_Toc233893738)

[3 Tabela de síntese 8](#_Toc233893739)

[4 Procedimentos de teste 9](#_Toc233893740)

[4.1 Criar hierarquia de produtos 9](#_Toc233893741)

## Objetivo

Este documento contém uma descrição sobre como criar dados mestre de hierarquia de produtos para seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo de conteúdo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento, embora possam exibir na tela.

Os dados mestre de hierarquia de produtos criados podem ser usados para a atribuição de canais de distribuição com uma hierarquia de produtos que, por sua vez, são usados no processamento subsequente de pedidos de venda.

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
| Especialista de configuração - configuração de processo empresarial | SAP_BR_BPC_EXPERT | Configuração de processo empresarial / Configuração de processo empresarial - Finanças / Configuração de processo empresarial - Suprimento / Administrar sua solução / Configuração de processo empresarial - Workflow / Configuração empresarial - Administração de funcionalidades / Configuração de processo empresarial - Extensibility Explorer / Configuração de gestão empresarial - Transporte | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados de venda | Centro, organização de vendas, canal de distribuição | Dados de imposto, Grupo de categorias de item, Grupo de carregamento etc. |  | Centro:____________Organização de vendas:____________Canal de distribuição:______________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela a seguir oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de hierarquia de produtos.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório / Opcional | Comentários |
| --- | --- | --- | --- |
| Produto | No app Administrar hierarquias de produtos, é atribuída uma hierarquia com vários produtos como nós-folha ou nós finais. | Obrigatório | Quando você atribui registros de produto criados no app Administrar dados mestre de produtos, como nós-folha no app Administrar hierarquias de produtos, é fornecida relevância empresarial/completude à hierarquia. |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e sempre necessários para criar um registro de dados mestre de hierarquia de produtos.

#### Nós da hierarquia de produtos

A IU de configuração self-service (etapa de configuração) disponível para produto, Configurar nós para hierarquias de produtos, acessada por meio da filtragem da área de aplicação para Database and Data Management precisa ser atualizada para você selecionar ou formar a estrutura hierárquica.

Esta configuração oferece uma opção para criar vários valores de nó e uma descrição para cada nó.

|  |
| --- |
| Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration. |

### Etapas preliminares

#### Criar nós para hierarquias de produtos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

As entradas geradas na etapa Configurar nós para hierarquias de produtos de Configuração self-service são necessárias para criar uma hierarquia de produtos.

|  |
| --- |
| Nota Esta etapa deve ser executada pelo usuário Especialista em configuração no cenário empresarial comum. |

Procedimento

|  |
| --- |
| Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration. |

Configurar sua solução:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | A página Início é exibida. |  |
| 2 | Abrir o app SAP Fiori | Na seção Cockpit de implementação, clique em Administrar sua solução(F1241). | Uma nova janela é aberta exibindo a tela Administrar sua solução(F1241).Nota Esse app faz parte do modelo de função Especialista de configuração - configuração de processo empresarial. |  |
| 3 | Clique em Configurar sua solução | No app Administrar sua solução, clique em Configurar sua solução. | É aberta uma nova página com Configurar sua solução: Modificar fase. |  |
| 4 | Selecionar a área de aplicação | No app Configurar sua solução, selecione o filtro de Área de aplicação e escolha a opção Database and Data Management. | O número de entradas na tabela de resultados é reduzido a poucos registros. |  |
| 5 | Selecionar a subárea de aplicação | No app Configurar sua solução, selecione o filtro de Subárea de aplicação e escolha a opção Produto. | Apenas um registro é exibido na lista de resultados. |  |
| 6 | Realizar etapas de configuração de produto | Nas entradas mostradas na tabela, selecione o registro com Produto como subárea de aplicação.Em seguida, clique no título de seção Etapas de configuração. | A seção exibe uma lista com várias etapas de configuração de produto. |  |
| 7 | Configurar nós para hierarquias de produtos | Na etapa de configuração Configurar nós para hierarquias de produtos, clique em Configurar. | A página Atualização de ID de subnó da hierarquia de produtos é aberta. |  |
| 8 | Criar novas entradas | Clique em Entradas novas. | A página editável é aberta para a atualização de novos subnós com o título Entradas novas: síntese das entradas adicionadas. |  |
| 9 | Inserir novos subnós | Informe várias entradas para os subnós necessários na hierarquia de produtos de destino.Por exemplo, para uma hierarquia <Bebidas>:Os nós da hierarquia de produtos poderiam ser <BEBIDAS_AERADAS>, <BEBIDAS_NÃO_AERADAS> e assim por diante.A descrição dos subnós pode ser atualizada como <Bebidas aeradas>, <Bebidas não aeradas> e assim por diante. |  |  |
| 10 | Salvar as entradas | Clique em Salvar no rodapé da página. | A página Atualização de ID de subnó da hierarquia de produtos será exibida novamente com as novas entradas informadas. |  |
| 11 | Finalizar | Clique em Sair e efetue logoff. |  |  |

SAP Central Business Configuration:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login na experiência em projetos no SAP Central Business Configuration. |  |  |
| 2 | Abrir Workflow flexível ativo | Vá para o app Business Processes Configuration. Para localizar a atividade na visão de árvore, procure a seguinte atividade: Configure Nodes for Product Hierarchies.Escolha Open Documentation para o item encontrado para ver mais detalhes sobre esta atividade de configuração.Selecione o link para navegar diretamente para o sistema SAP S/4HANA Cloud Public Edition. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial. |  |  |
| 3 | Criar novas entradas | Clique em Entradas novas. | A página editável é aberta para a atualização de novos subnós com o título Entradas novas: síntese das entradas adicionadas. |  |
| 4 | Inserir novos subnós | Informe várias entradas para os subnós necessários na hierarquia de produtos de destino.Por exemplo, para uma hierarquia <Bebidas>:Os nós da hierarquia de produtos poderiam ser <BEBIDAS_AERADAS>, <BEBIDAS_NÃO_AERADAS> e assim por diante.A descrição dos subnós pode ser atualizada como <Bebidas aeradas>, <Bebidas não aeradas> e assim por diante. |  |  |
| 5 | Salvar as entradas | Clique em Salvar no rodapé da página. | A página Atualização de ID de subnó da hierarquia de produtos será exibida novamente com as novas entradas informadas. |  |
| 6 | Finalizar | Clique em Sair e efetue logoff. |  |  |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar hierarquia de produtos](#unique_11) [página ] 9 | Especialista em dados mestre - Dados do produto | Administrar hierarquias de produtos(F4359) | O registro de dados mestre de hierarquia de produtos é criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar hierarquia de produtos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções sobre como criar uma hierarquia de produtos com produtos atribuídos à hierarquia como nós finais. Após a ativação, a hierarquia pode ser consumida durante a criação de ordens do cliente.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori usando suas credenciais de usuário. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar hierarquias de produtos(F4359). | O app é aberto. |  |
| 3 | Criar hierarquia de produtos | Em Administrar hierarquias de produtos, selecione + (Criar uma nova hierarquia). | A tela Criar nova hierarquia é exibida. |  |
| 4 | Inserir dados da hierarquia de produtos | Na tela Criar nova hierarquia, efetue as seguintes entradas:Tipo: por exemplo, <Hierarquia de produto>ID da hierarquia: por exemplo, <BEBIDAS>.Descrição da hierarquia: por exemplo, <Hierarquia de bebidas>.Válido desde: <insira uma data de início de validade da hierarquia>Válido até: <altere a data predefinida, se necessário, para criar uma hierarquia dependente do tempo> |  |  |
| 5 | Clicar em Criar | Na tela Criar nova hierarquia, clique em Criar. | A lista Hierarquia é filtrada para mostrar a entrada recém-criada da hierarquia de produtos com o Status exibido como Esboço. |  |
| 6 | Selecionar a nova hierarquia de produtos | No app Administrar hierarquias de produtos(F4359), selecione a hierarquia de produtos recém-criada com o status Esboço listada no resultado. | A estrutura da Hierarquia de produtos é exibida em um formato de tabela em árvore. |  |
| 7 | Editar a hierarquia de produtos | Selecione Editar no rodapé da tela. | A tela é exibida no modo de edição, permitindo que você modifique valores ou adicione novos nós. |  |
| 8 | Adicionar nós ao nó raiz | Clique em + (Adicionar) para o primeiro nó. | A tela Adicionar nó é exibida. |  |
| 9 | Selecionar subnós da raiz | Na caixa de diálogo Adicionar nó, a opção Subnó está selecionada por padrão.Insira dados no campo Nó. Os valores configurados na etapa preliminar [Criar nós para hierarquias de produtos](#unique_9) [página ] 5 podem ser usados aqui.Por exemplo, <AERATED_DRINKS>, <NON_AERATED_DRINKS>, e assim por diante.Nota A caixa de diálogo de entradas possíveis podem ajudar você a selecionar vários nós e a atribuí-los ao nó selecionado da hierarquia.Clique em OK. | Os nós selecionados são adicionados como nós inferiores na estrutura em árvore da tabela para o nó raiz da hierarquia de produtos. |  |
| 10 | Adicionar nós a subnós | Selecione + (Adicionar) para o nó a fim de adicionar mais subnós.Por exemplo, selecione + (Adicionar) para o nó <NON_AERATED_DRINKS>. | A tela Adicionar nó é exibida. |  |
| 11 | Selecionar nós para subnós | Na tela Adicionar nó, selecione outros nós nas entradas possíveis para adicioná-los como subnós de <NON_AERATED_DRINKS> (por exemplo).Clique em OK. | Os nós selecionados são adicionados como nós inferiores do nó selecionado da hierarquia de produtos na estrutura em árvore da tabela. |  |
| 12 | Adicionar produto à hierarquia | Clique em + (Adicionar) para o nó a fim de adicionar produtos à hierarquia. | A tela Adicionar nó é exibida. |  |
| 13 | Selecionar produto | Na tela Adicionar nó, selecione Produto. | Na tela Adicionar nó, o campo de entrada é modificado para Produto. |  |
| 14 | Atribuir produtos à hierarquia | Na tela Adicionar nó, selecione entradas no campo Produto para atribuir os produtos necessários ao nó da hierarquia.Nota Você pode usar a caixa de diálogo de entradas possíveis para selecionar vários produtos e atribuí-los ao subnó selecionado da hierarquia. | Os produtos selecionados são atribuídos ao subnó necessário da hierarquia de produtos. |  |
| 15 | Salvar a hierarquia de produtos | Clique em Salvar. | As alterações foram salvas. |  |
| 16 | Ativar a hierarquia de produtos | Selecione Ativar. | A hierarquia de produtos é ativada, e o Status é modificado de Esboço para Ativo. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/4dx-415]]
- related-to :: [[02-business-partner-and-product-master-data/4dx-417]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-hierarchy-4dx-413]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-jerarquia-de-productos-4dx-414]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 19,639 chars in the whole document
