---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Produto acabado\" (MDS BNT) (BNT_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese SAP S/4HANA Cloud Public Edition master data test script for creating finished-product (FERT) material masters via MM01 and F1602, dated 02-07-26."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNT_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, material creation, basic data, sales and tax data, mrp planning data, accounting valuation data, storage data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-674
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Produto acabado" (MDS BNT) (BNT_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Produto acabado" – MDS (BNT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894134)

[2 Pré-requisitos 3](#_Toc233894135)

[2.1 Acesso ao sistema 3](#_Toc233894136)

[2.2 Funções 3](#_Toc233894137)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894138)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894139)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233894140)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233894141)

[2.5.2 Setor industrial 5](#_Toc233894142)

[3 Tabela de síntese 6](#_Toc233894143)

[4 Procedimentos de teste 7](#_Toc233894144)

[4.1 Criar dados mestre de produtos - Dados básicos 7](#_Toc233894145)

[4.2 Criar dados mestre de produtos – Dados de vendas / dados do IVA 10](#_Toc233894146)

[4.3 Criar dados mestre de produtos – Dados de planejamento MRP / Dados do centro 14](#_Toc233894147)

[4.4 Criar dados mestre de produtos - Dados do depósito 17](#_Toc233894148)

[4.5 Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação 20](#_Toc233894149)

[4.6 Criar dados mestre do produto - Produto configurável e variantes 22](#_Toc233894150)

[4.7 Criar dados mestre do produto – Salvar anexos 25](#_Toc233894151)

[4.8 Criar dados mestre do produto - Vendas do centro/Dados gerais 27](#_Toc233894152)

[4.9 Criar dados mestre do produto – Centro/Produção repetitiva 29](#_Toc233894153)

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
| Dados MRP/de planejamento (dados do centro) | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante validade, etc. |  | Centro:____________Depósito:__________ |
| Dados contábeis (dados de avaliação) | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Esta seção descreve alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais:

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão só fornece um setor industrial M. Atualmente, este só é visível no SAP GUI.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de produtos – Dados de vendas / dados do IVA](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas (dados do IVA) criados. |
| [Criar dados mestre de produtos – Dados de planejamento MRP / Dados do centro](#unique_13) [página ] 14 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados MRP/de planejamento (dados do centro) criados. |
| [Criar dados mestre de produtos - Dados do depósito](#unique_14) [página ] 17 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados do depósito criados. |
| [Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação](#unique_15) [página ] 20 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados de avaliação) criados. |
| [Criar dados mestre do produto - Produto configurável e variantes](#unique_16) [página ] 22 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Criar produto configurável e variantes. |
| [Criar dados mestre do produto – Salvar anexos](#unique_17) [página ] 25 | Especialista em dados mestre - Dados do produto | Modificar material(MM02)/Administrar dados mestre do produto(F1602) | Salvar anexos para o registro mestre de materiais. |
| [Criar dados mestre do produto - Vendas do centro/Dados gerais](#unique_18) [página ] 27 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |
| [Criar dados mestre do produto – Centro/Produção repetitiva](#unique_19) [página ] 29 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre de produtos - Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas e clique em Selecionar visões:Material: <Número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: FERT | A visão Seleção de visões é exibida. |  |
| 4 | Selecionar Visões | Na visão Selecionar visões, selecione Dados básicos 1 e Dados básicos 2. Clique em Continuar. | A visão Criar material (produto acabado) é exibida. |  |
| 5 | Inserir dados básicos | Na visão Material (produto acabado), guia Dados básicos 1, insira a descrição do material (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: <Unidade de medida básica>Grupo de mercadorias: <grupo de mercadorias>GrpCtgsItemGer.: <GrpCtgsItemGer.> |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas e pressione Enter:Peso bruto: <Peso bruto>Unidade de peso: <Unidade de peso>Peso líquido: <Peso líquido> | A guia Dados básicos 2 é exibida. |  |
| 8 | Inserir dados básicos | Na guia Dados básicos 2, você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a visão Dados mestre - Produto.Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento seguinte caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 3 | Selecionar Criar novo mestre de produtos | Clique em Criar produtos. | A visão Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na visão Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z …Nota Insira aqui qualquer ID alfanumérico externo … (deve começar pelo menos com um caractere). Caso não seja atribuída nenhuma entrada aqui, o sistema atribuirá um ID numérico automaticamente.Para mais informações sobre o número do produto, consulte a seção Tipo de material e intervalos de numeração em Parâmetros principais para a criação de dados.Tipo de produto: FERTGrupo de produtos: por exemplo, L004Unidade básica: por exemplo, UNDescrição: <descrição> |  |  |
| 5 | Clicar em OK | Na visão Administrar mestre de produtos, clique em OK. | A visão Administrar mestre de produtos é aberta. |  |
| 6 | Inserir dados básicos | Vá para Administrar mestre de produtos > DADOS BÁSICOS > Dados básicos e efetue a seguinte entrada:Setor de atividade: por exemplo, 00 |  |  |
| 7 | Ir para a visão Descrições | Vá para a visão Descrições. | A descrição no idioma padrão (inglês, por exemplo) já está preenchida. |  |
| 8 | Clicar em Criar | Na visão DESCRIÇÕES, clique em Criar. | A visão Mestre de produtos - Descrição é exibida.Alguns campos já estão preenchidos. |  |
| 9 | Inserir dados de descrição | Na visão Mestre de produtos - Descrição, efetue as seguintes entradas:Idioma: Por exemplo, AlemãoDescrição do produto: <Descrição do produto> | As descrições podem ser atualizadas em diferentes idiomas. |  |
| 10 | Retornar ao mestre de produtos | Clique na seta "Voltar" para retornar à visão Mestre de produtos. | A visão Mestre de produtos é exibida. |  |
| 11 | Selecionar unidade de medida básica | Na visão Mestre de produtos acesse DADOS BÁSICOS e selecione Unidade de medida básica. | A visão Unidade de medida básica é exibida. |  |
| 12 | Inserir dados de unidade de medida básica | Clique em Mostrar mais e efetue as seguintes entradas para os campos relacionados a Peso:Unidade de peso: por exemplo, KGPeso bruto: por exemplo, 2Peso líquido: por exemplo, 1Nota Caso os campos Peso bruto, Unidade de peso ou Peso líquido não sejam exibidos como campos de entrada, atualize/recarregue a visão. Após atualizar/recarregar, você poderá efetuar as entradas indicadas nestes campos. |  |  |
| 13 | Retornar à tela principal | Clique na seta "Voltar" para retornar à visão Mestre de produtos. | A visão Mestre de produtos é exibida. |  |
| 14 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de produtos – Dados de vendas / dados do IVA

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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: FERTClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, clique em Vendas: Dados organizacionais de vendas 1, Vendas: Dados organizacionais de vendas 2 e Vendas: Dados gerais/dados do centro.Selecione Continuar.Nota Só para a Polônia: para inserir o número de classificação PKWiU, você precisa selecionar também Comércio internacional: exportação. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas e selecione Continuar:Centro: por exemplo, 1710.Organização de vendas: por exemplo, 1710.Canal de distribuição: por exemplo, 10. | A tela Criar material (produto acabado) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados de vendas | Na tela Material (produto acabado), na guia Vendas: organização de vendas 1, insira um valor apropriado para o campo Classificação fiscal. Por exemplo, 1 para totalmente tributável. | A guia Vendas: organização de vendas 2 é exibida.O valor inserido indica que o material é (geralmente) totalmente tributável. |  |
| 6 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Conceitos de agrupamento efetue as seguintes entradas:Grupo de categorias de item <Grupo de categorias de item> | A guia Vendas: geral/centro é exibida. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Dados gerais, efetue a seguinte entrada:Verificação de disponibilidade: por exemplo, EO |  |  |
| 8 | Inserir dados de vendas | Na seção Dados de expedição (prazos em dias), efetue as seguintes entradas:Grupo transp.: por exemplo, 0001.Grp.carregamento: por exemplo, 0001. |  |  |
| 9 | Inserir dados de vendas | Na seção Parâmetros gerais de centro, efetue as seguintes entradas:Centro de lucro: por exemplo, YB110 ou YB111.PerfilNºs série Selecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. | A tela Última visão de dados alcançada é exibida com a mensagem: O processamento será encerrado. Deseja salvar primeiro seus dados para este material?. |  |
| Só para a Polônia | Inserir dados de vendas – somente para a Polônia | Na seção Comércio internacional: exportação, efetue a seguinte entrada:Código de controle: por exemplo, 26.70.13.0. | O código PKWiU é atualizado para a Polônia. |  |
| 10 | Salvar os dados | Na tela Última visão de dados alcançada, selecione Sim. | É exibida a tela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar as cadeias de distribuição | Na tela Mestre de produtos, selecione CADEIAS DE DISTRIBUIÇÃO. | É exibida a tela CADEIAS DE DISTRIBUIÇÃO. |  |
| 4 | Clicar em Criar | Vá para CADEIAS DE DISTRIBUIÇÃO > Cadeias de distribuição e selecione Criar. | A tela Cadeia de distribuição é exibida no modo de edição. |  |
| 5 | Inserir dados de cadeias de distribuição | Na tela Cadeia de distribuição, efetue as seguintes entradas:DADOS GERAIS – Informações geraisOrganização de vendas: <Número da organização de vendas>, por exemplo, 1710Canal de distribuição: por exemplo, 10.Centro fornecedor: <Nº do centro>, por exemplo, 1710CRITÉRIOS DE AGRUPAMENTOGrupo de categorias de item: por exemplo, NORM.Grupo de classificações contábeis: por exemplo, 03 Produtos acabados.IVAPaís: <código do país>, por exemplo, DECategoria de imposto: TTX1Classificação fiscal: Inserir 1 para material ou 2 para serviços.Classificação fiscal: por exemplo, 1 Imposto total ao utilizar a condição de imposto UTXJ para US.Nota A classificação fiscal depende de requisitos de país ou região específicos. A classificação fiscal no mestre de materiais e nas tabelas mestre de clientes determinam as entradas da porcentagem do imposto.Somente para o Brasil:Na seção Classificação fiscal, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: Inserir 1 para material ou 2 para serviços. |  |  |
| 6 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos – Dados de planejamento MRP / Dados do centro

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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: FERTClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, escolha MRP1, MRP2, MRP3 e MRP4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <código do centro>, por exemplo, 1710Depósito: por exemplo, 171A. | A tela Criar material (produto acabado) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados MRP/de planejamento | Na tela Material (produto acabado), na ficha MRP 1, na seção Dados gerais, efetue a entrada seguinte:Grupo de compradores: <grupo de compradores> |  |  |
| 6 | Inserir dados MRP/de planejamento | Na seção Procedimento MRP, efetue as entradas seguintes:Tipo de MRP: por exemplo, PD.Planejador MRP: por exemplo, 001. |  |  |
| 7 | Inserir dados MRP/de planejamento | Na seçãoRegra para cálculo do tamanho de lotes, efetue a seguinte entrada:Regra para cálculo do tamanho de lotes: EX | A ficha MRP 2 é exibida. |  |
| 8 | Inserir dados MRP/de planejamento | Na tela Criar material (produto acabado), na guia MRP 2, efetue entradas com base em suas necessidades ou pelo menos insira valores para os campos obrigatórios. Por exemplo, o tempo de produção interna em dias. | A ficha MRP 3 é exibida. |  |
| 9 | Inserir dados MRP/de planejamento | Na tela Criar material (produto acabado), na guia MRP 3, na seção Planejamento, efetue as entradas seguintes:Grupo de estratégias: por exemplo, 40.Modo de consumo: por exemplo, 2.Int.compens.regress.: <Int.compens.regress.>Int.compens.progres.: <Int.compens.progres.> |  |  |
| 10 | Inserir dados MRP/de planejamento | Na seção Verificação de disponibilidade, efetue as entradas seguintes:Verificação de disponibilidade: por exemplo, EO.Tempo total reposição por exemplo, 3. | A ficha MRP 4 é exibida. |  |
| 11 | Inserir dados MRP/de planejamento | Na tela Criar material (Produto acabado), na guia MRP 4 você não precisa efetuar entradas. | A tela Última visão de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 12 | Salvar | Na tela Última visão de dados alcançada, selecione Sim. | É exibida a tela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Mestre de produtos, selecione CENTROS. | É exibida a tela CENTROS. |  |
| 4 | Clicar em Criar | Na tela CENTROS, selecione Criar. | A tela Centro é exibida no modo de edição. |  |
| 5 | Inserir centros - dados de informações gerais | Vá para Centro > INFORMAÇÃO GERAL e efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710Centro de lucro: por exemplo, YB110 ou YB111. |  |  |
| 6 | Inserir centros - dados MRP | Na tela Mestre de produtos, selecione DADOS MRP.Na seção DADOS MRP > Dados MRP, efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EO.Tipo de MRP: por exemplo, PD.Planejador MRP: por exemplo, 001. |  |  |
| 7 | Inserir centros - dados do tamanho do lote | Na tela DADOS MRP, selecione Dados do tamanho do lote.Na tela Dados do tamanho do lote, efetue a seguinte entrada:Procedimento de cálculo do tamanho do lote: por exemplo, EX. |  |  |
| 8 | Inserir centros - dados de suprimento | Vá para Dados MRP > Suprimento, e efetue a seguinte entrada:Prazo de entrega previsto: por exemplo, 3.Tempo de processamento da entrada de mercadorias: por exemplo, 1. |  |  |
| 9 | Selecionar centros - dados de previsão | Vá para Administrar mestre de produtos > CENTROS e selecione PREVISÃO. | A tela PREVISÃO é exibida. |  |
| 10 | Inserir centros - dados de previsão | Na tela PREVISÃO, efetue as entradas a seguir:Tipo de período: por exemplo, M. |  |  |
| 11 | Retornar à tela principal | Selecione Aplicar para voltar à tela Produto. | É exibida a tela Mestre de produtos. |  |
| 12 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de produtos - Dados do depósito

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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: FERTClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2 | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: por exemplo, 1710.Depósito: por exemplo, 171A. | A tela Criar material (produto acabado) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados do depósito | Na tela Criar material (produto acabado), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue a seguinte entrada:Número de notas de EM: por exemplo, 1. | A guia Dds.cen./armazmto.2 é exibida. |  |
| 6 | Confirmar entradas | Na guia Dds.cen./armazmto 2, você não precisa efetuar entradas.Nota Para o campo SerialNoProfile, selecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. | A tela Última visão de dados alcançada é exibida com a mensagem: O processamento será encerrado. Deseja salvar primeiro seus dados para este material?. |  |
| 7 | Salvar | Na tela Última visão de dados alcançada, selecione Sim. | É exibida a tela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Administrar mestre de produtos, selecione CENTROS.Nota Se não houver registro de dados do centro, siga as etapas da seção anterior: [Criar dados mestre de produtos – Dados de planejamento MRP / Dados do centro](#unique_13) [página ] 14. | É exibida a tela CENTROS. |  |
| 4 | Selecionar detalhes do centro | Na tela CENTROS, use o ícone de seta para selecionar os dados do Centro criados na etapa anterior. | A tela Mestre de produtos – Centro é exibida. |  |
| 5 | Navegar para o centro: Depósito | Na tela Mestre de produtos – Centro, vá para CENTROS > DEPÓSITOS. | A tela Mestre de produtos – CENTRO é exibida no modo de edição. |  |
| 6 | Clicar em Criar | Vá para DEPÓSITOS > Depósitos e selecione Criar. | A tela Centro – Depósito é exibida no modo de edição. |  |
| 7 | Inserir centro: Dados do depósito | Na tela Depósitos, efetue a seguinte entrada:Depósito: <número do depósito>, por exemplo, 171A |  |  |
| 8 | Retornar à tela principal | Selecione Aplicar duas vezes para voltar para a tela Produto. | É exibida a tela Mestre de produtos. |  |
| 9 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação

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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: FERTClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Contabilidade 1Contabilidade 2 | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <código do centro> | A tela Criar material (produto acabado) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados contábeis | Na tela Criar material (produto acabado), na guia Contabilidade 1, na seção Dados de avaliação gerais, efetue a entrada seguinte:Classe de avaliação: 7920 |  |  |
| 6 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Preço padrão: <Preço padrão>Por Preço unitário: Por exemplo, 20.Controle de preço: por exemplo, S. | A guia Contabilidade 2 é exibida. |  |
| 7 | Confirmar entradas | Na guia Contabilidade 2, você não precisa efetuar entradas. | A tela Última visão de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 8 | Salvar os dados | Na tela Última visão de dados alcançada, selecione Sim. | É exibida a tela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados da área de avaliação | Na tela Admin. mestre de produtos, selecione ÁREAS DE AVALIAÇÃO. | A tela ÁREAS DE AVALIAÇÃO é exibida. |  |
| 4 | Clicar em Criar | Na tela ÁREAS DE AVALIAÇÃO, selecione Criar. | A tela ÁREAS DE AVALIAÇÃO é exibida no modo de edição. |  |
| 5 | Inserir dados da área de avaliação | Vá para ÁREAS DE AVALIAÇÃO > Área de Avaliação e efetue as seguintes entradas:Área de avaliação: <Área de avaliação>, por exemplo, 1710Determinação do controle de preço: 2Classe de avaliação: Por exemplo, 7920. |  |  |
| 6 | Inserir dados da área de avaliação atual | Na tela Avaliação, selecione Período atual e efetue as seguintes entradas:Preço médio móvel: Por exemplo, 20.Controle de preço: por exemplo, S. |  |  |
| 7 | Retornar à tela principal | Selecione Aplicar para voltar à tela Produto. | É exibida a tela Mestre de produtos. |  |
| 8 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto - Produto configurável e variantes

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com este procedimento.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 - Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | É aberta uma nova janela exibindo Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: FERTClique em Selecionar visão(ões). | É aberta uma nova janela exibindo a visão Selecionar visão(visões). |  |
| 3 | Selecionar visões | Na janela Marcar visão(ões), selecione as visões seguintes e escolha Continuar:Dados básicos 1Dados básicos 2Classificação |  |  |
| 4 | Inserir dados básicos | Na visão Material (produto acabado), na guia Dados básicos 1, insira a descrição de material (texto breve) e a unidade de medida básica.Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 2, marque o campo de seleção Material é configurável.Pressione Enter. | A guia Classificação é exibida e o popup Tipo de classe é aberto. |  |
| 6 | Selecionar o tipo de classe | No popup Tipo de classe, marque o tipo de classe 300 (variante) e selecione Continuar. | A visão Classificação é exibida. |  |
| 7 | Atribuir classe | Na seção Atribuição, atribua uma classe e pressione Enter. | As características correspondentes são exibidas abaixo da seção Atribuição. |  |
| 8 | Selecionar valores da característica | Selecione os valores necessários das características. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | O material configurável é criado. Agora você tem de criar a variante. |  |
| 10 | Criar variante | Para criar a variante, abra de novo o bloco Criar material(MM01) e siga as etapas acima para criar um novo material com Dados básicos 1 e Dados básicos 2. |  |  |
| 11 | Criar variante | Em Dados básicos 2, acesse a configuração dependente do mandante e insira o material configurável previamente criado no material configurável válido para vários centros, clique em Configurar variante e, em seguida, selecione o valor da característica necessário para configurar variantes. | A variante é criada. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto .Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Tornar o produto configurável | Na visão Produto, acesse a guia Configuração e marque o campo de seleção Produto é configurável. |  |  |
| 4 | Atribuir classe de variantes | Na visão Produto, acesse a guia Classificação e selecione Clique aqui para atribuir uma classe e, em seguida, selecione uma classe do tipo 300 (variante). | As características da classe atribuída serão exibidas. |  |
| 5 | Selecionar características | Selecione os valores da característica necessários para cada característica. |  |  |
| 6 | Acessar a guia Variantes | Na visão Produto, acesse a guia Variantes e selecione Selecionar variantes do produto. | Uma árvore/tabela será exibida com diferentes características. |  |
| 7 | Selecionar características e criar variantes | Selecione a combinação de valores da característica e clique em Aplicar. | As variantes serão criadas. |  |
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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Modificar material

Siga este procedimento caso seu acesso de usuário ofereça a você o app Modificar material(MM02).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Modificar material(MM02). | É exibida a tela Modificar material (1ª tela). |  |
| 2 | Inserir número do material | Efetue a seguinte entrada e clique em Selecionar visões:Número do material: <número do material> | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2.Selecione Continuar. | A tela Modificar material (produto acabado) é exibida. |  |
| 4 | Selecionar serviços para objeto | Na barra de ferramentas da aplicação, vá para Serviços para objeto > Criar anexo. | A tela Importar arquivo é exibida. |  |
| 5 | Selecionar Upload. | Na tela Importar arquivo, selecione Carregar. | A tela Carregar arquivo é exibida. |  |
| 6 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 7 | Salvar | Escolha Selecionar e Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Selecione Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Selecione Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar Anexos | Na tela Produto, vá para a guia Anexos. | A guia Anexos é exibida. |  |
| 4 | Selecionar Upload. | Na seção Sistema de administração de documentos, clique em Carregar. | A tela Carregar arquivo é exibida. |  |
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

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre (produto) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01) | Exibe-se Criar material (primeira tela). |  |
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela) , efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: FERTClique em Seleção de visões. | A tela Seleção de visões é aberta. |  |
| 3 | Selecionar Visões | Na janela Selecionar visões, escolha Dados básicos e Vendas: dados do centro/gerais e selecione continuar. | Níveis organizacionais é exibida |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material... (produto acabado) é exibida. |  |
| 5 | Inserir dados na guia Dados básicos 1 | Na visão Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição : Atualizar descrição para produtoUnidade básica: Atualizar unidade de medida básica "EA", por exemplo 1 |  |  |
| 6 | Inserir dados em vendas: geral/centro | Na seção Dados de expedição (prazos em dias), efetue a seguinte entrada:Grupo de carregamento: selecione qualquer valor de entradas possíveis |  |  |
| 7 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento seguinte caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Clique em Administrar dados mestre do produto(F1602) | O app Administrar dados mestre de produtos (F1602) é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na visão Produto, selecione Centros | A guia Centros é exibida. |  |
| 4 | Clicar em Criar | Na visão Centros, clique em Criar. |  |  |
| 5 | Inserir centros - dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: nº do centro, por exemplo, 1710 |  |  |
| 6 | Inserir dados MRP | Na seção MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND |  |  |
| 7 | Inserir Centro - Vendas | Na seção Vendas efetue as seguintes entradas:Grupo de carregamento: selecione a partir das entradas possíveis |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar para a visão Produto. | A visão Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do produto – Centro/Produção repetitiva

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

Você deve concluir o capítulo anterior, [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01) | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: FERTClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões clique em Dados básicos1, MRP 1 e MRP 4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 5 | Inserir dados na guia Dados básicos 1 | Na tela Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição: <Descrição do produto>Unidade básica: Atualizar unidade básica EA, por exemplo, 1 |  |  |
| 6 | Inserir dados em MRP 1 | Na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir dados em MRP 4 | Na seção Produção repetitiva/conjunto/estratégia de desdobramento, efetue as seguintes entradas:Produção Repetitiva: Marque o campo de seleção.Perfil prod.repetitiva: <selecione qualquer valor de entradas possíveis> |  |  |
| 8 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

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
> Flagged while digesting this document, not verified: Extracted title 'Objetivo' is only the first heading; real title is the cover 'Script de dados mestre'. Steps differ slightly between sections on whether the 'sem entrada' industry-sector field is 'no escuro' vs 'esmaecido' (translation inconsistency).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnt-675]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnt-673]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 60,258 chars in the whole document
