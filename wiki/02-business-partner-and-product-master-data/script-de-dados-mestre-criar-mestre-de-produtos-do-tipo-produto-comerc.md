---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Produto comercializável\" – MDS (BNF) (BNF_S4CLD2608_Master_Data_PT_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (PT) for creating tradable-goods product master data via MM01 or F1602, by view; Brazil (BNF) variant."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-trading-goods]
aliases: [BNF_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Trading Goods", product master data, material master views, basic data, sales data, purchasing data, mrp planning data, warehouse data, accounting valuation data, configurable products]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-596
topic: 02-business-partner-and-product-master-data/product-master-trading-goods
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Produto comercializável" – MDS (BNF) (BNF_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Trading Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Produto comercializável" – MDS (BNF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893966)

[2 Pré-requisitos 3](#_Toc233893967)

[2.1 Acesso ao sistema 3](#_Toc233893968)

[2.2 Funções 3](#_Toc233893969)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893970)

[2.4 Dados mestre obrigatórios e operacionais 4](#_Toc233893971)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233893972)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233893973)

[2.5.2 Setor industrial 5](#_Toc233893974)

[3 Tabela de síntese 6](#_Toc233893975)

[4 Procedimentos de teste 7](#_Toc233893976)

[4.1 Criar dados mestre de materiais (produto) - dados básicos 7](#_Toc233893977)

[4.2 Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA) 10](#_Toc233893978)

[4.3 Criar dados mestre de materiais (produto) - dados de compras 13](#_Toc233893979)

[4.4 Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro) 15](#_Toc233893980)

[4.5 Criar dados mestre de materiais (produto) - dados do depósito 19](#_Toc233893981)

[4.6 Criar dados mestre de materiais (produto) - dados contábeis (dados da área de avaliação) 21](#_Toc233893982)

[4.7 Criar dados mestre do produto - Produto configurável e variantes 24](#_Toc233893983)

[4.8 Criar dados mestre do produto – Salvar anexos 26](#_Toc233893984)

[4.9 Criar dados mestre do produto - Vendas do centro/Dados gerais 28](#_Toc233893985)

[4.10 Criar dados mestre do produto – Centro/Produção repetitiva 30](#_Toc233893986)

## Objetivo

O mestre de materiais ou de produtos contém informações referentes a todos os materiais físicos supridos, produzidos, armazenados e vendidos. É também utilizado para gerenciar informações sobre serviços, por exemplo, para compra e venda de serviços por hora.

O mestre de materiais contém informações como o número único de material, nome, tipo de material, unidade de medida, descrições, peso e dimensões. Estas informações de material são utilizadas e armazenadas em transações, como ordens do cliente, remessas, pedidos ou movimentos de mercadorias.

Visto que todas as informações de um material são armazenadas centralmente, as informações mestre do material são organizadas em diferentes visões. Por exemplo, vendas, armazenamento, MRP, cálculo de custos e contabilidade.

Algumas informações em cada material são específicas a determinadas unidades organizacionais. Por exemplo, uma descrição de vendas é específica a uma unidade de vendas (conhecida como área de vendas), um planejador MRP é específico a um certo local (conhecido como centro), ou algumas informações podem ser específicas de um depósito.

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
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre do material são dependentes das unidades organizacionais da empresa, os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do material (texto breve), número do material, grupo de materiais, unidade de medida básica, etc. | Os dados básicos só existem uma vez para um registro de dados mestre de materiais. | não aplicável |
| Dados de vendas | Centro, organização de vendas, canal de distribuição | Dados de imposto, grupo de categorias do item, grupo transp., grupo de carregamento, tempo de preparação da expedição, etc. | Os dados de venda podem existir para todas as organizações de vendas de sua estrutura empresarial nas quais o registro mestre de materiais seja utilizado. | Centro:____________Organização de vendas:__________Canal de distribuição:__________ |
| Dados de compras | Centro | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material deve ser utilizado em processos de compras. | Centro:__________ |
| Dados MRP/de planejamento | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante de validade, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de cliente.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados contábeis | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e operacionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais:

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão fornece apenas um setor industrial M. Atualmente, isso é visível apenas no SAP GUI.

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA)](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas criados. |
| [Criar dados mestre de materiais (produto) - dados de compras](#unique_13) [página ] 13 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de compra criados. |
| [Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)](#unique_14) [página ] 15 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados MRP/de planejamento criados. |
| [Criar dados mestre de materiais (produto) - dados do depósito](#unique_15) [página ] 19 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados do depósito criados. |
| [Criar dados mestre de materiais (produto) - dados contábeis (dados da área de avaliação)](#unique_16) [página ] 21 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados da área de avaliação) criados. |
| [Criar dados mestre do produto - Produto configurável e variantes](#unique_17) [página ] 24 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Criar produto configurável e variantes. |
| [Criar dados mestre do produto – Salvar anexos](#unique_18) [página ] 26 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Salvar anexos para o registro mestre de materiais. |
| [Criar dados mestre do produto - Vendas do centro/Dados gerais](#unique_19) [página ] 28 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |
| [Criar dados mestre do produto – Centro/Produção repetitiva](#unique_20) [página ] 30 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre de materiais (produto) - dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 4 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2.Selecione Continuar. | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados básicos | Na tela Material...(Produtos comercializáveis), na guia Dados básicos 1, insira a Descrição de material (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: <Unidade de medida básica>Grupo de mercadorias: <grupo de mercadorias>GrpCtgsItemGer.: <GrpCtgsItemGer.> |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas:Peso bruto: <peso bruto>Unidade de peso: <Unidade de peso>Peso líquido: <peso líquido>Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 8 | Preencher dados básicos | Na guia Dados básicos 2, você não precisa efetuar nenhuma entrada. |  |  |
| 9 | Salvar os dados | Clique em Salvar para salvar seus dados. | É exibida a tela Criar material (1ª tela).Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 3 | Selecione Criar produtos. | Na tela Administrar dados mestre de produtos, selecione Criar produto. | A tela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na tela Criar dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z … ou qualquer ID alfanumérico externo. Ele deve começar com um caractere ou nenhuma entrada e então o sistema atribuirá um ID numérico automaticamente.Nota Para obter mais informações sobre Número do produto, consulte o capítulo anterior [Tipo de material e intervalos de numeração](#unique_8) [página ] 5.Tipo de produto: Produtos comercializáveisGrupo de produtos: Por exemplo, L001.Unidade básica: por exemplo, PC.Descrição: <qualquer descrição> |  |  |
| 5 | Clicar em OK | Na tela Administrar mestre de produtos, selecione OK. | A tela Administrar mestre de produtos é exibida. |  |
| 6 | Inserir dados básicos | Vá para a tela Administrar mestre de produtos > DADOS BÁSICOS > Dados básicos e efetue a seguinte entrada:Setor de atividade: Por exemplo, 00. |  |  |
| 7 | Clicar em Criar | Vá apara a tela Administrar mestre de produtos > DADOS BÁSICOS > Descrição e selecione Criar. | A descrição no idioma padrão (por exemplo, inglês) é exibida. |  |
| 8 | Inserir dados de descrição | Na tela Descrições, efetue as seguintes entradas:Idioma: Por exemplo, Alemão.Descrição do produto: <descrição do produto> |  |  |
| 9 | Retornar à tela principal | Selecione a seta para voltar à tela principal. | É exibida a tela Mestre de produtos. |  |
| 10 | Selecionar unidade de medida básica | Vá para Administrar mestre de produtos > DADOS BÁSICOS, e selecione Unidade de medida básica. |  |  |
| 11 | Retornar à tela principal | Selecione a seta para voltar à tela principal. | É exibida a tela Mestre de produtos. |  |
| 12 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, clique em Vendas: Dados organizacionais de vendas 1, Vendas: Dados organizacionais de vendas 2 e Vendas: Dados gerais/dados do centro.Selecione Continuar.Nota Só para a Polônia: selecione também Comércio exterior - dados de exportação para inserir o número de classificação PKWiU. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:CentroOrganização de vendasCanal de DistribuiçãoClique em Continuar.Nota A mensagem do sistema exibe que O material já existe e será ampliado. | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados de vendas | Na tela Material...(produtos comercializáveis), na guia Vendas: organização de vendas 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básicaCentro fornecedor |  |  |
| 6 | Inserir dados de vendas | Na tela Material...(produtos comercializáveis), na guia Vendas: organização de vendas 1, na seção Dados fiscais, efetue a seguinte entrada:Classificação fiscal: 1Nota O valor inserido indica que o material é (geralmente) totalmente tributável.Somente para o Brasil:Na seção Dados fiscais, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: Inserir 1 para material ou 2 para serviços. | A guia Vendas: organização de vendas 2 é exibida. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento efetue as seguintes entradas:Grp.estatísticas mat.Grupo de categorias do itemGrp.class.cont.mat. 01 | A guia Vendas: geral/centro é exibida. |  |
| 8 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Dados gerais, efetue a seguinte entrada:Verificação de disponibilidade: SP |  |  |
| 9 | Inserir dados de vendas | Na guia Vendas: Gerais/do Centro, na seção Dados de expedição (tempos em dias), efetue as seguintes entradas:Grupo transp.: <0001>Grp.carregamento: <0001> |  |  |
| 10 | Inserir dados de vendas | Na seção Parâmetros gerais de centro, efetue a seguinte entrada:Centro de lucro: <Centro de lucro>Nota Para SerialNoProfile, selecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. |  |  |
| Só para a Polônia | Inserir dados de vendas | Só para a Polônia:Na seção Comércio internacional: exportação, efetue a seguinte entrada:Código de controle: por exemplo, 26.70.13.0. | O código PKWiU é atualizado para a Polônia. |  |
| 11 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar as cadeias de distribuição | Na tela Produto, clique na guia Cadeias de distribuição. | A guia Cadeias de distribuição é exibida. |  |
| 4 | Clique em + (adicionar). | Na guia Cadeias de distribuição, clique em + (Adicionar) | A tela Cadeias de distribuição é exibida no modo de edição. |  |
| 5 | Inserir dados de cadeias de distribuição | Na tela Cadeias de distribuição, efetue as seguintes entradas:Na seção DADOS GERAIS - Informação geral:Organização de vendas: <número da organização de vendas>Nota O valor da Unidade organizacional é determinado pelo que é oferecido nas entradas possíveis.Canal de distribuição: Por exemplo, 10.Centro fornecedor: <número do centro>Na seção CRITÉRIOS DE AGRUPAMENTO:Grupo de categorias de item: por exemplo, NORM.Grupo de classificações contábeis: por exemplo, 01 Produtos comercializáveisNa seção IVA:País: <código do país>Categoria de imposto: Por exemplo, TTX1.Classificação fiscal: por exemplo, insira 1 para material ou 2 para serviços.Classificação fiscal: por exemplo, 1 Imposto total ao utilizar a condição de imposto UTXJ para US.Nota A classificação fiscal depende dos requisitos específicos do país ou da região. A classificação fiscal no mestre de materiais e nas tabelas mestre de clientes determinam as entradas da porcentagem.Somente para o Brasil:Na seção Classificação fiscal, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: Inserir 1 para material ou 2 para serviços. |  |  |
| 6 | Retornar à tela principal | Selecione Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto) - dados de compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, selecione Compras e, em seguida, Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue a seguinte entrada:Centro: <número do centro>Clique em Continuar.Nota A mensagem do sistema exibe que O material já existe e será ampliado. | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados de compras | Na tela Material...(produtos comercializáveis), na guia Compras, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: por exemplo, KG.Grupo de compradores: por exemplo, 001.Grupo de mercadorias: por exemplo, L001. |  |  |
| 6 | Inserir dados de compras | Na seçãoOutros dados/dados de fabricante, efetue a seguinte entrada:Tempo de processamento da entrada de mercadorias: por exemplo, 1. |  |  |
| 7 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de compras | Na tela Produto, selecione Compras. | A tela Compras é exibida. |  |
| 4 | Inserir dados de compras | Na tela Compras, efetue as seguintes entradas:Chave de valor de compras: Por exemplo, 1.Status de unidade de medida do pedido variável: AtivoNa seção dos dados de cabeçalho, selecione Editar cabeçalho e efetue as seguintes entradas:Grupo de produtos: Por exemplo, L001. |  |  |
| 5 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, escolha MRP1, MRP2, MRP3 e MRP4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados MRP/de planejamento | Na tela Criar material...(produtos comercializáveis), na guia MRP1, na seção Dados gerais, efetue as seguintes entradas:Tipo de MRP: PDPlanejador MRP: <001>Nota A mensagem do sistema exibe que O material já existe e será ampliado. |  |  |
| 6 | Inserir dados MRP/de planejamento | Na seçãoDados do tamanho do lote, efetue a seguinte entrada:Procedimento de dimensionamento de lotes: <EX> | A ficha MRP 2 é exibida. |  |
| 7 | Inserir dados MRP/de planejamento | Na tela Criar material...(produtos comercializáveis), na guia MRP 2, na seção Planejamento, efetue as seguintes entradas:Prazo de entrega previsto: Por exemplo, 3.Entrada de mercadorias Data de processamento: Por exemplo, 1.Chave de horizontes: Por exemplo, 000. | A ficha MRP 3 é exibida. |  |
| 8 | Inserir dados MRP/de planejamento | Na tela Criar material...(produtos comercializáveis), na ficha MRP 3, na seção Planejamento, efetue as seguintes entradas:Grupo de estratégias: Por exemplo, 40. |  |  |
| 9 | Inserir dados MRP/de planejamento | Na seção Verificação de disponibilidade, efetue as entradas seguintes:Verificação de disponibilidade: por exemplo, EO.Tempo total reposição Por exemplo, 3. | A ficha MRP 4 é exibida. |  |
| 10 | Inserir dados MRP/de planejamento | Na tela Criar material...(produtos comercializáveis), na guia MRP 4, na seção Explosão da lista técnica/necessidades dependentes, efetue as seguintes entradas:Indiv./colet. ind/col. 1 |  |  |
| 11 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique em Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Criar | Na guia Centros, selecione Criar. | A tela Centro é exibida no modo de edição. |  |
| 5 | Inserir dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710Centro de lucro: por exemplo, YB700.Grp.carregamento: Por exemplo, 0001. |  |  |
| 6 | Inserir dados MRP | Vá para a seção Dados MRP > Dados MRP e efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EO.Tipo de MRP: por exemplo, PD.Planejador MRP: Por exemplo, 001. |  |  |
| 7 | Inserir Dados do tamanho do lote | Na seção Dados MRP > Dados do tamanho do lote, efetue a seguinte entrada:Regra para cálculo do tamanho de lotes: por exemplo, EX. |  |  |
| 8 | Inserir dados de suprimento | Vá para a seção Dados MRP > Suprimento e efetue a seguinte entrada:Prazo de entrega previsto: Por exemplo, 3.Tempo de processamento da entrada de mercadorias: Por exemplo, 1. |  |  |
| 9 | Selecione Dados de previsão | Na tela Centro, clique na guia Previsão. | A guia Previsão é exibida. |  |
| 10 | Inserir dados de previsão | Na guia Previsão, efetue a seguinte entrada:Tipo de período: por exemplo, Mensal |  |  |
| 11 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 12 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto) - dados do depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, selecione as seguintes visões:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2Clique em Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as entradas seguintes:Centro: <número do centro>Depósito: <número do depósito>Nota A mensagem do sistema exibe que O material já existe e será ampliado. | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados do depósito | Na tela Criar material...(produtos comercializáveis), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue a seguinte entrada:Número de notas de EM: Por exemplo, 1. | A guia Dds.cen./armazmto.2 é exibida. |  |
| 6 | Confirmar entradas | Na guia Dds.cen./armazmto 2, você não precisa efetuar entradas.Nota Para o campo Perfil do nº série, selecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. |  |  |
| 7 | Salvar os dados | Clique em Salvar. | A tela Dados mestre – Produto é exibida.Seus dados são salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique na guia Centros.Nota Se não houver registro de dados do centro, siga as etapas do capítulo anterior, [Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)](#unique_14) [página ] 15. | A guia Centros é exibida. |  |
| 4 | Selecionar detalhes do centro | Na guia Centros, use o ícone de seta para selecionar os dados de centro criados na etapa anterior. | A tela Centro é exibida. |  |
| 5 | Navegar para o centro: Depósitos | Na tela Centro, vá para Depósitos > Depósitos. |  |  |
| 6 | Clicar em Criar | Vá para Depósitos > Depósitos, e clique em Criar. | A tela Centro – Depósito é exibida no modo de edição. |  |
| 7 | Inserir centro: Dados do depósito | Na tela Depósitos, efetue a seguinte entrada:Depósito: <número do depósito> |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto) - dados contábeis (dados da área de avaliação)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça a você o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar Visões | Na telaSeleção de visões, selecione as seguintes visões:Contabilidade 1Contabilidade 2Clique em Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue a seguinte entrada:Centro: <Centro>Nota São exibidas informações na parte inferior da tela: o material já existe e será ampliado. | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados contábeis | Na tela Criar material...(Produtos comercializáveis), guia Contabilidade 1, seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: <número> |  |  |
| 6 | Inserir dados | Na seçãoPreços e valores, efetue as seguintes entradas:Por Preço unitário: por exemplo, 20Controle de preço: Por exemplo, V | A guia Contabilidade 2 é exibida. |  |
| 7 | Confirmar entradas | Você não precisa efetuar entradas na guia Contabilidade 2. |  |  |
| 8 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | É exibida a tela Dados mestre - produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Clique em Administrar dados mestre do produto(F1602). | O app é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados da área de avaliação | Na visão Produto, escolha a guia Áreas de avaliação. | A guia Áreas de avaliação é exibida. |  |
| 4 | Clicar em Criar | Na seção Áreas de avaliação, selecione Criar. | Avaliação é aberta no modo de edição. |  |
| 5 | Inserir dados da área de avaliação | Na visão Avaliação, efetue as seguintes entradas:Área de avaliação: <Número de área de avaliação>Determinação do controle de preço: 2Classe de avaliação: por exemplo, 3100 |  |  |
| 6 | Inserir dados da área de avaliação atual | Vá para ÁREAS DE AVALIAÇÃO > Avaliação e efetue as seguintes entradas:Preço do estoque: por exemplo, 20Código de controle de preço: Por exemplo, VNota Ao inserir V como o Código de controle de preço, o valor adicionado em Preço do estoque torna-se o Preço médio móvel. Ao inserir S como o Código de controle de preço, o valor adicionado em Preço do estoque torna-se o Preço padrão. |  |  |
| 7 | Retornar à tela principal | Clique em Aplicar para voltar para a visão Produto. | A visão Administrar mestre de produtos é aberta. |  |
| 8 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do produto - Produto configurável e variantes

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados básicos 1Dados básicos 2Classificação |  |  |
| 4 | Inserir dados básicos | Na tela Material (produto acabado), na guia Dados básicos 1, insira a Descrição de material (texto breve) e a Unidade de medida básica.Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 2, marque o campo de seleção Material é configurável.Pressione Enter. | A guia Classificação é exibida e a caixa de diálogo Tipo de classe é exibida. |  |
| 6 | Selecionar Tipo de classe | Na caixa de diálogo Tipo de classe, marque o tipo de classe 300 (variante) e selecione Continuar. | A tela Classificação é exibida. |  |
| 7 | Atribuir classe | Na seção Atribuição, atribua uma classe e pressione Enter. | As características correspondentes são exibidas na seção Atribuição. |  |
| 8 | Selecionar valores da característica | Selecione os valores necessários para as características. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | O material configurável é criado. |  |
| 10 | Criar variante | Para criar uma Variante, abra de novo o bloco Criar material(MM01) novamente e siga as etapas acima para criar um novo material com Dados básicos 1 e Dados básicos 2. |  |  |
| 11 | Criar variante | Na guia Dados básicos 2, vá para Configuração específica do mandante e insira o material configurável previamente criado no campo Material configurável válido para vários centros, clique em Configurar variante e selecione o valor da característica necessário para configurar variantes. | A variante é criada. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Tornar o produto configurável | Na tela Produto, acesse a guia Configuração e marque o campo de seleção Produto é configurável. |  |  |
| 4 | Atribuir classe de variantes | Na tela Produto, acesse a guia Classificação, selecione Clique aqui para atribuir uma classe e, em seguida, selecione uma classe do tipo 300 (variante). | As características da classe atribuída são exibidas. |  |
| 5 | Selecionar características | Selecione os valores da característica necessários para cada característica. |  |  |
| 6 | Acessar a guia Variantes | Na tela Produto, acesse a guia Variantes e selecione Selecionar variantes do produto. | Uma árvore/tabela é exibida com diferentes características. |  |
| 7 | Selecionar características e criar variantes | Selecione a combinação de valores da característica e clique em Aplicar. | As variantes são criadas. |  |
| 8 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Salvar anexos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2.Selecione Continuar. | A tela Criar material (produto acabado) é exibida. |  |
| 4 | Selecionar serviços para objeto | Na barra de ferramentas da aplicação, vá para Serviços para objeto > Criar anexo. | A tela Importar arquivo é exibida. |  |
| 5 | Selecionar Upload. | Na tela Importar arquivo, selecione Carregar. | A tela Carregar arquivo é exibida. |  |
| 6 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 7 | Salvar | Selecione Selecionar e Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Selecione Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar Anexos | Na tela Produto, vá para a guia Anexos. | A guia Anexos é exibida. |  |
| 4 | Clicar em Criar | Na seção Sistema de administração de documentos, selecione Criar. | A tela Carregar arquivo é exibida. |  |
| 5 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 6 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto - Vendas do centro/Dados gerais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01) | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, clique em Dados básicos e Vendas: Dados gerais/dados do centro.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados na guia Dados básicos 1 | Na tela Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição: <Descrição do produto>Unidade básica: Atualizar unidade básica EA, por exemplo, 1 |  |  |
| 6 | Inserir dados | Na seção Dados de expedição (prazos em dias), efetue a seguinte entrada:Grupo de carregamento: <selecione qualquer valor de entradas possíveis> |  |  |
| 7 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique em Administrar dados mestre do produto(F1602) | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique em Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Criar | Na guia Centros, selecione Criar. |  |  |
| 5 | Inserir centros - dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710 |  |  |
| 6 | Inserir dados MRP | Na seção MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir Centro - Vendas | Na seção Vendas, efetue a seguinte entrada:Grupo de carregamento: <selecione nas entradas possíveis> |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Centro/Produção repetitiva

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01) | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões clique em Dados básicos1, MRP 1 e MRP 4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados na guia Dados básicos 1 | Na tela Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição: <Descrição do produto>Unidade básica: Atualizar unidade básica EA, por exemplo, 1 |  |  |
| 6 | Inserir dados MRP 1 | Na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir dados em MRP 4 | Na seção Produção repetitiva/conjunto/estratégia de desdobramento, efetue as seguintes entradas:Produção repetitiva: Marque o campo de seleção.Perfil prod.repetitiva: <selecione qualquer valor de entradas possíveis> |  |  |
| 8 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique em Administrar dados mestre do produto(F1602) | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique em Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Criar | Na guia Centros, selecione Criar. |  |  |
| 5 | Inserir centros - dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710 |  |  |
| 6 | Inserir dados MRP | Na seção MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir dados de produção repetitiva | Na seção Produção repetitiva, efetue as seguintes entradas:Produção repetitiva ativada: Marque o campo de seleção para ativar o campo Perfil produção repetitiva.Perfil produção repetitiva: <selecione qualquer valor de entradas possíveis> | Se você marcar o campo de seleção Produção repetitiva ativada, o campo Perfil produção repetitiva deve se tornar editável.Se você desmarcar o campo de seleção Produção repetitiva ativada, o campo Perfil produção repetitiva deverá ser protegido contra gravação. |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

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
> Flagged while digesting this document, not verified: Document title in extraction is 'Objetivo'; real title is the cover line. Setor industrial M in MM01 steps vs example sector 00 in F1602 step, a minor inconsistency in examples.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bnf-597]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnf-595]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 64,036 chars in the whole document
