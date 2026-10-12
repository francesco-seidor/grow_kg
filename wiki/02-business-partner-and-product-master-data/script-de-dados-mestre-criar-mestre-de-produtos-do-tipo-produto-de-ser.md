---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-de-ser
title: Script de dados mestre - Criar mestre de produtos do tipo Produto de serviço (31X) (31X_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT, 31X): create service product master via MM01 or F1602 across basic, sales, purchasing, accounting views."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-non-stock-and-service]
aliases: [31X_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Non-Stock Materials and Service Products", service product master, material master data, basic data view, sales data view, purchasing data view, accounting data view, business roles, organizational units, material types]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-308
topic: 02-business-partner-and-product-master-data/product-master-non-stock-and-service
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo Produto de serviço (31X) (31X_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Non-Stock Materials and Service Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo “Produto de serviço” - MDS (31X) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893610)

[2 Pré-requisitos 3](#_Toc233893611)

[2.1 Acesso ao sistema 3](#_Toc233893612)

[2.2 Funções 3](#_Toc233893613)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893614)

[2.4 Dados mestre obrigatórios e operacionais 4](#_Toc233893615)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233893616)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233893617)

[2.5.2 Setor industrial 5](#_Toc233893618)

[3 Tabela de síntese 6](#_Toc233893619)

[4 Procedimentos de teste 7](#_Toc233893620)

[4.1 Criar dados mestre de materiais (produto do serviço) – Dados básicos 7](#_Toc233893621)

[4.2 Criar dados mestre de materiais (produto do serviço) – Dados de vendas (dados do IVA) 9](#_Toc233893622)

[4.3 Criar dados mestre de materiais (produto do serviço) – Dados de compras 13](#_Toc233893623)

[4.4 Criar dados mestre de materiais (produto do serviço) – Dados contábeis (dados da área de avaliação) 15](#_Toc233893624)

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
| Sistema | Acessível via launchpad do SAP Fiori. Seu administrador do sistema fornece a você o URL para acessar os vários apps atribuídos à sua função. |

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
| Dados de vendas | Centro, organização de vendas, canal de distribuição | Dados de imposto, grupo de categorias do item, grupo transp., grupo de carregamento, tempo de preparação da expedição, etc. | Os dados de venda podem existir para toda organização de vendas de sua estrutura empresarial para a qual o registro mestre de materiais seja utilizado. | Centro:____________Organização de vendas:__________Canal de distribuição:__________ |
| Dados de compras | Centro | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material deve ser utilizado em processos de compras. | Centro:__________ |
| Dados contábeis | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e operacionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais.

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
| [Criar dados mestre de materiais (produto do serviço) – Dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de materiais (produto do serviço) – Dados de vendas (dados do IVA)](#unique_12) [página ] 9 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas criados. |
| [Criar dados mestre de materiais (produto do serviço) – Dados de compras](#unique_13) [página ] 13 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de compra criados. |
| [Criar dados mestre de materiais (produto do serviço) – Dados contábeis (dados da área de avaliação)](#unique_14) [página ] 15 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados da área de avaliação) criados. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa do processo que pertence a este item de escopo.

### Criar dados mestre de materiais (produto do serviço) – Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 - Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A visão Criar material(MM01) é exibida. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela)Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: produtos dos serviçosClique em Seleção de visões. | É aberta uma nova janela, Seleção de visões. |  |
| 4 | Selecionar visões | Em Seleção de visões, selecione Dados básicos 1 e, em seguida, Continuar. | Criar material...(produto do serviço) é aberto. |  |
| 5 | Inserir dados básicos | A partir de Material...(produto do serviço), na guia Dados básicos 1, insira uma Descrição do material (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, insira as descrições para o seguinte:Unidade de medida básicaGrupo de materiaisGrpCtgsItemGer. |  |  |
| 7 | Salvar os dados | Na parte inferior direita do display, clique em Salvar para salvar os dados. | Exibe-se Criar material (1ª tela).Os dados básicos são criados e salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | A tela Administrar dados mestre do produto(F1602) é exibida. |  |
| 3 | Selecionar Criar novo mestre de produtos | Na visão Administrar dados mestre de produtos, clique em Criar. | A tela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na 1ª tela Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z …Você insere qualquer ID alfanumérico externo e esse ID deve iniciar com um caracteres alfanumérico ou, se você não fornecer nenhuma entrada, o sistema atribui automaticamente um ID numérico.Para mais informações sobre o número do produto, consulte a seção anterior Tipo de material e intervalos de números.Tipo de produto: SERVGrupo de produtos: por exemplo, P001Unidade básica: por exemplo, HDescrição: qualquer descrição |  |  |
| 5 | Selecionar OK | Na visão Administrar mestre de produtos, selecione OK | A visão Administrar mestre de produtos é aberta. |  |
| 6 | Inserir dados básicos | Em Produto > Informações gerais > Dados básicos, faça a seguinte entrada:Setor de atividade: por exemplo, 00 |  |  |
| 7 | Clicar em Adicionar (+) | Em Produto > Informações gerais > Descrições, selecione + (adicionar). | A visão Mestre de produtos- Descrição é exibida.Alguns campos são exibidos preenchidos com dados da etapa anterior. |  |
| 8 | Inserir dados de descrição | Na visão Descrições, efetue as seguintes entradas:Idioma: por exemplo, AlemãoProduto: <sua descrição> |  |  |
| 9 | Salvar os dados | Clique em Salvar. | É exibida a mensagem do sistema de que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto do serviço) – Dados de vendas (dados do IVA)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre de materiais (serviços). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior, Criar dados mestre de materiais (produto do serviço) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 - Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A visão Criar material(MM01) é exibida. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Nota: se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: SERV produto do serviçoClique em Selecionar visão(ões). | Depois de preencher as entradas, é aberta uma nova janela Marcar visão(ões) |  |
| 4 | Selecionar visões | Na janela Marcar visão(ões), selecione Vendas: dados organizacionais de vendas 1, Vendas: dados organizacionais de vendas 2 e Vendas: dados gerais/do centro e selecione Continuar.Nota Apenas para a Polônia: selecione também Comércio exterior – Dados de exportação para inserir o número de classificação PKWiU. | É exibida uma janela com Níveis organizacionais. |  |
| 5 | Inserir dados dos níveis organizacionais | Em Níveis organizacionais, na seção Nível organizacional, insira as descrições para o seguinte:centroOrganização de vendasCanal de CanalSelecione Continuar.Nota As informações são exibidas na parte inferior da visão: o material já existe e será ampliado. | A visão Criar material…(serviços) é exibida. |  |
| 6 | Inserir dados de vendas | Em Material...(produto do serviço), a partir da guia Vendas: organização de vendas 1, na seção Dados gerais, efetue a seguinte entrada:Unidade de medida básicaCentro fornecedor |  |  |
| 7 | Inserir dados de vendas | Em Material...(produto do serviço), a partir da guia Vendas: organização de vendas 1, na seção Dados de imposto, efetue as seguintes entradasClassificação fiscal: 1Nota O valor inserido indica que o material é (geralmente) totalmente tributável.Somente para o Brasil:Na seção Dados de imposto, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: Inserir 1 para material ou 2 para serviços | Vendas: organização de vendas 2 é exibida |  |
| 8 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento efetue as seguintes entradas:Ger.grp. ctg.itemGrupo de categorias do item | A guia seguinte, Vendas: geral/centro é exibida. |  |
| 9 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Parâmetros gerais do centro, insira os seguintes dados:Centro de lucro |  |  |
| Só para a Polônia | Inserir dados de vendas | Na seção Comércio internacional: exportação, insira os seguintes dados:Código de controle: por exemplo, 41.00.30.0 | O código PKWiU é atualizado para a Polônia. |  |
| 10 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto(F1602) se abre e vários campos de pesquisa são exibidos. |  |
| 3 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 4 | Selecionar as cadeias de distribuição | Na visão Produto, selecione a guia Cadeias de distribuição. | A guia Cadeias de distribuição é exibida. |  |
| 5 | Clicar em Adicionar (+) | Na guia Cadeias de distribuição, clique em + (Adicionar) | A tela Cadeias de distribuição é aberta no modo de edição. |  |
| Não relevante para o Brasil | Insira dados de cadeias de distribuição | Em Cadeias de distribuição, efetue as seguintes entradas:Na seção DADOS GERAIS - Informação geral:Organização de vendas: nº org.vendasNota O valor da unidade organizacional é determinado pelo que é oferecido nas entradas possíveis.Canal de distribuição: por exemplo, 10Centro fornecedor: número do centroNa seção CRITÉRIOS DE AGRUPAMENTO:Grupo de categorias de item: por exemplo, SERVNa seção da visão IVA:País: código do paísCategoria de imposto: por exemplo, TTX1:Classificação fiscal: por exemplo, insira 1 para material ou 2 para serviços. Exemplo de Classificação fiscal: 1 Imposto total ao utilizar a condição de imposto UTXJ para EUA.Nota A classificação fiscal depende dos requisitos específicos do país ou da região. A classificação fiscal no mestre de materiais e nas tabelas mestre de clientes determinam as entradas da porcentagem. |  |  |
| 6 | Retornar à visão principal | Clique em Aplicar para voltar para a visão Produto. | A visão Produto é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto do serviço) – Dados de compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre de materiais (serviços). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criando dados mestre de materiais (produto do serviço) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que tiver salvo as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A visão Criar material(MM01) é exibida. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: SERV produto do serviçoClique em Seleção de visões. | A tela Seleção de visões é aberta. |  |
| 4 | Selecionar visões | Na janela Seleção de visões, clique em Compras e, em seguida, continuar. | É exibido Níveis organizacionais |  |
| 5 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue a entrada seguinte:Centro: número do centroClique em Continuar.Nota É exibida uma mensagem na parte inferior da tela: O material já existe e será ampliado | Criar Material…(serviços) é aberto. |  |
| Não relevante para o Brasil | Inserir dados de compras | Na tela Material (produto do serviço), na guia Compras, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica : por exemplo HGrupo de mercadorias: por exemplo, YBPM02 |  |  |
| 6 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto(F1602) se abre e vários campos de pesquisa são exibidos. |  |
| 3 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 4 | Selecionar dados de compras | Na visão Produto, clique em Compras. | A visão Compras é exibida. |  |
| 5 | Inserir dados de compras | Na visão Compras, efetue as seguintes entradas:Chave do valor de compra: por exemplo, 1 |  |  |
| 6 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais (produto do serviço) – Dados contábeis (dados da área de avaliação)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre de materiais (produto do serviço). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de materiais (produto do serviço) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A visão Criar material(MM01) é exibida. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: SERV produto do serviçoClique em Seleção de visões. | Seleção de visões é aberta. |  |
| 4 | Selecionar visões | Em Seleção de visões, selecione as seguintes visões:Contabilidade 1Clique em Continuar. | A tela Níveis organizacionais é aberta. |  |
| 5 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:centroNota São exibidas informações na parte inferior da tela: o material já existe e será ampliado. | Criar Material…(serviços) é aberto. |  |
| 6 | Inserir dados contábeis | Na tela Criar material...(produto do serviço), na guia Contabilidade 1, na seção Avaliação atual, efetue a seguinte entrada:Classe de avaliação: número |  |  |
| 7 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Por Preço unitário: por exemplo, 1 |  |  |
| 8 | Confirmar entradas (para todos os países/regiões, exceto o Brasil) | Você não precisa efetuar entradas na guia Contabilidade 2. |  |  |
| 9 | Salvar os dados | Na parte inferior do display, clique em Salvar. | A janela Dados mestre – Produto é exibida.Seus dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto(F1602) se abre e vários campos de pesquisa são exibidos. |  |
| 3 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 4 | Selecionar dados da área de avaliação | Na visão Produto, selecione a guia Áreas de avaliação | A guia Áreas de avaliação é exibida. |  |
| 5 | Clicar em Adicionar (+) | Na seção Áreas de avaliação, clique em + (Adicionar). | Avaliação abre-se no Modo de edição. |  |
| Não relevante para o Brasil | Inserir dados da área de avaliação | Na visão Avaliação, efetue as seguintes entradas:Área de avaliação: número de área de avaliaçãoClasse de avaliação: por exemplo, 3200 |  |  |
| 6 | Retornar à tela principal | Clique em Aplicar para voltar para a visão Produto. | A visão Administrar mestre de produtos é aberta. |  |
| 7 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-service-product-mds-3]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31x-307]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31x-309]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-producto-d]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 32,034 chars in the whole document
