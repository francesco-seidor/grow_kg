---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Produto semiacabado\" – MDS (BNS) (BNS_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script: test steps to create semi-finished (HALB) product masters via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNS_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, semi-finished products, basic data views, purchasing data, mrp planning data, storage data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-668
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Produto semiacabado" – MDS (BNS) (BNS_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Produto semiacabado" – MDS (BNS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894062)

[2 Pré-requisitos 3](#_Toc233894063)

[2.1 Acesso ao sistema 3](#_Toc233894064)

[2.2 Funções 3](#_Toc233894065)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894066)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894067)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233894068)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233894069)

[2.5.2 Setor industrial 5](#_Toc233894070)

[3 Tabela de síntese 6](#_Toc233894071)

[4 Procedimentos de teste 7](#_Toc233894072)

[4.1 Criar dados mestre de produtos - Dados básicos 7](#_Toc233894073)

[4.2 Criar dados mestre de produtos - Dados de compra 10](#_Toc233894074)

[4.3 Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro 12](#_Toc233894075)

[4.4 Criar dados mestre de produtos - Dados do depósito 16](#_Toc233894076)

[4.5 Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação 19](#_Toc233894077)

[4.6 Criar dados mestre do produto – Produto configurável e variantes 21](#_Toc233894078)

[4.7 Criar dados mestre do produto – Salvar anexos 24](#_Toc233894079)

[4.8 Criar dados mestre do produto - Vendas do centro/Dados gerais 26](#_Toc233894080)

[4.9 Criar dados mestre do produto – Centro/Produção repetitiva 28](#_Toc233894081)

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
| Dados de compras | Centro | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material deve ser utilizado em processos de compras. | Centro:__________ |
| Dados MRP/de planejamento (dados do centro) | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de cliente.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados contábeis | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais.

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração.

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão só fornece um setor industrial M. Atualmente, este só é visível no SAP GUI.

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de produtos - Dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de produtos - Dados de compra](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de compras (dados do centro) criados. |
| [Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro](#unique_13) [página ] 12 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados MRP/de planejamento criados. |
| [Criar dados mestre de produtos - Dados do depósito](#unique_14) [página ] 16 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados do depósito criados. |
| [Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação](#unique_15) [página ] 19 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados de avaliação) criados. |
| [Criar dados mestre do produto – Produto configurável e variantes](#unique_16) [página ] 21 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Criar produto configurável e variantes. |
| [Criar dados mestre do produto – Salvar anexos](#unique_17) [página ] 24 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Salvar anexos para o registro mestre de materiais. |
| [Criar dados mestre do produto - Vendas do centro/Dados gerais](#unique_18) [página ] 26 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |
| [Criar dados mestre do produto – Centro/Produção repetitiva](#unique_19) [página ] 28 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |

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

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Clique em Seleção de visões. | A visão Seleção de visões é exibida. |  |
| 4 | Selecionar Visões | Na janela Marcar visão(ões), selecione Dados básicos 1 e Dados básicos 2 e escolha Continuar. | A visão Criar material (produto semiacabado) é exibida. |  |
| 5 | Inserir dados básicos | Na tela Material... (produto semiacabado), na guia Dados básicos 1, insira Descrição do material (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básicaGrupo de materiaisGrpCtgsItemGer. |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas e confirme duas vezes com Enter:Peso brutoUnidade de pesoPeso líquidoVá para a guia Dados básicos 2. | A guia Dados básicos 2 é exibida. |  |
| 8 | Inserir dados básicos | Na guia Dados básicos 2, você não precisa efetuar entradas. Confirme com Enter. | É aberta a nova visão Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Em Última visão de dados alcançada, selecione Sim. | É exibida a visão Dados mestre - Produto.Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento seguinte caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | A visão Administrar mestre de produtos é aberta. |  |
| 3 | Selecionar Criar novo mestre de produtos | Na visão Administrar mestre de produtos, clique em Criar produto. | A janela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na visão Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z …nenhum ID alfanumérico externo … (pelo menos este deve começar com um caractere) ou nenhuma entrada; assim o sistema atribui um ID numérico automaticamenteTipo de produto: HALB (produto semiacabado)Grupo de produtos: Por exemplo, L003Unidade básica: por exemplo, UNDescrição: <qualquer descrição> |  |  |
| 5 | Clicar em OK | Na visão Administrar mestre de produtos, clique em OK. | A visão Administrar mestre de produtos é aberta. |  |
| 6 | Inserir dados básicos | Na visão Administrar mestre de produtos > DADOS BÁSICOS > Dados básicos, efetue a seguinte entrada:Divisão: por exemplo, 00 |  |  |
| 7 | Clicar em Criar | Na Visão do produto, vá para a faceta DADOS BÁSICOS > Descrições e selecione Criar | A descrição no idioma padrão (por exemplo, inglês) já se encontra preenchida. |  |
| 8 | Inserir dados de descrição | Na visão Descrições, efetue as seguintes entradas:Idioma: Por exemplo, AlemãoDescrição do produto: <sua descrição> | As descrições podem ser atualizadas em diferentes idiomas. |  |
| 9 | Selecionar unidade de medida básica | Na visão Administrar mestre de produtos > DADOS BÁSICOS, selecione Unidade de medida básica | A visão Unidade de medida básica é exibida. |  |
| 10 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos - Dados de compra

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

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito na seção anterior.

Procedimento: Opção 1 - Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Criar material (visão inicial) é exibida. |  |
| 2 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: nº do materialSetor industrial:MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Clique em Selecionar visão(ões). | A tela Selecionar visão(s) é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visão(s), selecione Compras e, em seguida, Continuar.Nota Apenas para a Polônia: para inserir o código PKWiU, selecione também Comércio exterior - Dados de importação antes de selecionar Continuar. | É exibida a visão Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue a seguinte entrada e selecione Continuar:Centro: <número do centro> | A visão Criar material (produto semiacabado) é exibida. |  |
| 5 | Inserir dados de compras | Na visão Material (produto acabado), na guia Compras, na seção Dados gerais, efetue as seguintes entradas:Grupo de compradores : por exemplo, 001Grupo de mercadorias: por exemplo, L003 |  |  |
| 6 | Inserir dados de compras | Na seçãoOutros dados/dados de fabricante, efetue a seguinte entrada:Tempo de processamento da entrada de mercadorias: por exemplo, 1 | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| Só para a Polônia | Inserir comércio exterior - dados de importação | Para a Polônia, na seção Dados de comércio exterior, insira dados do código PKWiU:Código de controle: por exemplo, 24.10.32.0 | O código PKWiU é atualizado para a Polônia. |  |
| 7 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a janela Dados mestre - produto.Os dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre de produto é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto .Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de compras | Na visão Mestre de produtos, selecione COMPRAS | A visão COMPRAS é exibida. |  |
| 4 | Inserir dados de compras | Na visão COMPRAS, efetuar a seguinte entrada:• Chave do valor de compra: por exemplo, 1 |  |  |
| 5 | Salvar os dados | Clique em Salvar. | A notificação do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro

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

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A visão Criar material (visão inicial) é exibida. |  |
| 2 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:embalagem: Número do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Clique em Seleção de visões. | A visão Seleção de visões é exibida. |  |
| 3 | Clicar em Visões | Na janela Selecionar visões, selecione MRP1, MRP2, MRP3 e MRP4 e clique em Continuar. | A visão Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:CentroDepósito | A visão Criar material (produto semiacabado) é exibida. |  |
| 5 | Inserir dados MRP/de planejamento | Na visão Material (produto semiacabado), na guia MRP 1, na seção Dados gerais, efetue as seguintes entradas:Tipo de MRP: PDHorizonte de planejamento fixoPlanejador MRP: 001 | Você chama a seguinte mensagem de sistema na parte inferior da visão: O material já existe e será ampliado. | . |
| 6 | Inserir dados MRP/de planejamento | Na seçãoRegra para cálculo do tamanho de lotes, efetue a seguinte entrada:Regra para cálculo do tamanho de lotes: EX | A visão MRP 2 é exibida. |  |
| 7 | Inserir dados MRP/de planejamento | Na visão Criar material (produto semiacabado), na guia MRP 2, na seção Suprimento, efetue as seguintes entradas:Tipo de suprimentoDepósito de produção |  |  |
| 8 | Inserir dados MRP/de planejamento | Na seção Programação, efetue as seguintes entradas:Fabricação própriaPrazo de entrega planejadoTempo de processamento da entrada de mercadoriasChave de prazos | A visão MRP 3 é exibida. |  |
| 9 | Inserir dados MRP/de planejamento | Na visão Criar material (produto semiacabado), na guia MRP 3, na seção Planejamento, efetue as seguintes entradas:Grupo de estratégiasModo de consumoInt.compens.regress.Int.compens.progres. |  |  |
| 10 | Inserir dados MRP/de planejamento | Na seção Verificação de disponibilidade, efetue as seguintes entradas:Verificação de disponibilidadeTempo total reposição | A visão MRP 4 é exibida. |  |
| 11 | Inserir dados MRP/de planejamento | Nota Para o item de escopo Subcontratação – BMY, você precisa atualizar o campo Versões de produção para garantir a funcionalidade correta.Na visão Criar material (produto semiacabado), na guia MRP 4, na seção Explosão lista técnica/necessidades dependentes, efetue a seguinte entrada:Indiv./colet. | A nova janela Última visão de dados acessada se abre com a mensagem: O processamento será encerrado. Deseja salvar primeiro seus dados para este material? |  |
| 12 | Salvar os dados | Na janela Última visão de dados alcançada, clique em Sim. | A visão Dados mestre – Produto é produto.Seus dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na visão Mestre de produtos, selecione CENTROS. | A visão CENTROS é exibida. |  |
| 4 | Clicar em Criar | Na visão CENTROS, clique em Criar. | A visão Centros é aberta no modo de edição. |  |
| 5 | Inserir centros - dados de informações gerais | Na visão Centro > INFORMAÇÕES GERAIS, efetue as seguintes entradas:Centro: <número do centro>Centro de lucro: por exemplo, YB110 ou YB111Grp.carga: por exemplo, 0001 | A visão Criar material (produto semiacabado) é exibida. |  |
| 6 | Inserir centros - dados MRP | Nota Para o item de escopo Subcontratação – BMY, você também precisa atualizar o campo Grupo de estratégias.Na visão Mestre de produtos, selecione DADOS MRP.Na visão DADOS MRP, clique em Dados MRP e efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EOPrazo de entrega previsto: por exemplo, 3Tempo de processamento da entrada de mercadorias: por exemplo, 1Tipo MRP: por exemplo, PD MRPPlanejador MRP: por exemplo, 001 |  |  |
| 7 | Inserir centros - dados do tamanho do lote | Na visão DADOS MRP, selecione Dados do tamanho do lote.Na visão Dados do tamanho do lote, efetue a seguinte entrada:Procedimento de dimensionamento de lotes: por exemplo, EX |  |  |
| 8 | Inserir centros - dados de suprimento | Na seção Dados MRP > Suprimento, efetue a seguinte entrada:● Prazo de entrega previsto: por exemplo, 3Tempo de processamento da entrada de mercadorias: por exemplo, 1 |  |  |
| 9 | Selecionar centros - dados de previsão | Na visão Administrar mestre de produtos - CENTROS, selecione PREVISÃO. | A visão Centro - PREVISÃO é exibida. |  |
| 10 | Inserir centros - dados de previsão | Na visão PREVISÃO, efetue as seguintes entradas:Tipo de período: por exemplo, M |  |  |
| 11 | Retornar à visão principal | Clique em Aplicar para voltar para a visão Produto. | Volte para a visão Mestre de produtos. |  |
| 12 | Salvar os dados | Clique em Salvar. | O sistema exibe a notificação de que o objeto foi salvo. |  |

### Criar dados mestre de produtos - Dados do depósito

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

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito na seção anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | Criar material (visão inicial) é exibida. |  |
| 2 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Clique em Seleção de visões. | A visão Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Marcar visão(ões), selecione as visões seguintes e escolha Continuar:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2 | É exibida a visão Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | É aberta uma nova janela exibindo a visão Criar material (produto semiacabado).Na parte inferior da visão é exibida a seguinte mensagem do sistema: o material já existe e será ampliado. |  |
| 5 | Inserir dados do depósito | Na visão Criar material (produto semiacabado), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue a seguinte entrada e confirme com Enter:Número de notas de EM: por exemplo, 1 | A guia Dds.cen./armazmto.2 é exibida. |  |
| 6 | Confirmar entradas | Na guia Dds.cen./armazmto 2, na seção Parâmetros gerais de centro, efetue as seguintes entradas:Centro de lucro: por exemplo, YB110 ou YB111PerfilNºs sérieSelecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. | É aberta uma nova janela Última visão de dados alcançada com a seguinte mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 7 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a visão Dados mestre - Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento seguinte caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre de produto é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na visão Administrar mestre de produtos, selecione CENTROSNota Se você ainda não adicionou um registro de dados do centro, siga as etapas no procedimento anterior Criar dados mestre de produtos - dados de planejamento MRP/dados do centro. | A visão CENTROS é exibida. |  |
| 4 | Selecionar detalhes do centro | Na visão CENTROS, utilize o a seta direita para selecionar os dados de centro criados no procedimento anterior. | A visão Centro do mestre de produtos é exibida. |  |
| 5 | Navegar para o centro: Depósito | Na visão CENTROS, navegue para CENTROS > DEPÓSITO | A visão CENTROS é aberta no modo de edição. |  |
| 6 | Clicar em Criar | Na visão CENTROS > DEPÓSITOS > Depósitos, selecione Criar | Avisão Depósito é aberta no modo de edição. |  |
| 7 | Inserir centro: Dados do depósito | Na visão Depósito, efetue as seguintes entradas:Depósito: <número do depósito> | A visão Novo registro - Depósito é exibida. |  |
| 8 | Retornar à visão principal | Selecione duas vezes a seta para voltar para Mestre de produtos | Volte para a visão Mestre de produtos. |  |
| 9 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação

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

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | Criar material (visão inicial) é exibida. |  |
| 2 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Clique em Seleção de visões. | A visão Seleção de visões é exibida. |  |
| 3 | Selecionar Visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Contabilidade 1Contabilidade 2 | É exibida a visão Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro | Abre-se uma nova janela exibindo a visão Criar material (produto semiacabado).Na parte inferior da visão é exibida a seguinte mensagem do sistema: O material já existe e será ampliado | . |
| 5 | Inserir dados contábeis | Na visão Criar material (produto semiacabado), na guia Contabilidade 1, na seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: por exemplo, 7900 |  |  |
| 6 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Preço padrãoPor Preço unitário: por exemplo, 20Ctrl. prç.: por exemplo, SPara confirmar suas entradas, pressione Enter duas vezes. | A guia Contabilidade 2 é exibida. |  |
| 7 | Confirmar entradas | Na guia Contabilidade 2, você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 8 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a janela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento seguinte caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre de produto é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados da área de avaliação | Na visão Mestre de produtos, selecione ÁREA DE AVALIAÇÃO | A área da visão ÁREA DE AVALIAÇÃO é exibida. |  |
| 4 | Clicar em Criar | Na seção da visão Novo mestre de produtos - ÁREA DE AVALIAÇÃO, selecione Criar. | A visão Mestre de produtos - Avaliação é aberta no modo de edição. |  |
| 5 | Inserir dados da área de avaliação | Na visão Novo mestre de produtos - avaliação, efetue as seguintes entradas:Área de avaliação: <número>Determinação do controle de preço: por exemplo, 2Nota Somente para Brasil: Determinação do preço para o Brasil deve ser 3, para princípios contábeis de custos para Brasil.Classe de avaliação: <número>, por exemplo, 3100 |  |  |
| 6 | Inserir dados da área de avaliação atual | Na visão ÁREAS DE AVALIAÇÃO > AVALIAÇÃO, selecione Período atual... e efetue as seguintes entradas:Preço médio móvel: por exemplo, 20Código de controle de preço: por exemplo, S |  |  |
| 7 | Retornar à visão principal | Clique em Aplicar para voltar para a visão Produto. | Volte para a visão principal Mestre de produtos. |  |
| 8 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Produto configurável e variantes

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
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <Número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALB (produto semiacabado)Escolha Selecionar visões. | É aberta uma nova janela exibindo a visão Selecionar visão(visões). |  |
| 3 | Selecionar visões | Na janela Marcar visão(ões), selecione as visões seguintes e escolha Continuar:Dados básicos 1Dados básicos 2Classificação |  |  |
| 4 | Inserir dados básicos | Na visão Material (produto acabado), na guia Dados básicos 1, insira a descrição de material (texto breve) e a unidade de medida básica.Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 2, marque o campo de seleção Material é configurável.Pressione Enter. | A guia Classificação é exibida e o popup Tipo de classe é aberto. |  |
| 6 | Selecionar o tipo de classe | Na caixa de diálogo Tipo de classe, marque o tipo de classe 300 (variante) e selecione Continuar. | A visão Classificação é exibida. |  |
| 7 | Atribuir classe | Na seção Atribuição, atribua uma classe e pressione Enter. | As características correspondentes são exibidas abaixo da seção Atribuição. |  |
| 8 | Selecionar valores da característica | Selecione os valores necessários das características. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | O material configurável é criado. Agora você deve criar a variante. |  |
| 10 | Criar variante | Para criar a variante, abra de novo o bloco Criar material e siga as etapas acima descritas para criar um material novo com Dados básicos 1 e Dados básicos 2. |  |  |
| 11 | Criar variante | Em Dados básicos 2, vá para a Configuração específica do cliente e insira o material configurável previamente criado em Material configurável válido para vários centros. Selecione Configurar variante e, em seguida, selecione os valores de características necessários para a configuração de variantes. | A variante é criada. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre de produto é aberto e são exibidos vários campos de pesquisa. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que irá navegar você para a visão Produto.Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Tornar o produto configurável | Na visão Produto, acesse a guia Configuração e marque o campo de seleção Produto é configurável. |  |  |
| 4 | Atribuir classe de variantes | Na visão Produto, vá para a guia Classificação e selecione Clique aqui para atribuir uma classe. Em seguida, selecione uma classe do tipo 300 (variante). | As características da classe atribuída são exibidas. |  |
| 5 | Selecionar características | Selecione os valores da característica necessários para cada característica. |  |  |
| 6 | Acessar a guia Variantes | Na visão Produto, acesse a guia Variantes e selecione Selecionar variantes do produto | Uma árvore/tabela é exibida com diferentes características. |  |
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

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com este procedimento.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | É aberta uma nova janela exibindo Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), selecione no menu Mais Material > Modificar > Imediatamente e efetue as seguintes entradas:Material: nº do materialSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro.Tipo de material: HALB (produto semiacabado)Clique em Seleção de visões. | É aberta uma nova janela exibindo a visão Seleção de visões. |  |
| 3 | Selecionar Visões | Na janela Marcar visão(ões), selecione Dados básicos 1 e Dados básicos 2 e escolha Continuar. | A visão Criar material (produto acabado) é exibida. |  |
| 4 | Selecionar serviços para objeto | Na barra de ferramentas da aplicação, clique em Serviços para objeto > Criar anexo. | A janela Importar arquivo é aberta. |  |
| 5 | Selecionar Upload. | Na janela Importar arquivo, selecione o botão Upload. | Uma janela Upload de arquivo é aberta. |  |
| 6 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 7 | Salvar | Selecione Selecionar e Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto na lista que levará você para a visão Produto.Clique em Editar. | O produto é exibido em modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar Anexos | Na visão Produto, acesse a guia Anexos. | A visão Anexos é exibida. |  |
| 4 | Clicar em Criar | Na seção Sistema de administração de documentos, selecione Criar. | Uma janela Upload de arquivo é aberta. |  |
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
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela) , efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALBClique em Seleção de visões. | A tela Seleção de visões é aberta. |  |
| 3 | Selecionar Visões | Na janela Selecionar visões, escolha Dados básicos e Vendas: dados do centro/gerais e selecione continuar. | Níveis organizacionais é exibida |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material…(Produtos comercializáveis) é aberta. |  |
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

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre (produto) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01) | Exibe-se Criar material (primeira tela). |  |
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela) , efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: HALBClique em Seleção de visões. | A tela Seleção de visões é aberta. |  |
| 3 | Selecionar Visões | Na janela Selecionar visões selecione Dados básicos1, MRP 1 e MRP 4 e escolha Continuar. | Níveis organizacionais é exibida |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material…(Produtos comercializáveis) é aberta. |  |
| 5 | Inserir dados na guia Dados básicos 1 | Na visão Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição : Atualizar descrição para produtoUnidade básica: Atualizar unidade de medida básica "EA", por exemplo 1 |  |  |
| 6 | Inserir dados em MRP 1 | Na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: Atualizar tipo de MRP “ND” por exemplo |  |  |
| 7 | Inserir dados em MRP 4 | Na seção Produção repetitiva/montagem/estratégia de desdobramento, efetue a seguinte entrada:Produção repetitiva: Marque o campo de seleçãoPerfil prod.repetitiva: selecione qualquer valor de entradas possíveis |  |  |
| 8 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

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
| 7 | Inserir dados de produção repetitiva | Na seção Produção repetitiva, efetue as seguintes entradas:Produção repetitiva ativada: marque o campo de seleção para ativar o campo Perfil produção repetitivaPerfil produção repetitiva: selecione qualquer valor de entradas possíveis | Ao marcar o campo de seleção Produção repetitiva ativada , o campo Perfil produção repetitiva deve se tornar editável.Ao desmarcar o campo de seleção Produção repetitiva ativada, o campo Perfil de produção repetitiva deve ser somente exibição. |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar para a visão Produto. | A visão Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

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
> Flagged while digesting this document, not verified: Document title in metadata is 'Objetivo' while the cover title is the master data script; the step sections contain template placeholders (<X.XX>) and some typos (e.g. 'Material (produto acabado)' used for HALB semi-finished product).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-669]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-sap-s-4hana-cloud-public-edition-2608-japanese-667]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 59,104 chars in the whole document
