---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Matéria-prima\" – MDS (BNR) (BNR_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese (Brazil) SAP S/4HANA Cloud Public Edition test script for creating raw-material (ROH) product master data via MM01 and F1602, by data view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNR_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, material master creation, basic data, purchasing data, mrp planning data, storage data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-662
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Matéria-prima" – MDS (BNR) (BNR_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Matéria-prima" – MDS (BNR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894083)

[2 Pré-requisitos 3](#_Toc233894084)

[2.1 Acesso ao sistema 3](#_Toc233894085)

[2.2 Funções 3](#_Toc233894086)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894087)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894088)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233894089)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233894090)

[2.5.2 Setor industrial 5](#_Toc233894091)

[3 Tabela de síntese 6](#_Toc233894092)

[4 Procedimentos de teste 7](#_Toc233894093)

[4.1 Criar dados mestre de materiais - Dados básicos 7](#_Toc233894094)

[4.2 Criar dados mestre de materiais - Dados de compra 10](#_Toc233894095)

[4.3 Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro) 12](#_Toc233894096)

[4.4 Criar dados mestre de materiais - Dados do depósito 16](#_Toc233894097)

[4.5 Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação) 18](#_Toc233894098)

[4.6 Criar dados mestre do produto - Produto configurável e variantes 21](#_Toc233894099)

[4.7 Criar dados mestre do produto – Salvar anexos 25](#_Toc233894100)

[4.8 Criar dados mestre do produto - Vendas do centro/Dados gerais 27](#_Toc233894101)

[4.9 Criar dados mestre do produto – Centro/Produção repetitiva 29](#_Toc233894102)

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
| Dados MRP/de planejamento | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante prateleira, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de cliente.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito | Centro:____________Depósito:__________ |
| Dados contábeis | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
|  |  | Opcional |  |
|  |  | Obrigatório |  |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais:

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão só fornece um setor industrial M.

|  |
| --- |
| Nota Atualmente, isto só é visível no SAP GUI. |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Os dados mestre de material básico são criados. |
| [Criar dados mestre de materiais - Dados de compra](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Os dados mestre de compras são criados. |
| [Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)](#unique_13) [página ] 12 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Os dados mestre do planejamento MRP são criados. |
| [Criar dados mestre de materiais - Dados do depósito](#unique_14) [página ] 16 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Os dados mestre do depósito são criados |
| [Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação)](#unique_15) [página ] 18 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Os dados mestre contábeis são criados. |
| [Criar dados mestre do produto - Produto configurável e variantes](#unique_16) [página ] 21 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) ou Modificar material(MM02) se necessário | O produto configurável e as variantes são criados. |
| [Criar dados mestre do produto – Salvar anexos](#unique_17) [página ] 25 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) | Salvar anexos para o registro mestre de Material. |
| [Criar dados mestre do produto - Vendas do centro/Dados gerais](#unique_18) [página ] 27 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |
| [Criar dados mestre do produto – Centro/Produção repetitiva](#unique_19) [página ] 29 | Especialista em dados mestre - Dados do produto | Criar material(MM01)/Administrar dados mestre do produto(F1602) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre de materiais - Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | O launchpad do SAP Fiori é exibido.Nota Efetuar login via launchpad só é relevante se WebGUI for utilizado. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 4 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2.Selecione Continuar. | A tela Criar material (matérias-primas) é exibida. |  |
| 5 | Inserir dados básicos | Na tela Material ... (matérias-primas), na guia Dados básicos 1, insira a descrição no campo Descrição. |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: <Unidade de medida básica>Grupo de mercadorias: <grupo de mercadorias>GrpCtgsItemGer.: <GrpCtgsItemGer.> |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas:Peso bruto: <peso bruto>Unidade de peso: <Unidade de peso>Peso líquido: <peso líquido>Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 8 | Inserir dados básicos | Na guia Dados básicos 2, você não precisa efetuar nenhuma entrada. | A tela Última tela de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Na tela Última tela de dados alcançada, clique em Sim. | A tela Dados mestre – Produto é exibida.Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | No catálogo Mestre de produtos, clique em Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 3 | Clicar em Criar | Na tela Administrar dados mestre do produto, selecione Criar. | A tela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir campos obrigatórios | Na tela Criar registro de dados mestre, efetue as seguintes entradas e selecione OK:Número do produto: por exemplo, Z ou qualquer outro ID alfanumérico externo. Ele deve começar com um caractere ou nenhuma entrada e então o sistema atribuirá um ID numérico automaticamente.Nota Para obter mais informações sobre a criação do número do produto, consulte o capítulo anterior [Tipo de material e intervalos de numeração](#unique_8) [página ] 5.Tipo de produto: ROHGrupo de produtos: Por exemplo, L002.Unidade básica: por exemplo, PC.Descrição: <qualquer descrição> |  |  |
| 5 | Retornar à tela principal | Volte para a tela Administrar mestre de produtos. | A tela Administrar mestre de produtos é aberta. |  |
| 6 | Inserir dados básicos | Vá para Administrar mestre de produtos > DADOS BÁSICOS > Dados básicos e efetue a seguinte entrada:Setor de atividade: Por exemplo, 00. |  |  |
| 7 | Adicionar uma descrição | Vá para Administrar mestre de produtos > DADOS BÁSICOS > Descrições e clique em Criar. | A descrição no idioma padrão (por exemplo, inglês) é exibida. |  |
| 8 | Inserir dados de descrição | Na tela Descrição, efetue as seguintes entradas:Idioma: Por exemplo, Alemão.Descrição do produto: <descrição do produto> |  |  |
| 9 | Retornar à tela principal | Selecione a seta para voltar à tela principal. | É exibida a tela Mestre de produtos. |  |
| 10 | Selecionar unidade de medida básica | Vá para Informações gerais > DADOS BÁSICOS e escolha Unidade de medida básica. | A tela Unidade de medida básica é exibida. |  |
| 11 | Salvar os dados | Clique em Criar. | A mensagem do sistema Registro dados mestre criado é exibida e indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais - Dados de compra

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você completou e salvou os dados básicos para o material, como descrito na seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, selecione Compras e, em seguida, Continuar.Nota Só para a Polônia: para inserir o código PKWiU, selecione também Comércio exterior - Dados de importação antes de selecionar Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Níveis organizacionais, na seção Nível organizacional, efetue a seguinte entrada e selecione Continuar:Centro: <código do centro> | A tela Criar material (matérias-primas) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados de compras | Na tela Material (matérias-primas), na guia Compras, na seção Dados gerais, efetue as seguintes entradas:Grupo de compradores: <nº do grupo de compradores>Grupo de mercadorias: Por exemplo, L002. |  |  |
| 6 | Inserir dados de compras | Na seçãoOutros dados/dados de fabricante, efetue a seguinte entrada:Tempo de processamento da entrada de mercadorias: Por exemplo, 1. | A tela Última tela de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| Só para a Polônia | Inserir comércio exterior - dados de importação | Só para a Polônia: na seção Dados de comércio exterior, insira dados do código PKWiU:Código de controle: por exemplo, 24.10.32.0. | O código PKWiU é atualizado para a Polônia. |  |
| 7 | Salvar os dados | Na tela Última tela de dados alcançada, clique em Sim. | A tela Dados mestre – Produto é exibida.Seus dados são salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione na lista Produto (original), que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de compras | Na tela Mestre de produtos, escolha Compras. | A tela Compras é exibida. |  |
| 4 | Editar cabeçalho | Escolha Editar cabeçalho na parte superior da tela e efetue a seguinte entrada:Grupo de produtos: Por exemplo, A001. | A tela Editar cabeçalho é exibida. |  |
| 5 | Inserir dados de compras | Na tela Compras, efetue a seguinte entrada:Chave de valor de compras: Por exemplo, 1. |  |  |
| 6 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você preencheu os dados para o material, como descrito na seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7, e concluiu e salvou os dados mestre de compra.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, escolha MRP1, MRP2, MRP3 e MRP4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: Por exemplo, 1710.Depósito: Por exemplo, 171C. | A tela Criar material (matérias-primas) é exibida. |  |
| 5 | Inserir dados MRP/de planejamento | Na tela Material (matérias-primas), na ficha MRP 1, na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, PD.Planejador MRP: Por exemplo, 001. | A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 6 | Inserir dados MRP/de planejamento | Na seçãoDados do tamanho do lote, efetue a seguinte entrada:Procedimento de dimensionamento de lotes: por exemplo, EX. | A ficha MRP 2 é exibida. |  |
| 7 | Inserir dados MRP/de planejamento | Na tela Criar material (matérias-primas), na ficha MRP 2, na seção Suprimento, efetue as seguintes entradas:Tipo de suprimento: por exemplo, FDepósito da produçãoDepósito para supr. Data de |  |  |
| 8 | Inserir dados MRP/de planejamento | Na seção Programação, efetue as seguintes entradas:Prazo de entrega planejado: Por exemplo, 3.Entrada de mercadorias Data de processamento: Por exemplo, 1.Chave de horizontes: Por exemplo, 000. | A ficha MRP 3 é exibida. |  |
| 9 | Inserir dados MRP/de planejamento | Na tela Criar material (matérias-primas), na guia MRP 3, na seção Verificação de disponibilidade, efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EO.Tempo Reposição total: Por exemplo, 3. | A ficha MRP 4 é exibida. |  |
| 10 | Inserir dados MRP/de planejamento | Na tela Criar material (matérias-primas), na guia MRP 4, na seção Explosão lista técnica/Necessidades depend., efetue a seguinte entrada:Necessidades ind/col. 2 | A tela Última tela de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 11 | Salvar os dados | Na tela Última tela de dados alcançada, clique em Sim. | A tela Dados mestre – Produto é exibida.Seus dados são salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Escolher centros | Na tela Mestre de produtos, selecione CENTROS. | É exibida a tela CENTROS. |  |
| 4 | Clicar em Criar | Na seção Centros, selecione Criar. | A tela Centros é exibida no modo de edição. |  |
| 5 | Inserir centros - dados de informações gerais | Na tela Centro - Informações gerais, efetue as seguintes entradas:Centro: <número do centro>Centro de lucro: por exemplo, YB110 ou YB111.Na seção Vendas, efetue a seguinte entrada:Grupo de carregamento: Por exemplo, 0001. |  |  |
| 6 | Inserir centros - dados MRP | Na tela Dados MRP, efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EO.Prazo de entrega previsto: Por exemplo, 3.Tempo de processamento da entrada de mercadorias: Por exemplo, 1.Tipo de MRP: por exemplo, PD.Planejador MRP: Por exemplo, 001. |  |  |
| 7 | Inserir centros - dados do tamanho do lote | Na tela DADOS MRP, selecione Dados do tamanho do lote.Na tela Dados do tamanho do lote, efetue a seguinte entrada:Procedimento de cálculo do tamanho do lote: por exemplo, EX. |  |  |
| 8 | Inserir centros - dados de suprimento | Vá para Dados MRP > Suprimento, e efetue a seguinte entrada:Prazo de entrega previsto: Por exemplo, 3.Tempo de processamento da entrada de mercadorias: Por exemplo, 1. |  |  |
| 9 | Selecionar Centros - Previsão | Na tela Mestre de produtos - CENTROS, selecione PREVISÃO. | A tela Centro - PREVISÃO é exibida. |  |
| 10 | Inserir dados de previsão | Na tela PREVISÃO, efetue a entrada a seguir:Tipo de período: por exemplo, M. |  |  |
| 11 | Retornar à tela principal | Clique em Aplicar. | A tela Administrar mestre de produtos é aberta. |  |
| 12 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais - Dados do depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você preencheu os dados para o material como descrito na seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 e concluiu e salvou os dados MRP/de planejamento.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2 |  |  |
| 4 | Inserir dados dos níveis organizacionais | Clique em Níveis organizacion. na parte superior da telaNa tela Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: <código do centro>Depósito: <número do depósito> | A tela Criar material (matérias-primas) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados do depósito | Na tela Criar material (matéria-prima), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue a seguinte entrada:Número de notas de EM: Por exemplo, 1.Pressione Enter para ir à próxima tela. | A guia Dds.cen./armazmto.2 é exibida. |  |
| 6 | Confirmar entradas | Na guia Dds.cen./armazmto 2, na seção Parâmetros gerais de centro, efetue as seguintes entradas:Centro de lucro: <Centro de lucro>Perfil do nº série: <perfil do número de série>Selecione um perfil do número de série válido que tenha sido atribuído com a categoria de equipamento adequada para o seu negócio. | A última tela de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 7 | Salvar os dados | Na tela Última tela de dados alcançada, clique em Sim. | A tela Dados mestre – Produto é exibida.Seus dados são salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Escolher centros | Na tela Administrar mestre de produtos, selecione CENTROS.Nota Um registro de dados do centro já deve ter sido criado. Se este registro não estiver disponível, siga as etapas da seção anterior [Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)](#unique_13) [página ] 12. | É exibida a tela CENTROS. |  |
| 4 | Selecionar detalhes do centro | Na seção Mestre de produtos - CENTROS, clique no ícone da seta para os dados do centro criados na seção anterior [Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)](#unique_13) [página ] 12. | É exibida a tela Centro do mestre de produtos. |  |
| 5 | Navegar para o centro: Depósito | Na tela Mestre de produtos – CENTROS, vá para CENTROS > DEPÓSITO. | A tela Mestre de produtos – CENTROS é exibida no modo de edição. |  |
| 6 | Clicar em Criar | Vá para CENTROS > DEPÓSITO > Depósito e selecione Criar. | A tela Centro – Depósito é exibida no modo de edição. |  |
| 7 | Inserir centro: Dados do depósito | Na tela Depósito, efetue a seguinte entrada:Depósito: <número do depósito> | A visão Novo registro - Depósito é exibida. |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Administrar mestre de produtos é aberta. |  |
| 9 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você preencheu os dados para o material como descrito na seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 e concluiu e salvou os dados do depósito.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Contabilidade 1Contabilidade 2 | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue a seguinte entrada:Centro: <Centro> | A tela Criar material (matérias-primas) é exibida.A mensagem do sistema exibe que O material já existe e será ampliado. |  |
| 5 | Inserir dados contábeis | Na tela Criar material.(matérias-primas), na guia Contabilidade 1, na seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: 3000 |  |  |
| 6 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Por Preço unitário: Por exemplo, 20.Controle de preço: <V> | A guia Contabilidade 2 é exibida. |  |
| 7 | Confirmar entradas | Na guia Contabilidade 2, você não precisa efetuar entradas. | A tela Última tela de dados alcançada é exibida com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 8 | Salvar os dados | Na tela Última tela de dados alcançada, clique em Sim. | A tela Dados mestre – Produto é exibida.Seus dados são salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar áreas de avaliação | Na tela Admin. mestre de produtos, selecione ÁREAS DE AVALIAÇÃO. | A tela ÁREAS DE AVALIAÇÃO é exibida. |  |
| 4 | Clicar em Criar | Na tela ÁREAS DE AVALIAÇÃO, selecione Criar. | A tela Novo registro - Área de avaliação é exibida no modo de edição. |  |
| 5 | Inserir dados da área de avaliação | Na tela ÁREAS DE AVALIAÇÃO, efetue as seguintes entradas:Área de avaliação: <Número de área de avaliação>Determinação do controle de preço: 2Nota Somente para o Brasil: Determinação do controle do preço é 2 se Controle do preço for V e 3 se Controle do preço for S, quando forem abordados os princípios contábeis de custos para Brasil.Classe de avaliação: <número da classe de avaliação> |  |  |
| 6 | Inserir dados da área de avaliação atual | Na tela Avaliação, vá para Avaliação > Período atual e efetue as seguintes entradas:Preço padrão: Por exemplo, 20.Controle de preço: por exemplo, S. |  |  |
| 7 | Retornar à tela principal | Clique em Aplicar para voltar à tela Administrar mestre de produtos. | A tela Administrar mestre de produtos é aberta. |  |
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

Você deve concluir o capítulo anterior, [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos Dados básicos, tal como descrito no capítulo anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | O launchpad do SAP Fiori é exibido.Nota Efetuar login via launchpad só é relevante se WebGUI for utilizado. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 4 | Selecionar visões | Nota Se a caixa de diálogo Tipo de classe for exibida ao executar a etapa 3, você precisará seguir as etapas 7, 8, 9 e 10 primeiro antes da etapa 4 e, em seguida, reabrir o material no app Modificar material(MM02) para executar as etapas 5 e 6.Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados básicos 1Dados básicos 2Classificação |  |  |
| 5 | Inserir dados básicos | Na tela Material (matérias-primas), na guia Dados básicos 1, efetue as seguintes entradas:Descrição de material (texto breve): <Descrição de material>Unidade de medida básica: <Unidade de medida básica>Pressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 2, marque o campo de seleção Material configurável.Pressione Enter. | A guia Classificação é exibida e a caixa de diálogo Tipo de classe é exibida. |  |
| 7 | Selecionar o tipo de classe | Na caixa de diálogo Tipo de classe, marque o tipo de classe 300 (variante) e selecione Continuar. | A tela Classificação é exibida. |  |
| 8 | Atribuir classe | Na seção Atribuição, atribua uma classe e pressione Enter. | As características correspondentes são exibidas abaixo da seção Atribuição. |  |
| 9 | Selecionar valores da característica | Selecione os valores necessários das características. |  |  |
| 10 | Salvar dados | Clique em Salvar. | O material configurável é criado. |  |
| 11 | Navegar para transação CU41 | Navegue até a transação CU41 e efetue as seguintes entradas:Nome do perfil: <Nome do perfil>Tipo de classe: 300 |  |  |
| 12 | Salvar dados | Clique em Salvar. | O perfil de configuração é criado. |  |
| 13 | Navegar para a Transação CU42 | Navegue para a transação CU42.Clicar duas vezes em Nome do perfil > Configurar tela inicial > Modo de processamento: Configuração de variante avançada.Clique em Salvar. | O Perfil é criado. |  |
| 14 | Criar variante | Para criar uma variante, abra de novo o bloco Criar material(MM01) novamente e siga as etapas acima para criar um novo material com Dados básicos 1 e Dados básicos 2. |  |  |
| 15 | Criar variante | Em Dados básicos 2, vá para a Configuração específica do cliente e insira o material configurável previamente criado em Material configurável válido para vários centros. Selecione Configurar variante e escolha os valores de características necessários para a configuração de variantes. | A variante é criada. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário. | O launchpad do SAP Fiori é exibido.Nota Efetuar login via launchpad só é relevante se WebGUI for utilizado. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 3 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O Produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 4 | Tornar o produto configurável | Na tela Produto, acesse a guia Configuração e marque o campo de seleção Produto é configurável. |  |  |
| 5 | Atribuir classe de variantes | Na tela Produto, vá para a guia Classificação e selecione Clique aqui para atribuir uma classe.Selecione uma classe do tipo 300 (variante). | As características da classe atribuída são exibidas. |  |
| 6 | Selecionar características | Selecione os valores da característica necessários para cada característica. |  |  |
| 7 | Acessar a guia Variantes | Na tela Produto, acesse a guia Variantes e selecione Selecionar variantes do produto. | Uma árvore/tabela é exibida com diferentes características. |  |
| 8 | Selecionar características e criar variantes | Selecione a combinação de valores da característica e clique em Aplicar. | As variantes são criadas. |  |
| 9 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

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

Você deve concluir a seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 para prosseguir com este capítulo.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito na seção anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2.Selecione Continuar. | A tela Criar material (matérias-primas) é exibida. |  |
| 4 | Selecionar serviços para objeto | Vá para Serviços para objeto > Criar anexo. | A tela Importar arquivo é exibida. |  |
| 5 | Selecionar Upload. | Na tela Importar arquivo, selecione Carregar. | A tela Carregar arquivo é exibida. |  |
| 6 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 7 | Salvar | Escolha Selecionar e Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar Anexos | Na tela Produto, vá para a guia Anexos. | A tela Anexos é exibida. |  |
| 4 | Selecionar Upload. | Na seção Sistema de administração de documentos, clique em Carregar. | A tela Carregar arquivo é exibida. |  |
| 5 | Carregar anexo | Marque o arquivo e selecione Abrir. | O arquivo é carregado. |  |
| 6 | Salvar | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

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

Você deve concluir a seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 para prosseguir com este capítulo.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito na seção anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões, clique em Dados básicos 1 e Vendas: Dados gerais/dados do centro.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Organização de vendas: <nº org.vendas>Canal de Distrib.: <canal de distribuição> | A tela Criar material... (matérias-primas) é exibida. |  |
| 5 | Inserir dados na tela Dados básicos 1 | Na tela Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição: Insira uma descrição para o produto.Unidade básica: Atualizar Unidade básica EA, por exemplo, 1 |  |  |
| 6 | Insira dados em Vendas: Dados gerais/dados do centro | Na seção Dados de expedição (prazos em dias), efetue a seguinte entrada:Grupo de carregamento: <selecione qualquer valor de entradas possíveis> |  |  |
| 8 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique em Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Criar | Na tela Centros, clique em Criar. |  |  |
| 5 | Inserir centros - dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710 |  |  |
| 6 | Inserir dados MRP | Na seção MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir Centro - Vendas | Na seção Vendas, efetue a seguinte entrada:Grupo de carregamento: <selecione qualquer valor de entradas possíveis> |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
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

O procedimento a seguir apresenta instruções sobre como criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior [Criar dados mestre de materiais - Dados básicos](#unique_11) [página ] 7 para prosseguir com este capítulo.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito na seção anterior.

Procedimento: Opção 1 – Criar material

Siga este procedimento caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: ROH = Matérias-primasClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Selecionar visões | Na tela Selecionar visões clique em Dados básicos1, MRP 1 e MRP 4.Selecione Continuar. | É exibida a tela Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais na seção Nível organizacional, efetue as seguintes entradas:Centro: <número do centro>Depósito: <número do depósito> | A tela Criar material... (matérias-primas) é exibida. |  |
| 5 | Inserir dados na tela Dados básicos 1 | Na tela Dados básicos 1, efetue as seguintes entradas e pressione Enter:Descrição: Insira uma descrição para o produto.Unidade básica: Atualizar Unidade básica EA, por exemplo, 1 |  |  |
| 6 | Inserir dados na tela MRP 1 | Na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir dados na tela MRP 4 | Na seção Produção repetitiva/conjunto/estratégia de desdobramento, efetue a seguinte entrada:Produção Repetitiva: Marque o campo de seleção.Perfil prod.repetitiva: <selecione qualquer valor de entradas possíveis> |  |  |
| 8 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Siga este procedimento caso seu acesso de usuário ofereça a você o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que o levará até a tela Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique em Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Adicionar (+) | Na tela Centros, clique em Adicionar (+). |  |  |
| 5 | Inserir centros - dados gerais | Na seção Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710 |  |  |
| 6 | Inserir dados MRP | Na seção MRP, efetue as seguintes entradas:Tipo de MRP: por exemplo, ND. |  |  |
| 7 | Inserir dados de produção repetitiva | Na seção Produção repetitiva, efetue as seguintes entradas:Produção repetitiva ativada: Marque o campo de seleção para ativar o campo Perfil produção repetitiva.Perfil produção repetitiva: <selecione qualquer valor de entradas possíveis>Nota Depois de marcar o campo de seleção Produção repetitiva ativada, o campo Perfil produção repetitiva deve se tornar editável.Depois de desmarcar o campo de seleção Produção repetitiva ativada, o campo Perfil produção repetitiva deve se tornar somente leitura. |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
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
> Flagged while digesting this document, not verified: Internal inconsistencies: step numbering skips 7 in the plant sales Option 1 table; the mandatory/optional master data table is empty; the storage data row text refers to 'registro mestre de cliente' instead of material.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-661]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-663]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 58,898 chars in the whole document
